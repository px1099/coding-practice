import json


""" Start of solution """
class MyCircularDeque:
    def __init__(self, k: int):
        self.size, self.cap = 0, k
        self.dequeue = [0] * k
        self.start, self.end = 0, 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.start = (self.start - 1) if (self.start > 0) else (self.cap - 1)
        self.dequeue[self.start] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dequeue[self.end] = value
        self.end = (self.end + 1) if (self.end < self.cap - 1) else 0
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) if (self.start < self.cap - 1) else 0
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.end = (self.end - 1) if (self.end > 0) else (self.cap - 1)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        idx = self.start
        return self.dequeue[idx]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        idx = (self.end - 1) if (self.end > 0) else (self.cap - 1)
        return self.dequeue[idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
""" End of solution """


def solve():
    func_list = json.loads(input())
    args_list = json.loads(input())
    obj = None
    results = []
    for func, args in zip(func_list, args_list):
        if func == "MyCircularDeque":
            obj = MyCircularDeque(*args)
            results.append("null")
            continue
        method = getattr(obj, func)
        val = method(*args)
        results.append(str(val).lower())
    result = "[" + ", ".join(results) + "]"
    print(result)


if __name__ == "__main__":
    tc = 1
    # tc = int(input())
    for t in range(tc):
        # print(f"Case #{t}: ", end=None)
        solve()
