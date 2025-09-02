"""
Comprehensive tests for Maximum XOR of Two Numbers in an Array.

Tests the Trie-based solution for finding maximum XOR.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.maximum_xor_of_two_numbers_in_an_array import Solution


class TestMaximumXorOfTwoNumbers:
    """Test class for maximum XOR of two numbers implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example(self):
        """LeetCode example case."""
        return [3, 10, 5, 25, 2, 8]

    @pytest.fixture
    def two_elements(self):
        """Simple two element arrays."""
        return ([5, 3], [1, 2], [15, 7])

    @pytest.fixture
    def power_of_two(self):
        """Powers of two."""
        return [1, 2, 4, 8, 16]

    @pytest.fixture
    def same_numbers(self):
        """Array with duplicate numbers."""
        return [5, 5, 5, 5]

    def test_leetcode_example(self, leetcode_example):
        """Test with LeetCode example."""
        result = self.solution.findMaximumXOR(leetcode_example)
        assert result == 28  # 25 XOR 3 = 28

    def test_two_elements(self, two_elements):
        """Test with two element arrays."""
        for arr in two_elements:
            result = self.solution.findMaximumXOR(arr)
            expected = arr[0] ^ arr[1]
            assert result == expected

    def test_power_of_two_sequence(self, power_of_two):
        """Test with powers of two."""
        result = self.solution.findMaximumXOR(power_of_two)
        # 8 XOR 16 = 24 is maximum
        assert result == 24

    def test_same_numbers(self, same_numbers):
        """Test array with all same numbers."""
        result = self.solution.findMaximumXOR(same_numbers)
        assert result == 0  # XOR of same numbers is 0

    def test_single_element(self):
        """Test single element array."""
        result = self.solution.findMaximumXOR([42])
        assert result == 0  # No pair possible

    def test_binary_opposites(self):
        """Test with binary opposites."""
        arr = [0, 15]  # 0000 and 1111 in binary
        result = self.solution.findMaximumXOR(arr)
        assert result == 15

    def test_consecutive_numbers(self):
        """Test consecutive numbers."""
        arr = [1, 2, 3, 4, 5]
        result = self.solution.findMaximumXOR(arr)
        # 4 XOR 3 = 7 is maximum
        assert result == 7

    def test_large_numbers(self):
        """Test with large numbers."""
        arr = [1000000, 2000000, 3000000]
        result = self.solution.findMaximumXOR(arr)
        # Calculate manually: max XOR would be between extremes
        expected = max(arr[i] ^ arr[j] for i in range(len(arr)) 
                      for j in range(i+1, len(arr)))
        assert result == expected

    def test_alternating_bits(self):
        """Test numbers with alternating bit patterns."""
        arr = [85, 170]  # 01010101 and 10101010 in binary
        result = self.solution.findMaximumXOR(arr)
        assert result == 255  # All bits different

    def test_small_range(self):
        """Test small range of numbers."""
        arr = [0, 1, 2, 3]
        result = self.solution.findMaximumXOR(arr)
        assert result == 3  # 0 XOR 3 = 3

    def test_mixed_values(self):
        """Test mixed positive values."""
        arr = [1, 5, 6, 3]
        result = self.solution.findMaximumXOR(arr)
        # 5 XOR 6 = 3, 1 XOR 6 = 7, etc. Max is 7
        assert result == 7

    def test_fibonacci_sequence(self):
        """Test Fibonacci-like sequence."""
        arr = [1, 1, 2, 3, 5, 8]
        result = self.solution.findMaximumXOR(arr)
        # Check all combinations manually
        expected = max(arr[i] ^ arr[j] for i in range(len(arr)) 
                      for j in range(i+1, len(arr)))
        assert result == expected

    def test_geometric_progression(self):
        """Test geometric progression."""
        arr = [1, 2, 4, 8, 16, 32]
        result = self.solution.findMaximumXOR(arr)
        # 16 XOR 32 = 48 should be maximum
        assert result == 48

    def test_prime_numbers(self):
        """Test with prime numbers."""
        arr = [2, 3, 5, 7, 11, 13]
        result = self.solution.findMaximumXOR(arr)
        expected = max(arr[i] ^ arr[j] for i in range(len(arr)) 
                      for j in range(i+1, len(arr)))
        assert result == expected

    def test_edge_bit_patterns(self):
        """Test edge bit patterns."""
        arr = [0, 2**20 - 1]  # 0 and maximum 20-bit number
        result = self.solution.findMaximumXOR(arr)
        assert result == 2**20 - 1

    def test_multiple_optimal_pairs(self):
        """Test when multiple pairs give same maximum XOR."""
        arr = [1, 6, 3, 4]
        result = self.solution.findMaximumXOR(arr)
        # 1 XOR 6 = 7, 3 XOR 4 = 7
        assert result == 7

    def test_descending_order(self):
        """Test with numbers in descending order."""
        arr = [100, 50, 25, 10, 5]
        result = self.solution.findMaximumXOR(arr)
        expected = max(arr[i] ^ arr[j] for i in range(len(arr)) 
                      for j in range(i+1, len(arr)))
        assert result == expected

    def test_random_pattern(self):
        """Test with random-like pattern."""
        arr = [7, 14, 21, 28, 35]
        result = self.solution.findMaximumXOR(arr)
        expected = max(arr[i] ^ arr[j] for i in range(len(arr)) 
                      for j in range(i+1, len(arr)))
        assert result == expected

    def test_bit_manipulation_edge_case(self):
        """Test specific bit manipulation edge case."""
        arr = [8, 10, 2]
        result = self.solution.findMaximumXOR(arr)
        # 8 XOR 2 = 10, 10 XOR 8 = 2, 10 XOR 2 = 8
        # Maximum is 10
        assert result == 10

    def test_large_array_performance(self):
        """Test with larger array for performance."""
        arr = list(range(1, 101))  # 1 to 100
        result = self.solution.findMaximumXOR(arr)
        # Should handle reasonably sized arrays efficiently
        assert result > 0


if __name__ == '__main__':
    pytest.main([__file__])
