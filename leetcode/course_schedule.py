"""
LeetCode Problem #207: Course Schedule

URL: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

This is essentially a cycle detection problem in a directed graph.
"""
from typing import List
from collections import defaultdict


class Solution:
    """Solution for course schedule using topological sorting (Kahn's algorithm)."""

    def canFinish(self, total_courses: int, prerequisite_pairs: List[List[int]]) -> bool:
        """
        Determine if all courses can be finished given prerequisites.

        Uses Kahn's algorithm for topological sorting to detect cycles in the
        prerequisite dependency graph. If a cycle exists, not all courses can
        be completed.

        Args:
            total_courses: Total number of courses (labeled 0 to total_courses-1)
            prerequisite_pairs: List of [course, prerequisite] pairs where
                              prerequisite must be taken before course

        Returns:
            True if all courses can be finished, False if there's a cycle

        Time Complexity: O(V + E) where V is courses and E is prerequisites
        Space Complexity: O(V + E) for graph and indegree arrays
        """
        # Build adjacency list and calculate indegrees
        dependency_graph = defaultdict(list)
        indegree = [0] * total_courses

        for course, prerequisite in prerequisite_pairs:
            dependency_graph[prerequisite].append(course)
            indegree[course] += 1

        # Start with courses that have no prerequisites
        processing_queue = [i for i in range(total_courses) if indegree[i] == 0]

        completed_courses = 0
        while processing_queue:
            current_course = processing_queue.pop(0)
            completed_courses += 1

            # Process all courses that depend on the current course
            for dependent_course in dependency_graph[current_course]:
                indegree[dependent_course] -= 1
                if indegree[dependent_course] == 0:
                    processing_queue.append(dependent_course)

        return completed_courses == total_courses


if __name__ == "__main__":
    # Example test case
    example_num_courses = 4
    example_prerequisites = [[1, 0], [2, 1], [3, 2]]
    solution = Solution()
    print(solution.canFinish(example_num_courses, example_prerequisites))
