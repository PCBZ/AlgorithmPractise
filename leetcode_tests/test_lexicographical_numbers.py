"""
Comprehensive test suite for LeetCode Problem #386: Lexicographical Numbers.
Tests the DFS-based solution for generating numbers in lexicographical order.
"""

import pytest
from leetcode.lexicographical_numbers import Solution


class TestLexicographicalNumbers:
    """Test cases for lexicographical numbers generation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_13(self):
        """Test basic example with n=13."""
        result = self.solution.lexical_order(13)
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

    def test_basic_example_2(self):
        """Test basic example with n=2."""
        result = self.solution.lexical_order(2)
        expected = [1, 2]
        assert result == expected

    def test_single_digit(self):
        """Test with single digit n=1."""
        result = self.solution.lexical_order(1)
        expected = [1]
        assert result == expected

    def test_single_digit_9(self):
        """Test with n=9 (all single digits)."""
        result = self.solution.lexical_order(9)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

    def test_exactly_10(self):
        """Test with n=10 (includes first two-digit number)."""
        result = self.solution.lexical_order(10)
        expected = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

    def test_exactly_100(self):
        """Test with n=100 (includes first three-digit number)."""
        result = self.solution.lexical_order(100)
        expected = [1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                    2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                    3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                    4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                    5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                    6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                    7, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                    8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                    9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        assert result == expected

    def test_partial_range_23(self):
        """Test with n=23."""
        result = self.solution.lexical_order(23)
        expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                    2, 20, 21, 22, 23, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

    def test_partial_range_101(self):
        """Test with n=101 (just past 100)."""
        result = self.solution.lexical_order(101)
        # Should be same as 100 plus 101 in correct position
        expected = [1, 10, 100, 101, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                    2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                    3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                    4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
                    5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
                    6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
                    7, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                    8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
                    9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        assert result == expected

    def test_large_number_999(self):
        """Test with n=999 (all 3-digit numbers)."""
        result = self.solution.lexical_order(999)
        # Should start with 1, 10, 100, 1000 (if <= 999), 1001, ..., 199
        assert result[0] == 1
        assert result[1] == 10
        assert result[2] == 100
        assert result[3] == 101
        assert len(result) == 999
        # Check that all numbers from 1 to 999 are present
        assert sorted(result) == list(range(1, 1000))

    def test_large_number_1000(self):
        """Test with n=1000."""
        result = self.solution.lexical_order(1000)
        assert result[0] == 1
        assert result[1] == 10
        assert result[2] == 100
        assert result[3] == 1000  # 1000 comes before 101
        assert result[4] == 101
        assert len(result) == 1000
        assert sorted(result) == list(range(1, 1001))

    def test_result_length_consistency(self):
        """Test that result length always equals n."""
        test_cases = [1, 5, 10, 15, 23, 50, 99, 100, 150, 200]
        for n in test_cases:
            result = self.solution.lexical_order(n)
            assert len(result) == n, f"Length mismatch for n={n}"

    def test_result_contains_all_numbers(self):
        """Test that result contains all numbers from 1 to n."""
        test_cases = [1, 9, 10, 25, 100, 150]
        for n in test_cases:
            result = self.solution.lexical_order(n)
            assert sorted(result) == list(range(1, n + 1)), f"Missing numbers for n={n}"

    def test_lexicographical_order_property(self):
        """Test that result is in lexicographical order."""
        test_cases = [13, 25, 100, 150]
        for n in test_cases:
            result = self.solution.lexical_order(n)
            str_result = [str(num) for num in result]
            assert str_result == sorted(str_result), f"Not lexicographical for n={n}"

    def test_first_element_always_1(self):
        """Test that first element is always 1."""
        test_cases = [1, 5, 10, 50, 100, 500, 1000]
        for n in test_cases:
            result = self.solution.lexical_order(n)
            assert result[0] == 1, f"First element not 1 for n={n}"

    def test_specific_ordering_patterns(self):
        """Test specific ordering patterns in lexicographical sequence."""
        # Test that 10 comes before 2
        result = self.solution.lexical_order(15)
        assert result.index(10) < result.index(2)
        
        # Test that 100 comes before 11
        result = self.solution.lexical_order(150)
        assert result.index(100) < result.index(11)

        # Test that 11 comes before 2
        result = self.solution.lexical_order(15)
        assert result.index(11) < result.index(2)

    def test_dfs_depth_boundaries(self):
        """Test DFS behavior at different depth boundaries."""
        # Test single digit boundary
        result = self.solution.lexical_order(9)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

        # Test two-digit boundary
        result = self.solution.lexical_order(19)
        assert result.index(10) == 1
        assert result.index(19) == 10
        assert result.index(2) == 11

    def test_consecutive_numbers_pattern(self):
        """Test patterns with consecutive numbers."""
        result = self.solution.lexical_order(12)
        expected = [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected

        # Verify 10, 11, 12 are consecutive in result
        assert result[1:4] == [10, 11, 12]

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        n = 123
        result = self.solution.lexical_order(n)
        
        # Property 1: Correct length
        assert len(result) == n
        
        # Property 2: All numbers present
        assert set(result) == set(range(1, n + 1))
        
        # Property 3: Lexicographical ordering
        str_nums = [str(num) for num in result]
        assert str_nums == sorted(str_nums)
        
        # Property 4: No duplicates
        assert len(result) == len(set(result))

    def test_performance_medium_input(self):
        """Test performance with medium-sized input."""
        n = 1000
        result = self.solution.lexical_order(n)
        assert len(result) == n
        assert result[0] == 1
        assert sorted(result) == list(range(1, n + 1))

    def test_edge_case_boundary_values(self):
        """Test edge cases at boundary values."""
        # Test powers of 10
        for power in [1, 10, 100, 1000]:
            result = self.solution.lexical_order(power)
            assert len(result) == power
            assert result[0] == 1
            
        # Test values just before powers of 10
        for power in [9, 99, 999]:
            result = self.solution.lexical_order(power)
            assert len(result) == power
            assert result[0] == 1

    def test_dfs_recursion_termination(self):
        """Test that DFS recursion terminates correctly."""
        # Test various sizes to ensure no infinite recursion
        test_sizes = [1, 5, 15, 50, 100, 200, 500]
        for n in test_sizes:
            result = self.solution.lexical_order(n)
            assert isinstance(result, list)
            assert all(isinstance(x, int) for x in result)
            assert len(result) == n

    def test_lexicographical_ordering_verification(self):
        """Verify lexicographical ordering with string comparison."""
        n = 50
        result = self.solution.lexical_order(n)
        
        # Convert to strings and verify ordering
        str_result = [str(num) for num in result]
        for i in range(len(str_result) - 1):
            assert str_result[i] <= str_result[i + 1], \
                f"Order violation at {str_result[i]} -> {str_result[i + 1]}"

    def test_specific_number_positions(self):
        """Test positions of specific numbers in sequence."""
        result = self.solution.lexical_order(25)
        
        # Check specific positions
        assert result.index(1) == 0
        assert result.index(10) == 1
        
        # 2 should come after all numbers starting with 1
        pos_2 = result.index(2)
        pos_19 = result.index(19) if 19 in result else -1
        if pos_19 != -1:
            assert pos_2 > pos_19

    def test_comprehensive_small_examples(self):
        """Test comprehensive small examples for manual verification."""
        # n=3: [1, 2, 3]
        assert self.solution.lexical_order(3) == [1, 2, 3]
        
        # n=11: [1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9]
        assert self.solution.lexical_order(11) == [1, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # n=20: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
        expected_20 = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
        assert self.solution.lexical_order(20) == expected_20

    def test_return_type_validation(self):
        """Test that return type is correct."""
        result = self.solution.lexical_order(10)
        assert isinstance(result, list)
        assert all(isinstance(x, int) for x in result)
        assert all(x > 0 for x in result)


if __name__ == "__main__":
    pytest.main([__file__])
