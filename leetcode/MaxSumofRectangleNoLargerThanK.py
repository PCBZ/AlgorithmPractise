from typing import List

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
        print(prefix_sum)

        max_area = 0
        for i in range(m):
            for j in range(n):
                for k in range(i+1, m):
                    for t in range(j+1, n):
                        area = prefix_sum[k+1][t+1] - prefix_sum[k+1][j] - prefix_sum[i][t+1] + prefix_sum[i][j]
                        print(area)


if __name__ == "__main__":
    matrix = [[1,0,1],[0,-2,3]]
    k = 2
    print(Solution().maxSumSubmatrix(matrix, k))