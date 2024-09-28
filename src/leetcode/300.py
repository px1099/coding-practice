from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        next_valid_nums = []
        for x in nums:
            idx = bisect.bisect(next_valid_nums, x)
            next_valid = x + 1
            if idx >= len(next_valid_nums):
                next_valid_nums.append(next_valid)
            if next_valid < next_valid_nums[idx]:
                next_valid_nums[idx] = next_valid
        return len(next_valid_nums)


if __name__ == "__main__":
    tc = 1
    # tc = int(input())
    solver = Solution()
    for t in range(tc):
        # print(f"Case #{t}: ", end=None)
        nums = [int(x) for x in input()[1:-1].split(",")]
        print(solver.lengthOfLIS(nums))
