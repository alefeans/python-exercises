import bisect
from typing import List


def bool_binary_search(arr: List[bool]) -> int:
    index = -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] is True:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index


def first_not_smaller(arr: List[int], target: int) -> int:
    index = -1
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index


def find_first_ocurrence(arr: List[int], target: int) -> int:
    index = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            index = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return index


def find_min_in_rotated_array(arr: List[int]) -> int:
    index = -1
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] <= arr[-1]:
            index = mid
            right = mid - 1
        else:
            left = mid + 1
    return index


def plates_between_candles(string, queries):
    candles_indexes = [i for i, c in enumerate(string) if c == "|"]
    res = []
    for a, b in queries:
        i = bisect.bisect_left(candles_indexes, a)
        j = bisect.bisect(candles_indexes, b) - 1
        res.append((candles_indexes[j] - candles_indexes[i]) - (j - i) if i < j else 0)
    return res


if __name__ == "__main__":
    # print(bool_binary_search([False, False, False, False, True, True]))

    # print(first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6))

    # print(find_first_ocurrence([2, 3, 5, 7, 11], 2))

    # print(find_min_in_rotated_array([30, 40, 50, 10, 20]))
    # print(find_min_in_rotated_array([2, 3, 4, 5, 1]))
    # print(find_min_in_rotated_array([60, 1, 2, 40, 50]))

    # string = "***|**|*****|**||**|*"
    # queries = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
    # print(plates_between_candles(string, queries))
    pass
