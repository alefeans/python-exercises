class QuickUnion:
    def __init__(self, n: int) -> None:
        self.ids = list(range(n))

    def __str__(self) -> str:
        return f"ids: {self.ids}"

    def root(self, p: int) -> int:
        while self.ids[p] != p:
            p = self.ids[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        pid, qid = self.root(p), self.root(q)
        self.ids[pid] = qid


if __name__ == "__main__":
    quick_union = QuickUnion(4)
    quick_union.union(1, 2)
    print(quick_union)
    print(f"Connected 1, 2? {quick_union.connected(1, 2)}")
    quick_union.union(1, 3)
    print(quick_union)
    print(f"Connected 0, 3? {quick_union.connected(0, 3)}")
    print(quick_union)
    print(f"Connected 1, 3? {quick_union.connected(1, 3)}")
