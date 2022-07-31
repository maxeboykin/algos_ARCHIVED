from typing import List


# Given an array of integers sorted in increasing order and a target,
# find the index of the first element in the array
# that is larger than or equal to the target.
# Assume that it is guaranteed to find a satisfying number.
#
#

def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


inputArr = [0, 2, 3, 4, 5, 7, 10, 15, 26, 56, 78]
target = 11
print("inputArr", inputArr, "target", target)
result = first_not_smaller(inputArr, target)
print("result of binary search\n", result, inputArr[result])


def first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            boundary_index = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index


inputArr = [0, 2, 2, 2, 2, 2, 12, 15, 26, 56, 78]
target = 2
print("inputArr", inputArr, "target", target)
result = first_occurrence(inputArr, target)
print("result of binary search\n", result)
