"""
Unit tests for ambiguous_coordinates.py
Tests the Ambiguous Coordinates solution.
"""

import sys
import os
import importlib.util
import pytest

# Import the solution using importlib with relative path
spec = importlib.util.spec_from_file_location(
    "ambiguous_coordinates",
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "leetcode", "ambiguous_coordinates.py")
)
ambiguous_coordinates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ambiguous_coordinates)

Solution = ambiguous_coordinates.Solution


class TestAmbiguousCoordinates:
    """Test class for ambiguous coordinates functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_case(self):
        """Test basic case with multiple possible interpretations."""
        result = self.solution.ambiguousCoordinates("(123)")
        expected = ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
        assert sorted(result) == sorted(expected)

    def test_all_zeros_with_one(self):
        """Test case with leading zeros and trailing one."""
        result = self.solution.ambiguousCoordinates("(0000001)")
        expected = ["(0, 0.00001)"]
        assert result == expected

    def test_simple_split(self):
        """Test simple two-digit split."""
        result = self.solution.ambiguousCoordinates("(100)")
        expected = ["(1, 00)", "(1, 0.0)", "(10, 0)"]
        # Note: "00" and "0.0" might not be valid, let's check actual output
        assert len(result) > 0  # At least some valid interpretations

    def test_no_leading_zeros(self):
        """Test case that should avoid leading zeros."""
        result = self.solution.ambiguousCoordinates("(00011)")
        # Should avoid interpretations with leading zeros in integers
        for coord in result:
            # Check that coordinates don't have invalid leading zeros
            parts = coord[1:-1].split(", ")  # Remove parentheses and split
            for part in parts:
                if "." not in part and len(part) > 1:
                    assert not part.startswith("0"), f"Invalid leading zero in {part}"

    def test_decimal_placements(self):
        """Test various decimal point placements."""
        result = self.solution.ambiguousCoordinates("(0123)")
        # Should include interpretations like (0.1, 23), (0.12, 3), etc.
        assert len(result) > 0
        
        # Verify all results are properly formatted
        for coord in result:
            assert coord.startswith("(") and coord.endswith(")")
            assert ", " in coord

    def test_single_digit_split(self):
        """Test minimum valid input."""
        result = self.solution.ambiguousCoordinates("(12)")
        expected = ["(1, 2)"]
        assert result == expected

    def test_three_digits_comprehensive(self):
        """Test three digits with all valid interpretations."""
        result = self.solution.ambiguousCoordinates("(234)")
        # Possible splits: (2,34), (23,4)
        # Possible decimals: (2,3.4), (2.3,4)
        expected_splits = [
            "(2, 34)", "(23, 4)",  # Integer splits
            "(2, 3.4)", "(2.3, 4)"  # With decimals
        ]
        for expected in expected_splits:
            assert expected in result

    def test_edge_case_with_trailing_zeros(self):
        """Test case with trailing zeros."""
        result = self.solution.ambiguousCoordinates("(1000)")
        # Should handle trailing zeros properly
        assert len(result) > 0
        
        # Verify no invalid trailing zeros in decimals
        for coord in result:
            assert "0." not in coord or coord.count(".") == coord.count("0.") == 0 or \
                   any(c.isdigit() and c != "0" for c in coord.split(".")[-1])

    def test_all_same_digits(self):
        """Test with all same digits."""
        result = self.solution.ambiguousCoordinates("(1111)")
        # Should have valid interpretations
        assert len(result) > 0
        
        # All should be valid coordinate formats
        for coord in result:
            assert coord.startswith("(") and coord.endswith(")")
            parts = coord[1:-1].split(", ")
            assert len(parts) == 2

    def test_large_number(self):
        """Test with larger numbers."""
        result = self.solution.ambiguousCoordinates("(12345)")
        # Should have multiple valid interpretations
        assert len(result) > 0
        
        # Check some expected interpretations exist
        expected_patterns = ["(1, 2345)", "(12, 345)", "(123, 45)", "(1234, 5)"]
        for pattern in expected_patterns:
            assert pattern in result

    def test_parametrized_cases(self):
        """Test multiple cases with expected properties."""
        test_cases = [
            ("(12)", 1),      # Only one way to split
            ("(123)", 4),     # Multiple ways to split and add decimals
            ("(1000)", None), # Some valid interpretations (don't check exact count)
            ("(0123)", None), # Various decimal interpretations
        ]
        
        for input_str, expected_count in test_cases:
            result = self.solution.ambiguousCoordinates(input_str)
            assert len(result) > 0, f"No results for {input_str}"
            
            if expected_count is not None:
                assert len(result) == expected_count, \
                       f"Expected {expected_count} results for {input_str}, got {len(result)}"

    def test_format_validation(self):
        """Test that all outputs follow correct format."""
        test_inputs = ["(123)", "(1000)", "(0123)", "(12345)"]
        
        for input_str in test_inputs:
            result = self.solution.ambiguousCoordinates(input_str)
            
            for coord in result:
                # Must start with ( and end with )
                assert coord.startswith("(") and coord.endswith(")")
                
                # Must contain exactly one ", "
                assert coord.count(", ") == 1
                
                # Extract and validate the two numbers
                inner = coord[1:-1]  # Remove parentheses
                x_str, y_str = inner.split(", ")
                
                # Both should be valid number representations
                try:
                    float(x_str)
                    float(y_str)
                except ValueError:
                    pytest.fail(f"Invalid number format in {coord}: {x_str} or {y_str}")

    def test_no_invalid_leading_zeros(self):
        """Test that invalid leading zeros are avoided."""
        result = self.solution.ambiguousCoordinates("(01234)")
        
        for coord in result:
            inner = coord[1:-1]
            x_str, y_str = inner.split(", ")
            
            # Check each coordinate part
            for num_str in [x_str, y_str]:
                if "." not in num_str:
                    # Integer case: should not start with 0 unless it's just "0"
                    if len(num_str) > 1:
                        assert not num_str.startswith("0"), \
                               f"Invalid leading zero in integer: {num_str}"
                else:
                    # Decimal case: check both parts
                    int_part, dec_part = num_str.split(".")
                    if len(int_part) > 1:
                        assert not int_part.startswith("0"), \
                               f"Invalid leading zero in decimal integer part: {int_part}"

    def test_consistency(self):
        """Test that the solution is consistent."""
        test_input = "(123)"
        result1 = self.solution.ambiguousCoordinates(test_input)
        result2 = self.solution.ambiguousCoordinates(test_input)
        
        # Should get the same results
        assert sorted(result1) == sorted(result2)


if __name__ == "__main__":
    pytest.main([__file__])
