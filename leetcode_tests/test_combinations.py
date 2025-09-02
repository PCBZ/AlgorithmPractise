"""
Comprehensive tests for LeetCode Problem #77: Combinations.
Tests the backtracking algorithm for generating k-size combinations from range [1, n].
"""

import pytest
from math import comb

from leetcode.combinations import Solution


class TestCombinations:
    """Test cases for the combinations problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example 1: n = 4, k = 2."""
        result = self.solution.combine(4, 2)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        
        # Sort both result and expected for comparison
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_example_case_2(self):
        """Test LeetCode example 2: n = 1, k = 1."""
        result = self.solution.combine(1, 1)
        expected = [[1]]
        assert result == expected

    def test_single_element_combinations(self):
        """Test k = 1 with various values of n."""
        # n = 3, k = 1
        result = self.solution.combine(3, 1)
        expected = [[1], [2], [3]]
        assert sorted(result) == sorted(expected)
        
        # n = 5, k = 1
        result = self.solution.combine(5, 1)
        expected = [[1], [2], [3], [4], [5]]
        assert sorted(result) == sorted(expected)

    def test_full_combinations(self):
        """Test k = n (all elements)."""
        # n = 3, k = 3
        result = self.solution.combine(3, 3)
        expected = [[1, 2, 3]]
        assert result == expected
        
        # n = 4, k = 4
        result = self.solution.combine(4, 4)
        expected = [[1, 2, 3, 4]]
        assert result == expected

    def test_empty_combinations(self):
        """Test k = 0 (empty combinations)."""
        # k = 0 should return one empty combination (mathematically correct)
        result = self.solution.combine(5, 0)
        assert result == [[]]

    def test_impossible_combinations(self):
        """Test cases where k > n."""
        # k > n should return empty list
        assert self.solution.combine(3, 5) == []
        assert self.solution.combine(1, 2) == []
        assert self.solution.combine(2, 10) == []

    def test_two_element_combinations(self):
        """Test k = 2 with various values of n."""
        # n = 3, k = 2
        result = self.solution.combine(3, 2)
        expected = [[1, 2], [1, 3], [2, 3]]
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted
        
        # n = 5, k = 2
        result = self.solution.combine(5, 2)
        expected = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], 
                   [3, 4], [3, 5], [4, 5]]
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted

    def test_three_element_combinations(self):
        """Test k = 3 with various values of n."""
        # n = 4, k = 3
        result = self.solution.combine(4, 3)
        expected = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        assert result_sorted == expected_sorted

    def test_combination_count_correctness(self):
        """Test that the number of combinations matches C(n,k)."""
        test_cases = [
            (4, 2, 6),   # C(4,2) = 6
            (5, 3, 10),  # C(5,3) = 10
            (6, 2, 15),  # C(6,2) = 15
            (6, 4, 15),  # C(6,4) = 15
            (7, 3, 35),  # C(7,3) = 35
        ]
        
        for n, k, expected_count in test_cases:
            result = self.solution.combine(n, k)
            assert len(result) == expected_count
            assert len(result) == comb(n, k)  # Using math.comb for verification

    def test_combination_properties(self):
        """Test that all combinations satisfy required properties."""
        test_cases = [(5, 3), (6, 2), (7, 4)]
        
        for n, k in test_cases:
            result = self.solution.combine(n, k)
            
            for combo in result:
                # Each combination should have exactly k elements
                assert len(combo) == k
                
                # All elements should be in range [1, n]
                assert all(1 <= num <= n for num in combo)
                
                # All elements should be unique
                assert len(set(combo)) == len(combo)
                
                # Elements should be in ascending order (due to algorithm)
                assert combo == sorted(combo)

    def test_no_duplicate_combinations(self):
        """Test that no duplicate combinations are returned."""
        result = self.solution.combine(6, 3)
        
        # Convert to tuples for set comparison
        result_tuples = [tuple(sorted(combo)) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_ascending_order_generation(self):
        """Test that combinations are generated in proper order."""
        result = self.solution.combine(5, 3)
        
        # Each combination should be in ascending order
        for combo in result:
            assert combo == sorted(combo)

    def test_large_combinations(self):
        """Test with larger values of n and k."""
        # n = 10, k = 3
        result = self.solution.combine(10, 3)
        expected_count = comb(10, 3)  # 120
        assert len(result) == expected_count
        
        # Verify a few specific combinations exist
        assert [1, 2, 3] in result
        assert [8, 9, 10] in result
        assert [1, 5, 10] in result

    def test_edge_case_n_equals_2(self):
        """Test edge cases with n = 2."""
        # n = 2, k = 1
        result = self.solution.combine(2, 1)
        expected = [[1], [2]]
        assert sorted(result) == sorted(expected)
        
        # n = 2, k = 2
        result = self.solution.combine(2, 2)
        expected = [[1, 2]]
        assert result == expected

    def test_medium_complexity_case(self):
        """Test a medium complexity case."""
        # n = 6, k = 3
        result = self.solution.combine(6, 3)
        
        # Should have C(6,3) = 20 combinations
        assert len(result) == 20
        
        # Check some specific combinations
        expected_combinations = [
            [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 2, 6],
            [1, 3, 4], [1, 3, 5], [1, 3, 6], [1, 4, 5],
            [1, 4, 6], [1, 5, 6], [2, 3, 4], [2, 3, 5],
            [2, 3, 6], [2, 4, 5], [2, 4, 6], [2, 5, 6],
            [3, 4, 5], [3, 4, 6], [3, 5, 6], [4, 5, 6]
        ]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected_combinations])
        assert result_sorted == expected_sorted

    def test_return_type(self):
        """Test that the function returns the correct type."""
        result = self.solution.combine(4, 2)
        assert isinstance(result, list)
        assert all(isinstance(combo, list) for combo in result)
        assert all(isinstance(num, int) for combo in result for num in combo)

    def test_algorithm_efficiency(self):
        """Test that the algorithm generates combinations efficiently."""
        # Test with a moderately large case
        result = self.solution.combine(8, 4)
        expected_count = comb(8, 4)  # 70
        assert len(result) == expected_count
        
        # Verify no duplicates
        result_tuples = [tuple(combo) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_boundary_combinations(self):
        """Test boundary cases."""
        # Minimum valid case
        result = self.solution.combine(1, 1)
        assert result == [[1]]
        
        # k = 0 (should return one empty combination)
        result = self.solution.combine(5, 0)
        assert result == [[]]

    @pytest.mark.parametrize("n,k,expected_count", [
        (1, 1, 1),
        (2, 1, 2),
        (2, 2, 1),
        (3, 1, 3),
        (3, 2, 3),
        (3, 3, 1),
        (4, 2, 6),
        (4, 3, 4),
        (5, 2, 10),
        (5, 3, 10),
    ])
    def test_parametrized_combination_counts(self, n, k, expected_count):
        """Test combination counts for various n and k values."""
        result = self.solution.combine(n, k)
        assert len(result) == expected_count

    def test_lexicographic_properties(self):
        """Test lexicographic properties of generated combinations."""
        result = self.solution.combine(5, 2)
        
        # Combinations should be generated in lexicographic order
        # (due to the nature of the backtracking algorithm)
        for i in range(len(result) - 1):
            assert result[i] < result[i + 1] or result[i][0] < result[i + 1][0]

    def test_completeness_verification(self):
        """Test that all possible combinations are generated."""
        # For n=4, k=2, manually verify all combinations
        result = self.solution.combine(4, 2)
        expected_all = [
            [1, 2], [1, 3], [1, 4],
            [2, 3], [2, 4], [3, 4]
        ]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected_all])
        assert result_sorted == expected_sorted

    def test_range_validation(self):
        """Test that all numbers are within the valid range [1, n]."""
        result = self.solution.combine(7, 3)
        
        for combo in result:
            for num in combo:
                assert 1 <= num <= 7

    def test_combination_uniqueness_within_set(self):
        """Test that within each combination, all numbers are unique."""
        result = self.solution.combine(6, 4)
        
        for combo in result:
            assert len(combo) == len(set(combo))

    def test_backtracking_correctness(self):
        """Test that backtracking generates correct combinations."""
        # Test a case where we can manually verify
        result = self.solution.combine(4, 3)
        
        # Should generate: [1,2,3], [1,2,4], [1,3,4], [2,3,4]
        expected = [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
        
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        assert result_sorted == expected_sorted

    def test_invalid_input_handling(self):
        """Test handling of invalid inputs."""
        # k > n
        assert self.solution.combine(3, 5) == []
        
        # k = 0 (returns one empty combination)
        assert self.solution.combine(5, 0) == [[]]
        
        # n = 0 (edge case)
        assert self.solution.combine(0, 1) == []

    def test_mathematical_correctness(self):
        """Test mathematical correctness against known formulas."""
        # Test several cases and verify with binomial coefficient
        test_cases = [(5, 2), (6, 3), (7, 4), (8, 3)]
        
        for n, k in test_cases:
            result = self.solution.combine(n, k)
            expected_count = comb(n, k)
            assert len(result) == expected_count
            
            # Verify all combinations are valid
            for combo in result:
                assert len(combo) == k
                assert all(1 <= x <= n for x in combo)
                assert combo == sorted(combo)
                assert len(set(combo)) == k
