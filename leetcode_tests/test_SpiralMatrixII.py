"""
Comprehensive test suite for LeetCode 59: Spiral Matrix II

This module contains extensive test cases to validate the spiral matrix generation
algorithm, including edge cases, performance tests, and validation tests.
"""

import pytest
import sys
import os
import time
from typing import List

# Add the parent directory to the path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from leetcode.spiral_matrix import Solution


class TestSpiralMatrixII:
    """Test class for Spiral Matrix II problem"""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Basic functionality tests
    def test_single_cell(self):
        """Test matrix generation for n=1"""
        result = self.solution.generateMatrix(1)
        expected = [[1]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_two_by_two(self):
        """Test matrix generation for n=2"""
        result = self.solution.generateMatrix(2)
        expected = [[1, 2], [4, 3]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_three_by_three(self):
        """Test matrix generation for n=3 (LeetCode example)"""
        result = self.solution.generateMatrix(3)
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_four_by_four(self):
        """Test matrix generation for n=4"""
        result = self.solution.generateMatrix(4)
        expected = [
            [1,  2,  3,  4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9,  8,  7]
        ]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_five_by_five(self):
        """Test matrix generation for n=5"""
        result = self.solution.generateMatrix(5)
        expected = [
            [1,  2,  3,  4,  5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Property-based tests
    def test_matrix_dimensions(self):
        """Test that generated matrices have correct dimensions"""
        for n in range(1, 11):
            result = self.solution.generateMatrix(n)
            assert len(result) == n, f"Matrix should have {n} rows, got {len(result)}"
            for row in result:
                assert len(row) == n, f"Each row should have {n} elements, got {len(row)}"
    
    def test_all_numbers_present(self):
        """Test that all numbers from 1 to n² are present exactly once"""
        for n in range(1, 11):
            result = self.solution.generateMatrix(n)
            
            # Flatten the matrix
            all_values = []
            for row in result:
                all_values.extend(row)
            
            # Check that we have exactly n² elements
            assert len(all_values) == n * n, f"Should have {n*n} elements, got {len(all_values)}"
            
            # Check that all values from 1 to n² are present exactly once
            all_values.sort()
            expected = list(range(1, n * n + 1))
            assert all_values == expected, f"Values should be 1 to {n*n}, got {all_values}"
    
    def test_spiral_pattern_validation(self):
        """Test that the spiral pattern is correct by checking adjacent values"""
        for n in range(2, 8):
            result = self.solution.generateMatrix(n)
            
            # Create a mapping from value to position
            value_to_pos = {}
            for i in range(n):
                for j in range(n):
                    value_to_pos[result[i][j]] = (i, j)
            
            # Check that consecutive values are adjacent (Manhattan distance = 1)
            for val in range(1, n * n):
                pos1 = value_to_pos[val]
                pos2 = value_to_pos[val + 1]
                manhattan_dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
                assert manhattan_dist == 1, f"Values {val} and {val+1} should be adjacent"
    
    def test_spiral_direction_pattern(self):
        """Test that the spiral follows the correct direction pattern"""
        n = 4
        result = self.solution.generateMatrix(n)
        
        # Expected pattern for 4x4: should start right, then down, then left, then up
        expected_first_row = [1, 2, 3, 4]  # Right direction
        expected_last_col = [4, 5, 6, 7]   # Down direction
        expected_last_row_rev = [10, 9, 8, 7]  # Left direction (reversed)
        expected_first_col_rev = [1, 12, 11, 10]  # Up direction (reversed)
        
        # Check first row (left to right)
        first_row = result[0]
        assert first_row == expected_first_row, f"First row should be {expected_first_row}, got {first_row}"
        
        # Check right column (top to bottom)
        right_col = [result[i][n-1] for i in range(n)]
        assert right_col == expected_last_col, f"Right column should be {expected_last_col}, got {right_col}"
    
    # Edge cases and constraints
    def test_minimum_constraint(self):
        """Test the minimum constraint n=1"""
        result = self.solution.generateMatrix(1)
        assert result == [[1]]
    
    def test_maximum_practical_size(self):
        """Test with larger practical sizes"""
        for n in [10, 15, 20]:
            result = self.solution.generateMatrix(n)
            assert len(result) == n
            assert len(result[0]) == n
            
            # Verify all numbers are present
            all_values = [val for row in result for val in row]
            assert len(set(all_values)) == n * n  # All unique
            assert min(all_values) == 1
            assert max(all_values) == n * n
    
    # Performance tests
    def test_performance_small_matrices(self):
        """Test performance for small matrices"""
        start_time = time.time()
        for n in range(1, 21):
            self.solution.generateMatrix(n)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Small matrices should be fast, took {execution_time:.3f}s"
    
    def test_performance_large_matrix(self):
        """Test performance for larger matrix"""
        n = 100
        start_time = time.time()
        result = self.solution.generateMatrix(n)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 2.0, f"Large matrix (100x100) should complete in under 2s, took {execution_time:.3f}s"
        assert len(result) == n
        assert len(result[0]) == n
    
    # Return type validation
    def test_return_type_structure(self):
        """Test that the return type is correctly structured"""
        for n in range(1, 6):
            result = self.solution.generateMatrix(n)
            
            # Should return a list
            assert isinstance(result, list), f"Should return a list, got {type(result)}"
            
            # Each element should be a list
            for i, row in enumerate(result):
                assert isinstance(row, list), f"Row {i} should be a list, got {type(row)}"
                
                # Each element in the row should be an integer
                for j, val in enumerate(row):
                    assert isinstance(val, int), f"Element at [{i}][{j}] should be int, got {type(val)}"
                    assert val >= 1, f"Element should be positive, got {val}"
                    assert val <= n * n, f"Element should be <= {n*n}, got {val}"
    
    # Correctness validation helpers
    def test_corner_elements(self):
        """Test that corner elements are correctly placed for various sizes"""
        test_cases = [
            (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
            (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
        ]
        
        for n, expected in test_cases:
            result = self.solution.generateMatrix(n)
            
            # Check corners
            assert result[0][0] == expected[0][0], f"Top-left corner mismatch"
            assert result[0][n-1] == expected[0][n-1], f"Top-right corner mismatch"
            assert result[n-1][0] == expected[n-1][0], f"Bottom-left corner mismatch"
            assert result[n-1][n-1] == expected[n-1][n-1], f"Bottom-right corner mismatch"
    
    def test_center_elements(self):
        """Test center elements for odd-sized matrices"""
        # For odd n, the center should be n²
        odd_sizes = [1, 3, 5, 7]
        for n in odd_sizes:
            result = self.solution.generateMatrix(n)
            center_i = center_j = n // 2
            center_value = result[center_i][center_j]
            expected_center = n * n
            assert center_value == expected_center, f"Center of {n}x{n} should be {expected_center}, got {center_value}"
    
    # Parametrized tests for comprehensive coverage
    @pytest.mark.parametrize("n", range(1, 16))
    def test_spiral_generation_parametrized(self, n):
        """Parametrized test for various matrix sizes"""
        result = self.solution.generateMatrix(n)
        
        # Basic validations
        assert len(result) == n
        assert all(len(row) == n for row in result)
        
        # Collect all values
        all_values = [val for row in result for val in row]
        
        # Check uniqueness and range
        assert len(set(all_values)) == n * n
        assert min(all_values) == 1
        assert max(all_values) == n * n


if __name__ == "__main__":
    """Run the tests when script is executed directly"""
    pytest.main([__file__, "-v", "--tb=short"])