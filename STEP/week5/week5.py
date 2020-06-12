def load_input_csv(file_path):
    '''
    load input_csv and make dictionary of cities
    '''
    with open(file_path) as f:
        reader = csv.reader(f)
        cities = {}
        index = 0
        for row in reader:
            if row[0] != 'x':
                cities[index] = [float(row[0]),float(row[1])]
                index += 1
    return cities

def distance(city1,city2):

    dis = (city1[0]-city2[0])**2 + (city1[1]-city2[1])**2

    return dis

def calculate_sum_length(cities,tour):

    sum_length = 0

    for i in range(len(tour)):
        sum_length += distance(cities[tour[i]],cities[tour[(i+1)%len(tour)]])

    return sum_length

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

def CHI(spots):
    '''
    Convex Hull Insertion algorithm
    '''
    return

def GS(spots):
    '''
    GrahamScan algorithm
    '''
    return

def _2opt(cities,tour,max_iter):
    '''
    swap randomly chosen two edges if better route is find by that
    '''
    _iter = 0
    len_tour = len(tour)

    while _iter < max_iter:

        i = random.randrange(len_tour)
        j = random.randrange(len_tour)
        while j in [i-1,i,i+1]:
            j = random.randrange(len_tour)
        
        pair_i = []
        pair_i.append(cities[tour[i]])
        pair_i.append(cities[tour[(i+1)%len_tour]])
        
        pair_j = []
        pair_j.append(cities[tour[j]])
        pair_j.append(cities[tour[(j+1)%len_tour]])
        
        current_dis = distance(pair_i[0],pair_i[1]) + distance(pair_j[0],pair_j[1])
        new_dis = distance(pair_i[0],pair_j[0]) + distance(pair_i[1],pair_j[1])

        if new_dis < current_dis:

            new_tour = tour[(i+1)%len_tour:(j+1)%len_tour]
            tour[(i+1)%len_tour:(j+1)%len_tour] = new_tour[::-1]
            print('changed!')
            print('sum_length:',calculate_sum_length(cities,tour))
        
        _iter += 1

    return tour

if __name__ == '__main__':

    import random
    import csv
    import argparse

    parser = argparse.ArgumentParser(description='Program for solving TSP problem')
    parser.add_argument('-i','--index',help='index of input_csv',default='0')
    args = parser.parse_args()

    cities = load_input_csv('./google-step-tsp/input_'+args.index+'.csv')
    #cities = {0:[1,5],1:[3,3],2:[4,9],3:[6,7],4:[2,8]}
    tour = NN(cities)
    print(tour)
    print('sum_length:',calculate_sum_length(cities,tour))

    tour = _2opt(cities,tour,100)
    print(tour)