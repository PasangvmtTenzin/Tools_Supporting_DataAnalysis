def sum_2d(lst):
    total_sum = 0

    for row in lst:
        for num in row:
            if isinstance(num, (int, float)):
                total_sum += num

    return total_sum

if __name__ == '__main__':
    # Test cases
    print(sum_2d([]))                        # Output: 0
    print(sum_2d([[], [], []]))               # Output: 0
    print(sum_2d([[1, 2, 3], [], [-34, 23423, -23425]]))  # Output: -30
