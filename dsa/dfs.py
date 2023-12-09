from typing import Any, Optional


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right


def find_target(root: Optional[Node], target: int) -> Optional[Node]:
    if root is None:
        return None

    if root.value == target:
        return root

    return find_target(root.left, target) or find_target(root.right, target)


def pretty_print_path(root: Optional[Node], ident: str = "") -> None:
    if not root:
        return None

    print(f"{ident}{root.value}")
    next_ident = ident + "  "
    pretty_print_path(root.left, next_ident)
    pretty_print_path(root.right, next_ident)


def greatest_value(root: Optional[Node]) -> Any:
    if not root:
        return -float("inf")

    return max(root.value, greatest_value(root.left), greatest_value(root.right))


def tree_max_depth(root: Optional[Node]) -> int:
    def dfs(root: Optional[Node]) -> int:
        if not root:
            return 0

        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0


def visible_nodes_count(root: Optional[Node]) -> int:
    def dfs(root: Optional[Node], greatest: float) -> int:
        if not root:
            return 0

        total = 0
        if root.value >= greatest:
            total += 1
            greatest = root.value

        total += dfs(root.left, greatest)
        total += dfs(root.right, greatest)
        return total

    return dfs(root, -float("inf")) if root else 0


def is_balanced_tree(root: Optional[Node]) -> bool:
    def dfs(root: Optional[Node]) -> int:
        if not root:
            return 0

        left_depth, right_depth = dfs(root.left), dfs(root.right)

        if left_depth == -1 or right_depth == -1:
            return -1

        if abs(left_depth - right_depth) > 1:
            return -1

        return max(left_depth, right_depth) + 1

    return dfs(root) != -1


def serialize(root: Optional[Node]) -> str:
    if not root:
        return "x"

    result = []
    result.append(str(root.value))
    result.append(serialize(root.left))
    result.append(serialize(root.right))
    return " ".join(result)


def deserialize(s):
    def dfs(nodes):
        node = next(nodes)
        if node == "x":
            return

        curr = Node(int(node))
        curr.left = dfs(nodes)
        curr.right = dfs(nodes)
        return curr

    return dfs(iter(s.split()))


def invert(root: Optional[Node]) -> Optional[Node]:
    # one-liner creating a new Node every time
    # return Node(root.value, invert(root.right), invert(root.left)) if root else None

    if root:
        root.left, root.right = invert(root.right), invert(root.left)
    return root


def find(root: Optional[Node], val: int) -> bool:
    if not root:
        return False
    if root.value == val:
        return True
    elif root.value < val:
        return find(root.right, val)
    else:
        return find(root.left, val)


def insert(tree, val):
    if tree is None:
        return Node(val)
    if tree.value < val:
        tree.right = insert(tree.right, val)
    elif tree.value > val:
        tree.left = insert(tree.left, val)
    return tree


def is_bst(tree: Optional[Node]) -> bool:
    def dfs(tree: Optional[Node], min_value: float, max_value: float) -> bool:
        if not tree:
            return True

        if not (min_value < tree.value < max_value):
            return False

        return dfs(tree.left, min_value, tree.value) and dfs(tree.right, tree.value, max_value)

    return dfs(tree, -float("inf"), float("inf"))


def lca(tree: Optional[Node], p: int, q: int) -> Any:
    if not tree:
        return -1
    if p < tree.value and q < tree.value:
        return lca(tree.left, p, q)
    elif p > tree.value and q > tree.value:
        return lca(tree.right, p, q)
    return tree.value


if __name__ == "__main__":
    # path = Node("/")
    # path.left = Node("bar")
    # path.left.left = Node("zee")
    # path.right = Node("baz")
    # path.right.right = Node("foo")
    # path.right.right.right = Node("bla")
    # pretty_print_path(path)

    # left_subtree = Node(4)
    # left_leaf, right_leaf = Node(3), Node(8)
    # left_subtree.left = left_leaf
    # left_subtree.right = right_leaf

    # tree = Node(5)
    # tree.right = Node(6)
    # tree.left = left_subtree
    # print(serialize(tree))
    # print(serialize(deserialize(serialize(tree))))
    # print(serialize(invert(tree)))

    # bst = Node(7)
    # insert(bst, 2)
    # insert(bst, 5)
    # insert(bst, 3)
    # insert(bst, 6)
    # insert(bst, 11)
    # insert(bst, 9)
    # insert(bst, 14)
    # insert(bst, 13)
    # print(is_bst(bst))

    # lca_ex = Node(6)
    # insert(lca_ex, 2)
    # insert(lca_ex, 8)

    # print(lca(lca_ex, 2, 8))
    pass
