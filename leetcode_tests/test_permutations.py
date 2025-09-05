"""
Test cases for LeetCode Problem 46: Permutations.
"""

import pytest
from leetcode.permutations import Solution


class TestPermutations:
    """Test class for permutations problem."""

    def setup_method(self):
        """Set up test fixtures."""
        self.solution = Solution()

    @pytest.mark.parametrize("nums,expected_length", [
        # Basic test cases
        ([1, 2, 3], 6),          # 3! = 6 permutations
        ([0, 1], 2),             # 2! = 2 permutations
        ([1], 1),                # 1! = 1 permutation
        ([1, 2], 2),             # 2! = 2 permutations
        
        # Larger arrays
        ([1, 2, 3, 4], 24),      # 4! = 24 permutations
        ([5, 4, 6, 2], 24),      # 4! = 24 permutations
        
        # Negative numbers
        ([-1, 0, 1], 6),         # 3! = 6 permutations
        ([-2, -1], 2),           # 2! = 2 permutations
        
        # Mix of positive and negative
        ([-1, 2, -3], 6),        # 3! = 6 permutations
        ([10, -5, 0], 6),        # 3! = 6 permutations
    ])
    def test_permutations_count(self, nums, expected_length):
        """Test that the number of permutations is correct."""
        result = self.solution.permute(nums)
        assert len(result) == expected_length, f"Expected {expected_length} permutations, got {len(result)}"

    def test_single_element(self):
        """Test with single element."""
        nums = [42]
        result = self.solution.permute(nums)
        expected = [[42]]
        assert result == expected

    def test_two_elements(self):
        """Test with two elements."""
        nums = [1, 2]
        result = self.solution.permute(nums)
        
        # Should have exactly 2 permutations
        assert len(result) == 2
        assert [1, 2] in result
        assert [2, 1] in result

    def test_three_elements_specific(self):
        """Test specific case with three elements."""
        nums = [1, 2, 3]
        result = self.solution.permute(nums)
        
        expected_permutations = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        
        # Check count
        assert len(result) == 6
        
        # Check all expected permutations are present
        for perm in expected_permutations:
            assert perm in result, f"Missing permutation: {perm}"

    def test_all_permutations_are_valid(self):
        """Test that all generated permutations are valid."""
        nums = [1, 2, 3]
        result = self.solution.permute(nums)
        
        for perm in result:
            # Each permutation should have same length as original
            assert len(perm) == len(nums)
            
            # Each permutation should contain all original elements exactly once
            assert sorted(perm) == sorted(nums)
            
            # No duplicates within permutation
            assert len(set(perm)) == len(perm)

    def test_no_duplicate_permutations(self):
        """Test that no duplicate permutations are generated."""
        nums = [1, 2, 3, 4]
        result = self.solution.permute(nums)
        
        # Convert to tuples for set comparison
        result_set = set(tuple(perm) for perm in result)
        assert len(result_set) == len(result), "Found duplicate permutations"

    def test_empty_input_edge_case(self):
        """Test with empty array (edge case)."""
        nums = []
        result = self.solution.permute(nums)
        expected = [[]]  # One empty permutation
        assert result == expected

    def test_return_type(self):
        """Test that return type is correct."""
        nums = [1, 2]
        result = self.solution.permute(nums)
        
        assert isinstance(result, list)
        assert all(isinstance(perm, list) for perm in result)
        assert all(isinstance(x, int) for perm in result for x in perm)

    def test_original_array_unchanged(self):
        """Test that original array is not modified."""
        nums = [1, 2, 3]
        original_nums = nums.copy()
        
        self.solution.permute(nums)
        
        assert nums == original_nums, "Original array was modified"

    def test_large_array_performance(self):
        """Test with larger array to check basic performance."""
        nums = [1, 2, 3, 4, 5]  # 5! = 120 permutations
        result = self.solution.permute(nums)
        
        # Should generate 5! = 120 permutations
        assert len(result) == 120
        
        # Verify a few specific permutations exist
        assert [1, 2, 3, 4, 5] in result
        assert [5, 4, 3, 2, 1] in result

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, 0]
        result = self.solution.permute(nums)
        
        assert len(result) == 6
        
        # Check that all elements are preserved in each permutation
        for perm in result:
            assert sorted(perm) == sorted(nums)

    def test_duplicate_values_not_in_input(self):
        """Test assumes distinct integers as per problem statement."""
        # This test verifies the algorithm works correctly with distinct integers
        nums = [10, 20, 30]
        result = self.solution.permute(nums)
        
        # Should have 3! = 6 permutations
        assert len(result) == 6
        
        # All should be different
        result_tuples = set(tuple(perm) for perm in result)
        assert len(result_tuples) == 6

    def test_mathematical_factorial_property(self):
        """Test that n! permutations are generated for n elements."""
        import math
        
        test_cases = [
            ([1], 1),
            ([1, 2], 2), 
            ([1, 2, 3], 3),
            ([1, 2, 3, 4], 4)
        ]
        
        for nums, n in test_cases:
            result = self.solution.permute(nums)
            expected_count = math.factorial(n)
            assert len(result) == expected_count, f"For {n} elements, expected {expected_count} permutations"
