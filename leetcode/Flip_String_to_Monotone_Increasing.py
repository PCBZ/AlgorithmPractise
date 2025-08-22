class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for digit in s:
            if digit == '0':
                dp1 = min(dp0, dp1) + 1
            else:
                dp1 = min(dp0, dp1)
                dp0 += 1
        return min(dp0, dp1)




if __name__ == "__main__":
    s = "00110"
    print(Solution().minFlipsMonoIncr(s))  # Example usage