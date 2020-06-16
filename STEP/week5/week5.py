def NN(cities):
    '''
    greedy algorithm / nearest neighbor algorithm
    copied from google-step-tsp/solver_greedy.py
    '''

    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

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

    index = -1
    count = 0
    while True:
        index += 1
        count += 1
        angle_ijk = angle(cities_lst[index][1:],cities_lst[index+1][1:],cities_lst[index+2][1:])
        if angle_ijk < 0:
            del cities_lst[index+1]
            count = 0
        if count == len(cities_lst):
            break
        if index >= len(cities_lst) - 3:
            index -= 1
    
    return cities_lst

def CHI(cities):
    '''
    Convex Hull Insertion algorithm
    '''
    convex_hull = GS(cities)
    # まずグラハムスキャン法により凸包を初期経路として求める

    return

def _2opt(cities,tour,max_iter):
    '''
    ランダムに二つの辺を選んで、入れ替えた方が経路が短くなる場合は入れ替える
    '''
    _iter = 0
    len_tour = len(tour)

    while _iter < max_iter:

        # ランダムに2つの辺を選ぶ
        i = random.randrange(len_tour)
        j = random.randrange(len_tour)

        cnt = 0
        while i==j or (i,j) in checked:
            # 同じ辺を見たり、もうすでに見た組み合わせはできるだけ避ける
            if cnt > 10 and i!=j:
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
            print('changed!')
            print('sum_length:',calculate_sum_length(cities,tour))
            
        _iter += 1

    return tour

if __name__ == '__main__':

    import random
    import argparse

    from util import *

    parser = argparse.ArgumentParser(description='Program for solving TSP problem')
    parser.add_argument('-i','--index',help='index of input_csv',default='0')
    parser.add_argument('-m','--max_iter',help='maximum times of iteration of swap operation',default=1000,type=int)
    args = parser.parse_args()

    cities = load_input_csv('./google-step-tsp/input_'+args.index+'.csv')

    convex_hull = GS(cities)
    print(convex_hull)

    #tour = NN(cities)
    #tour = double_2opt(cities,tour,args.max_iter)
    #print(tour)