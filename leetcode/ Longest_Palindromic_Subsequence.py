from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
    
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s1: str, s2: str) -> bool:
            i = j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    i += 1
                j += 1
            return i == len(s1)
        
        strs.sort(key=len, reverse=True)
        longest = -1
        n = len(strs)
        for i in range(n):
            is_uncommon = True
            for j in range(n):
                if i != j and isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            if is_uncommon:
                longest = max(longest, len(strs[i]))
        return longest

if __name__ == "__main__":
    s = "bbbab"
    print(Solution().longestPalindromeSubseq(s))
    strs = ["aaa","aaa","aa"]
    print(Solution().findLUSlength(strs))