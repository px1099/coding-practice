""" Start of solution """
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        pre_end = 0
        n1, n2 = len(words1), len(words2)
        while pre_end < n1 and words1[pre_end] == words2[pre_end]:
            pre_end += 1
        for i in range(pre_end, n1):
            if words1[i] != words2[n2-n1+i]:
                return False
        return True
""" End of solution """


def solve():
    sentence1 = input()[1:-1]
    sentence2 = input()[1:-1]
    solver = Solution()
    result = solver.areSentencesSimilar(sentence1, sentence2)
    print(str(result).lower())


if __name__ == "__main__":
    solve()
