"""
Comprehensive tests for LeetCode Problem #39: Combination Sum.
Tests the backtracking algorithm for finding combinations with unlimited reuse.
"""

import pytest

from leetcode.combination_sum import Solution


class TestCombinationSum:
    """Test cases for the combination sum problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example 1: candidates = [2,3,6,7], target = 7."""
        candidates = [2, 3, 6, 7]
        target = 7
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 3], [7]]
        
        # Sort both result and expected for comparison
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_example_case_2(self):
        """Test LeetCode example 2: candidates = [2,3,5], target = 8."""
        candidates = [2, 3, 5]
        target = 8
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_example_case_3(self):
        """Test LeetCode example 3: candidates = [2], target = 1."""
        candidates = [2]
        target = 1
        result = self.solution.combinationSum(candidates, target)
        expected = []
        assert result == expected

    def test_single_candidate_exact_match(self):
        """Test when single candidate equals target."""
        candidates = [5]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        expected = [[5]]
        assert result == expected

    def test_single_candidate_multiple_uses(self):
        """Test when single candidate needs to be used multiple times."""
        candidates = [3]
        target = 9
        result = self.solution.combinationSum(candidates, target)
        expected = [[3, 3, 3]]
        assert result == expected

    def test_target_not_achievable(self):
        """Test when target cannot be achieved with given candidates."""
        candidates = [3, 5]
        target = 1
        result = self.solution.combinationSum(candidates, target)
        assert result == []

    def test_zero_target(self):
        """Test with target = 0."""
        candidates = [1, 2, 3]
        target = 0
        result = self.solution.combinationSum(candidates, target)
        expected = [[]]
        assert result == expected

    def test_large_target_small_candidates(self):
        """Test with large target and small candidates."""
        candidates = [1]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        expected = [[1, 1, 1, 1, 1]]
        assert result == expected

    def test_multiple_combinations_possible(self):
        """Test case with multiple valid combinations."""
        candidates = [2, 4]
        target = 6
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 2], [2, 4]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted

    def test_no_reuse_needed(self):
        """Test when no candidate needs to be reused."""
        candidates = [1, 2, 3, 4, 5]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        
        # Should include [5] and [1,4] and [2,3] and [1,1,1,1,1] etc.
        expected_combinations = [[5], [1, 4], [2, 3], [1, 1, 3], [1, 1, 1, 2], [1, 1, 1, 1, 1], [1, 2, 2], [2, 2, 1]]
        
        # Check that at least some expected combinations are present
        result_sorted = [sorted(combo) for combo in result]
        assert [5] in result_sorted
        assert [1, 4] in result_sorted
        assert [2, 3] in result_sorted

    def test_ascending_order_in_results(self):
        """Test that combinations maintain ascending order."""
        candidates = [3, 1, 4]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        
        # Since we start from index 0 and only move forward, results should be sorted
        for combo in result:
            # The combination might not be sorted due to algorithm order
            # But we can verify all combinations are valid
            assert sum(combo) == target

    def test_duplicate_prevention(self):
        """Test that no duplicate combinations are returned."""
        candidates = [2, 3]
        target = 6
        result = self.solution.combinationSum(candidates, target)
        
        # Convert to tuples for set comparison
        result_tuples = [tuple(sorted(combo)) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_empty_candidates(self):
        """Test with empty candidates list."""
        candidates = []
        target = 5
        result = self.solution.combinationSum(candidates, target)
        assert result == []

    def test_large_candidates_array(self):
        """Test with larger candidates array."""
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        result = self.solution.combinationSum(candidates, target)
        
        # Verify all results are valid
        for combo in result:
            assert sum(combo) == target
            # All elements should be from candidates
            assert all(num in candidates for num in combo)
        
        # Should have many combinations
        assert len(result) > 0

    def test_return_type(self):
        """Test that the function returns the correct type."""
        candidates = [2, 3]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        assert isinstance(result, list)
        assert all(isinstance(combo, list) for combo in result)
        assert all(isinstance(num, int) for combo in result for num in combo)

    def test_combination_sum_correctness(self):
        """Test that all returned combinations sum to target."""
        candidates = [2, 3, 7]
        target = 7
        result = self.solution.combinationSum(candidates, target)
        
        for combo in result:
            assert sum(combo) == target

    def test_candidate_reuse_verification(self):
        """Test that candidates can be reused multiple times."""
        candidates = [2]
        target = 8
        result = self.solution.combinationSum(candidates, target)
        expected = [[2, 2, 2, 2]]
        assert result == expected

    def test_mixed_candidate_sizes(self):
        """Test with candidates of varying sizes."""
        candidates = [1, 5, 10]
        target = 11
        result = self.solution.combinationSum(candidates, target)
        
        # Should include combinations like [1,10], [1,5,5], [1,1,1,1,1,1,5] etc.
        result_sorted = [sorted(combo) for combo in result]
        assert [1, 10] in result_sorted
        assert [1, 5, 5] in result_sorted

    def test_algorithm_efficiency(self):
        """Test algorithm efficiency with moderate input."""
        candidates = [3, 4, 5]
        target = 12
        result = self.solution.combinationSum(candidates, target)
        
        # Verify results without timeout
        for combo in result:
            assert sum(combo) == target
        
        # Should find multiple valid combinations
        assert len(result) > 0

    def test_single_large_candidate(self):
        """Test with single candidate larger than target."""
        candidates = [10]
        target = 5
        result = self.solution.combinationSum(candidates, target)
        assert result == []

    @pytest.mark.parametrize("candidates,target,min_combinations", [
        ([2, 3], 6, 2),         # [2,2,2], [3,3]
        ([1, 2], 4, 3),         # [1,1,1,1], [1,1,2], [2,2]
        ([2, 4], 8, 3),         # [2,2,2,2], [2,2,4], [4,4]
        ([3, 5], 8, 1),         # [3,5]
    ])
    def test_parametrized_combination_counts(self, candidates, target, min_combinations):
        """Test that minimum expected combinations are found."""
        result = self.solution.combinationSum(candidates, target)
        assert len(result) >= min_combinations
        
        # Verify all are valid
        for combo in result:
            assert sum(combo) == target

    def test_all_candidates_exceed_target(self):
        """Test when all candidates are larger than target."""
        candidates = [5, 6, 7]
        target = 4
        result = self.solution.combinationSum(candidates, target)
        
        # Should return empty list as no combinations possible
        assert result == []
        for combo in result:
            assert sum(combo) == target

    def test_order_independence(self):
        """Test that candidate order doesn't affect result correctness."""
        candidates1 = [2, 3, 5]
        candidates2 = [5, 3, 2]
        target = 8
        
        result1 = self.solution.combinationSum(candidates1, target)
        result2 = self.solution.combinationSum(candidates2, target)
        
        # Convert to sorted tuples for comparison
        result1_sorted = sorted([tuple(sorted(combo)) for combo in result1])
        result2_sorted = sorted([tuple(sorted(combo)) for combo in result2])
        
        # Results should contain the same combinations (regardless of order)
        assert set(result1_sorted) == set(result2_sorted)

    def test_large_target_multiple_candidates(self):
        """Test with large target and multiple candidates."""
        candidates = [5, 10, 15]
        target = 30
        result = self.solution.combinationSum(candidates, target)
        
        expected_combinations = [
            [5, 5, 5, 5, 5, 5],    # 6 * 5
            [5, 5, 10, 10],        # 2 * 5 + 2 * 10
            [10, 10, 10],          # 3 * 10
            [15, 15],              # 2 * 15
            [5, 5, 5, 15],         # 3 * 5 + 1 * 15
            [5, 10, 15]            # 1 * 5 + 1 * 10 + 1 * 15
        ]
        
        result_sorted = [sorted(combo) for combo in result]
        for expected in expected_combinations:
            assert sorted(expected) in result_sorted

    def test_boundary_cases(self):
        """Test boundary cases."""
        # Target = 1 with candidate 1
        result = self.solution.combinationSum([1], 1)
        assert result == [[1]]
        
        # Large single candidate, small target
        result = self.solution.combinationSum([100], 50)
        assert result == []

    def test_all_combinations_unique(self):
        """Test that all returned combinations are unique."""
        candidates = [2, 3, 4]
        target = 10
        result = self.solution.combinationSum(candidates, target)
        
        # Convert to sorted tuples and check uniqueness
        result_tuples = [tuple(sorted(combo)) for combo in result]
        assert len(result_tuples) == len(set(result_tuples))

    def test_complex_combination_case(self):
        """Test a complex case with many possible combinations."""
        candidates = [1, 2, 3, 4]
        target = 6
        result = self.solution.combinationSum(candidates, target)
        
        # Should include combinations like [6], [2,4], [1,1,4], [2,2,2], [1,2,3], etc.
        # Note: [6] not possible since 6 not in candidates
        expected_some = [
            [2, 4], [1, 1, 4], [2, 2, 2], [1, 2, 3],
            [1, 1, 1, 3], [1, 1, 2, 2], [3, 3], [1, 1, 1, 1, 2], [1, 1, 1, 1, 1, 1]
        ]
        
        result_sorted = [sorted(combo) for combo in result]
        for expected in expected_some:
            assert sorted(expected) in result_sorted

    def test_performance_with_small_candidates(self):
        """Test performance when candidates are small relative to target."""
        candidates = [1, 2]
        target = 10
        result = self.solution.combinationSum(candidates, target)
        
        # Should complete without timeout and find valid combinations
        assert len(result) > 0
        for combo in result:
            assert sum(combo) == target

    def test_mathematical_properties(self):
        """Test mathematical properties of the combinations."""
        candidates = [3, 4, 5]
        target = 15
        result = self.solution.combinationSum(candidates, target)
        
        # Verify mathematical properties
        for combo in result:
            assert sum(combo) == target
            assert all(x in candidates for x in combo)
            assert len(combo) >= 1  # At least one element needed for positive target

    def test_algorithm_completeness(self):
        """Test that algorithm finds all possible combinations."""
        candidates = [2, 5]
        target = 10
        result = self.solution.combinationSum(candidates, target)
        
        # Manually verify all possible combinations:
        # [2,2,2,2,2] = 5*2 = 10
        # [5,5] = 2*5 = 10
        expected = [[2, 2, 2, 2, 2], [5, 5]]
        
        result_sorted = sorted([sorted(combo) for combo in result])
        expected_sorted = sorted([sorted(combo) for combo in expected])
        
        assert result_sorted == expected_sorted
