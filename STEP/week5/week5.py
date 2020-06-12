import csv

def load_input_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        spots = {}
        index = 0
        for row in reader:
            if row[0] != 'x':
                spots[index] = [float(row[0]),float(row[1])]
                index += 1
    return spots

if __name__ == '__main__':
    spots = load_input_csv('./google-step-tsp/input_1.csv')
