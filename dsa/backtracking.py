from math import inf
from typing import List


class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if not children else children


def ternary_tree_paths(root):
    res = []

    def dfs(root, path):
        if not root.children:
            res.append("->".join(path) + "->" + str(root.val))
            return

        for child in root.children:
            path.append(str(root.val))
            dfs(child, path)
            path.pop()

    if root:
        dfs(root, [])
    return res


def letter_combination(n: int, letters: str) -> List[str]:
    res = []

    def dfs(path):
        if len(path) == n:
            res.append("".join(path))
            return

        for letter in letters:
            path.append(letter)
            dfs(path)
            path.pop()

    dfs([])
    return res


number_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    res = []

    def dfs(start_index, path):
        if len(path) == len(digits):
            res.append("".join(path))
            return

        number = digits[start_index]
        for letter in number_to_letters[number]:
            path.append(letter)
            dfs(start_index + 1, path)
            path.pop()

    dfs(0, [])
    return res


def partition(s: str) -> List[List[str]]:
    ans = []

    n = len(s)

    def is_palindrome(word):
        return word == word[::-1]

    def dfs(start, cur_path):
        if start == n:
            ans.append(cur_path[:])
            return

        for end in range(start + 1, n + 1):
            prefix = s[start:end]
            if is_palindrome(prefix):
                dfs(end, cur_path + [prefix])

    dfs(0, [])
    return ans


def permutations(letters: str) -> List[str]:
    res = []

    def dfs(path, seen=set()):
        if len(path) == len(letters):
            res.append("".join(path))
            return

        for letter in letters:
            if letter not in seen:
                path.append(letter)
                seen.add(letter)
                dfs(path, seen)
                path.pop()
                seen.discard(letter)

    dfs([])
    return res


def word_break(s: str, words: List[str]) -> bool:
    memo = {}  # type: ignore

    def dfs(start_index: int) -> bool:
        if start_index == len(s):
            return True

        if start_index in memo:
            return memo[start_index]  # type: ignore

        ans = False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ans = True
                    break

        memo[start_index] = ans
        return ans

    return dfs(0)


def decode_ways(digits: str) -> int:
    if len(digits) == 0:
        return 1
    elif digits[0] == "0":
        return 0
    else:
        answer = decode_ways(digits[1:])
        if 10 <= int(digits[:2]) <= 26:
            answer += decode_ways(digits[2:])
        return answer


def min_coins(coins, amount, sum):
    if sum == amount:
        return 0

    if sum > amount:
        return inf

    ans = inf
    for coin in coins:
        result = min_coins(coins, amount, sum + coin)
        if result == inf:
            continue
        ans = min(ans, result + 1)

    return ans


def coin_change(coins: List[int], amount: int) -> int:
    result = min_coins(coins, amount, 0)
    return result if result != inf else -1  # type: ignore


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(index, path):
        res.append(path[:])

        for i in range(index, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return res


if __name__ == "__main__":
    # left = Node(2)
    # left.children.append(Node(3))
    # middle = Node(4)
    # right = Node(6)
    # ternary_tree = Node(1)
    # ternary_tree.children.append(left)
    # ternary_tree.children.append(middle)
    # ternary_tree.children.append(right)
    # print(ternary_tree_paths(ternary_tree))

    # print(letter_combination(0, "ab"))

    # print(letter_combinations_of_phone_number("56"))

    # print(permutations("abc"))

    # print(decode_ways("102"))

    # print(coin_change([1, 2, 5], 11))

    # print(subsets([1, 2, 3]))
    pass
