"""
Test module for majority element problems (LeetCode #169 and #229).

Comprehensive test cases covering Boyer-Moore voting algorithm,
edge cases, and alternative implementations.
"""
import pytest
from leetcode.majority_element import Solution


class TestMajorityElement:
    """Test class for majority element problems."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_majority_element_basic_cases(self):
        """Test basic cases for majority element (> n/2)."""
        test_cases = [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1], 1),
            ([1, 1], 1),
            ([1, 2, 1], 1),
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element(nums)
            assert result == expected, f"Failed for {nums}: got {result}, expected {expected}"

    def test_majority_element_edge_cases(self):
        """Test edge cases for majority element."""
        test_cases = [
            ([0], 0),
            ([-1], -1),
            ([1, 1, 1, 1, 1], 1),
            ([5, 5, 5, 4, 4], 5),
            ([-1, -1, 0], -1),
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element(nums)
            assert result == expected, f"Failed for {nums}: got {result}, expected {expected}"

    def test_majority_element_large_arrays(self):
        """Test majority element with larger arrays."""
        # Array where first half is 1s and second half + 1 more is 2s
        nums1 = [1] * 100 + [2] * 101
        result1 = self.solution.majority_element(nums1)
        assert result1 == 2

        # Array with clear majority
        nums2 = [7] * 75 + [8] * 25
        result2 = self.solution.majority_element(nums2)
        assert result2 == 7

    def test_majority_element_ii_basic_cases(self):
        """Test basic cases for majority element II (> n/3)."""
        test_cases = [
            ([3, 2, 3], [3]),
            ([1], [1]),
            ([1, 2], [1, 2]),  # Both appear > n/3 (n=2, n/3=0.67, both appear 1 > 0.67)
            ([1, 1, 2, 2, 3], [1, 2]),  # n=5, n/3=1.67, 1 and 2 appear 2 > 1.67
            ([1, 1, 1, 2, 2, 3, 3, 3], [1, 3]),
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element_ii(nums)
            assert sorted(result) == sorted(expected), f"Failed for {nums}: got {result}, expected {expected}"

    def test_majority_element_ii_edge_cases(self):
        """Test edge cases for majority element II."""
        test_cases = [
            ([], []),
            ([0], [0]),
            ([1, 2, 3], []),  # Each appears exactly n/3 = 1, not > n/3
            ([1, 1, 2, 2], [1, 2]),  # n=4, n/3=1.33, both appear 2 > 1.33
            ([1, 1, 1], [1]),
            ([1, 1, 2, 2, 2], [1, 2]),
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element_ii(nums)
            assert sorted(result) == sorted(expected), f"Failed for {nums}: got {result}, expected {expected}"

    def test_majority_element_ii_complex_cases(self):
        """Test complex cases for majority element II."""
        # Case from problem example
        nums1 = [1, 1, 3, 2, 2, 2, 3, 3, 1, 2, 1]
        result1 = self.solution.majority_element_ii(nums1)
        # 1 appears 4 times, 2 appears 4 times, 3 appears 3 times
        # threshold = 11//3 = 3, so 1 and 2 qualify
        assert sorted(result1) == [1, 2]

        # No majority elements
        nums2 = [1, 2, 3, 4, 5, 6]
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == []

        # Single majority element
        nums3 = [1, 1, 1, 1, 2, 3]
        result3 = self.solution.majority_element_ii(nums3)
        assert result3 == [1]

    def test_boyer_moore_algorithm_properties(self):
        """Test specific properties of Boyer-Moore algorithm."""
        # Test that algorithm correctly handles cancellation
        nums = [1, 2, 1, 2, 1, 2, 1]  # 1 appears 4 times, 2 appears 3 times
        result = self.solution.majority_element(nums)
        assert result == 1

        # Test with alternating pattern
        nums2 = [1, 2, 1, 2, 1]  # 1 appears 3 times out of 5
        result2 = self.solution.majority_element(nums2)
        assert result2 == 1

    def test_negative_numbers(self):
        """Test with negative numbers."""
        test_cases = [
            ([-1, -1, -2], -1),
            ([-5, -5, -5, -3, -3], -5),
            ([0, 0, -1], 0),
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element(nums)
            assert result == expected, f"Failed for {nums}: got {result}, expected {expected}"

    def test_majority_element_ii_negative_numbers(self):
        """Test majority element II with negative numbers."""
        test_cases = [
            ([-1, -1, -2], [-1]),
            ([-1, -1, -2, -2, -3], [-1, -2]),
            ([0, 0, -1, -1], [0, -1]),  # n=4, n/3=1.33, both appear 2 > 1.33
        ]

        for nums, expected in test_cases:
            result = self.solution.majority_element_ii(nums)
            assert sorted(result) == sorted(expected), f"Failed for {nums}: got {result}, expected {expected}"

    def test_hashmap_implementation_consistency(self):
        """Test that hashmap implementation gives same results."""
        test_cases = [
            [3, 2, 3],
            [2, 2, 1, 1, 1, 2, 2],
            [1],
            [1, 1, 1, 1, 1],
        ]

        for nums in test_cases:
            result1 = self.solution.majority_element(nums)
            result2 = self.solution.majority_element_hashmap(nums)
            assert result1 == result2, f"Inconsistent results for {nums}: Boyer-Moore={result1}, Hashmap={result2}"

    def test_majority_element_ii_hashmap_consistency(self):
        """Test that hashmap implementation for II gives same results."""
        test_cases = [
            [3, 2, 3],
            [1, 1, 1, 2, 2, 3, 3, 3],
            [1, 2, 3],
            [],
            [1],
        ]

        for nums in test_cases:
            result1 = sorted(self.solution.majority_element_ii(nums))
            result2 = sorted(self.solution.majority_element_ii_hashmap(nums))
            assert result1 == result2, f"Inconsistent results for {nums}: Boyer-Moore={result1}, Hashmap={result2}"

    def test_sorting_implementation_consistency(self):
        """Test that sorting implementation gives same results."""
        test_cases = [
            [3, 2, 3],
            [2, 2, 1, 1, 1, 2, 2],
            [1],
            [5, 5, 5, 4, 4],
        ]

        for nums in test_cases:
            result1 = self.solution.majority_element(nums.copy())
            result2 = self.solution.majority_element_sorting(nums.copy())
            assert result1 == result2, f"Inconsistent results for {nums}: Boyer-Moore={result1}, Sorting={result2}"

    def test_mathematical_properties(self):
        """Test mathematical properties of majority elements."""
        # If there are exactly 2 candidates in majority_element_ii,
        # their combined count should be > 2n/3
        nums = [1, 1, 1, 2, 2, 2, 3]  # 1 and 2 each appear 3 times, total 6 > 2*7/3 = 4.67
        result = self.solution.majority_element_ii(nums)
        assert sorted(result) == [1, 2]

        # At most 2 elements can appear > n/3 times
        nums2 = [1] * 10 + [2] * 10 + [3] * 10  # Each appears exactly n/3
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == []  # None appear > n/3

    def test_boundary_thresholds(self):
        """Test boundary cases around thresholds."""
        # Exactly n/2 case (should not be majority for strict >)
        # But majority_element assumes majority exists
        nums1 = [1, 1, 2, 2]  # Each appears exactly n/2
        result1 = self.solution.majority_element(nums1)
        assert result1 in [1, 2]  # Either could be returned

        # Exactly n/3 + 1 case for majority_element_ii
        nums2 = [1] * 3 + [2] * 3 + [3] * 3  # n=9, each appears exactly n/3
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == []

        nums3 = [1] * 4 + [2] * 3 + [3] * 2  # n=9, 1 appears 4 > 9/3
        result3 = self.solution.majority_element_ii(nums3)
        assert result3 == [1]

    def test_duplicate_candidates_handling(self):
        """Test that duplicate candidates are handled correctly."""
        # Case where both candidates might be the same initially
        nums = [1, 1, 1, 1, 1, 2]
        result = self.solution.majority_element_ii(nums)
        assert result == [1]

        # Ensure no duplicates in result
        nums2 = [5] * 10  # Only one element
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == [5]
        assert len(result2) == 1

    def test_empty_and_single_element_cases(self):
        """Test empty arrays and single elements."""
        # Empty array
        assert self.solution.majority_element_ii([]) == []

        # Single element
        assert self.solution.majority_element([42]) == 42
        assert self.solution.majority_element_ii([42]) == [42]

    def test_performance_characteristics(self):
        """Test performance characteristics."""
        # Large array to verify O(n) complexity
        large_nums = [1] * 5000 + [2] * 4999  # 1 is majority
        result = self.solution.majority_element(large_nums)
        assert result == 1

        # Large array for majority_element_ii
        large_nums2 = [1] * 3334 + [2] * 3333 + [3] * 3333  # Only 1 is > n/3
        result2 = self.solution.majority_element_ii(large_nums2)
        assert result2 == [1]

    def test_algorithm_correctness_verification(self):
        """Verify algorithm correctness with known test cases."""
        # Verify that Boyer-Moore finds correct majority
        test_cases = [
            ([2, 2, 1, 1, 1, 2, 2], 2),  # LeetCode example
            ([3, 2, 3], 3),  # LeetCode example
            ([6, 5, 5], 5),
        ]

        for nums, expected in test_cases:
            # Test all implementations give same result
            result_boyer = self.solution.majority_element(nums)
            result_hash = self.solution.majority_element_hashmap(nums)
            result_sort = self.solution.majority_element_sorting(nums.copy())

            assert result_boyer == expected
            assert result_hash == expected
            assert result_sort == expected

    def test_majority_element_ii_verification(self):
        """Verify majority element II with manual verification."""
        nums = [1, 1, 3, 2, 2, 2, 3, 3, 1, 2, 1]
        # Count: 1 appears 4 times, 2 appears 4 times, 3 appears 3 times
        # n = 11, threshold = 11//3 = 3
        # 1: 4 > 3 ✓, 2: 4 > 3 ✓, 3: 3 = 3 ✗
        result = self.solution.majority_element_ii(nums)
        assert sorted(result) == [1, 2]

        # Verify with hashmap implementation
        result_hash = self.solution.majority_element_ii_hashmap(nums)
        assert sorted(result) == sorted(result_hash)

    def test_stress_patterns(self):
        """Test with various stress patterns."""
        # Alternating pattern
        nums1 = [1, 2] * 50 + [1]  # 1 appears 51 times, 2 appears 50 times
        result1 = self.solution.majority_element(nums1)
        assert result1 == 1

        # Three-way split with one majority
        nums2 = [1] * 34 + [2] * 33 + [3] * 33  # n=100, 1 appears 34 > 33.33
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == [1]

        # No majority case
        nums3 = [1] * 33 + [2] * 33 + [3] * 34  # n=100, 3 appears 34 > 33.33
        result3 = self.solution.majority_element_ii(nums3)
        assert result3 == [3]

    def test_corner_case_comprehensive(self):
        """Test comprehensive corner cases."""
        # Two elements with exactly threshold count
        nums1 = [1] * 4 + [2] * 4 + [3] * 1  # n=9, threshold=3, both 1 and 2 appear 4>3
        result1 = self.solution.majority_element_ii(nums1)
        assert sorted(result1) == [1, 2]

        # Boundary case where count equals threshold
        nums2 = [1] * 3 + [2] * 3 + [3] * 3  # n=9, threshold=3, all appear exactly 3
        result2 = self.solution.majority_element_ii(nums2)
        assert result2 == []  # None appear > threshold

        # Single element repeated
        nums3 = [7] * 100
        result3 = self.solution.majority_element_ii(nums3)
        assert result3 == [7]

    def test_final_verification_cases(self):
        """Final verification with additional test cases."""
        verification_cases = [
            # (input, expected_majority_element, expected_majority_element_ii)
            ([1, 2, 3, 1, 1], 1, [1]),
            ([1, 2, 1, 2, 1, 2, 2], 2, [1, 2]),  # n=7, n/3=2.33, 1 appears 3>2.33, 2 appears 4>2.33
            ([5], 5, [5]),
            ([1, 1, 2, 2, 3, 1, 1], 1, [1]),  # 1 appears 4 times > 7/2 = 3.5
        ]

        for nums, expected_maj, expected_maj_ii in verification_cases:
            result_maj = self.solution.majority_element(nums)
            result_maj_ii = sorted(self.solution.majority_element_ii(nums))

            assert result_maj == expected_maj, f"majority_element failed for {nums}"
            assert result_maj_ii == sorted(expected_maj_ii), f"majority_element_ii failed for {nums}"
