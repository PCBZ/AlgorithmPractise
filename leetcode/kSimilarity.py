from typing import List, Tuple
from collections import deque

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbors(s: str) -> List[str]:
            all_neighbors = []
            i = 0
            while i <= len(s) and s[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    list_s = list(s)
                    list_s[i], list_s[j] = list_s[j], list_s[i]
                    all_neighbors.append("".join(list_s))
            return all_neighbors
    
        queue = deque([(s1, 0)])
        visited = set(s1)
        while queue:
            s, step = queue.popleft()
            if s == s2:
                return step
            for neighbor in neighbors(s):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, step + 1))
        return -1



if __name__ == "__main__":
    s1 = "ab"
    s2 = "ba"
    print(Solution().kSimilarity(s1, s2))
