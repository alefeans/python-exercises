"""
Given a list of players, pair up players so that:

1. Each player gives a gift once
2. Each player receives a gift once
3. Players cannot give or receive to themselves
4. Selections must be random

Input: ['Alice', 'Bob', 'Michael', 'Renna']
Output: [['Alice', 'Bob'], ['Bob', 'Michael'], ['Michael', 'Renna'], ['Renna', 'Alice']]
"""
import random
from typing import List


def secret_gift(players: List[str]) -> List[List[str]]:
    resp = []
    random.shuffle(players)

    for i, player in enumerate(players):
        previous = i % len(players) - 1
        resp.append([players[previous], player])
    return resp


if __name__ == "__main__":
    print(secret_gift(["Alice", "Bob", "Michael", "Renna"]))
