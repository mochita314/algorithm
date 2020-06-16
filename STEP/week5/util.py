def load_input_csv(file_path):
    import csv

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

    dis = ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)**0.5

    return dis

def cities_to_dist(cities):

    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
    
    return dist

def angle(i,j,k):

    outer_product = (j[0]-i[0])*(k[1]-i[1]) - (k[0]-i[0])*(j[1]-i[1])

    return outer_product

def calculate_sum_length(cities,tour):

    sum_length = 0

    for i in range(len(tour)):
        sum_length += distance(cities[tour[i]],cities[tour[(i+1)%len(tour)]])

    return sum_length

def dct_to_lst(dct):
    lst = []
    for key in dct:
        lst.append([key,dct[key][0],dct[key][1]])
    return lst

def record_tour(tour,file_index):
    import csv
    '''
    結果をoutput_{0~6}.csvに書き込む関数
    '''
    file_path = './google-step-tsp/output_'+str(file_index)+'.csv'

    with open(file_path,'w') as f:
        f.write('index')
        f.write('\n')
        for i in range(len(tour)):
            num = str(tour[i])
            f.write(num)
            f.write('\n')