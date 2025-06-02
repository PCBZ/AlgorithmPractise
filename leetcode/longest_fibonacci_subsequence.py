from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {ele: index for index, ele in enumerate(arr)}
        n = len(arr)
        dp = [[2] * n for _ in range(n)] 
        longest = 0
        for i in range(n):
            for j in range(i):
                first = arr[i] - arr[j]
                if first < arr[j] and first in index_map:
                    new_idx = index_map[first]
                    dp[j][i] = dp[new_idx][j] + 1
                    longest = max(longest, dp[j][i])
        return longest if longest >= 3 else 0

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(Solution().lenLongestFibSubseq(arr))  # Output: 5
    arr = [1, 3, 7, 11, 12, 14, 18]
    print(Solution().lenLongestFibSubseq(arr))  # Output: 3
    arr = [1, 2, 3]
    print(Solution().lenLongestFibSubseq(arr))  # Output: 3

