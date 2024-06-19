import statistics

def calculate_statistics(data):
    headers = data[0]
    data = data[1:]  # Exclude headers from calculation
    variety_index = headers.index("variety")
    headers = headers[:variety_index] + headers[variety_index+1:]  # Remove 'variety' column header
    num_cols = len(headers)
    result = []

    for i in range(num_cols):
        if i != variety_index:  # Skip the 'variety' column
            col_values = [float(row[i]) for row in data]
            col_mean = statistics.mean(col_values)
            col_median = statistics.median(col_values)
            col_std = statistics.stdev(col_values)
            result.append([headers[i], 'Mean', col_mean])
            result.append([headers[i], 'Median', col_median])
            result.append([headers[i], 'Standard Deviation', col_std])

    return result
