""" Start of solution """
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        alphabet_len = ord("z") - ord("a") + 1
        diff_counter = [0] * alphabet_len
        for c in s1:
            diff_counter[ord(c) - ord("a")] += 1
        for c in s2[:n1]:
            diff_counter[ord(c) - ord("a")] -= 1
        if not any(diff_counter):
            return True
        for i in range(n1, n2):
            diff_counter[ord(s2[i-n1]) - ord("a")] += 1
            diff_counter[ord(s2[i]) - ord("a")] -= 1
            if not any(diff_counter):
                return True
        return False
""" End of solution """


def solve():
    s1 = input()[1:-1]
    s2 = input()[1:-1]
    solver = Solution()
    result = solver.checkInclusion(s1, s2)
    print(str(result).lower())


if __name__ == "__main__":
    solve()
