'''Write a function set_sum(lst1, lst2) that returns the set-theoretic sum of arguments. In this exercise, sets are to be represented as unordered lists of their elements (without duplicates).

Sample results of the function:

set_sum([], []) == []
set_sum([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
set_sum([], [1, 2, 3]) == [1, 2, 3]
set_sum([1, 2, 3], []) == [1, 2, 3]
set_sum([1, 3, -2], [-2, -3, 0, 1, 34]) == [1, 3, -2, -3, 0, 34] (the order maybe different)'''

def set_sum(lst1, lst2):
    # Create an empty set to store unique elements
    result_set = set()

    # Add elements from lst1 to the result_set
    for elem1 in lst1:
        result_set.add(elem1)

    # Add elements from lst2 to the result_set
    for elem2 in lst2:
        result_set.add(elem2)

    # Convert the result_set to a list to maintain order
    result = list(result_set)

    # Return the final list as the set-theoretic sum
    return result

print(set_sum([], []))                            # Output: []
print(set_sum([1, 2, 3], [1, 2, 3]))              # Output: [1, 2, 3]
print(set_sum([], [1, 2, 3]))                      # Output: [1, 2, 3]
print(set_sum([1, 2, 3], []))                      # Output: [1, 2, 3]
print(set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))    # Output: [0, 1, 3, 34, -2, -3] (order may vary)

