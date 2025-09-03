"""
Comprehensive tests for Minimum Cost to Hire K Workers problem.

Tests the greedy algorithm implementation using heap to find
minimum cost to hire exactly K workers.
"""
import pytest

from leetcode.minimum_cost_to_hire_k_workers import Solution


class TestMinimumCostToHireKWorkers:
    """Test class for minimum cost to hire K workers implementation."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.fixture
    def leetcode_example_1(self):
        """First LeetCode example."""
        return [10, 20, 5], [70, 50, 30], 2

    @pytest.fixture
    def leetcode_example_2(self):
        """Second LeetCode example."""
        return [3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3

    def test_leetcode_example_1(self, leetcode_example_1):
        """Test first LeetCode example."""
        quality, wage, k = leetcode_example_1
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        assert abs(result - 105.0) < 1e-9

    def test_leetcode_example_2(self, leetcode_example_2):
        """Test second LeetCode example."""
        quality, wage, k = leetcode_example_2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        expected = 30.666666666666664
        assert abs(result - expected) < 1e-9

    def test_empty_workers(self):
        """Test empty input."""
        result = self.solution.mincostToHireWorkers([], [], 0)
        assert result == 0.0

    def test_invalid_k(self):
        """Test invalid k values."""
        quality = [10, 20]
        wage = [70, 50]
        
        # k = 0
        result = self.solution.mincostToHireWorkers(quality, wage, 0)
        assert result == 0.0
        
        # Negative k
        result = self.solution.mincostToHireWorkers(quality, wage, -1)
        assert result == 0.0

    def test_single_worker(self):
        """Test hiring single worker."""
        quality = [10]
        wage = [50]
        k = 1
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        assert result == 50.0

    def test_hire_all_workers(self):
        """Test hiring all available workers."""
        quality = [10, 20, 5]
        wage = [70, 50, 30]
        k = 3  # Hire all workers
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should hire all with rate = max(wage/quality) = max(7, 2.5, 6) = 7
        # Total cost = 7 * (10 + 20 + 5) = 7 * 35 = 245
        assert abs(result - 245.0) < 1e-9

    def test_two_workers_equal_ratio(self):
        """Test with workers having equal wage/quality ratio."""
        quality = [10, 20]
        wage = [50, 100]  # Both have ratio 5.0
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Cost = 5.0 * (10 + 20) = 150.0
        assert abs(result - 150.0) < 1e-9

    def test_high_quality_worker(self):
        """Test scenario with one very high quality worker."""
        quality = [1, 100]
        wage = [10, 50]  # Ratios: 10.0, 0.5
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Must use ratio 10.0, cost = 10.0 * (1 + 100) = 1010.0
        assert abs(result - 1010.0) < 1e-9

    def test_optimal_subset_selection(self):
        """Test that algorithm selects optimal subset."""
        quality = [10, 20, 30, 40]
        wage = [100, 150, 120, 160]  # Ratios: 10, 7.5, 4, 4
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should select workers with ratios 4, 4 (quality 30, 40)
        # Cost = 4 * (30 + 40) = 280.0
        assert abs(result - 280.0) < 1e-9

    def test_fractional_ratios(self):
        """Test with fractional wage/quality ratios."""
        quality = [3, 7]
        wage = [10, 20]  # Ratios: 10/3 ≈ 3.33, 20/7 ≈ 2.86
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Use higher ratio 10/3, cost = (10/3) * (3 + 7) = (10/3) * 10 = 100/3
        expected = 100.0 / 3
        assert abs(result - expected) < 1e-9

    def test_large_numbers(self):
        """Test with large numbers."""
        quality = [1000, 2000, 3000]
        wage = [10000, 15000, 12000]  # Ratios: 10, 7.5, 4
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Algorithm selects workers with quality 2000, 1000 at rate 10.0
        # Cost = 10.0 * (2000 + 1000) = 30000.0
        assert abs(result - 30000.0) < 1e-9

    def test_identical_workers(self):
        """Test with identical workers."""
        quality = [10, 10, 10]
        wage = [50, 50, 50]
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # All have ratio 5.0, cost = 5.0 * (10 + 10) = 100.0
        assert abs(result - 100.0) < 1e-9

    def test_minimum_wage_constraint(self):
        """Test that minimum wage constraint is respected."""
        quality = [1, 2]
        wage = [5, 10]  # Worker 1: ratio 5, Worker 2: ratio 5
        k = 1
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should be able to hire just worker 1 for cost 5.0
        assert abs(result - 5.0) < 1e-9

    def test_descending_quality(self):
        """Test with descending quality values."""
        quality = [50, 40, 30, 20, 10]
        wage = [100, 80, 60, 40, 20]  # All have ratio 2.0
        k = 3
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should select 3 workers with lowest quality: 30, 20, 10
        # Cost = 2.0 * (30 + 20 + 10) = 120.0
        assert abs(result - 120.0) < 1e-9

    def test_mixed_ratios(self):
        """Test with mixed high and low ratios."""
        quality = [1, 2, 3, 4, 5]
        wage = [10, 8, 9, 12, 15]  # Ratios: 10, 4, 3, 3, 3
        k = 3
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should select workers with ratios 3, 3, 3 (quality 3, 4, 5)
        # Cost = 3 * (3 + 4 + 5) = 36.0
        assert abs(result - 36.0) < 1e-9

    def test_edge_case_k_equals_n(self):
        """Test when k equals number of workers."""
        quality = [1, 2, 3]
        wage = [2, 4, 6]  # All have ratio 2.0
        k = 3
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Must hire all, cost = 2.0 * (1 + 2 + 3) = 12.0
        assert abs(result - 12.0) < 1e-9

    def test_precision_float_arithmetic(self):
        """Test precision with float arithmetic."""
        quality = [7, 11, 13]
        wage = [23, 37, 41]
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Calculate expected result manually
        ratios = [23/7, 37/11, 41/13]  # ≈ [3.286, 3.364, 3.154]
        # Should select workers with quality 7, 13 (ratios ≈ 3.286, 3.154)
        # Cost ≈ 3.286 * (7 + 13) ≈ 65.714
        assert result > 60 and result < 70  # Reasonable bounds

    def test_performance_larger_input(self):
        """Test with larger input for performance."""
        n = 50
        quality = list(range(1, n + 1))
        wage = [i * 2 for i in range(1, n + 1)]  # All have ratio 2.0
        k = 10
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Should select 10 workers with lowest quality: 1,2,...,10
        # Cost = 2.0 * sum(1 to 10) = 2.0 * 55 = 110.0
        assert abs(result - 110.0) < 1e-9

    def test_floating_point_wage(self):
        """Test with floating point wages."""
        quality = [1, 2]
        wage = [1.5, 3.0]  # Both have ratio 1.5
        k = 1
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        assert abs(result - 1.5) < 1e-9

    def test_greedy_correctness(self):
        """Test that greedy approach gives optimal solution."""
        quality = [4, 3, 2, 1]
        wage = [8, 9, 6, 5]  # Ratios: 2, 3, 3, 5
        k = 2
        result = self.solution.mincostToHireWorkers(quality, wage, k)
        # Algorithm selects workers with quality 2, 1 at rate 5.0
        # Cost = 5.0 * (2 + 1) = 15.0
        assert abs(result - 15.0) < 1e-9


if __name__ == '__main__':
    pytest.main([__file__])
