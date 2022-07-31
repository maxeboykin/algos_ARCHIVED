from typing import List


# O(n*log(n))
#
#
def merge_sort(unsorted_list: List[int]) -> List[int]:
    n = len(unsorted_list)
    if n <= 1:
        return unsorted_list
    midpoint = n // 2
    left_arr, right_arr = merge_sort(unsorted_list[:midpoint]), merge_sort(unsorted_list[midpoint:])
    result_list = []
    left_pointer, right_pointer = 0, 0
    while left_pointer < midpoint or right_pointer < n - midpoint:
        if left_pointer == midpoint:
            result_list.append(right_arr[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint:
            result_list.append(left_arr[left_pointer])
            left_pointer += 1
        elif left_arr[left_pointer] < right_arr[right_pointer]:
            result_list.append(left_arr[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_arr[right_pointer])
            right_pointer += 1
    return result_list


inputArr = [0, 2, 4, 1, 4]
print("inputArr", inputArr)
newArr = merge_sort(inputArr)
print("merge sort\n", newArr)
