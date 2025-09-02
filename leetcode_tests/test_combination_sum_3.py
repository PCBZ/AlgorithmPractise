"""
Comprehensive tests for LeetCode Problem #216: Combination Sum III.
Tests the backtracking algorithm for finding k-number combinations that sum to target.
"""

import pytest

from leetcode.combination_sum_3 import Solution


class TestCombinationSum3:
    """Test cases for the combination sum III problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example 1: k = 3, n = 7."""
        result = self.solution.combinationSum3(3, 7)
        expected = [[1, 2, 4]]
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example 2: k = 3, n = 9."""
        result = self.solution.combinationSum3(3, 9)
        expected = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
        
        # Sort both result and expected for comparison
        result_sorted = [sorted(combo) for combo in result]
        expected_sorted = [sorted(combo) for combo in expected]
        result_sorted.sort()
        expected_sorted.sort()
        
        assert result_sorted == expected_sorted

    def test_example_case_3(self):
        """Test LeetCode example 3: k = 4, n = 1."""
        result = self.solution.combinationSum3(4, 1)
        expected = []
        assert result == expected

    def test_single_number_combination(self):
        """Test k = 1 with various targets."""
        # Valid single numbers 1-9
        for i in range(1, 10):
            result = self.solution.combinationSum3(1, i)
            assert result == [[i]]
        
        # Invalid single number targets
        assert self.solution.combinationSum3(1, 10) == []
        assert self.solution.combinationSum3(1, 0) == []

    def test_two_number_combinations(self):
        """Test k = 2 with various targets."""
        # Test k = 2, n = 3 (1 + 2)
        result = self.solution.combinationSum3(2, 3)
        assert result == [[1, 2]]
        
        # Test k = 2, n = 5 (1 + 4, 2 + 3)
        result = self.solution.combinationSum3(2, 5)
        expected = [[1, 4], [2, 3]]
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted

    def test_maximum_k_value(self):
        """Test with k = 9 (maximum possible)."""
        # k = 9, n = 45 (1+2+3+4+5+6+7+8+9 = 45)
        result = self.solution.combinationSum3(9, 45)
        expected = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        assert result == expected
        
        # k = 9, n = 44 (impossible, sum too small)
        result = self.solution.combinationSum3(9, 44)
        assert result == []
        
        # k = 9, n = 46 (impossible, sum too large)
        result = self.solution.combinationSum3(9, 46)
        assert result == []

    def test_impossible_combinations(self):
        """Test cases where no valid combinations exist."""
        # k too large for any valid sum
        assert self.solution.combinationSum3(10, 20) == []
        
        # Target too small for k numbers
        assert self.solution.combinationSum3(3, 5) == []  # Min sum for k=3 is 1+2+3=6
        
        # Target too large for k numbers
        assert self.solution.combinationSum3(2, 18) == []  # Max sum for k=2 is 8+9=17
        
        # k = 0
        assert self.solution.combinationSum3(0, 5) == []
        
        # Negative values
        assert self.solution.combinationSum3(2, -1) == []

    def test_edge_case_minimum_sum(self):
        """Test combinations with minimum possible sums."""
        # k = 2, minimum sum = 1 + 2 = 3
        result = self.solution.combinationSum3(2, 3)
        assert result == [[1, 2]]
        
        # k = 3, minimum sum = 1 + 2 + 3 = 6
        result = self.solution.combinationSum3(3, 6)
        assert result == [[1, 2, 3]]
        
        # k = 4, minimum sum = 1 + 2 + 3 + 4 = 10
        result = self.solution.combinationSum3(4, 10)
        assert result == [[1, 2, 3, 4]]

    def test_edge_case_maximum_sum(self):
        """Test combinations with maximum possible sums."""
        # k = 2, maximum sum = 8 + 9 = 17
        result = self.solution.combinationSum3(2, 17)
        assert result == [[8, 9]]
        
        # k = 3, maximum sum = 7 + 8 + 9 = 24
        result = self.solution.combinationSum3(3, 24)
        assert result == [[7, 8, 9]]
        
        # k = 4, maximum sum = 6 + 7 + 8 + 9 = 30
        result = self.solution.combinationSum3(4, 30)
        assert result == [[6, 7, 8, 9]]

    def test_medium_combinations(self):
        """Test medium complexity combinations."""
        # k = 4, n = 20
        result = self.solution.combinationSum3(4, 20)
        expected = [[1, 2, 8, 9], [1, 3, 7, 9], [1, 4, 6, 9], [1, 4, 7, 8], 
                   [1, 5, 6, 8], [2, 3, 6, 9], [2, 3, 7, 8], [2, 4, 5, 9], 
                   [2, 4, 6, 8], [2, 5, 6, 7], [3, 4, 5, 8], [3, 4, 6, 7]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted

    def test_large_target_values(self):
        """Test with larger target values."""
        # k = 5, n = 35
        result = self.solution.combinationSum3(5, 35)
        
        # Verify all results are valid
        for combo in result:
            assert len(combo) == 5
            assert sum(combo) == 35
            assert all(1 <= num <= 9 for num in combo)
            assert len(set(combo)) == 5  # All numbers unique
            assert combo == sorted(combo)  # Should be sorted due to algorithm

    def test_algorithm_properties(self):
        """Test that the algorithm maintains expected properties."""
        # Test multiple cases and verify properties
        test_cases = [(2, 10), (3, 15), (4, 18), (5, 25)]
        
        for k, n in test_cases:
            result = self.solution.combinationSum3(k, n)
            
            for combo in result:
                # Each combination should have exactly k numbers
                assert len(combo) == k
                
                # Sum should equal target
                assert sum(combo) == n
                
                # All numbers should be 1-9
                assert all(1 <= num <= 9 for num in combo)
                
                # All numbers should be unique
                assert len(set(combo)) == len(combo)
                
                # Numbers should be in ascending order (due to algorithm)
                assert combo == sorted(combo)

    def test_return_type(self):
        """Test that the function returns the correct type."""
        result = self.solution.combinationSum3(3, 9)
        assert isinstance(result, list)
        assert all(isinstance(combo, list) for combo in result)
        assert all(isinstance(num, int) for combo in result for num in combo)

    def test_no_duplicate_results(self):
        """Test that no duplicate combinations are returned."""
        result = self.solution.combinationSum3(3, 12)
        
        # Convert to tuples for set comparison
        result_tuples = [tuple(sorted(combo)) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_backtracking_efficiency(self):
        """Test that backtracking works efficiently without redundant paths."""
        # This test focuses on the algorithm's efficiency
        result = self.solution.combinationSum3(6, 30)
        
        # Verify results are valid and non-empty
        assert len(result) > 0
        for combo in result:
            assert len(combo) == 6
            assert sum(combo) == 30
            assert len(set(combo)) == 6

    def test_boundary_values(self):
        """Test boundary values for k and n."""
        # k = 1 boundary
        assert self.solution.combinationSum3(1, 1) == [[1]]
        assert self.solution.combinationSum3(1, 9) == [[9]]
        
        # n = 1 boundary
        assert self.solution.combinationSum3(1, 1) == [[1]]
        assert self.solution.combinationSum3(2, 1) == []

    @pytest.mark.parametrize("k,n,has_solution", [
        (1, 5, True),
        (2, 3, True),
        (3, 6, True),
        (4, 10, True),
        (5, 15, True),
        (6, 21, True),
        (7, 28, True),
        (8, 36, True),
        (9, 45, True),
        (2, 1, False),
        (3, 5, False),
        (4, 9, False),
        (10, 20, False),
    ])
    def test_parametrized_cases(self, k, n, has_solution):
        """Test various k and n combinations."""
        result = self.solution.combinationSum3(k, n)
        
        if has_solution:
            assert len(result) > 0
            for combo in result:
                assert len(combo) == k
                assert sum(combo) == n
        else:
            assert len(result) == 0

    def test_ascending_order_property(self):
        """Test that all combinations are returned in ascending order."""
        result = self.solution.combinationSum3(4, 22)
        
        for combo in result:
            assert combo == sorted(combo), f"Combination {combo} is not in ascending order"

    def test_combination_completeness(self):
        """Test that all valid combinations are found."""
        # For k=2, n=8, valid combinations are: [1,7], [2,6], [3,5]
        result = self.solution.combinationSum3(2, 8)
        expected = [[1, 7], [2, 6], [3, 5]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted

    def test_number_uniqueness_constraint(self):
        """Test that each number is used at most once in each combination."""
        result = self.solution.combinationSum3(3, 18)
        
        for combo in result:
            # Check no duplicates within combination
            assert len(combo) == len(set(combo))
            
            # Verify sum and length
            assert sum(combo) == 18
            assert len(combo) == 3

    def test_range_constraint(self):
        """Test that only numbers 1-9 are used."""
        result = self.solution.combinationSum3(5, 30)
        
        for combo in result:
            for num in combo:
                assert 1 <= num <= 9

    def test_empty_result_scenarios(self):
        """Test various scenarios that should return empty results."""
        empty_cases = [
            (10, 10),  # k too large
            (3, 3),    # sum too small for k=3
            (2, 20),   # sum too large for k=2
            (5, 50),   # sum too large for any k
            (0, 5),    # k is 0
        ]
        
        for k, n in empty_cases:
            result = self.solution.combinationSum3(k, n)
            assert result == [], f"Expected empty result for k={k}, n={n}, got {result}"

    def test_algorithm_optimality(self):
        """Test that the algorithm finds the optimal number of solutions."""
        # k=3, n=9 should have exactly 3 solutions
        result = self.solution.combinationSum3(3, 9)
        assert len(result) == 3
        
        # k=2, n=9 should have exactly 4 solutions: [1,8], [2,7], [3,6], [4,5]
        result = self.solution.combinationSum3(2, 9)
        assert len(result) == 4
