"""
Test suite for LeetCode #842: Split Array into Fibonacci Sequence
"""

import pytest
import time

from leetcode.split_array_into_fibonacci import Solution


class TestSplitArrayIntoFibonacci:
    """Comprehensive test suite for Split Array into Fibonacci Sequence problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # LeetCode Examples
    def test_example_1_leetcode(self):
        """Test LeetCode Example 1: "11235813" -> [1,1,2,3,5,8,13]"""
        num = "11235813"
        expected = [1,1,2,3,5,8,13]
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_2_leetcode(self):
        """Test LeetCode Example 2: "123456579" -> [123,456,579]"""
        num = "123456579"
        expected = [123,456,579]
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_3_leetcode(self):
        """Test LeetCode Example 3: "0123" -> []"""
        num = "0123"
        expected = []
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge Cases
    def test_too_short(self):
        """Test string too short to form Fibonacci sequence."""
        test_cases = ["1", "12", ""]
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == [], f"String '{num}' should return empty list"
    
    def test_single_digit_fibonacci(self):
        """Test valid single digit Fibonacci sequences."""
        num = "112"
        expected = [1,1,2]
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_leading_zeros_invalid(self):
        """Test cases with invalid leading zeros."""
        test_cases = ["0011", "001234"]  # Remove "01123" as it has valid split [0,1,1,2,3]
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == [], f"String '{num}' with leading zeros should return empty list"
    
    def test_valid_zero_start(self):
        """Test cases where starting with 0 is valid."""
        test_cases = [
            ("01123", [0,1,1,2,3]),
            ("011235", [0,1,1,2,3,5])
        ]
        for num, expected in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == expected, f"For '{num}' expected {expected}, got {result}"
    
    def test_single_zero_valid(self):
        """Test cases where single '0' is valid."""
        num = "011"
        expected = [0,1,1]
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_all_zeros(self):
        """Test string of all zeros."""
        num = "000"
        expected = [0,0,0]
        result = self.solution.splitIntoFibonacci(num)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_no_valid_split(self):
        """Test cases where no valid Fibonacci split exists."""
        test_cases = ["1234", "54321", "98765"]
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == [], f"String '{num}' should have no valid split"
    
    # Complex Cases
    def test_multiple_valid_first_numbers(self):
        """Test case where multiple first number choices exist."""
        num = "1101111"
        expected = [11,0,11,11]  # One possible valid split
        result = self.solution.splitIntoFibonacci(num)
        assert len(result) >= 3, "Should find a valid sequence"
        # Verify it's a valid Fibonacci sequence
        if len(result) >= 3:
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2], f"Not Fibonacci at index {i}"
    
    def test_long_fibonacci_sequence(self):
        """Test longer Fibonacci sequences."""
        num = "112358132134"
        result = self.solution.splitIntoFibonacci(num)
        # Should find some valid sequence or empty
        if result:
            assert len(result) >= 3, "Valid sequence should have at least 3 numbers"
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2], f"Not Fibonacci at index {i}"
    
    def test_larger_numbers(self):
        """Test with larger numbers in sequence."""
        num = "1123581347"  # 1,123,581,347 should work
        result = self.solution.splitIntoFibonacci(num)
        if result:
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2], f"Not Fibonacci at index {i}"
    
    def test_alternating_pattern(self):
        """Test strings with alternating digit patterns."""
        num = "1213455"  # Could be 1,2,1,3,4,5,5 but not Fibonacci
        result = self.solution.splitIntoFibonacci(num)
        # May or may not have solution, but if it does, must be valid
        if result:
            assert len(result) >= 3
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2]
    
    # Boundary Cases
    def test_minimum_valid_sequence(self):
        """Test minimum valid Fibonacci sequence."""
        test_cases = [
            ("011", [0,1,1]),
            ("123", [1,2,3]),
            ("134", [1,3,4])
        ]
        for num, expected in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == expected, f"For '{num}' expected {expected}, got {result}"
    
    def test_large_single_numbers(self):
        """Test cases that might form large single numbers."""
        num = "123456789"
        result = self.solution.splitIntoFibonacci(num)
        # This specific case may not have a valid split
        if result:
            assert len(result) >= 3
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2]
    
    def test_repeated_digits(self):
        """Test strings with repeated digits."""
        test_cases = ["111", "222", "1111"]
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            if result:
                assert len(result) >= 3
                for i in range(2, len(result)):
                    assert result[i] == result[i-1] + result[i-2]
    
    # Performance Tests
    def test_performance_medium_string(self):
        """Test performance with medium-length string."""
        num = "1123581321345589"  # Fibonacci-like but long
        
        start_time = time.time()
        result = self.solution.splitIntoFibonacci(num)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Should complete quickly: {execution_time:.3f}s"
        
        if result:
            assert len(result) >= 3
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2]
    
    def test_performance_worst_case(self):
        """Test performance with potential worst-case input."""
        num = "9876543210"  # Unlikely to have solution, might explore many paths
        
        start_time = time.time()
        result = self.solution.splitIntoFibonacci(num)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 2.0, f"Even worst case should be reasonable: {execution_time:.3f}s"
        
        # This case likely has no solution
        assert isinstance(result, list), "Should return a list"
    
    # Validation Tests
    def test_return_type(self):
        """Test that function returns correct type."""
        num = "123"
        result = self.solution.splitIntoFibonacci(num)
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        if result:
            assert all(isinstance(x, int) for x in result), "All elements should be integers"
    
    def test_fibonacci_property_validation(self):
        """Test that returned sequences satisfy Fibonacci property."""
        test_cases = ["11235813", "123456579", "011", "1101111"]
        
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            if result:
                assert len(result) >= 3, f"Valid sequence should have ≥3 elements for '{num}'"
                
                # Check Fibonacci property
                for i in range(2, len(result)):
                    expected = result[i-2] + result[i-1]
                    assert result[i] == expected, \
                        f"Fibonacci property violated at index {i}: {result[i]} ≠ {expected}"
    
    def test_string_reconstruction(self):
        """Test that result can reconstruct original string."""
        test_cases = ["11235813", "123456579", "011", "112"]
        
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            if result:
                reconstructed = ''.join(map(str, result))
                assert reconstructed == num, \
                    f"Reconstruction failed: '{reconstructed}' ≠ '{num}'"
    
    def test_no_leading_zeros_in_result(self):
        """Test that result doesn't contain numbers with leading zeros."""
        test_cases = ["11235813", "0123", "011", "1101111"]
        
        for num in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            if result:
                for i, val in enumerate(result):
                    str_val = str(val)
                    if len(str_val) > 1:
                        assert not str_val.startswith('0'), \
                            f"Number {val} at index {i} has leading zero"
    
    # Specific Pattern Tests
    def test_fibonacci_starting_with_zero(self):
        """Test Fibonacci sequences that can start with 0."""
        test_cases = [
            ("011", [0,1,1]),
            ("0112", [0,1,1,2]),
            ("01123", [0,1,1,2,3])
        ]
        
        for num, expected in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == expected, f"For '{num}' expected {expected}, got {result}"
    
    def test_single_digit_sequences(self):
        """Test sequences with all single digits."""
        test_cases = [
            ("112", [1,1,2]),
            ("123", [1,2,3]),
            ("134", [1,3,4]),
            ("145", [1,4,5])
        ]
        
        for num, expected in test_cases:
            result = self.solution.splitIntoFibonacci(num)
            assert result == expected, f"For '{num}' expected {expected}, got {result}"
    
    def test_mixed_digit_lengths(self):
        """Test sequences with mixed digit lengths."""
        num = "112358132134"  # Mix of 1, 2, and 3 digit numbers
        result = self.solution.splitIntoFibonacci(num)
        if result:
            # Verify reconstruction
            reconstructed = ''.join(map(str, result))
            assert reconstructed == num
            
            # Verify Fibonacci property
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2]
    
    # Edge cases with different interpretations
    def test_ambiguous_splits(self):
        """Test cases where multiple valid splits might exist."""
        # The algorithm should return the first valid one it finds
        num = "1101111"
        result = self.solution.splitIntoFibonacci(num)
        
        if result:
            # Verify it's valid
            assert len(result) >= 3
            reconstructed = ''.join(map(str, result))
            assert reconstructed == num
            for i in range(2, len(result)):
                assert result[i] == result[i-1] + result[i-2]


if __name__ == "__main__":
    pytest.main([__file__])