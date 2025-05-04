class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [0] * (1 + n)
        dp[0] = 1.0
        window_sum = 1.0
        final_prob = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            else:
                final_prob += dp[i]

            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]

        return final_prob 




if __name__ == "__main__":
    n = 10
    k = 1
    maxPts = 10
    print(Solution().new21Game(n, k, maxPts))
    n = 6
    k = 1
    maxPts = 10
    print(Solution().new21Game(n, k, maxPts))
    n = 21
    k = 17
    maxPts = 10
    print(Solution().new21Game(n, k, maxPts))