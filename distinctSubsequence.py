class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [ (n+1) * [0] for _ in range(m+1) ]
        for i in range(m+1):
            for j in range(n+1):
                if j == 0:
                    dp[i][j] = 1
                if i > 0 and j > 0:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[-1][-1]



s = "rabbbit"
t = "rabbit"

print(Solution().numDistinct(s, t))