class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev, head = head, next
    return prev


if __name__ == "__main__":
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)

    linked_list = reverseList(linked_list)
    while linked_list:
        print(linked_list.val)
        linked_list = linked_list.next
