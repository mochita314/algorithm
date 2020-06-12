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

def calculate_sum_length(cities,tour):

    sum_length = 0

    for i in range(len(tour)):
        sum_length += distance(cities[tour[i]],cities[tour[(i+1)%len(tour)]])

    return sum_length
