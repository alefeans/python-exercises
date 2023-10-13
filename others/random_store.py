"""
Design a class for:
1 - Inserting a value (integers, no duplicates)
2 - Removing a value
3 - Get random value that is already inserted (equal probability)
"""

import random
from typing import Dict, List


class Store:
    def __init__(self) -> None:
        self.nums: List[int] = []
        self.nums_positions: Dict[int, int] = {}

    def add(self, num: int) -> None:
        if num in self.nums_positions:
            return

        self.nums.append(num)
        self.nums_positions[num] = len(self.nums) - 1

    def remove(self, num: int) -> None:
        if num not in self.nums_positions:
            return

        pos = self.nums_positions[num]
        last_pos = len(self.nums) - 1
        self.nums[pos], self.nums[last_pos] = self.nums[last_pos], self.nums[pos]
        self.nums_positions[self.nums[pos]] = pos

        self.nums.pop()
        del self.nums_positions[num]

    def get_random(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    store = Store()
    store.add(1)
    store.add(2)
    store.add(3)
    store.add(4)
    store.add(5)
    store.add(7)
    store.remove(4)
    store.remove(7)
    print(store.nums)
    print(store.get_random())
