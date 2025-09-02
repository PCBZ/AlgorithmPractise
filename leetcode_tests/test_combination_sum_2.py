"""
Comprehensive tests for LeetCode Problem #40: Combination Sum II.
Tests the backtracking algorithm for finding unique combinations with duplicates.
"""

import pytest

from leetcode.combination_sum_2 import Solution


class TestCombinationSum2:
    """Test cases for the combination sum II problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example 1: candidates = [10,1,2,7,6,1,5], target = 8."""
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        
        # Sort both result and expected for comparison
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_example_case_2(self):
        """Test LeetCode example 2: candidates = [2,5,2,1,2], target = 5."""
        candidates = [2, 5, 2, 1, 2]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 2, 2], [5]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_single_element_target(self):
        """Test when target can be achieved with single element."""
        candidates = [1, 2, 3, 4, 5]
        target = 3
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 2], [3]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_no_solution_exists(self):
        """Test when no combination can achieve the target."""
        candidates = [2, 4, 6, 8]
        target = 1
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    def test_target_too_large(self):
        """Test when target is larger than sum of all candidates."""
        candidates = [1, 2, 3]
        target = 10
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    def test_exact_sum_of_all_elements(self):
        """Test when target equals sum of all candidates."""
        candidates = [1, 2, 3, 4]
        target = 10
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 2, 3, 4]]
        assert result == expected

    def test_duplicate_handling(self):
        """Test proper handling of duplicate candidates."""
        candidates = [1, 1, 1, 2, 2]
        target = 4
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 1, 2], [2, 2]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_all_same_candidates(self):
        """Test when all candidates are the same."""
        candidates = [2, 2, 2, 2]
        target = 6
        result = self.solution.combinationSum2(candidates, target)
        expected = [[2, 2, 2]]
        assert result == expected

    def test_single_candidate_multiple_uses(self):
        """Test with single candidate that can be used multiple times."""
        candidates = [3, 3, 3]
        target = 9
        result = self.solution.combinationSum2(candidates, target)
        expected = [[3, 3, 3]]
        assert result == expected

    def test_empty_candidates(self):
        """Test with empty candidates list."""
        candidates = []
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    def test_zero_target(self):
        """Test with target = 0."""
        candidates = [1, 2, 3]
        target = 0
        result = self.solution.combinationSum2(candidates, target)
        expected = [[]]
        assert result == expected

    def test_negative_candidates(self):
        """Test with negative candidates."""
        candidates = [-1, -2, 3, 4]
        target = 2
        result = self.solution.combinationSum2(candidates, target)
        expected = [[-1, 3], [-2, 4]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_large_candidates_small_target(self):
        """Test when all candidates are larger than target."""
        candidates = [5, 6, 7, 8]
        target = 3
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    def test_multiple_valid_combinations(self):
        """Test case with multiple valid combinations."""
        candidates = [1, 2, 3, 4, 5]
        target = 6
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 2, 3], [1, 5], [2, 4]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_duplicate_prevention(self):
        """Test that duplicate combinations are prevented."""
        candidates = [4, 4, 2, 1, 4, 4, 6, 8]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        
        # Convert to tuples for set comparison to check for duplicates
        result_tuples = [tuple(sorted(combo)) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))
        
        # Verify some expected combinations exist
        assert [2, 6] in [sorted(combo) for combo in result]
        assert [4, 4] in [sorted(combo) for combo in result]

    def test_complex_duplicate_scenario(self):
        """Test complex scenario with many duplicates."""
        candidates = [1, 1, 1, 1, 1, 2, 2, 2]
        target = 4
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_ascending_order_in_results(self):
        """Test that results maintain ascending order within combinations."""
        candidates = [5, 1, 3, 2, 4]
        target = 7
        result = self.solution.combinationSum2(candidates, target)
        
        for combo in result:
            assert combo == sorted(combo)

    def test_return_type(self):
        """Test that the function returns the correct type."""
        candidates = [1, 2, 3]
        target = 4
        result = self.solution.combinationSum2(candidates, target)
        assert isinstance(result, list)
        assert all(isinstance(combo, list) for combo in result)
        assert all(isinstance(num, int) for combo in result for num in combo)

    def test_candidate_uniqueness_within_combination(self):
        """Test that each candidate index is used at most once."""
        candidates = [1, 2, 2, 3]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        expected = [[1, 2, 2], [2, 3]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_large_input_performance(self):
        """Test performance with larger input."""
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2  # 20 elements with duplicates
        target = 15
        result = self.solution.combinationSum2(candidates, target)
        
        # Verify all results are valid
        for combo in result:
            assert sum(combo) == target
            assert combo == sorted(combo)
        
        # Verify no duplicates in results
        result_tuples = [tuple(combo) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_early_pruning_efficiency(self):
        """Test that algorithm efficiently prunes when total exceeds target."""
        candidates = [10, 20, 30, 40]
        target = 25
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    @pytest.mark.parametrize("candidates,target,expected_count", [
        ([1, 2, 3], 4, 1),      # [1,3]
        ([2, 2, 2], 6, 1),      # [2,2,2]
        ([1, 1, 2], 3, 1),      # [1,2]
        ([1, 2, 1], 3, 1),      # [1,2] (same as above after sorting)
        ([1, 1, 1, 2, 2], 4, 2), # [1,1,2], [2,2]
    ])
    def test_parametrized_cases(self, candidates, target, expected_count):
        """Test various candidate and target combinations."""
        result = self.solution.combinationSum2(candidates, target)
        
        # Verify all results are valid
        for combo in result:
            assert sum(combo) == target
            assert combo == sorted(combo)
        
        # Check expected count
        assert len(result) == expected_count

    def test_combination_sum_correctness(self):
        """Test that all returned combinations actually sum to target."""
        candidates = [3, 1, 3, 5, 1, 1]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        
        for combo in result:
            assert sum(combo) == target

    def test_sorted_candidates_property(self):
        """Test that algorithm works correctly with pre-sorted candidates."""
        candidates = [1, 2, 3, 4, 5]  # Already sorted
        target = 6
        result = self.solution.combinationSum2(candidates, target)
        
        # Verify results
        for combo in result:
            assert sum(combo) == target
            assert combo == sorted(combo)

    def test_reverse_sorted_candidates(self):
        """Test with reverse sorted candidates."""
        candidates = [5, 4, 3, 2, 1]
        target = 6
        result = self.solution.combinationSum2(candidates, target)
        
        # Algorithm should sort first, so results should be same as sorted input
        for combo in result:
            assert sum(combo) == target
            assert combo == sorted(combo)

    def test_edge_case_single_candidate(self):
        """Test with single candidate."""
        # Target achievable
        candidates = [5]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        assert result == [[5]]
        
        # Target not achievable
        candidates = [3]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        assert result == []

    def test_medium_complexity_case(self):
        """Test a medium complexity case."""
        candidates = [1, 1, 2, 5, 6, 7, 10]
        target = 8
        result = self.solution.combinationSum2(candidates, target)
        
        # Verify some expected combinations
        expected_combinations = [
            [1, 1, 6], [1, 2, 5], [1, 7], [2, 6]
        ]
        
        result_sorted = [sorted(combo) for combo in result]
        for expected in expected_combinations:
            assert sorted(expected) in result_sorted

    def test_all_elements_needed(self):
        """Test when all elements are needed to reach target."""
        candidates = [1, 2, 3, 4]
        target = 10
        result = self.solution.combinationSum2(candidates, target)
        assert result == [[1, 2, 3, 4]]

    def test_algorithm_determinism(self):
        """Test that algorithm produces consistent results."""
        candidates = [2, 1, 3, 2, 4]
        target = 6
        
        # Run multiple times
        result1 = self.solution.combinationSum2(candidates.copy(), target)
        result2 = self.solution.combinationSum2(candidates.copy(), target)
        
        # Results should be identical
        result1_sorted = sorted([sorted(combo) for combo in result1])
        result2_sorted = sorted([sorted(combo) for combo in result2])
        
        assert result1_sorted == result2_sorted

    def test_boundary_target_values(self):
        """Test boundary target values."""
        candidates = [1, 2, 3, 4, 5]
        
        # Minimum possible target
        result_min = self.solution.combinationSum2(candidates, 1)
        assert [1] in result_min
        
        # Maximum possible target
        result_max = self.solution.combinationSum2(candidates, 15)
        assert [1, 2, 3, 4, 5] in result_max

    def test_duplicate_result_prevention_complex(self):
        """Test complex duplicate prevention scenario."""
        candidates = [1, 1, 1, 2, 2, 3]
        target = 5
        result = self.solution.combinationSum2(candidates, target)
        
        # Convert to sorted tuples and check for uniqueness
        result_tuples = [tuple(sorted(combo)) for combo in result]
        unique_results = set(result_tuples)
        
        assert len(result_tuples) == len(unique_results)
        
        # Verify specific expected combinations
        expected = [(1, 1, 1, 2), (1, 1, 3), (1, 2, 2), (2, 3)]
        result_sorted = [tuple(sorted(combo)) for combo in result]
        
        for exp in expected:
            assert exp in result_sorted
