class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev, head = head, next
    return prev


def merge_two_lists(self, list1, list2):
    head = ListNode()
    curr = head

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next

    curr.next = list1 or list2
    return head.next


if __name__ == "__main__":
    # linked_list = ListNode(1)
    # linked_list.next = ListNode(2)
    # linked_list.next.next = ListNode(3)

    # linked_list = reverse_list(linked_list)
    # while linked_list:
    #     print(linked_list.val)
    #     linked_list = linked_list.next
    pass
