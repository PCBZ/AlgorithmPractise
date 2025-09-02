"""
Comprehensive test suite for LeetCode Problem #329: Longest Increasing Path in a Matrix.
Tests the DFS with memoization solution for finding the longest increasing path.
"""

import pytest

from leetcode.longest_increasing_path_in_a_matrix import Solution


class TestLongestIncreasingPathInMatrix:
    """Test cases for longest increasing path in matrix calculation."""

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    @pytest.mark.parametrize("matrix,expected", [
        ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
        ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
        ([[1]], 1),
        ([[1, 2], [4, 3]], 4),
    ])
    def test_basic_examples(self, matrix, expected):
        """Test basic examples using parametrized inputs."""
        result = self.solution.longest_increasing_path(matrix)
        assert result == expected

    @pytest.mark.parametrize("matrix,expected", [
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),  # All same values
        ([[1, 2, 3, 4, 5]], 5),  # Strictly increasing row
        ([[1], [2], [3], [4], [5]], 5),  # Strictly increasing column
        ([[5, 4, 3], [2, 1, 0]], 4),  # Decreasing sequence -> increasing path
    ])
    def test_pattern_variations(self, matrix, expected):
        """Test various matrix patterns using parametrized inputs."""
        result = self.solution.longest_increasing_path(matrix)
        assert result == expected

    def test_all_same_values(self):
        """Test matrix where all elements are the same."""
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 1

    def test_strictly_increasing_row(self):
        """Test matrix with strictly increasing row."""
        matrix = [[1, 2, 3, 4, 5]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 5

    def test_strictly_increasing_column(self):
        """Test matrix with strictly increasing column."""
        matrix = [[1], [2], [3], [4], [5]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 5

    def test_decreasing_sequence(self):
        """Test matrix with decreasing values."""
        matrix = [[5, 4, 3], [2, 1, 0]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 4  # Path: 0->3->4->5

    def test_spiral_pattern(self):
        """Test matrix with spiral increasing pattern."""
        matrix = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 16

    def test_mountain_pattern(self):
        """Test matrix with mountain-like pattern."""
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 9

    def test_random_pattern(self):
        """Test matrix with random values."""
        matrix = [
            [3, 1, 6, 4],
            [2, 5, 8, 7],
            [9, 12, 11, 10]
        ]
        result = self.solution.longest_increasing_path(matrix)
        expected = 5  # Path: 1->2->3->6->8 or similar
        assert result == expected

    @pytest.mark.performance
    def test_large_matrix(self):
        """Test with larger matrix."""
        matrix = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 25

    @pytest.mark.negative_values
    def test_negative_numbers(self):
        """Test matrix with negative numbers."""
        matrix = [[-1, -2, -3], [-4, -5, -6]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 4  # Path: -6->-3->-2->-1

    @pytest.mark.negative_values
    def test_mixed_positive_negative(self):
        """Test matrix with mixed positive and negative numbers."""
        matrix = [[-3, -2, -1], [0, 1, 2]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 4  # Path: -3->-2->-1->2

    @pytest.mark.details_method
    def test_get_longest_path_details_basic(self):
        """Test get_longest_path_details method with basic example."""
        matrix = [[1, 2, 3], [6, 5, 4]]
        result = self.solution.get_longest_path_details(matrix)
        assert result['length'] == 6
        assert len(result['starting_positions']) >= 1
        assert len(result['path_values']) == 6

    @pytest.mark.details_method
    def test_get_longest_path_details_single_element(self):
        """Test get_longest_path_details with single element."""
        matrix = [[5]]
        result = self.solution.get_longest_path_details(matrix)
        assert result['length'] == 1
        assert result['starting_positions'] == [(0, 0)]
        assert result['path_values'] == [5]

    @pytest.mark.edge_cases
    def test_get_longest_path_details_empty_matrix(self):
        """Test get_longest_path_details with empty matrix."""
        matrix = []
        result = self.solution.get_longest_path_details(matrix)
        assert result['length'] == 0
        assert result['starting_positions'] == []
        assert result['path_values'] == []

    @pytest.mark.edge_cases
    def test_empty_row_matrix(self):
        """Test matrix with empty row."""
        matrix = [[]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 0

    def test_algorithm_correctness_properties(self):
        """Test algorithm correctness properties."""
        # Property 1: Single element matrix always returns 1
        for value in [-10, 0, 5, 100]:
            matrix = [[value]]
            assert self.solution.longest_increasing_path(matrix) == 1

        # Property 2: Matrix with all same values returns 1
        matrix = [[7, 7], [7, 7]]
        assert self.solution.longest_increasing_path(matrix) == 1

        # Property 3: Strictly increasing sequence
        matrix = [[1, 2, 3, 4]]
        assert self.solution.longest_increasing_path(matrix) == 4

    @pytest.mark.edge_cases
    def test_boundary_conditions(self):
        """Test boundary conditions and edge cases."""
        # Test with maximum single path
        matrix = [[1, 2], [4, 3]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 4  # Path: 1->2->3->4

        # Test with no increasing path possible (all same)
        matrix = [[5, 5], [5, 5]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 1

    @pytest.mark.performance
    @pytest.mark.slow
    def test_performance_larger_matrix(self):
        """Test performance with larger matrix."""
        # Create a 10x10 matrix with sequential values in row-major order
        size = 10
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(i * size + j + 1)
            matrix.append(row)
        
        result = self.solution.longest_increasing_path(matrix)
        # The longest path will be down the rightmost column then across bottom
        assert result == 19  # Best we can do in this layout

    def test_invalid_input_handling(self):
        """Test that invalid inputs are handled gracefully."""
        # Empty matrix should return 0, not raise an exception
        result = self.solution.longest_increasing_path([])
        assert result == 0
        
        # Matrix with empty row should return 0
        result = self.solution.longest_increasing_path([[]])
        assert result == 0

    def test_complex_path_patterns(self):
        """Test with complex path patterns."""
        matrix = [
            [1, 17, 8, 25],
            [2, 18, 9, 26],
            [3, 19, 10, 27],
            [4, 20, 11, 28]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result >= 4  # At least one column worth

    def test_path_validation(self):
        """Test that the returned path is valid."""
        matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
        details = self.solution.get_longest_path_details(matrix)
        
        # Verify path is strictly increasing
        path_values = details['path_values']
        if len(path_values) > 1:
            for i in range(1, len(path_values)):
                assert path_values[i] > path_values[i-1]

    def test_memoization_efficiency(self):
        """Test that memoization improves efficiency."""
        # Create a matrix where naive DFS would be exponential
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        
        # This should complete quickly due to memoization
        result = self.solution.longest_increasing_path(matrix)
        assert result == 8  # Best path length in this grid pattern

    def test_return_type_validation(self):
        """Test that return types are correct."""
        matrix = [[1, 2], [3, 4]]
        
        # Test longest_increasing_path return type
        result = self.solution.longest_increasing_path(matrix)
        assert isinstance(result, int)
        assert result >= 1

        # Test get_longest_path_details return type
        details = self.solution.get_longest_path_details(matrix)
        assert isinstance(details, dict)
        assert 'length' in details
        assert 'starting_positions' in details
        assert 'path_values' in details
        assert isinstance(details['length'], int)
        assert isinstance(details['starting_positions'], list)
        assert isinstance(details['path_values'], list)

    def test_input_preservation(self):
        """Test that input matrix is not modified."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        original_matrix = [row[:] for row in matrix]  # Deep copy
        
        self.solution.longest_increasing_path(matrix)
        assert matrix == original_matrix

        self.solution.get_longest_path_details(matrix)
        assert matrix == original_matrix

    def test_both_methods_consistency(self):
        """Test that both methods return consistent results."""
        test_matrices = [
            [[1, 2, 3], [6, 5, 4]],
            [[9, 9, 4], [6, 6, 8], [2, 1, 1]],
            [[1]],
            [[1, 2], [4, 3]]
        ]
        
        for matrix in test_matrices:
            length1 = self.solution.longest_increasing_path(matrix)
            details = self.solution.get_longest_path_details(matrix)
            length2 = details['length']
            assert length1 == length2

    def test_diagonal_paths(self):
        """Test matrices where optimal path might be diagonal."""
        matrix = [
            [1, 3, 5],
            [2, 4, 6],
            [7, 8, 9]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result >= 5  # Should find a good path

    def test_multiple_optimal_paths(self):
        """Test matrix with multiple optimal paths of same length."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        result = self.solution.longest_increasing_path(matrix)
        details = self.solution.get_longest_path_details(matrix)
        
        assert result == 5  # Best path like 1->2->3->6->9
        assert details['length'] == 5
        assert len(details['starting_positions']) >= 1

    def test_zero_and_negative_values(self):
        """Test matrix with zero and negative values."""
        matrix = [
            [-5, -4, -3],
            [0, 1, 2],
            [3, 4, 5]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 5  # Best achievable path

    def test_large_value_differences(self):
        """Test matrix with large value differences."""
        matrix = [
            [1, 1000000],
            [2, 999999]
        ]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 4  # Path: 1->2->999999->1000000

    def test_edge_case_matrix_shapes(self):
        """Test various matrix shapes."""
        # Single row
        matrix = [[1, 3, 2, 4]]
        result = self.solution.longest_increasing_path(matrix)
        assert result >= 1

        # Single column  
        matrix = [[1], [3], [2], [4]]
        result = self.solution.longest_increasing_path(matrix)
        assert result >= 1

        # Tall rectangle
        matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 5  # Best path length in this pattern

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        # Test with duplicate values in path
        matrix = [[1, 2, 2], [3, 4, 5]]
        result = self.solution.longest_increasing_path(matrix)
        assert result >= 3  # Can't use duplicate 2s in path

        # Test with isolated peaks
        matrix = [[1, 3, 1], [1, 2, 1], [1, 1, 1]]
        result = self.solution.longest_increasing_path(matrix)
        assert result == 3  # 1 -> 2 -> 3
