# iris_analysis/io/save.py

import csv

def save_result(filepath, result):
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in result:
            writer.writerow(row)
