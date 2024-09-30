from dataclasses import dataclass, field
from typing import Any
import heapq
import itertools


@dataclass(order=True)
class PrioritizedItem:
    item: Any = field(compare=False)
    priority: int = field(compare=False)
    min_pq_priority: int = field(repr=False)
    entry_number: int = field(repr=False)


class PriorityQueue:
    def __init__(self, max_queue: bool = False) -> None:
        self.pq: list[PrioritizedItem] = []
        self.p_factor = -1 if max_queue else 1
        self.entry_counter = itertools.count()

    def __len__(self) -> int:
        return len(self.pq)

    def top(self) -> PrioritizedItem:
        return self.pq[0]

    def push(self, priority: int, item: Any = None) -> None:
        min_pq_priority = self.p_factor * priority
        entry_number = next(self.entry_counter)
        pq_item = PrioritizedItem(item, priority, min_pq_priority, entry_number)
        heapq.heappush(self.pq, pq_item)

    def pop(self) -> PrioritizedItem:
        return heapq.heappop(self.pq)


def solve():
    n = int(input())
    potions = [int(x) for x in input().split()]
    drank_potions = PriorityQueue()
    hp = 0
    for a in potions:
        if hp + a >= 0:
            hp += a
            drank_potions.push(a)
            continue
        if len(drank_potions) == 0:
            continue
        b = drank_potions.top().priority
        if a <= b:
            continue
        drank_potions.pop()
        drank_potions.push(a)
        hp += (a - b)
    result = len(drank_potions)
    print(result)


if __name__ == "__main__":
    tc = 1
    # tc = int(input())
    for t in range(tc):
        # print(f"Case #{t}: ", end=None)
        solve()
