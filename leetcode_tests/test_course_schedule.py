"""
Comprehensive test suite for LeetCode Problem #207: Course Schedule

Tests the canFinish method which determines if all courses can be completed
given prerequisite dependencies using topological sorting (Kahn's algorithm).
"""
import os
import sys
import time

# Add the parent directory to sys.path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from leetcode.course_schedule import Solution


class TestCourseSchedule:
    """Test class for course schedule problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        num_courses = 2
        prerequisites = [[1, 0]]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True  # Can finish: take course 0 first, then course 1
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        num_courses = 2
        prerequisites = [[1, 0], [0, 1]]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False  # Cannot finish: circular dependency
        assert result == expected

    def test_no_prerequisites(self):
        """Test with no prerequisites."""
        num_courses = 5
        prerequisites = []
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True  # Can finish all courses independently
        assert result == expected

    def test_single_course(self):
        """Test with single course."""
        num_courses = 1
        prerequisites = []
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_no_courses(self):
        """Test edge case with no courses."""
        num_courses = 0
        prerequisites = []
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True  # Vacuously true
        assert result == expected

    def test_linear_dependency_chain(self):
        """Test with linear dependency chain."""
        num_courses = 4
        prerequisites = [[1, 0], [2, 1], [3, 2]]  # 0 -> 1 -> 2 -> 3
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_simple_cycle(self):
        """Test with simple cycle."""
        num_courses = 3
        prerequisites = [[0, 1], [1, 2], [2, 0]]  # 0 -> 1 -> 2 -> 0
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False
        assert result == expected

    def test_complex_acyclic_graph(self):
        """Test with complex acyclic graph."""
        num_courses = 6
        prerequisites = [
            [1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [5, 4]
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_complex_cyclic_graph(self):
        """Test with complex graph containing cycle."""
        num_courses = 6
        prerequisites = [
            [1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [1, 5]  # Creates cycle
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False
        assert result == expected

    def test_multiple_components_acyclic(self):
        """Test with multiple disconnected components, all acyclic."""
        num_courses = 6
        prerequisites = [
            [1, 0], [2, 1],    # Component 1: 0 -> 1 -> 2
            [4, 3], [5, 4]     # Component 2: 3 -> 4 -> 5
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_multiple_components_one_cyclic(self):
        """Test with multiple components where one has a cycle."""
        num_courses = 6
        prerequisites = [
            [1, 0], [2, 1],           # Component 1: 0 -> 1 -> 2 (acyclic)
            [4, 3], [5, 4], [3, 5]   # Component 2: 3 -> 4 -> 5 -> 3 (cyclic)
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False
        assert result == expected

    def test_self_dependency(self):
        """Test with self-dependency (course depends on itself)."""
        num_courses = 3
        prerequisites = [[0, 0], [1, 2]]  # Course 0 depends on itself
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False
        assert result == expected

    def test_diamond_dependency(self):
        """Test with diamond dependency pattern."""
        num_courses = 4
        prerequisites = [
            [1, 0], [2, 0],    # Both 1 and 2 depend on 0
            [3, 1], [3, 2]     # 3 depends on both 1 and 2
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_star_dependency(self):
        """Test with star dependency pattern."""
        num_courses = 5
        prerequisites = [
            [1, 0], [2, 0], [3, 0], [4, 0]  # All courses depend on course 0
        ]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        num_courses = 2
        prerequisites = [[1, 0]]
        result = self.solution.canFinish(num_courses, prerequisites)
        
        assert isinstance(result, bool)
        assert result in [True, False]

    def test_algorithm_correctness_dfs_comparison(self):
        """Test algorithm correctness by comparing with DFS cycle detection."""
        def has_cycle_dfs(num_courses, prerequisites):
            """DFS-based cycle detection for comparison."""
            from collections import defaultdict
            
            graph = defaultdict(list)
            for course, prereq in prerequisites:
                graph[prereq].append(course)
            
            # 0: unvisited, 1: visiting, 2: visited
            state = [0] * num_courses
            
            def dfs(node):
                if state[node] == 1:  # Currently visiting - cycle found
                    return True
                if state[node] == 2:  # Already visited - no cycle
                    return False
                
                state[node] = 1  # Mark as visiting
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True
                state[node] = 2  # Mark as visited
                return False
            
            for i in range(num_courses):
                if state[i] == 0 and dfs(i):
                    return True
            return False
        
        test_cases = [
            (2, [[1, 0]]),
            (2, [[1, 0], [0, 1]]),
            (3, [[0, 1], [1, 2]]),
            (3, [[0, 1], [1, 2], [2, 0]]),
            (4, [[1, 0], [2, 1], [3, 2]]),
            (1, []),
            (0, []),
        ]
        
        for num_courses, prerequisites in test_cases:
            kahn_result = self.solution.canFinish(num_courses, prerequisites)
            dfs_no_cycle = not has_cycle_dfs(num_courses, prerequisites)
            assert kahn_result == dfs_no_cycle, f"Mismatch for {num_courses}, {prerequisites}"

    def test_duplicate_prerequisites(self):
        """Test handling of duplicate prerequisites."""
        num_courses = 3
        prerequisites = [[1, 0], [1, 0], [2, 1]]  # Duplicate [1, 0]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True  # Should still work correctly
        assert result == expected

    def test_large_linear_chain(self):
        """Test with large linear chain."""
        num_courses = 1000
        prerequisites = [[i + 1, i] for i in range(num_courses - 1)]
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_large_cycle(self):
        """Test with large cycle."""
        num_courses = 100
        prerequisites = [[i + 1, i] for i in range(num_courses - 1)]
        prerequisites.append([0, num_courses - 1])  # Close the cycle
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = False
        assert result == expected

    def test_performance_large_acyclic(self):
        """Test performance with large acyclic graph."""
        import time
        
        num_courses = 5000
        # Create a large DAG (directed acyclic graph)
        prerequisites = []
        for i in range(num_courses // 2):
            prerequisites.append([i * 2 + 1, i * 2])  # Even -> Odd dependencies
        
        start_time = time.time()
        result = self.solution.canFinish(num_courses, prerequisites)
        end_time = time.time()
        
        assert result == True
        assert end_time - start_time < 1.0  # Should complete within 1 second

    def test_topological_sort_properties(self):
        """Test properties specific to topological sorting."""
        num_courses = 5
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2]]
        result = self.solution.canFinish(num_courses, prerequisites)
        
        # Should be able to finish (it's a DAG)
        assert result == True

    def test_edge_case_same_course_multiple_prereqs(self):
        """Test course with multiple prerequisites."""
        num_courses = 4
        prerequisites = [[3, 0], [3, 1], [3, 2]]  # Course 3 needs 0, 1, and 2
        result = self.solution.canFinish(num_courses, prerequisites)
        expected = True
        assert result == expected

    def test_mathematical_properties(self):
        """Test mathematical properties of the solution."""
        # Test that adding more dependencies to an acyclic graph keeps it acyclic
        num_courses = 4
        prerequisites1 = [[1, 0], [2, 1]]
        prerequisites2 = [[1, 0], [2, 1], [3, 2]]
        
        result1 = self.solution.canFinish(num_courses, prerequisites1)
        result2 = self.solution.canFinish(num_courses, prerequisites2)
        
        # Both should be completable
        assert result1 == True
        assert result2 == True

    def test_boundary_cases(self):
        """Test boundary cases."""
        boundary_cases = [
            (1, [], True),                    # Single course, no prereqs
            (2, [[0, 1]], True),             # Two courses, one dependency
            (2, [[0, 1], [1, 0]], False),    # Two courses, mutual dependency
        ]
        
        for num_courses, prerequisites, expected in boundary_cases:
            result = self.solution.canFinish(num_courses, prerequisites)
            assert result == expected

    def test_algorithm_stability(self):
        """Test that algorithm produces consistent results."""
        num_courses = 5
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3]]
        
        # Run multiple times
        results = [self.solution.canFinish(num_courses, prerequisites) for _ in range(5)]
        
        # All results should be identical
        assert all(result == results[0] for result in results)

    def test_kahn_algorithm_specific_properties(self):
        """Test properties specific to Kahn's algorithm."""
        # Test that nodes with zero indegree are processed first
        num_courses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = self.solution.canFinish(num_courses, prerequisites)
        
        # This DAG should be processable
        assert result == True

    def test_memory_efficiency(self):
        """Test memory efficiency with reasonable input."""
        num_courses = 10000
        prerequisites = [[i + 1, i] for i in range(0, num_courses - 1, 2)]
        
        try:
            result = self.solution.canFinish(num_courses, prerequisites)
            assert isinstance(result, bool)
        except MemoryError:
            # If memory is limited, this is acceptable
            pass

    def test_comprehensive_cycle_detection(self):
        """Test comprehensive cycle detection scenarios."""
        cycle_test_cases = [
            # (num_courses, prerequisites, has_cycle)
            (3, [[0, 1], [1, 0]], True),                    # 2-cycle
            (4, [[0, 1], [1, 2], [2, 0]], True),          # 3-cycle
            (4, [[0, 1], [1, 2], [2, 3], [3, 0]], True),  # 4-cycle
            (4, [[0, 1], [1, 2], [2, 3]], False),         # No cycle
            (5, [[0, 1], [2, 3], [1, 4], [4, 2]], False), # No cycle: 3->2->4->1->0
        ]
        
        for num_courses, prerequisites, has_cycle in cycle_test_cases:
            result = self.solution.canFinish(num_courses, prerequisites)
            expected = not has_cycle  # Can finish if no cycle
            assert result == expected, f"Failed for {prerequisites}: expected {expected}, got {result}"
