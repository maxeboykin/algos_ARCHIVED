from typing import List


# first item is considered then the net item
# we "insert" that item in the list by swapping it
# with the item before it until the item is smaller
# than the current item
def insertion_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current - 1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list


inputArr = [0, 2, 4, 1, 4]
print("inputArr", inputArr)
newArr = insertion_sort(inputArr)
print("insertion sort\n", newArr)


# selection sort means selecting the smallest item from the unsorted pile


def selection_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    return unsorted_list


inputArr = [6, 8, 3, 4, 1]
print("\ninputArr", inputArr)
selection_sort(inputArr)
print("selection sort\n", inputArr)
