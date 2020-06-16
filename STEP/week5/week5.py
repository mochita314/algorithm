def NN(cities,dist):
    '''
    greedy algorithm / nearest neighbor algorithm
    copied from google-step-tsp/solver_greedy.py
    '''

    N = len(cities)

    current_city = 0
    unvisited_cities = set(range(1, N))
    tour = [current_city]

    while unvisited_cities:

        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    return tour

def GS(cities):
    '''
    GrahamScan algorithm
    '''
    def find_min_y(cities):

        '''
        y座標最小の点を見つけ、リストの先頭に移動する関数
        '''

        # y座標最小の点を見つける（同じならx座標が小さいほう）
        min_x = cities[0][1]
        min_y = cities[0][2]
        index = 0
        
        for i in range(1,len(cities)):
            x = cities[i][1]
            y = cities[i][2]
            if y < min_y or y == min_y and x < min_x:
                min_x = x
                min_y = y
                index = i
        
        # y座標最小の点をリストの先頭にもってくる
        cities[0], cities[index] = cities[index], cities[0]

        return cities
    
    def sort_by_angle(cities):

        '''
        リストの先頭に移動した地点を基準として角度順に
        リスト全体を並び替える
        '''

        # cities: もともとの辞書の状態をリストに変えてから扱う
        len_cities = len(cities)
        count = 0
        index = 0

        while True:
            count += 1
            index += 1

            angle_ijk = angle(cities[0][1:],cities[index][1:],cities[index+1][1:])

            if angle_ijk < 0:
                cities[index],cities[index+1] = cities[index+1],cities[index]
                count = 0
            
            if count == len_cities - 1:
                break
            
            if index == len_cities - 2:
                index = 0

        return cities
    
    cities_lst = dct_to_lst(cities) 
    cities_lst = find_min_y(cities_lst)
    cities_lst = sort_by_angle(cities_lst)

    # 凸包から削除された都市を追加していくリスト
    left_cities = []

    index = -1
    count = 0
    while True:
        index += 1
        count += 1
        angle_ijk = angle(cities_lst[index][1:],cities_lst[index+1][1:],cities_lst[index+2][1:])
        if angle_ijk < 0:
            left_cities.append(cities_lst[index+1])
            del cities_lst[index+1]
            count = 0
        if count == len(cities_lst):
            break
        if index >= len(cities_lst) - 3:
            index -= 1
    
    return cities_lst,left_cities

def CHI(cities,dist):
    '''
    Convex Hull Insertion algorithm
    '''
    def eval_cost(dist,i,j,k):
        # cityの追加コストを求める関数
        cost = dist[i][k] + dist[k][j] - dist[i][j]
        return cost
    
    def additional_cost(dist,i,j,k):
        add_cost = (dist[i][k] + dist[k][j]) / dist[i][j]
        return add_cost
    
    def find_k(convex_hull,left_cities,dist):
        '''
        凸包上の連続した都市をi,jとし、内部の各都市kに対してコストを計算
        kに対するコスト最小とする都市i,jを決定し辞書にkeyをkとして格納していく
        '''
        k_dct = {}
        for k in range(len(left_cities)):
            index_k = left_cities[k][0]

            for i in range(len(convex_hull)):
                index_i = convex_hull[i][0]
                index_j = convex_hull[(i+1)%len(convex_hull)][0]
                cost = eval_cost(dist,index_i,index_j,index_k)
                if k==0:
                    min_cost = cost
                    min_i = i
                    min_i_in_cities = index_i
                    min_j_in_cities = index_j
                else:
                    if cost < min_cost:
                        min_cost = cost
                        min_i = i
                        min_i_in_cities = index_i
                        min_j_in_cities = index_j

            # index_k : left_citiesのk番目の都市の、cities全体でのindex
            # k : left_citiesのk番目の都市のまさにleft_cities上でのindex(=k)
            # min_i : left_citiesのk番目の都市を直後に挿入すべき、convex_hull上のindex
            # min_i(j)_in_cities : left_citiesのk番目の都市を直後に挿入すべき都市の、cities全体でのindex
            k_dct[index_k] = [k,min_i,min_i_in_cities,min_j_in_cities]
    
        return k_dct
    
    def add_best_k(convex_hull,left_cities,k_dct,dist):
        '''
        find_kで見つけたi,j,kの組み合わせの中から、
        追加コストが最小となるkを凸包に追加する
        '''
        min_cost = 10**10

        for index_k in k_dct:
            i = k_dct[index_k][2]
            j = k_dct[index_k][3]
            add_cost = additional_cost(dist,i,j,index_k)
            if add_cost < min_cost:
                best_k = index_k
        
        k = k_dct[best_k][0]
        i = k_dct[best_k][1]

        convex_hull.insert(i+1,left_cities[k])
        del left_cities[k]

        return convex_hull,left_cities
    
    convex_hull,left_cities = GS(cities)
    # まずグラハムスキャン法により凸包を初期経路として求める

    while left_cities:
        #残りの都市がなくなるまで追加していく
        k_dct = find_k(convex_hull,left_cities,dist)
        convex_hull,left_cities = add_best_k(convex_hull,left_cities,k_dct,dist)
    
    tour = []
    for i in range(len(convex_hull)):
        tour.append(convex_hull[i][0])
    
    return tour

def _2opt(cities,tour,max_iter):
    '''
    ランダムに二つの辺を選んで、入れ替えた方が経路が短くなる場合は入れ替える
    '''
    _iter = 0
    len_tour = len(tour)

    checked = set()

    while _iter < max_iter:

        # ランダムに2つの辺を選ぶ
        i = random.randrange(len_tour)
        j = random.randrange(len_tour)

        cnt = 0
        while i==j or (i,j) in checked:
            # 同じ辺を見たり、もうすでに見た組み合わせはできるだけ避ける
            if cnt > 100 and i!=j:
                # max_iterが組み合わせ数より大きい場合、何回やってもすでに見た組み合わせを見ることになる
                # その場合に無限ループにならないように10回やっても被ってたら抜ける
                break
            cnt += 1
            i = random.randrange(len_tour)
            j = random.randrange(len_tour)
        
        pair_i = []
        pair_i.append(cities[tour[i]])
        pair_i.append(cities[tour[(i+1)%len_tour]])
        
        pair_j = []
        pair_j.append(cities[tour[j]])
        pair_j.append(cities[tour[(j+1)%len_tour]])
        
        current_dis = distance(pair_i[0],pair_i[1]) + distance(pair_j[0],pair_j[1])
        new_dis = distance(pair_i[0],pair_j[0]) + distance(pair_i[1],pair_j[1])

        if new_dis <= current_dis:
            # 入れ替えた方が距離が短くなる場合、入れ替えを行う

            new_tour = tour[(i+1)%len_tour:(j+1)%len_tour]
            tour[(i+1)%len_tour:(j+1)%len_tour] = new_tour[::-1]
            #print('changed!')
            #print('sum_length:',calculate_sum_length(cities,tour))
        
        checked.add((i,j))
            
        _iter += 1

    return tour

if __name__ == '__main__':

    import random
    import argparse
    import csv
    import math

    from util import *

    parser = argparse.ArgumentParser(description='Program for solving TSP problem')
    parser.add_argument('-i','--index',help='index of input_csv',default='0')
    parser.add_argument('-m','--max_iter',help='maximum times of iteration of swap operation',default=1000,type=int)
    parser.add_argument('-o','--option',help='which method to use',default='CHI')
    args = parser.parse_args()

    cities = load_input_csv('./google-step-tsp/input_'+args.index+'.csv')

    dist = cities_to_dist(cities)

    if args.option == 'CHI':
        tour = CHI(cities,dist)
    elif args.option == 'NN':
        tour = NN(cities,dist)
    elif args.option == 'SPLIT':
        tour = SPLIT(cities,tour,size)
    else:
        print('正しい方法を入力してください')
        exit()

    tour = _2opt(cities,tour,args.max_iter)
    print(tour)
    print('sum_length:',calculate_sum_length(cities,tour))

    record_tour(tour,args.index)