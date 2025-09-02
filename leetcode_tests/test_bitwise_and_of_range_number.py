"""
Test cases for Bitwise AND of Numbers Range problem.
"""


import pytest
from leetcode.bitwise_and_of_range_number import Solution


class TestBitwiseAndOfRange:
    """Test class for Bitwise AND of Numbers Range solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_simple_range_5_7(self):
        """Test the example case [5, 7]."""
        # 5 = 101, 6 = 110, 7 = 111
        # AND = 100 = 4
        assert self.solution.rangeBitwiseAnd(5, 7) == 4
    
    def test_range_0_0(self):
        """Test single number range [0, 0]."""
        assert self.solution.rangeBitwiseAnd(0, 0) == 0
    
    def test_range_1_1(self):
        """Test single number range [1, 1]."""
        assert self.solution.rangeBitwiseAnd(1, 1) == 1
    
    def test_range_5_5(self):
        """Test single number range [5, 5]."""
        assert self.solution.rangeBitwiseAnd(5, 5) == 5
    
    def test_range_0_1(self):
        """Test range [0, 1]."""
        # 0 = 0, 1 = 1
        # AND = 0
        assert self.solution.rangeBitwiseAnd(0, 1) == 0
    
    def test_range_1_2(self):
        """Test range [1, 2]."""
        # 1 = 01, 2 = 10
        # AND = 00 = 0
        assert self.solution.rangeBitwiseAnd(1, 2) == 0
    
    def test_range_2_3(self):
        """Test range [2, 3]."""
        # 2 = 10, 3 = 11
        # AND = 10 = 2
        assert self.solution.rangeBitwiseAnd(2, 3) == 2
    
    def test_range_4_7(self):
        """Test range [4, 7]."""
        # 4 = 100, 5 = 101, 6 = 110, 7 = 111
        # AND = 100 = 4
        assert self.solution.rangeBitwiseAnd(4, 7) == 4
    
    def test_range_8_15(self):
        """Test range [8, 15]."""
        # 8 = 1000, 9 = 1001, ..., 15 = 1111
        # AND = 1000 = 8
        assert self.solution.rangeBitwiseAnd(8, 15) == 8
    
    def test_range_1_3(self):
        """Test range [1, 3]."""
        # 1 = 01, 2 = 10, 3 = 11
        # AND = 00 = 0
        assert self.solution.rangeBitwiseAnd(1, 3) == 0
    
    def test_large_range_different_bit_lengths(self):
        """Test range where numbers have different bit lengths."""
        # 7 = 111 (3 bits), 8 = 1000 (4 bits)
        # When crossing a power of 2, result is usually 0
        assert self.solution.rangeBitwiseAnd(7, 8) == 0
    
    def test_power_of_two_ranges(self):
        """Test ranges involving powers of 2."""
        # 15 = 1111, 16 = 10000
        assert self.solution.rangeBitwiseAnd(15, 16) == 0
        
        # 31 = 11111, 32 = 100000
        assert self.solution.rangeBitwiseAnd(31, 32) == 0
    
    def test_large_numbers(self):
        """Test with larger numbers."""
        # Test case where numbers are in the same "bit group"
        assert self.solution.rangeBitwiseAnd(1000, 1003) == 1000
        
        # Test case spanning different bit groups
        # 1000 = 1111101000, 1100 = 10001001100 (different bit lengths)
        # When ranges span very different bit patterns, result is often 0
        assert self.solution.rangeBitwiseAnd(1000, 1100) == 0
    
    def test_edge_case_zero_range(self):
        """Test range starting from 0."""
        assert self.solution.rangeBitwiseAnd(0, 5) == 0
        assert self.solution.rangeBitwiseAnd(0, 100) == 0
    
    def test_consecutive_powers_of_two(self):
        """Test consecutive powers of 2."""
        # 4 = 100, 8 = 1000
        assert self.solution.rangeBitwiseAnd(4, 8) == 0
        
        # 8 = 1000, 16 = 10000
        assert self.solution.rangeBitwiseAnd(8, 16) == 0
    
    def test_same_prefix_ranges(self):
        """Test ranges with same binary prefix."""
        # 12 = 1100, 13 = 1101, 14 = 1110, 15 = 1111
        # Common prefix is 11xx, but the last 2 bits differ
        # So result should be 1100 = 12
        assert self.solution.rangeBitwiseAnd(12, 15) == 12
    
    @pytest.mark.parametrize("left,right,expected", [
        (5, 7, 4),
        (0, 0, 0),
        (1, 1, 1),
        (0, 1, 0),
        (1, 2, 0),
        (2, 3, 2),
        (4, 7, 4),
        (8, 15, 8),
        (12, 15, 12),
    ])
    def test_parametrized_cases(self, left, right, expected):
        """Parametrized test for multiple input-output pairs."""
        assert self.solution.rangeBitwiseAnd(left, right) == expected
    
    def test_algorithm_insight_verification(self):
        """Test to verify the algorithm's core insight."""
        # The algorithm finds the common prefix of binary representations
        # For [5, 7]: 5=101, 6=110, 7=111
        # Common prefix is "1" (after right shifting until they're equal)
        # Then shift back to get 100 = 4
        assert self.solution.rangeBitwiseAnd(5, 7) == 4
        
        # For [12, 15]: 12=1100, 13=1101, 14=1110, 15=1111
        # Common prefix is "11" (after 2 right shifts)
        # Then shift back by 2 to get 1100 = 12
        assert self.solution.rangeBitwiseAnd(12, 15) == 12
    
    def test_return_type(self):
        """Test that the function returns an integer."""
        result = self.solution.rangeBitwiseAnd(5, 7)
        assert isinstance(result, int)
    
    def test_non_negative_result(self):
        """Test that the result is always non-negative."""
        test_cases = [(0, 0), (1, 5), (10, 20), (100, 200)]
        for left, right in test_cases:
            result = self.solution.rangeBitwiseAnd(left, right)
            assert result >= 0
    
    def test_result_bounds(self):
        """Test that result is within expected bounds."""
        # Result should never be greater than the left boundary
        test_cases = [(5, 7), (10, 15), (20, 30)]
        for left, right in test_cases:
            result = self.solution.rangeBitwiseAnd(left, right)
            assert result <= left
    
    def test_manual_verification_small_cases(self):
        """Manual verification for small cases by computing AND directly."""
        # For [2, 3]: 2 & 3 = 10 & 11 = 10 = 2
        assert self.solution.rangeBitwiseAnd(2, 3) == 2
        
        # For [4, 5]: 4 & 5 = 100 & 101 = 100 = 4
        assert self.solution.rangeBitwiseAnd(4, 5) == 4
        
        # For [6, 7]: 6 & 7 = 110 & 111 = 110 = 6
        assert self.solution.rangeBitwiseAnd(6, 7) == 6
    
    def test_efficiency_large_range(self):
        """Test that the algorithm is efficient for large ranges."""
        # The algorithm should complete quickly even for large ranges
        # because it doesn't iterate through all numbers
        result = self.solution.rangeBitwiseAnd(1000000, 2000000)
        assert isinstance(result, int)
        assert result >= 0


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
