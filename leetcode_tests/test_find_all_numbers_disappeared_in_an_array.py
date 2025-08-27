"""
Test cases for LeetCode Problem #448: Find All Numbers Disappeared in an Array
"""
import unittest
from leetcode.find_all_numbers_disappeared_in_an_array import Solution


class TestFindAllNumbersDisappeared(unittest.TestCase):
    """Test cases for the FindAllNumbersDisappeared solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test the first example case."""
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [5, 6]
        assert sorted(result) == sorted(expected)

    def test_example_case_2(self):
        """Test the second example case."""
        nums = [1, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [2]
        assert result == expected

    def test_no_missing_numbers(self):
        """Test case with no missing numbers."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = []
        assert result == expected

    def test_all_missing_except_one(self):
        """Test case where only one number is present."""
        nums = [1, 1, 1, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [2, 3, 4]
        assert sorted(result) == sorted(expected)

    def test_single_element_present(self):
        """Test single element array."""
        nums = [1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = []
        assert result == expected

    def test_single_element_missing(self):
        """Test single element missing."""
        nums = [1]  # Changed from [2] to follow constraint 1 ≤ a[i] ≤ n
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = []  # No missing numbers in this case
        assert result == expected

    def test_consecutive_duplicates(self):
        """Test with consecutive duplicate numbers."""
        nums = [1, 1, 2, 2]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [3, 4]
        assert sorted(result) == sorted(expected)

    def test_all_same_number(self):
        """Test with all same numbers."""
        nums = [3, 3, 3, 3, 3]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [1, 2, 4, 5]
        assert sorted(result) == sorted(expected)

    def test_reverse_order(self):
        """Test with numbers in reverse order."""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = []
        assert result == expected

    def test_missing_first_and_last(self):
        """Test missing first and last numbers."""
        nums = [2, 3, 4, 5, 6, 7, 8, 2]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [1, 8]  # Wait, this should be [1] since 8 is present
        # Let me recalculate: array has 8 elements, so we need 1-8
        # Present: 2,3,4,5,6,7,8,2 so missing is just [1]
        expected = [1]
        assert result == expected

    def test_alternating_pattern(self):
        """Test alternating pattern."""
        nums = [1, 3, 1, 3]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [2, 4]
        assert sorted(result) == sorted(expected)

    def test_large_gaps(self):
        """Test with large gaps in numbers."""
        nums = [1, 1, 1, 1, 1, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [2, 3, 4, 5, 6]
        assert sorted(result) == sorted(expected)

    def test_mixed_pattern(self):
        """Test with mixed missing pattern."""
        nums = [2, 4, 6, 2, 4, 6]  # Changed to follow constraints
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [1, 3, 5]
        assert sorted(result) == sorted(expected)

    def test_boundary_values(self):
        """Test with boundary values."""
        nums = [1, 2, 3, 4, 5, 6, 7, 1, 2]  # Changed to follow constraints
        result = self.solution.findDisappearedNumbers(nums.copy())
        # Array length is 9, so we need numbers 1-9
        # Missing: 8, 9
        expected = [8, 9]
        assert sorted(result) == sorted(expected)

    def test_duplicates_at_boundaries(self):
        """Test duplicates at array boundaries."""
        nums = [1, 2, 2, 3, 3, 1]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [4, 5, 6]
        assert sorted(result) == sorted(expected)

    def test_return_type_and_order(self):
        """Test that return type is list and order is correct."""
        nums = [2, 3, 2]  # Changed to follow constraints
        result = self.solution.findDisappearedNumbers(nums.copy())
        assert isinstance(result, list)
        assert all(isinstance(num, int) for num in result)
        assert result == sorted(result)

    def test_algorithm_correctness(self):
        """Test algorithm correctness with various patterns."""
        test_cases = [
            ([1], []),
            ([1, 1], [2]),  # Changed from ([2], [1]) to follow constraints
            ([1, 2], []),
            ([1, 1], [2]),  # Changed from ([1, 3], [2]) to follow constraints
            ([1, 1], [2]),  # Changed from ([2, 3], [1]) to follow constraints
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                result = self.solution.findDisappearedNumbers(nums.copy())
                assert sorted(result) == sorted(expected)

    def test_boundary_conditions(self):
        """Test edge cases and boundary conditions."""
        # Minimum case
        result = self.solution.findDisappearedNumbers([1])
        assert result == []
        
        # All duplicates
        result = self.solution.findDisappearedNumbers([2, 2])
        assert result == [1]

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create array with some missing numbers
        nums = [1] * 1000 + [500] * 1000  # 2000 elements, missing many numbers
        result = self.solution.findDisappearedNumbers(nums.copy())
        
        # Should find all missing numbers from 2 to 499 and 501 to 2000
        expected_count = 498 + 1500  # (499-2+1) + (2000-501+1)
        assert len(result) == expected_count

    def test_array_modification_safety(self):
        """Test that original array modification doesn't affect multiple calls."""
        nums = [1, 2, 1]  # Changed to follow constraints
        nums_copy = nums.copy()
        
        result1 = self.solution.findDisappearedNumbers(nums_copy)
        result2 = self.solution.findDisappearedNumbers(nums.copy())
        
        assert sorted(result1) == sorted(result2)

    def test_missing_in_middle(self):
        """Test missing numbers in the middle."""
        nums = [1, 2, 1, 2]  # Changed to follow constraints
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [3, 4]
        assert sorted(result) == sorted(expected)

    def test_pattern_validation(self):
        """Test specific patterns for correctness."""
        # Only even numbers present
        nums = [2, 4, 6, 2, 4, 6]
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [1, 3, 5]
        assert sorted(result) == sorted(expected)

    def test_deterministic_behavior(self):
        """Test that algorithm produces consistent results."""
        nums = [1, 3, 5, 1, 3]
        result1 = self.solution.findDisappearedNumbers(nums.copy())
        result2 = self.solution.findDisappearedNumbers(nums.copy())
        assert sorted(result1) == sorted(result2)

    def test_complete_sequence_gaps(self):
        """Test with complete sequence having specific gaps."""
        nums = [1, 1, 4, 4, 6, 6]  # Changed to follow constraints
        result = self.solution.findDisappearedNumbers(nums.copy())
        expected = [2, 3, 5]
        assert sorted(result) == sorted(expected)

    def test_negative_marking_algorithm(self):
        """Test that the negative marking algorithm works correctly."""
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        original_values = set(abs(x) for x in nums)
        
        result = self.solution.findDisappearedNumbers(nums.copy())
        
        # Verify all numbers from 1 to n are either in original or in result
        n = len(nums)
        all_numbers = set(range(1, n + 1))
        found_numbers = original_values.union(set(result))
        
        assert all_numbers == found_numbers

    def test_input_preservation_concept(self):
        """Test the concept of input preservation through copying."""
        original = [1, 2, 1, 2]  # Changed to follow constraints
        test_input = original.copy()
        
        result = self.solution.findDisappearedNumbers(test_input)
        
        # The method modifies the input array, but we used a copy
        # So we can verify the algorithm worked correctly
        expected = [3, 4]
        assert sorted(result) == sorted(expected)


if __name__ == "__main__":
    unittest.main()
