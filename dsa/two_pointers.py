from typing import List


def remove_duplicates(arr: List[int]) -> int:
    slow = 0
    for fast in range(len(arr)):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


def middle_of_linked_list(head: Node) -> int:
    if not head:
        return -1

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val  # type: ignore


def move_zeros(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow = slow + 1


if __name__ == "__main__":
    # print(remove_duplicates([0, 0, 1, 1, 1, 2, 2]))

    # linked_list = Node(0)
    # linked_list.next = Node(1)
    # linked_list.next.next = Node(2)
    # linked_list.next.next.next = Node(3)
    # linked_list.next.next.next.next = Node(4)
    # print(middle_of_linked_list(linked_list))
    
    # b = [0, 0, 9, 4, 0, 0, 3, 8, 0]
    # move_zeros(b)
    # print(b)
    pass
