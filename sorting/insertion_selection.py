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
newArr = insertion_sort(inputArr)
print("inputArr", inputArr, "\ninsertion sort\n", newArr)
