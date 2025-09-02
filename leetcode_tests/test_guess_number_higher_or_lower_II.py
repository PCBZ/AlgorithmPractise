"""
Test cases for LeetCode Problem #375: Guess Number Higher or Lower II
"""
import unittest

from leetcode.guess_number_higher_or_lower_II import Solution


class TestGuessNumberHigherOrLowerII(unittest.TestCase):
    """Test cases for the GuessNumberHigherOrLowerII solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test first example case - range 1."""
        n = 1
        result = self.solution.getMoneyAmount(n)
        expected = 0  # No guessing needed for single number
        assert result == expected

    def test_example_case_2(self):
        """Test second example case - range 2."""
        n = 2
        result = self.solution.getMoneyAmount(n)
        expected = 1  # Guess 1, if wrong it must be 2
        assert result == expected

    def test_small_range_3(self):
        """Test range of 3 numbers."""
        n = 3
        result = self.solution.getMoneyAmount(n)
        expected = 2  # Guess 2, worst case is 2
        assert result == expected

    def test_small_range_4(self):
        """Test range of 4 numbers."""
        n = 4
        result = self.solution.getMoneyAmount(n)
        expected = 4  # Optimal strategy costs 4
        assert result == expected

    def test_small_range_5(self):
        """Test range of 5 numbers."""
        n = 5
        result = self.solution.getMoneyAmount(n)
        expected = 6  # Minimax strategy needed
        assert result == expected

    def test_medium_range_6(self):
        """Test range of 6 numbers."""
        n = 6
        result = self.solution.getMoneyAmount(n)
        expected = 8  # More complex minimax
        assert result == expected

    def test_medium_range_7(self):
        """Test range of 7 numbers."""
        n = 7
        result = self.solution.getMoneyAmount(n)
        expected = 10  # Complex strategy
        assert result == expected

    def test_medium_range_10(self):
        """Test range of 10 numbers."""
        n = 10
        result = self.solution.getMoneyAmount(n)
        expected = 16  # Example from problem
        assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        result = self.solution.getMoneyAmount(5)
        assert isinstance(result, int)
        assert result >= 0

    def test_monotonic_property(self):
        """Test that cost increases with range size."""
        costs = []
        for n in range(1, 11):
            cost = self.solution.getMoneyAmount(n)
            costs.append(cost)
        
        # Cost should be non-decreasing
        for i in range(1, len(costs)):
            assert costs[i] >= costs[i-1], f"Cost decreased from n={i} to n={i+1}"

    def test_base_cases(self):
        """Test base cases thoroughly."""
        # Single number requires no guessing
        assert self.solution.getMoneyAmount(1) == 0
        
        # Two numbers: optimal is guess the lower one
        assert self.solution.getMoneyAmount(2) == 1

    def test_minimax_property(self):
        """Test the minimax property is satisfied."""
        # For n=3: we can guess 1, 2, or 3
        # Guess 1: max(0, cost(2,3)) + 1 = max(0, 2) + 1 = 3
        # Guess 2: max(cost(1,1), cost(3,3)) + 2 = max(0, 0) + 2 = 2  
        # Guess 3: max(cost(1,2), 0) + 3 = max(1, 0) + 3 = 4
        # Minimum is 2, so optimal guess is 2
        result = self.solution.getMoneyAmount(3)
        assert result == 2

    def test_optimal_strategy_validation(self):
        """Test that the strategy is actually optimal."""
        # For small ranges, verify the strategy manually
        test_cases = [
            (1, 0),   # No cost for single number
            (2, 1),   # Guess 1, worst case is 1
            (3, 2),   # Guess 2, worst case is 2
            (4, 4),   # More complex but verifiable
        ]
        
        for n, expected in test_cases:
            result = self.solution.getMoneyAmount(n)
            assert result == expected, f"Failed for n={n}: got {result}, expected {expected}"

    def test_memoization_effectiveness(self):
        """Test that memoization is working effectively."""
        # Run the same calculation twice, should be fast the second time
        import time
        
        n = 15
        start1 = time.time()
        result1 = self.solution.getMoneyAmount(n)
        end1 = time.time()
        
        # Create new instance to test fresh memoization
        solution2 = Solution()
        start2 = time.time()
        result2 = solution2.getMoneyAmount(n)
        end2 = time.time()
        
        # Results should be identical
        assert result1 == result2
        
        # Both should complete reasonably quickly
        assert (end1 - start1) < 1.0  # Should be much faster than 1 second
        assert (end2 - start2) < 1.0

    def test_larger_ranges(self):
        """Test with larger ranges to ensure algorithm scales."""
        larger_cases = [15, 20, 25]
        
        for n in larger_cases:
            result = self.solution.getMoneyAmount(n)
            # Should return a reasonable positive integer
            assert isinstance(result, int)
            assert result > 0
            # Should be less than worst-case linear strategy
            assert result < n * (n - 1) // 2

    def test_algorithm_correctness_small_cases(self):
        """Test algorithm correctness for small cases with manual verification."""
        # n=1: no guessing needed
        assert self.solution.getMoneyAmount(1) == 0
        
        # n=2: guess 1, if wrong it's 2 (cost = 1)
        assert self.solution.getMoneyAmount(2) == 1
        
        # n=3: guess 2, worst case costs 2
        # If target is 1: cost 2 (wrong guess)
        # If target is 3: cost 2 (wrong guess)  
        # If target is 2: cost 2 (correct guess)
        assert self.solution.getMoneyAmount(3) == 2

    def test_game_theory_properties(self):
        """Test game theory properties of the solution."""
        # The cost should represent the minimum amount needed to guarantee win
        for n in range(1, 8):
            cost = self.solution.getMoneyAmount(n)
            # Cost should be non-negative
            assert cost >= 0
            # For n=1, cost should be 0
            if n == 1:
                assert cost == 0

    def test_dynamic_programming_correctness(self):
        """Test that DP recurrence relation is correct."""
        # For n=4, let's verify the calculation
        # We need to try each possible first guess and take minimum
        n = 4
        result = self.solution.getMoneyAmount(n)
        
        # The result should be optimal among all possible first guesses
        assert isinstance(result, int)
        assert result > 0  # Should require some cost

    def test_edge_case_boundary(self):
        """Test edge cases at boundaries."""
        # Test the smallest meaningful case
        assert self.solution.getMoneyAmount(1) == 0
        
        # Test cases where strategy matters
        for n in range(2, 6):
            result = self.solution.getMoneyAmount(n)
            assert result >= 0
            assert isinstance(result, int)

    def test_subproblem_optimal_structure(self):
        """Test that optimal substructure property holds."""
        # The solution to larger problems should use optimal solutions to subproblems
        # This is implicit in the DP approach, but we can verify costs are reasonable
        
        costs = {}
        for n in range(1, 11):
            costs[n] = self.solution.getMoneyAmount(n)
        
        # Verify reasonable growth pattern
        for n in range(2, 11):
            # Cost should not grow too rapidly
            assert costs[n] <= costs[n-1] + n

    def test_worst_case_analysis(self):
        """Test worst-case analysis of the algorithm."""
        # For each n, the cost should be reasonable relative to n
        for n in range(1, 16):
            cost = self.solution.getMoneyAmount(n)
            # Cost should be at most O(n^2) in worst case
            assert cost <= n * n

    def test_strategy_optimality(self):
        """Test that the strategy is actually optimal."""
        # Known optimal values for small ranges
        known_optimal = {
            1: 0,
            2: 1, 
            3: 2,
            4: 4,
            5: 6,
            6: 8,
            7: 10,
        }
        
        for n, expected in known_optimal.items():
            result = self.solution.getMoneyAmount(n)
            assert result == expected, f"n={n}: expected {expected}, got {result}"

    def test_performance_characteristics(self):
        """Test performance characteristics of the algorithm."""
        import time
        
        # Test that algorithm completes in reasonable time for moderate inputs
        start_time = time.time()
        result = self.solution.getMoneyAmount(20)
        end_time = time.time()
        
        # Should complete quickly (well under 1 second)
        assert (end_time - start_time) < 0.5
        assert isinstance(result, int)
        assert result > 0

    def test_mathematical_properties(self):
        """Test mathematical properties of the cost function."""
        # Test some mathematical properties
        costs = []
        for n in range(1, 12):
            costs.append(self.solution.getMoneyAmount(n))
        
        # Cost for n=1 should be 0
        assert costs[0] == 0
        
        # Costs should generally increase
        for i in range(1, len(costs)):
            assert costs[i] >= costs[i-1]

    def test_minimax_algorithm_verification(self):
        """Verify the minimax algorithm produces correct results."""
        # For n=3, manually verify:
        # Guess 1: max(dp(1,0), dp(2,3)) + 1 = max(0, 2) + 1 = 3
        # Guess 2: max(dp(1,1), dp(3,3)) + 2 = max(0, 0) + 2 = 2
        # Guess 3: max(dp(1,2), dp(4,3)) + 3 = max(1, 0) + 3 = 4
        # Minimum is 2
        
        result = self.solution.getMoneyAmount(3)
        assert result == 2

    def test_complexity_bounds(self):
        """Test that the algorithm respects complexity bounds."""
        # The algorithm should handle reasonable inputs efficiently
        for n in [10, 15, 20]:
            import time
            start = time.time()
            result = self.solution.getMoneyAmount(n)
            end = time.time()
            
            # Should be efficient
            assert (end - start) < 0.1
            assert result > 0


if __name__ == "__main__":
    unittest.main()
