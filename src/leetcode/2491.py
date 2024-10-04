from typing import List


""" Start of solution """
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        sorted_skill = sorted(skill)
        team_skill = sorted_skill[0] + sorted_skill[-1]
        chemistry = 0
        for i in range(n//2):
            if sorted_skill[i] + sorted_skill[n-1-i] != team_skill:
                return -1
            chemistry += sorted_skill[i] * sorted_skill[n-1-i]
        return chemistry
""" End of solution """


def solve():
    skill = [int(x) for x in (input()[1:-1]).split(",")]
    solver = Solution()
    result = solver.dividePlayers(skill)
    print(result)


if __name__ == "__main__":
    solve()
