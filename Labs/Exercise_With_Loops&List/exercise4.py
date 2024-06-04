'''Write a function reverse(lst) that returns a reversed copy of the list given. Use the list addition operator +.

Sample results of the function:

reverse([]) == []
reverse([1, 2, 3]) == [3, 2, 1]'''
   
   
def reverse(lst):
    reversed_copy = lst[::-1]
    return reversed_copy
  
# cases
print(reverse([]))        # Output: []
print(reverse([1, 2, 3]))  # Output: [3, 2, 1]
print("\n")
# Another way / Method

def reverse(lst):
    reversed_copy = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_copy += [lst[i]]
    return reversed_copy

# cases
print(reverse([]))        # Output: []
print(reverse([1, 2, 3]))  # Output: [3, 2, 1]
