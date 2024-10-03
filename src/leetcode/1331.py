from typing import List


""" Start of solution """
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        rank_map = {num: idx + 1 for idx, num in enumerate(s)}
        return [rank_map[num] for num in arr]
""" End of solution """


def solve():
    arr = [int(x) for x in (input()[1:-1]).split(",")]
    solver = Solution()
    result = solver.arrayRankTransform(arr)
    print(f"[{','.join([str(x) for x in result])}]")


if __name__ == "__main__":
    solve()
