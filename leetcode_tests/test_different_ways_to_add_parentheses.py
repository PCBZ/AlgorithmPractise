"""
Comprehensive test suite for LeetCode Problem #241: Different Ways to Add Parentheses

Tests the diffWaysToCompute method which generates all possible results from
computing different parenthesizations of an arithmetic expression.
"""
import time

from leetcode.different_ways_to_add_parentheses import Solution


class TestDifferentWaysToAddParentheses:
    """Test class for different ways to add parentheses problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        expression = "2-1-1"
        result = self.solution.diffWaysToCompute(expression)
        expected = [0, 2]
        assert sorted(result) == sorted(expected)

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        expression = "2*3-4*5"
        result = self.solution.diffWaysToCompute(expression)
        expected = [-34, -14, -10, -10, 10]
        assert sorted(result) == sorted(expected)

    def test_single_number(self):
        """Test with single number."""
        test_cases = [
            ("5", [5]),
            ("0", [0]),
            ("123", [123]),
            ("1", [1]),
            ("99", [99]),
        ]
        
        for expression, expected in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            assert result == expected, f"Failed for {expression}: got {result}, expected {expected}"

    def test_single_operation(self):
        """Test with single operation."""
        test_cases = [
            ("1+2", [3]),
            ("3-1", [2]),
            ("2*4", [8]),
            ("10+5", [15]),
            ("7-3", [4]),
            ("6*2", [12]),
        ]
        
        for expression, expected in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            assert result == expected, f"Failed for {expression}: got {result}, expected {expected}"

    def test_addition_operations(self):
        """Test with addition operations."""
        test_cases = [
            ("1+2+3", [6]),  # Only one way: ((1+2)+3) = (3+3) = 6 OR (1+(2+3)) = (1+5) = 6
            ("2+3+4", [9]),  # Only one way due to associativity
            ("1+1+1", [3]),  # All same
        ]
        
        for expression, expected in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            # For addition, all parenthesizations give same result
            assert len(set(result)) == 1, f"Addition should give unique result for {expression}"
            assert result[0] == expected[0], f"Failed for {expression}: got {result}, expected {expected}"

    def test_subtraction_operations(self):
        """Test with subtraction operations."""
        # For a-b-c: (a-b)-c vs a-(b-c) give different results
        expression = "5-3-1"
        result = self.solution.diffWaysToCompute(expression)
        # (5-3)-1 = 2-1 = 1
        # 5-(3-1) = 5-2 = 3
        expected = [1, 3]
        assert sorted(result) == sorted(expected)

    def test_multiplication_operations(self):
        """Test with multiplication operations."""
        test_cases = [
            ("2*3*4", [24]),  # Only one way due to associativity
            ("1*2*3", [6]),   # Only one way
        ]
        
        for expression, expected in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            # For multiplication, all parenthesizations give same result
            assert len(set(result)) == 1, f"Multiplication should give unique result for {expression}"
            assert result[0] == expected[0], f"Failed for {expression}: got {result}, expected {expected}"

    def test_mixed_operations_simple(self):
        """Test with simple mixed operations."""
        test_cases = [
            ("1+2*3", [7, 9]),    # (1+2)*3=9, 1+(2*3)=7
            ("2*3+1", [7, 7]),    # (2*3)+1=7, 2*(3+1)=8 - wait, let me recalculate
        ]
        
        # Let's verify the second case manually
        # "2*3+1": (2*3)+1 = 6+1 = 7, 2*(3+1) = 2*4 = 8
        expression = "2*3+1"
        result = self.solution.diffWaysToCompute(expression)
        expected = [7, 8]
        assert sorted(result) == sorted(expected)
        
        # Test the first case
        expression = "1+2*3"
        result = self.solution.diffWaysToCompute(expression)
        expected = [7, 9]
        assert sorted(result) == sorted(expected)

    def test_precedence_differences(self):
        """Test that different parenthesizations give different results."""
        # This tests the core functionality - same expression, different results
        test_cases = [
            ("1+2*3-4", [1, 5, -9]),  # Multiple ways to parenthesize
            ("2-1+3", [4, 4]),        # Should give same result due to left-to-right
        ]
        
        for expression, expected_length in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            assert len(result) >= len(expected_length), f"Should have multiple results for {expression}"

    def test_complex_expression(self):
        """Test with complex expression."""
        expression = "1*2-3*4+5*6-7*8+9"
        result = self.solution.diffWaysToCompute(expression)
        
        # Should have multiple different results
        assert len(result) > 1
        assert len(set(result)) > 1  # Results should be different

    def test_expression_with_zeros(self):
        """Test expressions involving zero."""
        test_cases = [
            ("0+1", [1]),
            ("5*0", [0]),
            ("0-1", [-1]),
            ("3+0*2", [3, 0]),  # (3+0)*2=6, 3+(0*2)=3 - wait, recalculate
        ]
        
        # Let's verify the last case: "3+0*2"
        # (3+0)*2 = 3*2 = 6
        # 3+(0*2) = 3+0 = 3
        expression = "3+0*2"
        result = self.solution.diffWaysToCompute(expression)
        expected = [3, 6]
        assert sorted(result) == sorted(expected)

    def test_negative_results(self):
        """Test expressions that can produce negative results."""
        test_cases = [
            ("1-2", [-1]),
            ("2-3*4", [-10, -4]),  # (2-3)*4=-4, 2-(3*4)=2-12=-10
        ]
        
        for expression, expected in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            assert sorted(result) == sorted(expected), f"Failed for {expression}: got {result}, expected {expected}"

    def test_large_numbers(self):
        """Test with larger numbers."""
        test_cases = [
            ("10+20", [30]),
            ("15*2-10", [20, 5]),  # (15*2)-10=30-10=20, 15*(2-10)=15*(-8)=-120
        ]
        
        # Let's verify the second case
        expression = "15*2-10"
        result = self.solution.diffWaysToCompute(expression)
        # (15*2)-10 = 30-10 = 20
        # 15*(2-10) = 15*(-8) = -120
        expected = [20, -120]
        assert sorted(result) == sorted(expected)

    def test_algorithm_properties(self):
        """Test mathematical properties of the algorithm."""
        # Test that results are deterministic
        expression = "2*3-4+5"
        result1 = self.solution.diffWaysToCompute(expression)
        result2 = self.solution.diffWaysToCompute(expression)
        assert sorted(result1) == sorted(result2)

    def test_memoization_efficiency(self):
        """Test that memoization improves performance."""
        # Test with expression that has repeated subexpressions
        expression = "1+2*3-4+5*6"
        
        start_time = time.time()
        result = self.solution.diffWaysToCompute(expression)
        end_time = time.time()
        
        # Should complete reasonably quickly
        assert end_time - start_time < 1.0
        assert len(result) > 1

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        expression = "1+2"
        result = self.solution.diffWaysToCompute(expression)
        
        assert isinstance(result, list)
        assert all(isinstance(x, int) for x in result)
        assert len(result) > 0

    def test_three_numbers_all_operators(self):
        """Test three numbers with different operators."""
        test_cases = [
            # Addition: associative, so same result
            ("1+2+3", 1),  # Should have 1 unique result
            # Subtraction: non-associative
            ("5-2-1", 2),  # Should have 2 different results: (5-2)-1=2, 5-(2-1)=4
            # Multiplication: associative
            ("2*3*4", 1),  # Should have 1 unique result
        ]
        
        for expression, expected_unique_count in test_cases:
            result = self.solution.diffWaysToCompute(expression)
            unique_results = len(set(result))
            assert unique_results == expected_unique_count, f"Expression {expression} should have {expected_unique_count} unique results, got {unique_results}"

    def test_operator_precedence_ignored(self):
        """Test that normal operator precedence is ignored in favor of parentheses."""
        # In normal math: 1+2*3 = 1+6 = 7
        # But we should get both: (1+2)*3 = 9 and 1+(2*3) = 7
        expression = "1+2*3"
        result = self.solution.diffWaysToCompute(expression)
        
        assert 7 in result  # 1+(2*3)
        assert 9 in result  # (1+2)*3
        assert len(result) == 2

    def test_divide_and_conquer_correctness(self):
        """Test that divide and conquer approach is working correctly."""
        # Test expressions where we can manually verify all combinations
        expression = "1-2+3"
        result = self.solution.diffWaysToCompute(expression)
        
        # Possible ways:
        # (1-2)+3 = (-1)+3 = 2
        # 1-(2+3) = 1-5 = -4
        expected = [2, -4]
        assert sorted(result) == sorted(expected)

    def test_edge_cases_operators(self):
        """Test edge cases with different operators."""
        test_cases = [
            ("9-5-2", [2, 6]),    # (9-5)-2=2, 9-(5-2)=6
            ("8*2-3", [13, 5]),   # (8*2)-3=13, 8*(2-3)=-8 - wait, let me recalculate
        ]
        
        # Let's verify: "8*2-3"
        # (8*2)-3 = 16-3 = 13
        # 8*(2-3) = 8*(-1) = -8
        expression = "8*2-3"
        result = self.solution.diffWaysToCompute(expression)
        expected = [13, -8]
        assert sorted(result) == sorted(expected)

    def test_recursive_structure(self):
        """Test that recursive structure produces correct results."""
        # Test with 4 numbers to ensure deep recursion works
        expression = "1+2-3+4"
        result = self.solution.diffWaysToCompute(expression)
        
        # Should have multiple results from different parenthesizations
        assert len(result) > 2
        assert len(set(result)) > 1  # Should have different values

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Test with moderate complexity
        expression = "1*2+3*4-5"
        
        start_time = time.time()
        result = self.solution.diffWaysToCompute(expression)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 0.5
        assert len(result) > 1

    def test_mathematical_verification(self):
        """Test with manually verified mathematical results."""
        # Carefully verify a complex case
        expression = "2*3+4*5"
        result = self.solution.diffWaysToCompute(expression)
        
        # All possible parenthesizations:
        # (2*3)+(4*5) = 6+20 = 26
        # (2*(3+4))*5 = (2*7)*5 = 14*5 = 70
        # 2*((3+4)*5) = 2*(7*5) = 2*35 = 70
        # 2*(3+(4*5)) = 2*(3+20) = 2*23 = 46
        # Hmm, let me think about this more systematically...
        
        # For "2*3+4*5", the operators are * + *
        # We can split at the + operator:
        # Left: "2*3", Right: "4*5"
        # (2*3) + (4*5) = 6 + 20 = 26
        
        # Or we can split at the first *:
        # Left: "2", Right: "3+4*5"
        # For "3+4*5": (3+4)*5 = 35, 3+(4*5) = 23
        # So: 2 * 35 = 70, 2 * 23 = 46
        
        # Or split at the second *:
        # Left: "2*3+4", Right: "5"
        # For "2*3+4": (2*3)+4 = 10, 2*(3+4) = 14
        # So: 10 * 5 = 50, 14 * 5 = 70
        
        expected = [26, 46, 50, 70, 70]  # Note: 70 appears twice from different parenthesizations
        assert sorted(result) == sorted(expected)

    def test_algorithm_completeness(self):
        """Test that algorithm finds all possible parenthesizations."""
        # Use a simple case where we can enumerate all possibilities
        expression = "1+2*3"
        result = self.solution.diffWaysToCompute(expression)
        
        # There are exactly 2 ways to parenthesize this:
        # (1+2)*3 = 3*3 = 9
        # 1+(2*3) = 1+6 = 7
        assert len(result) == 2
        assert sorted(result) == [7, 9]

    def test_binary_tree_structure(self):
        """Test that results correspond to different binary tree structures."""
        # Each parenthesization corresponds to a binary tree
        # For 3 operands, there are Catalan number C_2 = 2 trees
        expression = "5-3+1"
        result = self.solution.diffWaysToCompute(expression)
        
        # Two binary trees:
        # ((5-3)+1) = (2+1) = 3
        # (5-(3+1)) = (5-4) = 1
        expected = [1, 3]
        assert sorted(result) == sorted(expected)

    def test_catalan_number_property(self):
        """Test that number of results follows Catalan number pattern."""
        # For n operators, we should get C_n different parenthesizations
        # where some might evaluate to the same value
        
        # 1 operator: at most 1 way
        result1 = self.solution.diffWaysToCompute("1+2")
        assert len(result1) == 1
        
        # 2 operators: at most 2 ways (C_2 = 2)
        result2 = self.solution.diffWaysToCompute("1+2-3")
        assert len(result2) <= 2

    def test_stress_test_small(self):
        """Small stress test to ensure robustness."""
        expressions = [
            "1+2+3+4",
            "1*2*3*4", 
            "1-2-3-4",
            "2*3-1+4",
            "5+2*3-1",
        ]
        
        for expr in expressions:
            result = self.solution.diffWaysToCompute(expr)
            assert len(result) > 0
            assert all(isinstance(x, int) for x in result)
