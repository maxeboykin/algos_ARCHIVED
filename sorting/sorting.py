from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in range(n):
        current = i
        while(current > 0 and unsorted_list[current] < unsorted_list[current - 1]):
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list


newArr = sort_list_insertion([0, 2, 4, 1, 4])
print(newArr)


def sort_list_bubble(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    for i in reversed(range(n)):
        swapped = False
        for j in range(i):
            if (unsorted_list[j + 1] < unsorted_list[j]):
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True

        if not swapped:
            return unsorted_list
    return unsorted_list


from typing import List


def sort_list(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    leftArray, rightArray = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    leftPointer, rightPointer = 0, 0
    results_Arr = []

    while leftPointer < midpoint or rightPointer < n - midpoint:
        if leftPointer == midpoint:
            results_Arr.append(rightArray[rightPointer])
            rightPointer += 1
        elif rightPointer == n - midpoint:
            results_Arr.append(leftArray[leftPointer])
            leftPointer += 1
        elif leftArray[leftPointer] <= rightArray[rightPointer]:
            results_Arr.append(leftArray[leftPointer])
            leftPointer += 1
        else:
            results_Arr.append(rightArray[rightPointer])
            rightPointer += 1

    return results_Arr