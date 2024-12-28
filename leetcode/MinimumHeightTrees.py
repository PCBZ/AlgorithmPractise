from typing import List
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        leaves = deque([node for node in graph if len(graph[node]) == 1])

        remaing_count = n
        while remaing_count > 2:
            leaf_count = len(leaves)
            remaing_count -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
        return list(leaves)


if __name__ == "__main__":
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print(Solution().findMinHeightTrees(n, edges))