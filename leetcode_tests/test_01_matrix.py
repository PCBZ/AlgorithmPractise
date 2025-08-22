"""
Test cases for 01 Matrix problem
Source: https://leetcode.com/problems/01-matrix/description/
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

# Import using importlib since module name starts with number
import importlib.util
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the module with numeric name
spec = importlib.util.spec_from_file_location(
    "matrix_01", 
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "leetcode", "01_matrix.py")
)
matrix_01 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_01)
Solution = matrix_01.Solution


class TestUpdateMatrix:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_case(self):
        """Test the basic example case."""
        mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        assert self.solution.updateMatrix(mat) == expected

    def test_example_case_2(self):
        """Test another example case."""
        mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
        expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        assert self.solution.updateMatrix(mat) == expected

    def test_single_zero(self):
        """Test with a single zero in the matrix."""
        mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        assert self.solution.updateMatrix(mat) == expected

    def test_all_zeros(self):
        """Test when all cells are zeros."""
        mat = [[0, 0], [0, 0]]
        expected = [[0, 0], [0, 0]]
        assert self.solution.updateMatrix(mat) == expected

    def test_all_ones(self):
        """Test when all cells are ones."""
        mat = [[1, 1], [1, 1]]
        # Since there are no zeros, distances should be infinite
        # But the problem guarantees at least one zero exists
        # This is an edge case that shouldn't occur per problem constraints
        pass

    def test_single_cell_zero(self):
        """Test with a single cell containing zero."""
        mat = [[0]]
        expected = [[0]]
        assert self.solution.updateMatrix(mat) == expected

    def test_single_cell_one(self):
        """Test with a single cell containing one."""
        # This violates problem constraints (at least one zero must exist)
        # But if it happened, it would be infinite distance
        pass

    def test_corner_zero(self):
        """Test with zero in corner."""
        mat = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
        assert self.solution.updateMatrix(mat) == expected

    def test_edge_zeros(self):
        """Test with zeros on edges."""
        mat = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        expected = [[0, 1, 0], [1, 2, 1], [0, 1, 0]]
        assert self.solution.updateMatrix(mat) == expected

    def test_large_matrix(self):
        """Test with a larger matrix."""
        mat = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 1]
        ]
        expected = [
            [2, 1, 2, 3],
            [1, 0, 1, 2],
            [2, 1, 1, 2],
            [2, 1, 0, 1]
        ]
        assert self.solution.updateMatrix(mat) == expected

    def test_rectangular_matrix(self):
        """Test with a rectangular (non-square) matrix."""
        mat = [[1, 0, 1, 1, 0]]
        expected = [[1, 0, 1, 1, 0]]
        assert self.solution.updateMatrix(mat) == expected

    def test_vertical_matrix(self):
        """Test with a vertical matrix."""
        mat = [[1], [0], [1], [1]]
        expected = [[1], [0], [1], [2]]
        assert self.solution.updateMatrix(mat) == expected

    @pytest.mark.parametrize("mat,expected", [
        ([[0, 1], [1, 0]], [[0, 1], [1, 0]]),
        ([[1, 0], [0, 1]], [[1, 0], [0, 1]]),
        ([[0, 1, 1], [1, 1, 0]], [[0, 1, 1], [1, 1, 0]]),
        ([[1, 1, 0], [0, 1, 1]], [[1, 1, 0], [0, 1, 1]])
    ])
    def test_parametrized_cases(self, mat, expected):
        """Test multiple cases using parametrization."""
        assert self.solution.updateMatrix(mat) == expected


if __name__ == "__main__":
    pytest.main([__file__])
