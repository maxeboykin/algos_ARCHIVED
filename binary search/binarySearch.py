from typing import List


# O(log(n))
#
#

def binary_search(arr: List[int], target: int) -> int:
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        midpoint = (left + right) // 2
        if arr[midpoint] == target:
            return midpoint
        if arr[midpoint] < target:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return -1


inputArr = [0, 2, 3, 4, 5]
target = 4
print("inputArr", inputArr, "target", target)
result = binary_search(inputArr, target)
print("result of binary search\n", result)


def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


