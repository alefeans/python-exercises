from typing import Callable, Deque, List

"""
Build a function that returns the tip of the day:
- You have a list of tips in memory;
- Return a new tip everytime an user asks for it;
"""

""" 
A possible solution using FP would be using a curried function that has an internal
state index to control the access of the tips in the list that gets reseted to 0
when it becomes bigger than the list length
"""


def get_tip_of_the_day_fp(tips: List[str]) -> Callable[[], List[str]]:
    index = -1

    def inner():
        nonlocal index
        index = 0 if index == len(tips) - 1 else index + 1
        return tips[index]

    return inner


get_tip = get_tip_of_the_day_fp(["a", "b", "z", "d", "c"])
get_tip()  # a
get_tip()  # b
get_tip()  # z
get_tip()  # d
get_tip()  # c
get_tip()  # a
get_tip()  # b

"""
Another solution would be rotating a collections.deque and returning the first item
"""
from collections import deque


def get_tip_of_the_day_deque(tips: Deque[str]) -> str:
    tips.rotate()
    return tips[0]


tips_deque = deque(["a", "b", "z", "d", "c"])
get_tip_of_the_day_deque(tips_deque)  # c
get_tip_of_the_day_deque(tips_deque)  # d
get_tip_of_the_day_deque(tips_deque)  # z
get_tip_of_the_day_deque(tips_deque)  # b
get_tip_of_the_day_deque(tips_deque)  # a
get_tip_of_the_day_deque(tips_deque)  # c
get_tip_of_the_day_deque(tips_deque)  # d
get_tip_of_the_day_deque(tips_deque)  # z


"""
Another one, using a cycle:
"""
from itertools import cycle

tips_cycle = cycle(["a", "b", "z", "d", "c"])
next(tips_cycle)  # a
next(tips_cycle)  # b
next(tips_cycle)  # z
next(tips_cycle)  # d
next(tips_cycle)  # c
next(tips_cycle)  # a
next(tips_cycle)  # b
next(tips_cycle)  # z
