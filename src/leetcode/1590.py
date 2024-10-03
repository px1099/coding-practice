from typing import List


""" Start of solution """
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        result = len(nums)
        total_sum = 0
        for num in nums:
            total_sum = (total_sum + num) % p
        if total_sum == 0:
            return 0
        current_sum = 0
        remaining_sum = total_sum
        mod_map = {}
        for idx, num in enumerate(nums):
            mod_map[current_sum] = idx
            current_sum = (current_sum + num) % p
            remaining_sum = (remaining_sum - num) % p
            required_sum = (p - remaining_sum) % p
            if required_sum in mod_map:
                sub_length = idx + 1 - mod_map[required_sum]
                if sub_length < result:
                    result = sub_length
        result = result if result < len(nums) else -1
        return result
""" End of solution """


def solve():
    nums = [int(x) for x in (input()[1:-1]).split(",")]
    p = int(input())
    solver = Solution()
    result = solver.minSubarray(nums, p)
    print(result)


if __name__ == "__main__":
    solve()
