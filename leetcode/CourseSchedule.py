from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = numCourses * [0]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        
        queue = [i for i in range(numCourses) if indegree[i] == 0]

        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
    
        return visited == numCourses
        


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(Solution().canFinish(numCourses, prerequisites))