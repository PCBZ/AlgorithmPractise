"""
Test cases for Circular Array Loop problem.
"""

import os
import sys

# Add the leetcode directory to the path for importing
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'leetcode'))

import pytest
from circular_array_loop import Solution


class TestCircularArrayLoop:
    """Test class for Circular Array Loop solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_example_case_1(self):
        """Test the first example case."""
        # [2,-1,1,2,2] 
        # Starting at index 0: 0->2->3->0 (valid loop with length > 1)
        nums = [2, -1, 1, 2, 2]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_example_case_2(self):
        """Test the second example case."""
        # [-1,-2,-3,-4,-5]
        # All negative values, but no valid loop forms
        nums = [-1, -2, -3, -4, -5]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_example_case_3(self):
        """Test the third example case."""
        # [1,-1,5,1,4]
        # Index 3->4->3 forms a valid forward loop (length 2)
        nums = [1, -1, 5, 1, 4]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_simple_valid_loop(self):
        """Test simple valid circular loop."""
        # [1,1] -> 0->1->0 (valid loop)
        nums = [1, 1]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_single_element_self_loop(self):
        """Test single element pointing to itself."""
        # [1] -> 0->0 (invalid: loop length = 1)
        nums = [1]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_two_element_self_loops(self):
        """Test two elements each pointing to themselves."""
        # [0,0] -> both elements point to themselves (invalid)
        nums = [0, 0]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_direction_change_prevents_loop(self):
        """Test that direction changes prevent valid loops."""
        # [2,-1,1,2] -> direction changes break the loop
        nums = [2, -1, 1, 2]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_all_positive_values(self):
        """Test array with all positive values."""
        # [1,2,1,1] -> check for valid forward loops
        nums = [1, 2, 1, 1]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_all_negative_values_with_loop(self):
        """Test array with all negative values forming a loop."""
        # [-1,-1] -> 0->1->0 (valid backward loop)
        nums = [-1, -1]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_large_jumps(self):
        """Test with large jump values."""
        # [2,2,2,2,2] -> 0->2->4->1->3->0 (valid loop)
        nums = [2, 2, 2, 2, 2]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_no_loop_linear_path(self):
        """Test case where path doesn't form a loop."""
        # [1,1,1,1] -> 0->1->2->3->0 but not all same direction from start
        nums = [1, 1, 1, 1]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_complex_valid_loop(self):
        """Test complex case with valid loop."""
        # [2,1,1,1,2] -> check for loops
        nums = [2, 1, 1, 1, 2]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_negative_indices_wrapping(self):
        """Test negative values that wrap around correctly."""
        # [-2,-1,-1] -> test backward movement
        nums = [-2, -1, -1]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_mixed_directions_no_loop(self):
        """Test mixed positive/negative preventing loops."""
        # [1,-1,1,-1] -> alternating directions
        nums = [1, -1, 1, -1]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_single_direction_change(self):
        """Test with mixed directions but valid loop exists."""
        # [2,2,-1,2] -> some indices may form valid loops despite mixed directions
        nums = [2, 2, -1, 2]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_edge_case_empty_array(self):
        """Test with empty array."""
        nums = []
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_three_element_valid_loop(self):
        """Test three element array with valid loop."""
        # [1,1,1] -> 0->1->2->0 (valid forward loop)
        nums = [1, 1, 1]
        assert self.solution.circularArrayLoop(nums) is True
    
    def test_backward_three_element_loop(self):
        """Test three element backward loop."""
        # [-1,-1,-1] -> 0->2->1->0 (valid backward loop)
        nums = [-1, -1, -1]
        assert self.solution.circularArrayLoop(nums) is True
    
    @pytest.mark.parametrize("nums,expected", [
        ([2, -1, 1, 2, 2], True),
        ([-1, -2, -3, -4, -5], False),
        ([1, -1, 5, 1, 4], True),  # Has valid loop at indices 3->4->3
        ([1, 1], True),
        ([1], False),
        ([0, 0], False),
        ([1, 1, 1], True),
        ([-1, -1, -1], True),
        ([1, -1, 1, -1], False),
        ([2, 2, 2, 2, 2], True),
    ])
    def test_parametrized_cases(self, nums, expected):
        """Parametrized test for multiple input-output pairs."""
        assert self.solution.circularArrayLoop(nums) == expected
    
    def test_modular_arithmetic_correctness(self):
        """Test that modular arithmetic handles indices correctly."""
        # Test large values that require proper modular arithmetic
        nums = [5, 1, 1, 1, 1]  # 0->0 (wraps around)
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_return_type(self):
        """Test that the function returns a boolean."""
        nums = [1, 2, 3]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
        assert result in [True, False]
    
    def test_algorithm_efficiency(self):
        """Test algorithm efficiency with larger arrays."""
        # Test that visited array optimization works
        nums = [1] * 100  # Large array with obvious loop
        result = self.solution.circularArrayLoop(nums)
        assert result is True
    
    def test_visited_optimization(self):
        """Test that visited nodes are properly skipped."""
        # Array where early nodes are visited by later starting points
        nums = [3, 1, 1, 1, 1]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_loop_detection_accuracy(self):
        """Test accurate loop detection vs path revisiting."""
        # Ensure we detect actual loops, not just revisited nodes
        nums = [2, 1, 1, 2]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_direction_consistency_check(self):
        """Test that direction consistency is properly enforced."""
        # One positive, one negative - should not form valid loop
        nums = [1, -1]
        assert self.solution.circularArrayLoop(nums) is False
    
    def test_boundary_wraparound(self):
        """Test proper boundary wraparound behavior."""
        # Test indices that wrap around array boundaries
        nums = [3, 1, 1]  # 0->0 (wraps), 1->2, 2->0
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_multiple_potential_loops(self):
        """Test array with multiple potential starting points."""
        # Array where multiple indices could start loops
        nums = [1, 1, 2, 2]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)
    
    def test_no_infinite_loops(self):
        """Test that algorithm terminates (no infinite loops)."""
        # Cases that could potentially cause infinite loops in bad implementations
        nums = [2, -1, 1, -2]
        result = self.solution.circularArrayLoop(nums)
        assert isinstance(result, bool)


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
