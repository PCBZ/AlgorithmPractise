"""
Test cases for LeetCode 486: Predict the Winner
Testing recursive game theory approach.
"""

import pytest
from leetcode.predict_winner import Solution


class TestPredictWinner:
    """Test cases for Predict the Winner problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Example test cases from LeetCode
    def test_example_1(self):
        """Test [1, 5, 2] -> False."""
        assert self.solution.predictTheWinner([1, 5, 2]) == False
    
    def test_example_2(self):
        """Test [1, 5, 233, 7] -> True."""
        assert self.solution.predictTheWinner([1, 5, 233, 7]) == True
    
    # Edge cases
    def test_single_element(self):
        """Test with single element."""
        assert self.solution.predictTheWinner([1]) == True
        assert self.solution.predictTheWinner([100]) == True
    
    def test_two_elements(self):
        """Test with two elements."""
        assert self.solution.predictTheWinner([1, 5]) == True  # Player 1 takes 5
        assert self.solution.predictTheWinner([5, 1]) == True  # Player 1 takes 5
        assert self.solution.predictTheWinner([1, 1]) == True  # Tie, Player 1 wins
        assert self.solution.predictTheWinner([3, 7]) == True  # Player 1 takes 7
    
    def test_equal_elements(self):
        """Test arrays with equal elements."""
        assert self.solution.predictTheWinner([2, 2]) == True
        assert self.solution.predictTheWinner([3, 3, 3]) == True
        assert self.solution.predictTheWinner([1, 1, 1, 1]) == True
    
    def test_alternating_pattern(self):
        """Test alternating high-low pattern."""
        assert self.solution.predictTheWinner([1, 100, 1]) == False
        assert self.solution.predictTheWinner([1, 100, 1, 100]) == True
        assert self.solution.predictTheWinner([100, 1, 100, 1]) == True
    
    def test_descending_array(self):
        """Test descending arrays."""
        assert self.solution.predictTheWinner([5, 4, 3, 2, 1]) == True
        assert self.solution.predictTheWinner([10, 8, 6, 4, 2]) == True
    
    def test_ascending_array(self):
        """Test ascending arrays."""
        assert self.solution.predictTheWinner([1, 2, 3, 4, 5]) == True
        assert self.solution.predictTheWinner([2, 4, 6, 8, 10]) == True
    
    def test_symmetric_arrays(self):
        """Test symmetric arrays."""
        assert self.solution.predictTheWinner([1, 3, 1]) == False
        assert self.solution.predictTheWinner([2, 4, 2]) == True
        assert self.solution.predictTheWinner([1, 5, 3, 5, 1]) == False
    
    def test_large_differences(self):
        """Test arrays with large differences between elements."""
        assert self.solution.predictTheWinner([1, 1000]) == True
        assert self.solution.predictTheWinner([1, 1000, 1]) == False
        assert self.solution.predictTheWinner([1000, 1, 1000]) == True
    
    def test_medium_arrays(self):
        """Test medium-sized arrays."""
        assert self.solution.predictTheWinner([1, 3, 5, 7, 9]) == True
        assert self.solution.predictTheWinner([2, 4, 6, 8]) == True
        assert self.solution.predictTheWinner([1, 2, 4, 8, 16]) == True
    
    def test_complex_cases(self):
        """Test more complex strategic cases."""
        # Cases where optimal play matters
        assert self.solution.predictTheWinner([1, 5, 233, 7]) == True
        assert self.solution.predictTheWinner([1, 5, 2]) == False
        assert self.solution.predictTheWinner([2, 4, 55, 6, 8]) == False
    
    # Mathematical property tests
    def test_even_length_arrays(self):
        """Player 1 should always win with even-length arrays."""
        # With even length, Player 1 can always force a win
        assert self.solution.predictTheWinner([1, 2]) == True
        assert self.solution.predictTheWinner([3, 7, 2, 3]) == True
        assert self.solution.predictTheWinner([1, 2, 3, 4, 5, 6]) == True
    
    def test_boundary_values(self):
        """Test with boundary values."""
        assert self.solution.predictTheWinner([0]) == True
        assert self.solution.predictTheWinner([0, 1]) == True
        assert self.solution.predictTheWinner([1, 0]) == True
    
    def test_strategic_play(self):
        """Test cases requiring strategic thinking."""
        # Player 1 must think ahead to avoid being trapped
        assert self.solution.predictTheWinner([3, 7, 2, 3]) == True
        assert self.solution.predictTheWinner([1, 567, 1, 1]) == True
        assert self.solution.predictTheWinner([20, 30, 2, 2, 2, 10]) == True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
