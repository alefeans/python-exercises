"""
Let's say we have a website and we keep track of what pages customers are viewing, for things 
like business metrics.

Every time somebody comes to the website, we write a record to a log file consisting of 
Timestamp, PageId, CustomerId. At the end of the day we have a big log file with many entries 
in that format. And for every day we have a new file.

Now, given two log files (log file from day 1 and log file from day 2) we want to generate a 
list of 'loyal customers' that meet the criteria of: (a) they came on both days, and (b) they 
visited at least two unique pages.

In this case, two unique pages means two unique pages overall
"""
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Iterator, List, Set

CURRENT_PATH = Path("others/loyal_customers")


def get_id(entry: str) -> str:
    """
    "user: 1" -> "1"
    """
    return entry.split(" ")[-1]


def get_user_and_page(access: str) -> List[str]:
    """
    "user: 1, page: 2, 2020-03-02 12:00:01" -> [1, 2]
    """
    user_and_page_entries = access.split(",")[:2]
    return [get_id(entry) for entry in user_and_page_entries]


def get_day_one_visitors() -> DefaultDict[str, Set[str]]:
    day_one_visitors = defaultdict(set)
    with open(CURRENT_PATH / "log_day_one.txt", "r") as log_day_one:
        for access in log_day_one:
            day_one_user, day_one_page = get_user_and_page(access)
            day_one_visitors[day_one_user].add(day_one_page)
    return day_one_visitors


def get_day_two_accesses() -> Iterator[str]:
    with open(CURRENT_PATH / "log_day_two.txt", "r") as log_day_two:
        for access in log_day_two:
            yield access


def get_loyal_customers(visitors: DefaultDict[str, Set[str]]) -> List[str]:
    loyal_customers = []
    for day_two_access in get_day_two_accesses():
        day_two_user, day_two_page = get_user_and_page(day_two_access)
        if day_two_user in visitors:
            accessed_pages = visitors[day_two_user]
            if len(accessed_pages) > 1 or day_two_page not in accessed_pages:
                loyal_customers.append(day_two_user)
                # we already found a loyal user, so we can delete it from visitors
                del visitors[day_two_user]

    return loyal_customers


if __name__ == "__main__":
    day_one_visitors = get_day_one_visitors()
    print(get_loyal_customers(day_one_visitors))
