"""
Comprehensive tests for New 21 Game problem.

Tests the dynamic programming algorithm for calculating the probability
that Alice ends with n or fewer points in the New 21 Game.
"""
import pytest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import using exec to handle the non-standard module name
solution_globals = {}
with open(os.path.join(os.path.dirname(__file__), '..', 'leetcode', 'new_21_game.py'), 'r') as f:
    exec(f.read(), solution_globals)

Solution = solution_globals['Solution']


class TestNew21Game:
    """Test class for New 21 Game implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return 10, 1, 10

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return 6, 1, 10

    @pytest.fixture
    def leetcode_example_3(self):
        """Third LeetCode example."""
        return 21, 17, 10

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        n, k, max_pts = leetcode_example_1
        result = self.solution.new21Game(n, k, max_pts)
        assert abs(result - 1.0) < 1e-9

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        n, k, max_pts = leetcode_example_2
        result = self.solution.new21Game(n, k, max_pts)
        assert abs(result - 0.6) < 1e-9

    def test_leetcode_example_3(self, leetcode_example_3):
        """Test third LeetCode example."""
        n, k, max_pts = leetcode_example_3
        result = self.solution.new21Game(n, k, max_pts)
        # Should be approximately 0.73278
        assert abs(result - 0.73278) < 1e-4

    def test_k_equals_zero(self):
        """Test when k = 0 (Alice never draws)."""
        result = self.solution.new21Game(5, 0, 3)
        assert result == 1.0

    def test_n_very_large(self):
        """Test when n >= k + max_pts (Alice always wins)."""
        result = self.solution.new21Game(100, 10, 5)
        assert result == 1.0

    def test_simple_case_k1_max1(self):
        """Test simple case with k=1, max_pts=1."""
        # Alice draws exactly 1 point and stops
        result = self.solution.new21Game(1, 1, 1)
        assert result == 1.0

    def test_impossible_case(self):
        """Test case where it's impossible to win."""
        # n=1, k=2, max_pts=10: Alice must draw at least 2 points
        result = self.solution.new21Game(1, 2, 10)
        assert result == 0.0

    def test_k_equals_n(self):
        """Test when k equals n."""
        result = self.solution.new21Game(5, 5, 3)
        # Alice stops at exactly k=5, but might overshoot
        assert abs(result - 0.49794238683127573) < 1e-9

    def test_small_values(self):
        """Test with small parameter values."""
        # n=2, k=2, max_pts=2: Alice can draw 1 or 2, if she draws 2 she stops at 2 (valid)
        # if she draws 1, she draws again and can get 3 or 4 (invalid) or 2 (valid)
        result = self.solution.new21Game(2, 2, 2)
        assert abs(result - 0.75) < 1e-9

    def test_probability_calculation(self):
        """Test probability calculation with known case."""
        # n=3, k=2, max_pts=2
        # Alice can get: 1 (50%), 2 (50%)
        # From 1: can get 2, 3 (each 50%)
        # Valid outcomes: 2, 3 → probability = 1.0
        result = self.solution.new21Game(3, 2, 2)
        assert result == 1.0

    def test_edge_case_n_equals_k_minus_1(self):
        """Test edge case where n = k - 1."""
        # Alice needs to reach at least k, but n < k
        result = self.solution.new21Game(4, 5, 3)
        assert result == 0.0

    def test_medium_complexity(self):
        """Test medium complexity case."""
        # n=5, k=3, max_pts=2
        result = self.solution.new21Game(5, 3, 2)
        # Should be a specific probability
        assert 0.0 <= result <= 1.0

    def test_probability_bounds(self):
        """Test that all probabilities are in [0, 1]."""
        test_cases = [
            (10, 5, 3),
            (20, 15, 5),
            (100, 50, 10),
            (5, 10, 2),
            (1, 5, 1)
        ]
        
        for n, k, max_pts in test_cases:
            result = self.solution.new21Game(n, k, max_pts)
            assert 0.0 <= result <= 1.0, f"Failed for n={n}, k={k}, max_pts={max_pts}"

    def test_monotonicity_in_n(self):
        """Test that probability increases as n increases."""
        k, max_pts = 5, 3
        prev_result = 0.0
        
        for n in range(k, k + max_pts + 5):
            result = self.solution.new21Game(n, k, max_pts)
            assert result >= prev_result, f"Non-monotonic at n={n}"
            prev_result = result

    def test_specific_probability_cases(self):
        """Test specific cases with known probabilities."""
        # Case where Alice draws 1 point with probability 1
        result = self.solution.new21Game(10, 1, 1)
        assert result == 1.0
        
        # Case where Alice must draw more than allowed
        result = self.solution.new21Game(1, 10, 5)
        assert result == 0.0

    def test_large_parameters(self):
        """Test with larger parameter values."""
        result = self.solution.new21Game(1000, 500, 100)
        assert 0.0 <= result <= 1.0

    def test_max_pts_equals_one(self):
        """Test when max_pts = 1 (deterministic draws)."""
        # Alice draws exactly 1 point each time
        result = self.solution.new21Game(5, 3, 1)
        # Alice will reach exactly k=3 points, which is <= 5
        assert result == 1.0

    def test_floating_point_precision(self):
        """Test that results have reasonable floating point precision."""
        result = self.solution.new21Game(10, 5, 3)
        # Should not have extreme precision issues
        assert isinstance(result, float)
        assert not (result < 0.0 or result > 1.0)

    def test_edge_cases_comprehensive(self):
        """Test comprehensive edge cases."""
        # k = 0
        assert self.solution.new21Game(10, 0, 5) == 1.0
        
        # n >= k + max_pts
        assert self.solution.new21Game(20, 5, 10) == 1.0
        
        # n < k (impossible to win)
        assert self.solution.new21Game(3, 5, 2) == 0.0

    def test_algorithm_correctness(self):
        """Test algorithm correctness with manual calculation."""
        # Simple case: n=2, k=2, max_pts=1
        # Alice draws 1 point (prob=1) and gets 1 point
        # Since 1 < k=2, Alice draws again and gets 1 more point → total 2
        # 2 <= n=2, so probability = 1.0
        result = self.solution.new21Game(2, 2, 1)
        assert result == 1.0

    def test_symmetry_properties(self):
        """Test certain symmetry properties."""
        # When n is very large compared to k + max_pts, should always be 1.0
        large_n_cases = [
            (1000, 10, 5),
            (500, 20, 8),
            (100, 5, 3)
        ]
        
        for n, k, max_pts in large_n_cases:
            if n >= k + max_pts:
                result = self.solution.new21Game(n, k, max_pts)
                assert result == 1.0

    def test_performance_larger_inputs(self):
        """Test performance with larger inputs."""
        # Should complete in reasonable time
        result = self.solution.new21Game(10000, 5000, 100)
        assert 0.0 <= result <= 1.0

    def test_dp_edge_conditions(self):
        """Test edge conditions for dynamic programming."""
        # Test when dp array boundary conditions are important
        test_cases = [
            (1, 1, 1),   # Minimal case
            (2, 1, 2),   # Small case
            (10, 9, 8),  # Close to boundary
        ]
        
        for n, k, max_pts in test_cases:
            result = self.solution.new21Game(n, k, max_pts)
            assert 0.0 <= result <= 1.0


if __name__ == '__main__':
    pytest.main([__file__])
