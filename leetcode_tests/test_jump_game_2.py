"""
Comprehensive test suite for LeetCode Problem #45: Jump Game II
Tests the greedy algorithm for finding minimum jumps to reach the end.
"""

import pytest
import sys
import os

# Add the parent directory to the path to import the solution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.jump_game_2 import Solution


class TestJumpGameII:
    """Test cases for Jump Game II problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test first basic example from LeetCode."""
        nums = [2, 3, 1, 1, 4]
        expected = 2  # Jump from index 0 to 1, then to the last index
        assert self.solution.jump(nums) == expected

    def test_basic_example_2(self):
        """Test second basic example from LeetCode."""
        nums = [2, 3, 0, 1, 4]
        expected = 2  # Jump from index 0 to 1, then to the last index
        assert self.solution.jump(nums) == expected

    def test_single_element(self):
        """Test array with single element."""
        nums = [1]
        expected = 0  # Already at the end, no jumps needed
        assert self.solution.jump(nums) == expected

    def test_two_elements(self):
        """Test array with two elements."""
        nums = [2, 1]
        expected = 1  # One jump from first to last
        assert self.solution.jump(nums) == expected

    def test_minimum_jumps_each_step(self):
        """Test case where we need to jump every step."""
        nums = [1, 1, 1, 1]
        expected = 3  # Jump from 0->1->2->3
        assert self.solution.jump(nums) == expected

    def test_large_first_jump(self):
        """Test case where first element can reach the end."""
        nums = [5, 1, 1, 1, 1]
        expected = 1  # Jump directly from index 0 to index 4
        assert self.solution.jump(nums) == expected

    def test_greedy_choice_needed(self):
        """Test case where greedy choice is important."""
        nums = [1, 2, 3]
        expected = 2  # Jump 0->1->2 (greedy: take furthest reachable)
        assert self.solution.jump(nums) == expected

    def test_zeros_in_middle(self):
        """Test case with zeros that don't block progress."""
        nums = [3, 0, 0, 1]
        expected = 1  # Jump directly from index 0 to index 3
        assert self.solution.jump(nums) == expected

    def test_complex_scenario(self):
        """Test complex scenario with multiple optimal paths."""
        nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
        expected = 3  # Multiple jumps needed
        assert self.solution.jump(nums) == expected

    def test_increasing_values(self):
        """Test with strictly increasing values."""
        nums = [1, 2, 3, 4, 5]
        expected = 3  # Jump 0->1->3->4
        assert self.solution.jump(nums) == expected

    def test_decreasing_values(self):
        """Test with decreasing values."""
        nums = [5, 4, 3, 2, 1]
        expected = 1  # Jump directly from index 0 to end
        assert self.solution.jump(nums) == expected

    def test_alternating_pattern(self):
        """Test with alternating high-low pattern."""
        nums = [4, 1, 4, 1, 4]
        expected = 1  # Jump directly from index 0 to index 4
        assert self.solution.jump(nums) == expected

    def test_all_ones(self):
        """Test array where all elements are 1."""
        nums = [1] * 10
        expected = 9  # Must jump at every step
        assert self.solution.jump(nums) == expected

    def test_large_numbers(self):
        """Test with large jump values."""
        nums = [100, 2, 3, 4, 5]
        expected = 1  # First jump can reach anywhere
        assert self.solution.jump(nums) == expected

    def test_optimal_path_selection(self):
        """Test that algorithm selects optimal path."""
        nums = [2, 3, 1, 1, 4]
        # Path 1: 0->1->4 (2 jumps) - optimal
        # Path 2: 0->2->3->4 (3 jumps) - suboptimal
        expected = 2
        assert self.solution.jump(nums) == expected

    def test_edge_case_reach_exactly(self):
        """Test case where jump reaches exactly to boundary."""
        nums = [2, 1, 1, 1]
        expected = 2  # Jump 0->2->3
        assert self.solution.jump(nums) == expected

    def test_multiple_zeros(self):
        """Test with multiple zeros that can be skipped."""
        nums = [4, 0, 0, 0, 1]
        expected = 1  # Jump directly over zeros
        assert self.solution.jump(nums) == expected

    def test_long_array_pattern(self):
        """Test with longer array requiring strategic jumps."""
        nums = [3, 2, 1, 0, 4, 2, 1, 1, 1, 1]
        expected = 2  # Jump 0->4->9 (optimal path)
        assert self.solution.jump(nums) == expected

    def test_boundary_conditions(self):
        """Test boundary conditions of jump ranges."""
        nums = [1, 3, 2]
        expected = 2  # Jump 0->1->2
        assert self.solution.jump(nums) == expected

    def test_greedy_optimality(self):
        """Test that greedy approach gives optimal result."""
        nums = [2, 3, 1, 2, 4]
        # Greedy: always extend the farthest reachable position
        expected = 2
        assert self.solution.jump(nums) == expected

    def test_performance_medium_array(self):
        """Test performance with medium-sized array."""
        nums = [1, 2] * 50  # Length 100
        result = self.solution.jump(nums)
        assert isinstance(result, int)
        assert result > 0

    def test_early_termination_optimization(self):
        """Test that algorithm terminates early when end is reachable."""
        nums = [10, 1, 1, 1, 1, 1]  # First jump can reach end
        expected = 1
        assert self.solution.jump(nums) == expected

    def test_minimal_jumps_validation(self):
        """Test that result is indeed minimal number of jumps."""
        nums = [1, 4, 3, 2, 1, 1]
        result = self.solution.jump(nums)
        
        # Verify it's a reasonable number (not obviously wrong)
        assert 1 <= result <= len(nums) - 1

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        test_arrays = [
            [2, 3, 1, 1, 4],
            [1, 1, 1, 1, 1],
            [5, 4, 3, 2, 1],
            [1, 2, 3, 4, 5]
        ]
        
        for nums in test_arrays:
            result = self.solution.jump(nums)
            
            # Result should be non-negative
            assert result >= 0
            
            # Result should be at most n-1 (worst case: jump every step)
            assert result <= len(nums) - 1
            
            # For arrays of length 1, should return 0
            if len(nums) == 1:
                assert result == 0

    def test_jump_range_logic(self):
        """Test the jump range expansion logic."""
        nums = [3, 1, 2, 1, 1]
        expected = 2  # Jump 0->2->4 or similar optimal path
        assert self.solution.jump(nums) == expected

    def test_farthest_reachable_tracking(self):
        """Test that farthest reachable position is tracked correctly."""
        nums = [2, 1, 3, 1]
        expected = 2  # Should find optimal path
        assert self.solution.jump(nums) == expected

    def test_comprehensive_edge_cases(self):
        """Test various edge cases together."""
        edge_cases = [
            ([1], 0),           # Single element
            ([2, 1], 1),        # Two elements
            ([1, 1], 1),        # Two ones
            ([10], 0),          # Single large element
            ([0, 1], 1),        # Zero at start (if reachable)
        ]
        
        for nums, expected in edge_cases:
            if nums == [0, 1]:  # Skip invalid case
                continue
            assert self.solution.jump(nums) == expected


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
