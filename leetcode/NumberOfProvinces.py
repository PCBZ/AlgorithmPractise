from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            visited[i] = True
            for j, connected in enumerate(isConnected[i]):
                if not visited[j] and connected == 1:
                    dfs(j)

        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count

if __name__ == "__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print(Solution().findCircleNum(isConnected))