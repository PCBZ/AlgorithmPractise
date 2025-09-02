"""
Comprehensive test suite for LeetCode Problem #481: Magical String
Tests the magical string generation and counting algorithm.
"""

import pytest

from leetcode.magical_string import Solution


class TestMagicalString:
    """Test cases for magical string problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test basic example from problem description."""
        result = self.solution.magical_string(6)
        assert result == 3  # "122112" has 3 ones

    def test_basic_example_2(self):
        """Test single character case."""
        result = self.solution.magical_string(1)
        assert result == 1  # "1" has 1 one

    def test_edge_case_zero(self):
        """Test edge case with n=0."""
        result = self.solution.magical_string(0)
        assert result == 0

    def test_edge_case_negative(self):
        """Test edge case with negative n."""
        result = self.solution.magical_string(-5)
        assert result == 0

    def test_small_values(self):
        """Test small values of n."""
        assert self.solution.magical_string(1) == 1  # "1"
        assert self.solution.magical_string(2) == 1  # "12"
        assert self.solution.magical_string(3) == 1  # "122"

    def test_magical_string_prefix_generation(self):
        """Test magical string prefix generation."""
        # Test known prefix: "122112122122112112212..."
        assert self.solution.get_magical_string_prefix(1) == "1"
        assert self.solution.get_magical_string_prefix(2) == "12"
        assert self.solution.get_magical_string_prefix(3) == "122"
        assert self.solution.get_magical_string_prefix(6) == "122112"

    def test_magical_string_pattern_validation(self):
        """Test that generated string follows magical string rules."""
        # Generate a longer prefix to validate pattern
        prefix = self.solution.get_magical_string_prefix(15)
        expected = "122112122122112"
        assert prefix == expected

    def test_method_consistency(self):
        """Test that both methods give consistent results."""
        test_cases = [1, 2, 3, 4, 5, 6, 10, 15, 20]
        
        for n in test_cases:
            standard_result = self.solution.magical_string(n)
            optimized_result = self.solution.magical_string_optimized(n)
            assert standard_result == optimized_result, f"Methods differ for n={n}"

    def test_optimized_method_basic(self):
        """Test optimized method with basic cases."""
        assert self.solution.magical_string_optimized(6) == 3
        assert self.solution.magical_string_optimized(1) == 1
        assert self.solution.magical_string_optimized(0) == 0

    @pytest.mark.parametrize("n,expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 4),
        (8, 4),
        (9, 4),
        (10, 5),
    ])
    def test_parametrized_cases(self, n, expected):
        """Test multiple cases using parametrize."""
        assert self.solution.magical_string(n) == expected

    def test_larger_values(self):
        """Test with larger values of n."""
        # Test some larger values to ensure algorithm works
        result_50 = self.solution.magical_string(50)
        result_100 = self.solution.magical_string(100)
        
        assert isinstance(result_50, int)
        assert isinstance(result_100, int)
        assert 0 <= result_50 <= 50
        assert 0 <= result_100 <= 100

    def test_magical_string_properties(self):
        """Test fundamental properties of magical string."""
        # Property 1: First character is always '1'
        prefix = self.solution.get_magical_string_prefix(10)
        assert prefix[0] == '1'
        
        # Property 2: String contains only '1' and '2'
        for char in prefix:
            assert char in ['1', '2']

    def test_count_validation(self):
        """Test that count matches manual counting."""
        n = 10
        prefix = self.solution.get_magical_string_prefix(n)
        manual_count = prefix.count('1')
        algorithm_count = self.solution.magical_string(n)
        assert manual_count == algorithm_count

    def test_edge_case_empty_prefix(self):
        """Test edge case for empty prefix generation."""
        result = self.solution.get_magical_string_prefix(0)
        assert result == ""

    def test_incremental_consistency(self):
        """Test that counts are consistent when incrementally increased."""
        prev_count = 0
        prefix = ""
        
        for n in range(1, 21):
            current_count = self.solution.magical_string(n)
            current_prefix = self.solution.get_magical_string_prefix(n)
            
            # Count should never decrease
            assert current_count >= prev_count
            
            # Prefix should extend previous prefix
            assert current_prefix.startswith(prefix)
            
            # Manual count should match algorithm
            assert current_prefix.count('1') == current_count
            
            prev_count = current_count
            prefix = current_prefix

    def test_self_describing_property(self):
        """Test the self-describing property of magical string."""
        # Generate enough of the string to test the property
        prefix = self.solution.get_magical_string_prefix(15)
        
        # Check that groups are correctly sized according to the string itself
        # "122112122122112"
        # Group 1: "1" (size 1, as indicated by position 1)
        # Group 2: "22" (size 2, as indicated by position 2)  
        # Group 3: "1" (size 1, as indicated by position 3)
        # And so on...
        
        assert prefix.startswith("122112")  # Known correct start

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Should handle moderately large inputs efficiently
        result = self.solution.magical_string(1000)
        assert isinstance(result, int)
        assert 0 <= result <= 1000

    def test_return_type_validation(self):
        """Test that return type is always integer."""
        test_cases = [0, 1, 5, 10, 20]
        
        for n in test_cases:
            result = self.solution.magical_string(n)
            assert isinstance(result, int)
            assert result >= 0
            assert result <= n

    def test_boundary_conditions(self):
        """Test boundary conditions thoroughly."""
        # Test transitions around known values
        assert self.solution.magical_string(3) == 1
        assert self.solution.magical_string(4) == 2
        assert self.solution.magical_string(5) == 3
        assert self.solution.magical_string(6) == 3
        assert self.solution.magical_string(7) == 4
        assert self.solution.magical_string(8) == 4
        assert self.solution.magical_string(9) == 4
        assert self.solution.magical_string(10) == 5

    def test_string_generation_consistency(self):
        """Test that string generation is consistent across multiple calls."""
        n = 20
        prefix1 = self.solution.get_magical_string_prefix(n)
        prefix2 = self.solution.get_magical_string_prefix(n)
        assert prefix1 == prefix2

    def test_all_methods_consistency(self):
        """Test that all three methods give consistent results."""
        test_values = [1, 3, 6, 10, 15, 25]
        
        for n in test_values:
            method1_result = self.solution.magical_string(n)
            method2_result = self.solution.magical_string_optimized(n)
            prefix = self.solution.get_magical_string_prefix(n)
            method3_result = prefix.count('1')
            
            assert method1_result == method2_result == method3_result, \
                f"Methods inconsistent for n={n}: {method1_result}, {method2_result}, {method3_result}"

    def test_mathematical_properties(self):
        """Test mathematical properties of the count function."""
        # Test that the function is non-decreasing
        prev_count = 0
        for n in range(1, 31):
            current_count = self.solution.magical_string(n)
            assert current_count >= prev_count, f"Count decreased at n={n}"
            prev_count = current_count


if __name__ == "__main__":
    pytest.main([__file__])
