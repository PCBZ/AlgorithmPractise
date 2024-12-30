from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        res = []
        def dfs(node: str):
            while graph[node]:
                next_node = heapq.heappop(graph[node])
                dfs(next_node)
            res.append(node)
        dfs("JFK")
        return res[::-1]



if __name__ == "__main__":
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(Solution().findItinerary(tickets))