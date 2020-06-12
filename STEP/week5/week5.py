import csv

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

def NN(cities):
    '''
    greedy algorithm / nearest neighbor algorithm
    copied from google-step-tsp/solver_greedy.py
    '''

    def distance(city1,city2):

        dis = (city1[0]-city2[0])**2 + (city1[1]-city2[1])**2

        return dis

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

def _2opt(route,times):
    '''
    swap randomly chosen two edges if better route is find by that
    '''
    return

if __name__ == '__main__':
    spots = load_input_csv('./google-step-tsp/input_1.csv')
