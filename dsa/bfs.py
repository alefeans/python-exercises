from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Node) -> List[List[int]]:
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level_nodes = []
        for _ in range(len(queue)):
            node = queue.popleft()
            if node:
                level_nodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level_nodes:
            res.append(level_nodes)

    return res


def zigzag_traversal(root: Node) -> List[deque[int]]:
    if not root:
        return []

    res = []
    queue = deque([root])
    reverse = False

    while queue:
        level_nodes = deque()

        for _ in range(len(queue)):
            node = queue.popleft()
            if reverse:
                level_nodes.appendleft(node.val)
            else:
                level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        reverse = not reverse
        res.append(level_nodes)

    return res


def binary_tree_right_side_view(root: Node) -> List[int]:
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        res.append(queue[-1].val)

        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


def binary_tree_min_depth(root: Node) -> int:
    if not root:
        return 0

    level = 0
    queue = deque([root])

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if not all([node.left, node.right]):
                return level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            level += 1

    return level
