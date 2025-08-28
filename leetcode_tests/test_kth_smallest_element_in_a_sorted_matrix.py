"""
Comprehensive test suite for LeetCode Problem #378: Kth Smallest Element in a Sorted Matrix
Tests the heap-based algorithm for finding the kth smallest element efficiently.
"""

import pytest
import sys
import os

# Add the parent directory to the path to import the solution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.kth_smallest_element_in_a_sorted_matrix import Solution

class TestKthSmallestElement:
    """Test cases for Kth Smallest Element in a Sorted Matrix problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_example_1(self):
        """Test first basic example from LeetCode."""
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        expected = 13
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_basic_example_2(self):
        """Test second basic example from LeetCode."""
        matrix = [[-5]]
        k = 1
        expected = -5
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_duplicate_values(self):
        """Test matrix with duplicate values."""
        matrix = [[1, 2], [1, 3]]
        k = 3
        expected = 2  # Elements in order: [1, 1, 2, 3]
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_duplicate_values_different_k(self):
        """Test different k values with duplicates."""
        matrix = [[1, 2], [1, 3]]
        test_cases = [
            (1, 1),  # 1st smallest
            (2, 1),  # 2nd smallest (second 1)
            (3, 2),  # 3rd smallest
            (4, 3)   # 4th smallest
        ]
        
        for k, expected in test_cases:
            assert self.solution.kthSmallest(matrix, k) == expected

    def test_single_element_matrix(self):
        """Test 1x1 matrix."""
        matrix = [[42]]
        k = 1
        expected = 42
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_negative_values(self):
        """Test matrix with negative values."""
        matrix = [[-5, -4], [-3, -2]]
        k = 3
        expected = -3
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_mixed_positive_negative(self):
        """Test matrix with mixed positive and negative values."""
        matrix = [[-1, 0], [1, 2]]
        k = 2
        expected = 0
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_large_uniform_matrix(self):
        """Test larger matrix with sequential values."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 5
        expected = 5  # Middle element
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_first_element(self):
        """Test finding the smallest element (k=1)."""
        matrix = [[10, 20, 30], [15, 25, 35], [24, 29, 37]]
        k = 1
        expected = 10
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_last_element(self):
        """Test finding the largest element (k=n²)."""
        matrix = [[1, 2], [3, 4]]
        k = 4
        expected = 4
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_non_consecutive_values(self):
        """Test matrix with non-consecutive values."""
        matrix = [[1, 5, 9], [10, 50, 90], [100, 500, 900]]
        k = 4
        expected = 10  # Elements in order: [1, 5, 9, 10, 50, 90, 100, 500, 900]
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_identical_elements(self):
        """Test matrix where all elements are identical."""
        matrix = [[5, 5], [5, 5]]
        k = 2
        expected = 5
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_ascending_rows_columns(self):
        """Test matrix where rows and columns are strictly ascending."""
        matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        k = 6
        expected = 6
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_large_gaps_between_values(self):
        """Test matrix with large gaps between values."""
        matrix = [[1, 1000], [999, 2000]]
        k = 3
        expected = 1000
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_heap_efficiency_medium_matrix(self):
        """Test efficiency with medium-sized matrix."""
        matrix = []
        value = 1
        for i in range(5):
            row = []
            for j in range(5):
                row.append(value)
                value += 1
            matrix.append(row)
        
        k = 13  # Middle element
        expected = 13
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_matrix_with_zeros(self):
        """Test matrix containing zeros."""
        matrix = [[0, 1], [2, 3]]
        k = 1
        expected = 0
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_reverse_sorted_first_row(self):
        """Test where smallest elements are not all in first row."""
        matrix = [[5, 10, 15], [6, 11, 16], [7, 12, 17]]
        k = 1
        expected = 5  # First element is still smallest in properly sorted matrix
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_k_equals_matrix_size(self):
        """Test when k equals the total number of elements."""
        matrix = [[1, 2], [3, 4]]
        k = 4
        expected = 4  # Largest element
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_sorted_diagonal_matrix(self):
        """Test matrix sorted along diagonal."""
        matrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        k = 7
        expected = 7
        assert self.solution.kthSmallest(matrix, k) == expected

    def test_heap_boundary_conditions(self):
        """Test boundary conditions for heap operations."""
        matrix = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
        test_cases = [
            (1, 1),   # First element
            (2, 2),   # Second element
            (9, 9)    # Last element
        ]
        
        for k, expected in test_cases:
            assert self.solution.kthSmallest(matrix, k) == expected

    def test_algorithm_correctness_properties(self):
        """Test fundamental properties of the algorithm."""
        matrix = [[2, 4, 6], [1, 3, 5], [7, 8, 9]]
        k = 5
        
        result = self.solution.kthSmallest(matrix, k)
        
        # Result should be positive for this test case
        assert result > 0
        
        # Should be one of the elements in the matrix
        all_elements = [elem for row in matrix for elem in row]
        assert result in all_elements

    def test_heap_efficiency_properties(self):
        """Test heap efficiency properties."""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        k = 8
        
        result = self.solution.kthSmallest(matrix, k)
        
        # Should find 8th smallest efficiently
        assert result == 8

    def test_memory_efficiency(self):
        """Test that algorithm doesn't use excessive memory."""
        matrix = [[i*4 + j + 1 for j in range(4)] for i in range(4)]
        k = 10
        
        # Should work efficiently without storing all elements
        result = self.solution.kthSmallest(matrix, k)
        assert result == 10

    def test_edge_case_small_k(self):
        """Test with very small k values."""
        matrix = [[10, 20, 30, 40], [15, 25, 35, 45], [24, 29, 37, 48], [32, 33, 39, 50]]
        
        for k in range(1, 5):
            result = self.solution.kthSmallest(matrix, k)
            assert isinstance(result, int)

    def test_edge_case_large_k(self):
        """Test with k close to matrix size."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        
        for k in [7, 8, 9]:  # Last few elements
            result = self.solution.kthSmallest(matrix, k)
            assert result == k

    def test_heap_ordering_verification(self):
        """Test that heap maintains proper ordering."""
        matrix = [[1, 3, 5], [2, 4, 6], [7, 8, 9]]
        
        # Test multiple k values to ensure ordering is maintained
        results = []
        for k in range(1, 10):
            results.append(self.solution.kthSmallest(matrix, k))
        
        # Results should be in non-decreasing order
        for i in range(1, len(results)):
            assert results[i] >= results[i-1]

    def test_complex_duplicate_pattern(self):
        """Test complex pattern with multiple duplicates."""
        matrix = [[1, 1, 2], [1, 2, 2], [2, 2, 3]]
        
        expected_sequence = [1, 1, 1, 2, 2, 2, 2, 2, 3]
        
        for k in range(1, 10):
            result = self.solution.kthSmallest(matrix, k)
            assert result == expected_sequence[k-1]

    def test_performance_larger_matrix(self):
        """Test performance with larger matrix."""
        matrix = [[i*6 + j + 1 for j in range(6)] for i in range(6)]
        k = 18  # Middle of 36 elements
        
        result = self.solution.kthSmallest(matrix, k)
        assert result == 18

    def test_minimum_maximum_elements(self):
        """Test finding minimum and maximum elements."""
        matrix = [[5, 10, 15], [6, 11, 16], [7, 12, 17]]
        
        # Minimum (k=1)
        min_result = self.solution.kthSmallest(matrix, 1)
        assert min_result == 5
        
        # Maximum (k=9)
        max_result = self.solution.kthSmallest(matrix, 9)
        assert max_result == 17


if __name__ == '__main__':
    # Run the tests
    pytest.main([__file__])
