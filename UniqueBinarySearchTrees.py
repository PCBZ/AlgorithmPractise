class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        def traceBST(start: int, end: int) -> int:
            if start >= end:
                return 1
            if (start, end) in memo:
                return memo[(start, end)]
            total_count = 0
            for i in range(start, end+1):
                left_count = traceBST(start, i-1)
                right_count = traceBST(i+1, end)
                total_count += left_count * right_count
            memo[(start, end)] = total_count
            return total_count

        return traceBST(1, n)

n = 19
print(Solution().numTrees(n))