from typing import List


# O(n^2)
#
#
def bubble_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            while unsorted_list[j] > unsorted_list[j + 1]:
                swapped = True
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
        if not swapped:
            return unsorted_list
    return unsorted_list


inputArr = [0, 2, 4, 1, 4]
print("inputArr", inputArr)
newArr = bubble_sort(inputArr)
print("bubble sort\n", newArr)

