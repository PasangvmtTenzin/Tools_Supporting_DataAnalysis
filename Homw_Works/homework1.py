from typing import List

def merge_sort(li: List[float]) -> List[float]:
    if len(li) <= 1:
        return li

    mid = len(li) // 2
    #Dividing
    left_half = li[:mid]
    right_half = li[mid:]

    #Recursively applies merge_sort to the left and right halves of the list (Conquer)
    left_half = merge_sort(left_half) 
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

#Mergers here
def merge(left: List[float], right: List[float]) -> List[float]:
    result = []
    i = j = 0

    for k in range(len(left) + len(right)):
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


org_list = [3.2, 1.5, 4.8, 2.7, 0.9, 6.4]
sorted_list = merge_sort(org_list)
print("Original List:", org_list)
print("Sorted List:", sorted_list)
