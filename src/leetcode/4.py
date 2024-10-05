from typing import List, Tuple


""" Start of solution """
import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if (m + n) % 2:
            return self.findSortedArrays(nums1, nums2, (m+n)//2)
        left_median = self.findSortedArrays(nums1, nums2, (m+n)//2 - 1)
        right_median = self.findSortedArrays(nums1, nums2, (m+n)//2)
        return (left_median + right_median) / 2.0
    
    def findSortedArrays(self, nums1: List[int], nums2: List[int], idx: int) -> int:
        m, n = len(nums1), len(nums2)
        l1, r1 = 0, m-1
        l2, r2 = 0, n-1
        if m > idx:
            r1 = idx
        if n > idx:
            r2 = idx
        alternate_flag = False
        limit = 1000000
        for _ in range(limit):
            alternate_flag = not alternate_flag
            if alternate_flag:
                if l1 > r1:
                    continue
                c = (l1 + r1) // 2
                left_idx = c + bisect.bisect_left(nums2, nums1[c])
                right_idx = c + bisect.bisect_right(nums2, nums1[c])
                if left_idx > idx:
                    r1 = c - 1
                elif right_idx < idx:
                    l1 = c + 1
                else:
                    return nums1[c]
            else:
                if l2 > r2:
                    continue
                c = (l2 + r2) // 2
                left_idx = c + bisect.bisect_left(nums1, nums2[c])
                right_idx = c + bisect.bisect_right(nums1, nums2[c])
                if left_idx > idx:
                    r2 = c - 1
                elif right_idx < idx:
                    l2 = c + 1
                else:
                    return nums2[c]
        return -1
""" End of solution """


def solve():
    nums1 = [int(x) for x in (input()[1:-1]).split(",") if x]
    nums2 = [int(x) for x in (input()[1:-1]).split(",") if x]
    solver = Solution()
    result = solver.findMedianSortedArrays(nums1, nums2)
    print(f"{result:.5f}")


if __name__ == "__main__":
    solve()
