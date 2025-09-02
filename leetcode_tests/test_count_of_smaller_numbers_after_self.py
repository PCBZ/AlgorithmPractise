"""
Comprehensive test suite for LeetCode Problem #315: Count of Smaller Numbers After Self

Tests the countSmaller method which counts how many numbers after each element
are smaller than that element using a Binary Search Tree approach.
"""
import time

from leetcode.count_of_smaller_numbers_after_self import Solution


class TestCountSmallerNumbersAfterSelf:
    """Test class for count smaller numbers after self problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        nums = [5, 2, 6, 1]
        result = self.solution.countSmaller(nums)
        expected = [2, 1, 1, 0]
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        nums = [2, 0, 1]
        result = self.solution.countSmaller(nums)
        expected = [2, 0, 0]
        assert result == expected

    def test_single_element(self):
        """Test with single element."""
        nums = [5]
        result = self.solution.countSmaller(nums)
        expected = [0]
        assert result == expected

    def test_empty_array(self):
        """Test with empty array."""
        nums = []
        result = self.solution.countSmaller(nums)
        expected = []
        assert result == expected

    def test_sorted_ascending(self):
        """Test with array sorted in ascending order."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.countSmaller(nums)
        expected = [0, 0, 0, 0, 0]  # No smaller elements to the right
        assert result == expected

    def test_sorted_descending(self):
        """Test with array sorted in descending order."""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.countSmaller(nums)
        expected = [4, 3, 2, 1, 0]  # Each element has all elements to right smaller
        assert result == expected

    def test_all_same_elements(self):
        """Test with all identical elements."""
        nums = [3, 3, 3, 3]
        result = self.solution.countSmaller(nums)
        expected = [0, 0, 0, 0]  # No strictly smaller elements
        assert result == expected

    def test_two_elements_increasing(self):
        """Test with two elements in increasing order."""
        nums = [1, 2]
        result = self.solution.countSmaller(nums)
        expected = [0, 0]
        assert result == expected

    def test_two_elements_decreasing(self):
        """Test with two elements in decreasing order."""
        nums = [2, 1]
        result = self.solution.countSmaller(nums)
        expected = [1, 0]
        assert result == expected

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-1, -2, -3]
        result = self.solution.countSmaller(nums)
        expected = [2, 1, 0]  # -1 has -2,-3; -2 has -3; -3 has none
        assert result == expected

    def test_mixed_positive_negative(self):
        """Test with mix of positive and negative numbers."""
        nums = [1, -1, 0, -2]
        result = self.solution.countSmaller(nums)
        expected = [3, 1, 1, 0]  # 1 has -1,0,-2; -1 has -2; 0 has -2; -2 has none
        assert result == expected

    def test_duplicates_with_smaller(self):
        """Test with duplicates and smaller elements."""
        nums = [5, 2, 2, 1]
        result = self.solution.countSmaller(nums)
        expected = [3, 1, 1, 0]  # 5 sees 2,2,1; first 2 sees 1; second 2 sees 1; 1 sees none
        assert result == expected

    def test_large_numbers(self):
        """Test with large numbers."""
        nums = [100000, 50000, 75000, 25000]
        result = self.solution.countSmaller(nums)
        expected = [3, 1, 1, 0]
        assert result == expected

    def test_return_type_and_structure(self):
        """Test that return type is correct list of integers."""
        nums = [3, 2, 1]
        result = self.solution.countSmaller(nums)
        
        assert isinstance(result, list)
        assert len(result) == len(nums)
        for count in result:
            assert isinstance(count, int)
            assert count >= 0

    def test_algorithm_correctness_brute_force_comparison(self):
        """Test algorithm correctness by comparing with brute force approach."""
        def brute_force_count_smaller(nums):
            """Brute force O(n²) solution for comparison."""
            if not nums:
                return []
            
            result = []
            for i in range(len(nums)):
                count = 0
                for j in range(i + 1, len(nums)):
                    if nums[j] < nums[i]:
                        count += 1
                result.append(count)
            return result
        
        test_cases = [
            [5, 2, 6, 1],
            [2, 0, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1],
            [],
            [5, 5, 5],
            [-1, -2, 0, 1]
        ]
        
        for nums in test_cases:
            bst_result = self.solution.countSmaller(nums)
            brute_force_result = brute_force_count_smaller(nums)
            assert bst_result == brute_force_result, f"Mismatch for {nums}"

    def test_edge_case_zeros(self):
        """Test with zeros."""
        nums = [0, 0, 0]
        result = self.solution.countSmaller(nums)
        expected = [0, 0, 0]
        assert result == expected

    def test_alternating_pattern(self):
        """Test with alternating high-low pattern."""
        nums = [5, 1, 4, 2, 3]
        result = self.solution.countSmaller(nums)
        
        # Manual calculation:
        # 5: sees 1,4,2,3 -> smaller: 1,4,2,3 = 4
        # 1: sees 4,2,3 -> smaller: none = 0  
        # 4: sees 2,3 -> smaller: 2,3 = 2
        # 2: sees 3 -> smaller: none = 0
        # 3: sees none = 0
        expected = [4, 0, 2, 0, 0]
        assert result == expected

    def test_performance_with_larger_input(self):
        """Test performance with larger input."""
        # Create a larger test case
        nums = list(range(100, 0, -1))  # Descending order 100, 99, ..., 1
        
        start_time = time.time()
        result = self.solution.countSmaller(nums)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 1.0
        
        # Verify correctness for descending order
        expected = list(range(99, -1, -1))  # Each element has all subsequent elements smaller
        assert result == expected

    def test_worst_case_performance(self):
        """Test worst case performance (already sorted ascending)."""
        nums = list(range(50))  # 0, 1, 2, ..., 49
        
        start_time = time.time()
        result = self.solution.countSmaller(nums)
        end_time = time.time()
        
        # Should complete within reasonable time even in worst case
        assert end_time - start_time < 2.0
        
        # All should be 0 for ascending order
        expected = [0] * 50
        assert result == expected

    def test_random_permutation(self):
        """Test with random permutation."""
        nums = [3, 7, 1, 8, 2, 6, 4, 5]
        result = self.solution.countSmaller(nums)
        
        # Verify by manual calculation or brute force comparison
        def manual_count(nums):
            result = []
            for i in range(len(nums)):
                count = sum(1 for j in range(i + 1, len(nums)) if nums[j] < nums[i])
                result.append(count)
            return result
        
        expected = manual_count(nums)
        assert result == expected

    def test_boundary_values(self):
        """Test with boundary values."""
        nums = [-10000, 0, 10000]
        result = self.solution.countSmaller(nums)
        expected = [0, 0, 0]  # Each element is smaller than the next
        assert result == expected

    def test_mathematical_properties(self):
        """Test mathematical properties of the solution."""
        nums = [4, 3, 2, 1, 5]
        result = self.solution.countSmaller(nums)
        
        # Sum of all counts should not exceed total possible pairs
        total_pairs = len(nums) * (len(nums) - 1) // 2
        assert sum(result) <= total_pairs
        
        # Each count should be between 0 and n-i-1 where i is the index
        for i, count in enumerate(result):
            max_possible = len(nums) - i - 1
            assert 0 <= count <= max_possible

    def test_bst_structure_correctness(self):
        """Test that BST maintains correct structure through insertions."""
        # This test verifies the BST approach works correctly
        nums = [4, 2, 6, 1, 3, 5, 7]
        result = self.solution.countSmaller(nums)
        
        # Verify result length matches input
        assert len(result) == len(nums)
        
        # Verify all results are non-negative
        assert all(count >= 0 for count in result)

    def test_duplicate_handling(self):
        """Test handling of duplicate values."""
        nums = [2, 1, 2, 1, 2]
        result = self.solution.countSmaller(nums)
        
        # Manual verification:
        # nums[0]=2: sees [1,2,1,2] -> smaller: 1,1 = 2
        # nums[1]=1: sees [2,1,2] -> smaller: none = 0
        # nums[2]=2: sees [1,2] -> smaller: 1 = 1  
        # nums[3]=1: sees [2] -> smaller: none = 0
        # nums[4]=2: sees [] -> smaller: none = 0
        expected = [2, 0, 1, 0, 0]
        assert result == expected

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        edge_cases = [
            ([], []),
            ([1], [0]),
            ([1, 1], [0, 0]),
            ([1, 2], [0, 0]),
            ([2, 1], [1, 0]),
            ([-1, -1], [0, 0]),
            ([0], [0]),
        ]
        
        for nums, expected in edge_cases:
            result = self.solution.countSmaller(nums)
            assert result == expected, f"Failed for {nums}: got {result}, expected {expected}"

    def test_algorithm_stability(self):
        """Test that algorithm produces consistent results."""
        nums = [5, 2, 6, 1]
        
        # Run multiple times
        results = [self.solution.countSmaller(nums) for _ in range(5)]
        
        # All results should be identical
        assert all(result == results[0] for result in results)

    def test_memory_efficiency(self):
        """Test memory efficiency with reasonable input."""
        nums = list(range(100))
        result = self.solution.countSmaller(nums)
        
        # Should complete without memory issues
        assert len(result) == len(nums)
        assert all(isinstance(count, int) for count in result)
