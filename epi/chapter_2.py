"""
Input: array of integers
Output: reorder its entries so that the even entries appear first
"""


def even_first_spacious(ints):
    """O(N) space"""
    even, odd = [], []
    for i in ints:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd


def even_first(ints):
    """O(1) space"""
    start, end = 0, len(ints) - 1
    while start < end:
        if ints[start] % 2 == 0:
            start += 1
        else:
            ints[start], ints[end] = ints[end], ints[start]
            end -= 1
    return ints


def dutch_national_flag():
    return
