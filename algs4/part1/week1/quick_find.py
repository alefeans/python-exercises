class QuickFind:
    def __init__(self, n: int) -> None:
        self.ids = list(range(n))

    def __str__(self) -> str:
        return f"ids: {self.ids}"

    def connected(self, p: int, q: int) -> bool:
        return self.ids[p] == self.ids[q]

    def union(self, p: int, q: int) -> None:
        pid, qid = self.ids[p], self.ids[q]
        for i, n in enumerate(self.ids):
            if n == pid:
                self.ids[i] = qid


if __name__ == "__main__":
    quick_find = QuickFind(4)
    quick_find.union(1, 2)
    print(quick_find)
    print(f"Connected 1, 2? {quick_find.connected(1, 2)}")
    quick_find.union(1, 3)
    print(quick_find)
    print(f"Connected 0, 3? {quick_find.connected(0, 3)}")
    print(quick_find)
    print(f"Connected 1, 3? {quick_find.connected(1, 3)}")
