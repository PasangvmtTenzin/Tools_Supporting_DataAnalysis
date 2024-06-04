"""Write a function my_sum(lst) that returns the total of numbers from a given (as a parameter) list. The total of an empty list is (of course) 0.

Sample results of the function:

my_sum([]) == 0
my_sum([1, 22, 3]) == 26"""

from collections.abc import Sequence as sek

def my_sum(seq: sek[float]) -> float:

    result = 0
    for item in seq:
        result +=item
    return result 

if __name__ == '__main__':
    print(my_sum([]))#output==0
    print(my_sum([1, 22, 3]))#output==26

print("\n")

"""Write a function sum_2d(lst) that returns the total of numbers stored in a two-dimensional list (ie. list of lists) of numbers. The component lists do not have to be of the same length.

Sample results of the function:

sum_2d([]) == 0
sum_2d([[],[],[]]) == 0
sum_2d([[1, 2, 3], [], [-34, 23423, -23425]]) == -30"""


def sum_2d(lst):
    total = 0

    for inner_lst in lst:
        for num in inner_lst:
            total += num

    return total
if __name__ == '__main__':
     print(sum_2d([]))  # Output==0
     print(sum_2d([[], [], []]))  # Output==0
     print(sum_2d([[1, 2, 3], [], [-34, 23423, -23425]]))#output== -30

"""Write a function reverse2(lst) that returns a reversed copy of the list given. This time use only the append operation (no addition of lists is allowed in this exercise).

Sample results of the function:

reverse2([]) == []
reverse2([1, 2, 3]) == [3, 2, 1]"""
print("\n")
def reverse2(lst):
    copy = []

    for item in reversed (lst):
        copy.append(item)
    return copy

if __name__ == '__main__':
     print(reverse2([])) #result==[]
     print(reverse2([1, 2, 3])) #result==[3,2,1]
