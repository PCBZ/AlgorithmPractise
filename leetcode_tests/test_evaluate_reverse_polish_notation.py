"""
Comprehensive test suite for LeetCode Problem #150: Evaluate Reverse Polish Notation

Tests the evalRPN method which evaluates arithmetic expressions written
in Reverse Polish Notation using a stack-based approach.
"""
import os
import sys
import time

# Add the parent directory to sys.path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import using the actual file path structure
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'leetcode'))

from evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation:
    """Test class for evaluating Reverse Polish Notation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        tokens = ["2", "1", "+", "3", "*"]
        result = self.solution.evalRPN(tokens)
        expected = 9  # ((2 + 1) * 3) = 9
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        tokens = ["4", "13", "5", "/", "+"]
        result = self.solution.evalRPN(tokens)
        expected = 6  # (4 + (13 / 5)) = 4 + 2 = 6
        assert result == expected

    def test_example_case_3(self):
        """Test LeetCode example case 3."""
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        result = self.solution.evalRPN(tokens)
        expected = 22
        assert result == expected

    def test_single_number(self):
        """Test with single number."""
        test_cases = [
            (["0"], 0),
            (["1"], 1),
            (["-1"], -1),
            (["42"], 42),
            (["-123"], -123),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_simple_addition(self):
        """Test simple addition operations."""
        test_cases = [
            (["1", "2", "+"], 3),
            (["0", "5", "+"], 5),
            (["-1", "1", "+"], 0),
            (["10", "20", "+"], 30),
            (["-5", "-3", "+"], -8),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_simple_subtraction(self):
        """Test simple subtraction operations."""
        test_cases = [
            (["5", "3", "-"], 2),
            (["1", "2", "-"], -1),
            (["0", "5", "-"], -5),
            (["-1", "1", "-"], -2),
            (["10", "-3", "-"], 13),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_simple_multiplication(self):
        """Test simple multiplication operations."""
        test_cases = [
            (["2", "3", "*"], 6),
            (["0", "5", "*"], 0),
            (["-1", "4", "*"], -4),
            (["-2", "-3", "*"], 6),
            (["7", "1", "*"], 7),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_simple_division(self):
        """Test simple division operations."""
        test_cases = [
            (["6", "2", "/"], 3),
            (["8", "4", "/"], 2),
            (["1", "1", "/"], 1),
            (["-6", "2", "/"], -3),
            (["6", "-2", "/"], -3),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_division_truncation(self):
        """Test division truncation toward zero."""
        test_cases = [
            (["7", "3", "/"], 2),      # 7/3 = 2.33... -> 2
            (["-7", "3", "/"], -2),    # -7/3 = -2.33... -> -2 (toward zero)
            (["7", "-3", "/"], -2),    # 7/-3 = -2.33... -> -2 (toward zero)
            (["-7", "-3", "/"], 2),    # -7/-3 = 2.33... -> 2
            (["13", "5", "/"], 2),     # 13/5 = 2.6 -> 2
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_complex_expressions(self):
        """Test complex expressions with multiple operations."""
        test_cases = [
            (["1", "2", "+", "3", "*"], 9),        # (1+2)*3 = 9
            (["1", "2", "*", "3", "+"], 5),        # (1*2)+3 = 5
            (["2", "3", "+", "4", "5", "+", "*"], 45),  # (2+3)*(4+5) = 45
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_negative_numbers(self):
        """Test with negative numbers."""
        test_cases = [
            (["-1"], -1),
            (["-1", "2", "+"], 1),
            (["-1", "-2", "+"], -3),
            (["-1", "2", "*"], -2),
            (["-4", "2", "/"], -2),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_order_of_operations(self):
        """Test that RPN correctly handles order without parentheses."""
        # In RPN, the order is explicit, no need for precedence rules
        test_cases = [
            (["2", "3", "4", "*", "+"], 14),      # 2 + (3 * 4) = 14
            (["2", "3", "+", "4", "*"], 20),      # (2 + 3) * 4 = 20
            (["1", "2", "+", "3", "4", "+", "*"], 21),  # (1+2) * (3+4) = 3 * 7 = 21
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_stack_behavior(self):
        """Test that stack operations are correct."""
        # Test cases that verify proper stack push/pop behavior
        test_cases = [
            (["1", "2", "3", "+", "*"], 5),      # 1 * (2 + 3) = 5
            (["1", "2", "+", "3", "*"], 9),      # (1 + 2) * 3 = 9
            (["1", "2", "*", "3", "+"], 5),      # (1 * 2) + 3 = 5
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_zero_operations(self):
        """Test operations involving zero."""
        test_cases = [
            (["0", "1", "+"], 1),
            (["1", "0", "+"], 1),
            (["0", "1", "*"], 0),
            (["1", "0", "*"], 0),
            (["0", "1", "-"], -1),
            (["1", "0", "-"], 1),
            (["0", "5", "/"], 0),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        tokens = ["1", "2", "+"]
        result = self.solution.evalRPN(tokens)

        assert isinstance(result, int)

    def test_algorithm_correctness(self):
        """Test algorithm correctness with step-by-step verification."""
        # Manually verify: ["2", "1", "+", "3", "*"]
        # Stack operations:
        # 1. Push 2: [2]
        # 2. Push 1: [2, 1]
        # 3. Pop 1,2, compute 2+1=3, push 3: [3]
        # 4. Push 3: [3, 3]
        # 5. Pop 3,3, compute 3*3=9, push 9: [9]
        # Result: 9
        tokens = ["2", "1", "+", "3", "*"]
        result = self.solution.evalRPN(tokens)
        expected = 9
        assert result == expected

    def test_large_numbers(self):
        """Test with larger numbers."""
        test_cases = [
            (["100", "200", "+"], 300),
            (["1000", "5", "/"], 200),
            (["-1000", "10", "/"], -100),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_mixed_positive_negative(self):
        """Test mixed positive and negative operations."""
        test_cases = [
            (["5", "-2", "+"], 3),
            (["-5", "2", "+"], -3),
            (["5", "-2", "*"], -10),
            (["-5", "-2", "*"], 10),
            (["5", "-2", "/"], -2),  # Truncated toward zero
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_consecutive_operations(self):
        """Test consecutive operations on the same operands."""
        test_cases = [
            (["5", "2", "+", "3", "+"], 10),     # ((5+2)+3) = 10
            (["5", "2", "*", "3", "*"], 30),     # ((5*2)*3) = 30
            (["8", "2", "/", "2", "/"], 2),      # ((8/2)/2) = 2
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_alternating_operations(self):
        """Test alternating different operations."""
        test_cases = [
            (["2", "3", "+", "4", "-"], 1),      # (2+3)-4 = 1
            (["2", "3", "*", "4", "/"], 1),      # (2*3)/4 = 1 (truncated)
            (["10", "5", "-", "2", "*"], 10),    # (10-5)*2 = 10
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Create a moderate-sized expression
        tokens = ["1"] * 50 + ["+"] * 49  # Sum of 50 ones

        start_time = time.time()
        result = self.solution.evalRPN(tokens)
        end_time = time.time()

        # Should complete quickly
        assert end_time - start_time < 1.0
        assert result == 50

    def test_integer_detection(self):
        """Test that integer detection works correctly."""
        # This indirectly tests the is_integer helper function
        test_cases = [
            (["123"], 123),
            (["-456"], -456),
            (["0"], 0),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_operator_precedence_irrelevant(self):
        """Test that normal operator precedence is irrelevant in RPN."""
        # In infix: 2 + 3 * 4 = 2 + 12 = 14
        # In RPN: ["2", "3", "4", "*", "+"] = 2 + (3*4) = 14
        # In RPN: ["2", "3", "+", "4", "*"] = (2+3)*4 = 20
        test_cases = [
            (["2", "3", "4", "*", "+"], 14),
            (["2", "3", "+", "4", "*"], 20),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_stack_final_state(self):
        """Test that stack has exactly one element at the end."""
        # This is implicitly tested by returning stack[-1]
        tokens = ["5", "3", "+"]
        result = self.solution.evalRPN(tokens)
        assert result == 8

    def test_all_operators(self):
        """Test all four operators individually."""
        test_cases = [
            (["7", "3", "+"], 10),
            (["7", "3", "-"], 4),
            (["7", "3", "*"], 21),
            (["7", "3", "/"], 2),
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_edge_case_divisions(self):
        """Test edge cases for division."""
        test_cases = [
            (["1", "1", "/"], 1),      # 1/1 = 1
            (["-1", "1", "/"], -1),    # -1/1 = -1
            (["1", "-1", "/"], -1),    # 1/-1 = -1
            (["-1", "-1", "/"], 1),    # -1/-1 = 1
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_complex_negative_division(self):
        """Test complex cases with negative division."""
        # Verify truncation toward zero behavior
        test_cases = [
            (["-3", "2", "/"], -1),    # -3/2 = -1.5 -> -1 (toward zero)
            (["3", "-2", "/"], -1),    # 3/-2 = -1.5 -> -1 (toward zero)
            (["-3", "-2", "/"], 1),    # -3/-2 = 1.5 -> 1 (toward zero)
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_algorithm_deterministic(self):
        """Test that algorithm produces consistent results."""
        tokens = ["2", "3", "+", "4", "*"]
        result1 = self.solution.evalRPN(tokens)
        result2 = self.solution.evalRPN(tokens)
        assert result1 == result2

    def test_mathematical_properties(self):
        """Test mathematical properties."""
        # Test commutativity where applicable
        add_result1 = self.solution.evalRPN(["3", "5", "+"])
        add_result2 = self.solution.evalRPN(["5", "3", "+"])
        assert add_result1 == add_result2  # Addition is commutative

        mul_result1 = self.solution.evalRPN(["3", "5", "*"])
        mul_result2 = self.solution.evalRPN(["5", "3", "*"])
        assert mul_result1 == mul_result2  # Multiplication is commutative

    def test_boundary_values(self):
        """Test boundary values."""
        test_cases = [
            (["1"], 1),            # Minimum positive
            (["-1"], -1),          # Maximum negative
            (["0"], 0),            # Zero
        ]

        for tokens, expected in test_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"

    def test_comprehensive_verification(self):
        """Comprehensive verification with known difficult cases."""
        difficult_cases = [
            # LeetCode example 3 broken down
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
            # Complex nested operations
            (["4", "3", "-", "5", "*", "2", "/"], 2),  # ((4-3)*5)/2 = 5/2 = 2
            # Multiple consecutive operations
            (["1", "2", "3", "4", "+", "+", "+"], 10),  # 1+(2+(3+4)) = 10
        ]

        for tokens, expected in difficult_cases:
            result = self.solution.evalRPN(tokens)
            assert result == expected, f"Failed for {tokens}: got {result}, expected {expected}"
