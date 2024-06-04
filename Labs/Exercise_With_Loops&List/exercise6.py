'''Write a function sorted_set_sum(lst1, lst2) that returns the set-theoretic sum of arguments. In this exercise, sets are to be represented as lists of their elements in ascending order (hence there are no duplicates on these lists). You are allowed to use on lists only indexing and the len and append functions.

Sample results of the function:

sorted_set_sum([], []) == []
sorted_set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
sorted_set_sum([], [1, 2, 3]) == [1, 2, 3]
sorted_set_sum([1, 2, 3], []) == [1, 2, 3]
sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]) == [-3, -2, 0, 1, 3, 34]'''

def sorted_set_sum(lst1, lst2):
    result = []
    i, j = 0, 0

    for i in range(len(lst1)):
        while j < len(lst2) and lst2[j] < lst1[i]:
            result.append(lst2[j])
            j += 1
        if j < len(lst2) and lst2[j] == lst1[i]:
            j += 1
        result.append(lst1[i])

    for j in range(j, len(lst2)):
        result.append(lst2[j])

    return result

# Test cases
print(sorted_set_sum([], []))                            # Output: []
print(sorted_set_sum([1, 2, 3], [1, 2, 3]))              # Output: [1, 2, 3]
print(sorted_set_sum([], [1, 2, 3]))                      # Output: [1, 2, 3]
print(sorted_set_sum([1, 2, 3], []))                      # Output: [1, 2, 3]
print(sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))    # Output: [-3, -2, 0, 1, 3, 34]
