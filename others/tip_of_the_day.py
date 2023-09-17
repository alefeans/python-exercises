from typing import Callable, List

"""
Build a function that returns the tip of the day:
- You have a list of tips in memory;

I've seen three generalizations of this problem:
- Return a new tip everytime an user asks for it;
- Return the same tip for the entire day, but:
    - You can't repeat the same tip for two consecutive days;
    - We don't have a tip for each day (so no monday -> tip1, tuesday -> tip2 solution here);
- Make a request to https://frog.tips and get only the ID and the tip itself of every tip
"""


""" 
For the first problem, a possible solution would be using a curried function that has an 
internal state index to control the access of the tips in the list that gets reseted to 0
when it becomes bigger than the list length
"""


def first_get_tip_of_the_day(tips: List[str]) -> Callable[[], List[str]]:
    index = -1

    def inner():
        nonlocal index
        index = 0 if index == len(tips) - 1 else index + 1
        return tips[index]

    return inner


tips = ["a", "b", "z", "d", "c"]
get_tip = first_get_tip_of_the_day(tips)
get_tip()  # a
get_tip()  # b
get_tip()  # z
get_tip()  # d
get_tip()  # c
get_tip()  # a
get_tip()  # b

"""
For the second problem, a possible solution would be having a function that receives
the unix timestamp of the day and maps it to an index of the list, so we will
always return the same tip for the same day, and it will change in the next day
"""
