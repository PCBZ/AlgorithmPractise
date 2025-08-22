"""
Test cases for Search a 2D Matrix problem
Source: https://leetcode.com/problems/search-a-2d-matrix/description/
"""

import sys
import os
import importlib.util

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

# Import the module with snake_case name
spec = importlib.util.spec_from_file_location(
    "search_a_2D_matrix", 
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "leetcode", "search_a_2D_matrix.py")
)
search_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search_module)
Solution = search_module.Solution


class TestSearchMatrix:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_basic_case_found(self):
        """Test basic case where target is found."""
        matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
        target = 5
        assert self.solution.searchMatrix(matrix, target) is True

    def test_basic_case_not_found(self):
        """Test basic case where target is not found."""
        matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
        target = 13
        assert self.solution.searchMatrix(matrix, target) is False

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 10
        assert self.solution.searchMatrix(matrix, target) is True

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
        target = 15
        assert self.solution.searchMatrix(matrix, target) is False

    def test_single_element_found(self):
        """Test with single element matrix - target found."""
        matrix = [[5]]
        target = 5
        assert self.solution.searchMatrix(matrix, target) is True

    def test_single_element_not_found(self):
        """Test with single element matrix - target not found."""
        matrix = [[5]]
        target = 3
        assert self.solution.searchMatrix(matrix, target) is False

    def test_single_row_found(self):
        """Test with single row matrix - target found."""
        matrix = [[1, 3, 5, 7, 9]]
        target = 5
        assert self.solution.searchMatrix(matrix, target) is True

    def test_single_row_not_found(self):
        """Test with single row matrix - target not found."""
        matrix = [[1, 3, 5, 7, 9]]
        target = 6
        assert self.solution.searchMatrix(matrix, target) is False

    def test_single_column_found(self):
        """Test with single column matrix - target found."""
        matrix = [[1], [3], [5], [7], [9]]
        target = 5
        assert self.solution.searchMatrix(matrix, target) is True

    def test_single_column_not_found(self):
        """Test with single column matrix - target not found."""
        matrix = [[1], [3], [5], [7], [9]]
        target = 6
        assert self.solution.searchMatrix(matrix, target) is False

    def test_first_element(self):
        """Test when target is the first element."""
        matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
        target = 1
        assert self.solution.searchMatrix(matrix, target) is True

    def test_last_element(self):
        """Test when target is the last element."""
        matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
        target = 16
        assert self.solution.searchMatrix(matrix, target) is True

    def test_target_too_small(self):
        """Test when target is smaller than all elements."""
        matrix = [[5, 6, 7], [8, 9, 10], [11, 12, 13]]
        target = 3
        assert self.solution.searchMatrix(matrix, target) is False

    def test_target_too_large(self):
        """Test when target is larger than all elements."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        target = 15
        assert self.solution.searchMatrix(matrix, target) is False

    def test_middle_elements(self):
        """Test searching for elements in the middle of rows."""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        assert self.solution.searchMatrix(matrix, 6) is True
        assert self.solution.searchMatrix(matrix, 10) is True

    def test_larger_matrix(self):
        """Test with a larger matrix."""
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        assert self.solution.searchMatrix(matrix, 14) is True
        assert self.solution.searchMatrix(matrix, 20) is False

    def test_consecutive_numbers(self):
        """Test with consecutive numbers."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for i in range(1, 10):
            assert self.solution.searchMatrix(matrix, i) is True
        assert self.solution.searchMatrix(matrix, 0) is False
        assert self.solution.searchMatrix(matrix, 10) is False

    @pytest.mark.parametrize("matrix,target,expected", [
        ([[1, 3, 5]], 3, True),
        ([[1, 3, 5]], 4, False),
        ([[1], [3], [5]], 3, True),
        ([[1], [3], [5]], 4, False),
        ([[1, 2], [3, 4]], 2, True),
        ([[1, 2], [3, 4]], 5, False),
        ([[1, 2, 3, 4, 5]], 1, True),
        ([[1, 2, 3, 4, 5]], 5, True),
        ([[1, 2, 3, 4, 5]], 3, True),
    ])
    def test_parametrized_cases(self, matrix, target, expected):
        """Test multiple cases using parametrization."""
        assert self.solution.searchMatrix(matrix, target) is expected


if __name__ == "__main__":
    pytest.main([__file__])
