""" Start of solution """
class Solution:
    def minLength(self, s: str) -> int:
        result = 0
        stack = []
        for c in s:
            if c == "A" or c == "C":
                stack.append(c)
            elif c == "B" and len(stack) > 0 and stack[-1] == "A":
                stack.pop()
            elif c == "D" and len(stack) > 0 and stack[-1] == "C":
                stack.pop()
            else:
                result += len(stack)
                result += 1
                stack.clear()
        result += len(stack)
        return result
""" End of solution """


def solve():
    s = input()[1:-1]
    solver = Solution()
    result = solver.minLength(s)
    print(result)


if __name__ == "__main__":
    solve()
