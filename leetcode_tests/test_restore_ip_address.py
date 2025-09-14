"""
Comprehensive test suite for LeetCode 93: Restore IP Addresses.
"""

import pytest

from leetcode.restore_ip_address import Solution


class TestRestoreIpAddresses:
    """Test cases for the Restore IP Addresses problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    # Basic Examples
    def test_example_1(self):
        """Test example 1: '25525511135'."""
        result = self.solution.restoreIpAddresses("25525511135")
        expected = ["255.255.11.135", "255.255.111.35"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self):
        """Test example 2: '0000'."""
        result = self.solution.restoreIpAddresses("0000")
        expected = ["0.0.0.0"]
        assert result == expected

    def test_example_3(self):
        """Test example 3: '101023'."""
        result = self.solution.restoreIpAddresses("101023")
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        assert sorted(result) == sorted(expected)

    # Edge Cases
    def test_minimum_length(self):
        """Test minimum valid length string."""
        result = self.solution.restoreIpAddresses("1111")
        expected = ["1.1.1.1"]
        assert result == expected

    def test_maximum_length(self):
        """Test maximum valid length string."""
        result = self.solution.restoreIpAddresses("255255255255")
        expected = ["255.255.255.255"]
        assert result == expected

    def test_too_short(self):
        """Test string too short for valid IP."""
        result = self.solution.restoreIpAddresses("123")
        assert result == []

    def test_too_long(self):
        """Test string too long for valid IP."""
        result = self.solution.restoreIpAddresses("1234567890123")
        assert result == []

    def test_empty_string(self):
        """Test empty string."""
        result = self.solution.restoreIpAddresses("")
        assert result == []

    def test_single_digit(self):
        """Test single digit."""
        result = self.solution.restoreIpAddresses("1")
        assert result == []

    # Leading Zero Cases
    def test_leading_zeros_valid(self):
        """Test valid cases with single zeros."""
        result = self.solution.restoreIpAddresses("1010")
        expected = ["1.0.1.0"]
        assert result == expected

    def test_leading_zeros_invalid(self):
        """Test invalid leading zeros."""
        # "0123" should not produce "01.2.3" or similar
        result = self.solution.restoreIpAddresses("0123")
        expected = ["0.1.2.3"]
        assert result == expected

    def test_multiple_leading_zeros(self):
        """Test strings with multiple leading zeros."""
        result = self.solution.restoreIpAddresses("0001")
        expected = ["0.0.0.1"]
        assert result == expected

    def test_all_zeros_leading(self):
        """Test string starting with multiple zeros."""
        result = self.solution.restoreIpAddresses("00000")
        # "00000" cannot form valid IP due to length constraints
        expected = []
        assert result == expected

    # Boundary Value Cases
    def test_max_values(self):
        """Test with maximum IP values (255)."""
        result = self.solution.restoreIpAddresses("255255255255")
        expected = ["255.255.255.255"]
        assert result == expected

    def test_over_255_values(self):
        """Test with values over 255."""
        result = self.solution.restoreIpAddresses("256256256256")
        assert result == []

    def test_just_over_255(self):
        """Test with values just over 255."""
        result = self.solution.restoreIpAddresses("1921681256")
        # 256 is invalid, so should find valid combinations
        expected = ["192.168.1.256"]  # This should NOT be in result
        result_set = set(result)
        assert "192.168.1.256" not in result_set

    def test_mixed_valid_invalid(self):
        """Test string with mix of valid and invalid segments."""
        result = self.solution.restoreIpAddresses("19216811")
        expected = ["1.92.168.11", "19.2.168.11", "19.21.68.11", "19.216.8.11", 
                   "19.216.81.1", "192.1.68.11", "192.16.8.11", "192.16.81.1", "192.168.1.1"]
        assert sorted(result) == sorted(expected)

    # Special Pattern Cases
    def test_all_same_digit(self):
        """Test strings with all same digits."""
        result = self.solution.restoreIpAddresses("2222")
        expected = ["2.2.2.2"]
        assert result == expected

    def test_all_same_digit_longer(self):
        """Test longer strings with all same digits."""
        result = self.solution.restoreIpAddresses("111111")
        expected = ["1.1.1.111", "1.1.11.11", "1.1.111.1", "1.11.1.11", 
                   "1.11.11.1", "1.111.1.1", "11.1.1.11", "11.1.11.1", 
                   "11.11.1.1", "111.1.1.1"]
        assert sorted(result) == sorted(expected)

    def test_palindromic_string(self):
        """Test palindromic strings."""
        result = self.solution.restoreIpAddresses("1221")
        expected = ["1.2.2.1"]
        assert result == expected

    # Realistic IP Patterns
    def test_common_ip_pattern_192(self):
        """Test common 192.x.x.x pattern."""
        result = self.solution.restoreIpAddresses("19216811")
        # Should include "192.168.1.1"
        assert "192.168.1.1" in result

    def test_common_ip_pattern_10(self):
        """Test common 10.x.x.x pattern."""
        result = self.solution.restoreIpAddresses("10001")
        # Should get "10.0.0.1" (not "1.0.0.1" due to greedy algorithm)
        assert "10.0.0.1" in result
        assert "1.0.0.01" not in result

    def test_localhost_pattern(self):
        """Test localhost-like pattern."""
        result = self.solution.restoreIpAddresses("127001")
        expected = ["1.2.7.001"]  # Invalid due to leading zeros
        # Should get valid combinations like "1.2.7.1", "12.7.0.1", etc.
        assert "1.2.7.001" not in result

    # Complex Valid Cases
    def test_multiple_valid_combinations(self):
        """Test string with many valid combinations."""
        result = self.solution.restoreIpAddresses("123123")
        expected = ["1.2.3.123", "1.2.31.23", "1.23.1.23", "1.23.12.3", 
                   "1.231.2.3", "12.3.1.23", "12.3.12.3", "12.31.2.3", "123.1.2.3"]
        assert sorted(result) == sorted(expected)

    def test_single_valid_combination(self):
        """Test string with only one valid combination."""
        result = self.solution.restoreIpAddresses("25525525525")
        expected = ["255.255.255.25"]
        assert result == expected

    # Invalid Pattern Cases
    def test_no_valid_combinations(self):
        """Test strings with no valid IP combinations."""
        result = self.solution.restoreIpAddresses("999999999999")
        assert result == []

    def test_partial_valid_segments(self):
        """Test where some segments are valid but overall combination isn't."""
        result = self.solution.restoreIpAddresses("25525525599")
        # 255.255.255.99 is valid, but check if 999 segments are properly rejected
        valid_ips = [ip for ip in result if all(0 <= int(seg) <= 255 for seg in ip.split('.'))]
        assert len(valid_ips) == len(result)  # All results should be valid

    # Edge Cases with Zeros
    def test_zeros_in_middle(self):
        """Test zeros appearing in middle of string."""
        result = self.solution.restoreIpAddresses("120034")
        expected = ["1.2.0.034"]  # Invalid due to leading zero
        # Should get valid combinations without leading zeros
        assert "1.2.0.034" not in result
        # Check that we get some valid results
        assert len(result) > 0
        valid_results = ["1.20.0.34", "1.200.3.4", "12.0.0.34", "120.0.3.4"]
        assert sorted(result) == sorted(valid_results)

    def test_trailing_zeros(self):
        """Test string ending with zeros."""
        result = self.solution.restoreIpAddresses("123400")
        expected = ["1.2.3.400"]  # Invalid as 400 > 255
        # Should get valid combinations
        assert "1.2.3.400" not in result
        assert "12.34.0.0" in result

    # Performance and Stress Cases
    def test_maximum_complexity(self):
        """Test case that exercises maximum backtracking."""
        result = self.solution.restoreIpAddresses("111111111111")
        # Should handle this efficiently without timeout
        assert isinstance(result, list)
        # All results should be valid IPs
        for ip in result:
            segments = ip.split('.')
            assert len(segments) == 4
            for segment in segments:
                assert 0 <= int(segment) <= 255
                if len(segment) > 1:
                    assert segment[0] != '0'  # No leading zeros

    def test_minimum_complexity(self):
        """Test simplest valid case."""
        result = self.solution.restoreIpAddresses("0000")
        expected = ["0.0.0.0"]
        assert result == expected


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])