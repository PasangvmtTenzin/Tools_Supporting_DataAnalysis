import csv

def load_data(filepath):
    data = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data
