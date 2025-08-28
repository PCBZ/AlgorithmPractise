"""
Comprehensive test suite for LeetCode Problem #875: Koko Eating Bananas
Tests the binary search algorithm for finding minimum eating speed.
"""

import pytest
import sys
import os

# Add the parent directory to the path to import the solution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import importlib.util
spec = importlib.util.spec_from_file_location('solution',
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'leetcode', 'Koko_eat_bananas.py'))
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution


class TestKokoEatingBananas:
    """Test cases for Koko Eating Bananas problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test first basic example from LeetCode."""
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4  # Eating speed 4: ceil(3/4) + ceil(6/4) + ceil(7/4) + ceil(11/4) = 1+2+2+3 = 8
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_basic_example_2(self):
        """Test second basic example from LeetCode."""
        piles = [30, 11, 23, 4, 20]
        h = 5
        expected = 30  # Must eat fastest pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_basic_example_3(self):
        """Test third basic example from LeetCode."""
        piles = [30, 11, 23, 4, 20]
        h = 6
        expected = 23  # Eating speed 23 allows finishing in 6 hours
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_single_pile_single_hour(self):
        """Test single pile that must be eaten in one hour."""
        piles = [100]
        h = 1
        expected = 100  # Must eat entire pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_single_pile_multiple_hours(self):
        """Test single pile with multiple hours available."""
        piles = [1000000000]
        h = 2
        expected = 500000000  # Can eat half per hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_multiple_piles_ample_time(self):
        """Test when there's ample time (one hour per banana)."""
        piles = [1, 1, 1, 1]
        h = 10
        expected = 1  # Can eat one banana per hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_exact_time_needed(self):
        """Test when time exactly matches pile count."""
        piles = [5, 5, 5, 5]
        h = 4
        expected = 5  # Need to eat one pile per hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_minimum_time_constraint(self):
        """Test when given exactly the number of piles as hours."""
        piles = [10, 20, 30]
        h = 3
        expected = 30  # Must handle largest pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_small_piles_many_hours(self):
        """Test small piles with many hours available."""
        piles = [1, 1, 1]
        h = 100
        expected = 1  # Minimum eating speed is 1
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_large_piles_tight_time(self):
        """Test large piles with tight time constraint."""
        piles = [1000, 1000, 1000]
        h = 3
        expected = 1000  # Must eat one pile per hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_uneven_pile_sizes(self):
        """Test with very uneven pile sizes."""
        piles = [1, 1000000]
        h = 2
        expected = 1000000  # Bottleneck is the largest pile
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_binary_search_boundary(self):
        """Test binary search finds correct boundary."""
        piles = [2, 2, 2, 2]
        h = 5
        expected = 2  # Speed 2: each pile takes 1 hour, total 4 hours < 5
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_fractional_eating_ceiling(self):
        """Test that partial pile eating is properly handled."""
        piles = [5, 5, 5]
        h = 5
        expected = 3  # Speed 3: ceil(5/3) = 2 hours per pile, total 6 > 5, so try speed 4
        # Actually speed 3: ceil(5/3)*3 = 2*3 = 6 > 5, speed 4: ceil(5/4)*3 = 2*3 = 6 > 5
        # Speed 5: ceil(5/5)*3 = 1*3 = 3 <= 5 ✓
        expected = 5
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_edge_case_minimum_speed(self):
        """Test edge case where minimum speed is required."""
        piles = [1, 1]
        h = 3
        expected = 1  # Can eat slowly, 1 banana per hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_edge_case_maximum_speed(self):
        """Test edge case where maximum speed is required."""
        piles = [100, 200, 300]
        h = 3
        expected = 300  # Must handle largest pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_optimization_middle_speed(self):
        """Test finding optimal middle speed."""
        piles = [10, 10, 10, 10]
        h = 6
        # Speed 7: ceil(10/7)*4 = 2*4 = 8 > 6
        # Speed 8: ceil(10/8)*4 = 2*4 = 8 > 6  
        # Speed 9: ceil(10/9)*4 = 2*4 = 8 > 6
        # Speed 10: ceil(10/10)*4 = 1*4 = 4 <= 6 ✓
        expected = 10
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_large_numbers(self):
        """Test with large numbers within constraints."""
        piles = [1000000, 1000000]
        h = 3
        expected = 1000000  # Need to handle one pile per hour (rounded up)
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_progressive_pile_sizes(self):
        """Test with progressively increasing pile sizes."""
        piles = [1, 2, 4, 8, 16]
        h = 8
        # Speed 4: ceil(1/4)+ceil(2/4)+ceil(4/4)+ceil(8/4)+ceil(16/4) = 1+1+1+2+4 = 9 > 8
        # Speed 5: ceil(1/5)+ceil(2/5)+ceil(4/5)+ceil(8/5)+ceil(16/5) = 1+1+1+2+4 = 9 > 8
        # Speed 6: 1+1+1+2+3 = 8 <= 8 ✓
        expected = 6
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_binary_search_convergence(self):
        """Test that binary search converges correctly."""
        piles = [3, 6, 7, 11]
        h = 9
        # More time available, should find lower speed than h=8 case
        expected = 3  # Speed 3: ceil(3/3)+ceil(6/3)+ceil(7/3)+ceil(11/3) = 1+2+3+4 = 10 > 9
        # Speed 4: 1+2+2+3 = 8 <= 9 ✓
        expected = 4
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_all_piles_same_size(self):
        """Test when all piles have the same size."""
        piles = [7, 7, 7, 7, 7]
        h = 10
        # Speed 4: ceil(7/4)*5 = 2*5 = 10 <= 10 ✓
        expected = 4
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_performance_large_input(self):
        """Test performance with larger input."""
        piles = [100] * 100  # 100 piles of 100 bananas each
        h = 150
        # Need to finish 100 piles in 150 hours
        # Speed 67: ceil(100/67)*100 = 2*100 = 200 > 150
        # Speed 100: ceil(100/100)*100 = 1*100 = 100 <= 150 ✓
        result = self.solution.minEatingSpeed(piles, h)
        assert isinstance(result, int) and result > 0

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        piles = [1, 4, 7, 10]
        h = 6
        
        result = self.solution.minEatingSpeed(piles, h)
        
        # Result should be positive
        assert result > 0
        
        # Result should be at most the maximum pile size
        assert result <= max(piles)
        
        # Verify the result actually works
        import math
        hours_needed = sum(math.ceil(pile / result) for pile in piles)
        assert hours_needed <= h

    def test_minimum_possible_result(self):
        """Test that result is indeed minimum."""
        piles = [5, 5, 5]
        h = 15
        result = self.solution.minEatingSpeed(piles, h)
        
        # With speed 1: ceil(5/1)*3 = 5*3 = 15 <= 15 ✓
        expected = 1
        assert result == expected

    def test_edge_case_h_equals_pile_count(self):
        """Test when h equals number of piles."""
        piles = [1, 2, 3, 4, 5]
        h = 5
        expected = 5  # Must handle largest pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_very_large_pile_single_hour(self):
        """Test very large pile with minimal time."""
        piles = [1000000000]
        h = 1
        expected = 1000000000  # Must eat entire pile in one hour
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_eating_speed_calculation(self):
        """Test eating speed calculation accuracy."""
        piles = [6, 8, 10]
        h = 4
        # Speed 8: ceil(6/8)+ceil(8/8)+ceil(10/8) = 1+1+2 = 4 <= 4 ✓
        # Speed 7: ceil(6/7)+ceil(8/7)+ceil(10/7) = 1+2+2 = 5 > 4
        expected = 8
        assert self.solution.minEatingSpeed(piles, h) == expected

    def test_boundary_condition_exact_division(self):
        """Test boundary when piles divide exactly by speed."""
        piles = [12, 8, 4]
        h = 3
        # Speed 12: ceil(12/12)+ceil(8/12)+ceil(4/12) = 1+1+1 = 3 <= 3 ✓
        expected = 12
        assert self.solution.minEatingSpeed(piles, h) == expected


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
