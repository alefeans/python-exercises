class WeightedQuickUnion:
    def __init__(self, n: int) -> None:
        self.ids = list(range(n))
        self.sizes = [1 for _ in range(n)]

    def __str__(self) -> str:
        return f"ids: {self.ids}"

    def root(self, p: int) -> int:
        while self.ids[p] != p:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int) -> None:
        pid, qid = self.root(p), self.root(q)
        if pid == qid:
            return

        if self.sizes[pid] > self.sizes[qid]:
            self.ids[qid] = pid
            self.sizes[qid] += self.sizes[pid]
        else:
            self.ids[pid] = qid
            self.sizes[pid] += self.sizes[qid]


if __name__ == "__main__":
    quick_union = WeightedQuickUnion(10)
    quick_union.union(4, 3)
    quick_union.union(3, 8)
    quick_union.union(6, 5)
    quick_union.union(9, 4)
    quick_union.union(2, 1)
    quick_union.union(5, 0)
    quick_union.union(7, 2)
    quick_union.union(6, 1)
    quick_union.union(7, 3)
    print(quick_union)
    print(f"Connected 7, 4? {quick_union.connected(7, 4)}")
