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

def GS(spots):
    '''
    GrahamScan algorithm
    '''
    return

def CHI(spots):
    '''
    Convex Hull Insertion algorithm
    '''
    return

def _2opt(cities,tour,max_iter):
    '''
    swap randomly chosen two edges if better route is find by that
    '''
    _iter = 0
    len_tour = len(tour)

    checked = set()

    while _iter < min(max_iter,len_tour*(len_tour-1)):

        i = random.randrange(len_tour)
        j = random.randrange(len_tour)

        cnt = 0
        while i==j or (i,j) in checked:
            if cnt > 10:
                break
            cnt += 1
            i = random.randrange(len_tour)
            j = random.randrange(len_tour)
        
        checked.add((i,j))
        
        pair_i = []
        pair_i.append(cities[tour[i]])
        pair_i.append(cities[tour[(i+1)%len_tour]])
        
        pair_j = []
        pair_j.append(cities[tour[j]])
        pair_j.append(cities[tour[(j+1)%len_tour]])
        
        current_dis = distance(pair_i[0],pair_i[1]) + distance(pair_j[0],pair_j[1])
        new_dis = distance(pair_i[0],pair_j[0]) + distance(pair_i[1],pair_j[1])

        if new_dis <= current_dis:

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
    parser.add_argument('-m','--max_iter',help='maximum times of iteration of swap operation',default=10000,type=int)
    args = parser.parse_args()

    cities = load_input_csv('./google-step-tsp/input_'+args.index+'.csv')
    tour = NN(cities)
    tour = _2opt(cities,tour,args.max_iter)
    print(tour)