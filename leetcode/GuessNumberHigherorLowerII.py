class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        def dfs(left: int, right: int) -> int:
            if (left, right) in memo:
                return memo[(left, right)]
            if left >= right:
                return 0
            min_val = float('inf')
            for i in range(left, right):
                min_val = min(min_val, max(dfs(left, i - 1), dfs(i + 1, right)) + i)
            memo[(left, right)] = min_val
            return min_val
        return dfs(1, n)


if __name__ == "__main__":
    n = 10
    print(Solution().getMoneyAmount(n))