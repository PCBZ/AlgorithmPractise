from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        memo = {}
        def backTrace(start: int):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            path = []
            for end in range(1, n+1):
                word = s[start:end]
                if word in wordDict:
                    rest = backTrace(end)
                    for sentence in rest:
                        if sentence:
                            path.append(word + " " + sentence)
                        else:
                            path.append(word)
            memo[start] = path
            return path
        
        return backTrace(0)


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))