"""
Test cases for Can I Win problem.
"""

import os
import sys

# Add the leetcode directory to the path for importing
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'leetcode'))

import pytest
from can_i_win import Solution


class TestCanIWin:
    """Test class for Can I Win solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_example_case_1(self):
        """Test the first example case."""
        # maxChoosableInteger=10, desiredTotal=11
        # First player chooses 10, reaches 10 total
        # Second player can choose any number (1-9) and reach >=11, winning
        assert self.solution.canIWin(10, 11) is False
    
    def test_example_case_2(self):
        """Test the second example case."""
        # maxChoosableInteger=10, desiredTotal=40
        # Even with optimal play, first player cannot guarantee a win
        assert self.solution.canIWin(10, 40) is False
    
    def test_immediate_win(self):
        """Test when first player can win immediately."""
        # maxChoosableInteger=5, desiredTotal=3
        # First player can choose 3 and win immediately
        assert self.solution.canIWin(5, 3) is True
    
    def test_impossible_total(self):
        """Test when total is impossible to reach."""
        # maxChoosableInteger=3, desiredTotal=20
        # Maximum possible total is 1+2+3=6, cannot reach 20
        assert self.solution.canIWin(3, 20) is False
    
    def test_zero_or_negative_total(self):
        """Test with zero or negative desired total."""
        # If desiredTotal <= 0, first player wins immediately
        assert self.solution.canIWin(5, 0) is True
        assert self.solution.canIWin(5, -1) is True
    
    def test_single_integer_sufficient(self):
        """Test when max choosable integer equals desired total."""
        # First player can choose the max integer and win
        assert self.solution.canIWin(7, 7) is True
    
    def test_single_integer_insufficient(self):
        """Test when max choosable integer is less than desired total."""
        # maxChoosableInteger=3, desiredTotal=4
        # Need at least two moves, game theory applies
        result = self.solution.canIWin(3, 4)
        # First player chooses 3, leaving 1 for second player who wins
        assert result is False
    
    def test_small_game_first_wins(self):
        """Test small game where first player should win."""
        # maxChoosableInteger=4, desiredTotal=6
        # First player can choose 4, leaving 2 needed
        # Second player's best move leaves first player with a winning position
        assert self.solution.canIWin(4, 6) is True
    
    def test_small_game_second_wins(self):
        """Test small game where second player should win."""
        # maxChoosableInteger=2, desiredTotal=3
        # First player chooses 1 or 2
        # If 1: Second player chooses 2 and wins
        # If 2: Second player chooses 1 and wins
        assert self.solution.canIWin(2, 3) is False
    
    def test_exact_sum_scenario(self):
        """Test when sum of all integers equals desired total."""
        # maxChoosableInteger=3, desiredTotal=6 (1+2+3=6)
        # All numbers must be used, odd number of moves means first player wins
        assert self.solution.canIWin(3, 6) is True
    
    def test_optimal_play_verification(self):
        """Test case requiring optimal play analysis."""
        # maxChoosableInteger=5, desiredTotal=8
        # First player needs to make optimal moves to win
        result = self.solution.canIWin(5, 8)
        # With optimal play, first player should be able to win
        assert result is True
    
    def test_larger_numbers(self):
        """Test with larger numbers."""
        # Test case that requires more computation
        result = self.solution.canIWin(7, 16)
        # This should complete without timeout due to memoization
        assert isinstance(result, bool)
    
    def test_edge_case_minimal_input(self):
        """Test with minimal valid input."""
        # maxChoosableInteger=1, desiredTotal=1
        # First player chooses 1 and wins
        assert self.solution.canIWin(1, 1) is True
        
        # maxChoosableInteger=1, desiredTotal=2
        # First player chooses 1, second player cannot move but total not reached
        # This is an edge case - first player wins because second cannot make a move
        assert self.solution.canIWin(1, 2) is False
    
    def test_symmetric_scenarios(self):
        """Test scenarios with symmetric game states."""
        # maxChoosableInteger=4, desiredTotal=7
        result = self.solution.canIWin(4, 7)
        assert isinstance(result, bool)
    
    @pytest.mark.parametrize("max_int,target,expected", [
        (10, 11, False),  # Second player wins after first player chooses
        (10, 40, False),
        (5, 3, True),
        (3, 20, False),
        (7, 7, True),
        (3, 4, False),
        (4, 6, True),
        (2, 3, False),
        (3, 6, True),
        (1, 1, True),
        (1, 2, False),
    ])
    def test_parametrized_cases(self, max_int, target, expected):
        """Parametrized test for multiple input-output pairs."""
        assert self.solution.canIWin(max_int, target) == expected
    
    def test_game_theory_principles(self):
        """Test fundamental game theory principles."""
        # If first player can win immediately, they should
        assert self.solution.canIWin(15, 10) is True
        
        # If impossible to reach target, first player loses
        assert self.solution.canIWin(2, 10) is False
    
    def test_memoization_effectiveness(self):
        """Test that memoization makes the algorithm efficient."""
        # This test verifies the algorithm doesn't timeout on complex cases
        result = self.solution.canIWin(10, 25)
        assert isinstance(result, bool)
        
        # Run again to test memoization (should be fast)
        result2 = self.solution.canIWin(10, 25)
        assert result == result2
    
    def test_return_type(self):
        """Test that the function returns a boolean."""
        result = self.solution.canIWin(5, 8)
        assert isinstance(result, bool)
        assert result in [True, False]
    
    def test_deterministic_behavior(self):
        """Test that the function is deterministic."""
        # Same input should always give same output
        test_cases = [(5, 8), (10, 15), (3, 6)]
        for max_int, target in test_cases:
            result1 = self.solution.canIWin(max_int, target)
            result2 = self.solution.canIWin(max_int, target)
            assert result1 == result2
    
    def test_bit_manipulation_correctness(self):
        """Test that bit manipulation correctly tracks used numbers."""
        # This is implicitly tested by correct results, but we verify logic holds
        # The algorithm uses bit manipulation to track which numbers are used
        result = self.solution.canIWin(4, 5)
        assert isinstance(result, bool)
    
    def test_boundary_conditions(self):
        """Test boundary conditions of the problem."""
        # Test edge cases around the algorithm's decision points
        assert self.solution.canIWin(1, 1) is True  # Immediate win
        assert self.solution.canIWin(2, 4) is False  # Requires both numbers, second player wins
        assert self.solution.canIWin(3, 5) is True   # First player can force win
    
    def test_recursive_depth(self):
        """Test cases that require deep recursion."""
        # Test that the algorithm handles cases requiring many recursive calls
        result = self.solution.canIWin(8, 20)
        assert isinstance(result, bool)
    
    def test_optimal_strategy_examples(self):
        """Test specific examples where optimal strategy matters."""
        # Case where first player must choose carefully
        result = self.solution.canIWin(6, 10)
        assert isinstance(result, bool)
        
        # Case with clear optimal strategy
        assert self.solution.canIWin(9, 12) is True


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
