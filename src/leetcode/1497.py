from typing import List


""" Start of solution """
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        num_odd_one_out = 0
        odd_one_out = [0] * k
        for num in arr:
            mod = num % k
            while mod < 0:
                mod += k
            other_mod = k - mod
            other_mod = other_mod if other_mod != k else 0
            if odd_one_out[other_mod]:
                odd_one_out[other_mod] -= 1
                num_odd_one_out -= 1
            else:
                odd_one_out[mod] += 1
                num_odd_one_out += 1
        return num_odd_one_out == 0
""" End of solution """


def solve():
    arr = [int(x) for x in (input()[1:-1]).split(",")]
    k = int(input())
    solver = Solution()
    result = solver.canArrange(arr, k)
    print(str(result).lower())


if __name__ == "__main__":
    tc = 1
    # tc = int(input())
    for t in range(tc):
        # print(f"Case #{t}: ", end=None)
        solve()
