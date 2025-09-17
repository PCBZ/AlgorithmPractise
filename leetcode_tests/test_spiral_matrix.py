"""
Comprehensive test suite for LeetCode Spiral Matrix Problems

This module contains extensive test cases to validate both:
- LeetCode 59: Spiral Matrix II (generate spiral matrix)
- LeetCode 885: Spiral Matrix III (spiral walk pattern)
Including edge cases, performance tests, and validation tests.
"""

import pytest
import time

from leetcode.spiral_matrix import Solution


class TestSpiralMatrix:
    """Test class for both Spiral Matrix problems"""
    
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


class TestSpiralMatrixIII:
    """Test class for Spiral Matrix III (LeetCode 885)"""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Basic functionality tests from LeetCode examples
    def test_example_1_leetcode(self):
        """Test LeetCode example 1: 1x4 grid starting from (0,0)"""
        result = self.solution.spiralMatrixIII(1, 4, 0, 0)
        expected = [[0, 0], [0, 1], [0, 2], [0, 3]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_2_leetcode(self):
        """Test LeetCode example 2: 5x6 grid starting from (1,4)"""
        result = self.solution.spiralMatrixIII(5, 6, 1, 4)
        expected = [
            [1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],
            [0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],
            [4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
            [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]
        ]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge cases
    def test_single_cell(self):
        """Test 1x1 grid"""
        result = self.solution.spiralMatrixIII(1, 1, 0, 0)
        expected = [[0, 0]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_single_row(self):
        """Test single row grids"""
        test_cases = [
            (1, 2, 0, 0, [[0, 0], [0, 1]]),
            (1, 3, 0, 1, [[0, 1], [0, 2], [0, 0]]),
            (1, 5, 0, 2, [[0, 2], [0, 3], [0, 1], [0, 4], [0, 0]])
        ]
        
        for rows, cols, rStart, cStart, expected in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            assert result == expected, f"For {rows}x{cols} start ({rStart},{cStart}): expected {expected}, got {result}"
    
    def test_single_column(self):
        """Test single column grids"""
        test_cases = [
            (2, 1, 0, 0, [[0, 0], [1, 0]]),
            (3, 1, 1, 0, [[1, 0], [2, 0], [0, 0]]),
            (4, 1, 2, 0, [[2, 0], [3, 0], [1, 0], [0, 0]])
        ]
        
        for rows, cols, rStart, cStart, expected in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            assert result == expected, f"For {rows}x{cols} start ({rStart},{cStart}): expected {expected}, got {result}"
    
    def test_square_grids(self):
        """Test square grids with center start"""
        # 2x2 grid starting from center
        result = self.solution.spiralMatrixIII(2, 2, 0, 0)
        expected = [[0, 0], [0, 1], [1, 1], [1, 0]]
        assert result == expected, f"Expected {expected}, got {result}"
        
        # 3x3 grid starting from center
        result = self.solution.spiralMatrixIII(3, 3, 1, 1)
        expected = [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Property validation tests
    def test_all_coordinates_visited(self):
        """Test that all grid coordinates are visited exactly once"""
        test_cases = [
            (2, 3, 0, 1),
            (3, 4, 1, 2),
            (4, 5, 2, 3),
            (5, 3, 3, 1)
        ]
        
        for rows, cols, rStart, cStart in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            
            # Check total number of coordinates
            assert len(result) == rows * cols, f"Should visit {rows*cols} coordinates, got {len(result)}"
            
            # Check all coordinates are unique
            unique_coords = set(tuple(coord) for coord in result)
            assert len(unique_coords) == rows * cols, f"All coordinates should be unique"
            
            # Check all valid coordinates are present
            expected_coords = {(i, j) for i in range(rows) for j in range(cols)}
            actual_coords = {tuple(coord) for coord in result}
            assert actual_coords == expected_coords, f"Missing or invalid coordinates"
    
    def test_starting_position_first(self):
        """Test that the starting position is always first in the result"""
        test_cases = [
            (3, 4, 0, 0),
            (3, 4, 1, 2),
            (3, 4, 2, 3),
            (5, 6, 2, 1),
            (1, 1, 0, 0)
        ]
        
        for rows, cols, rStart, cStart in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            assert result[0] == [rStart, cStart], f"First coordinate should be start position [{rStart}, {cStart}], got {result[0]}"
    
    def test_valid_coordinates_only(self):
        """Test that all returned coordinates are within grid bounds"""
        test_cases = [
            (2, 3, 0, 1),
            (4, 5, 2, 1),
            (6, 4, 3, 2),
            (10, 8, 5, 3)
        ]
        
        for rows, cols, rStart, cStart in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            
            for i, (r, c) in enumerate(result):
                assert 0 <= r < rows, f"Row {r} at step {i} is out of bounds [0, {rows})"
                assert 0 <= c < cols, f"Col {c} at step {i} is out of bounds [0, {cols})"
    
    # Corner start positions
    def test_corner_start_positions(self):
        """Test starting from each corner of the grid"""
        rows, cols = 4, 5
        
        # Top-left corner
        result = self.solution.spiralMatrixIII(rows, cols, 0, 0)
        assert result[0] == [0, 0]
        assert len(result) == rows * cols
        
        # Top-right corner
        result = self.solution.spiralMatrixIII(rows, cols, 0, cols-1)
        assert result[0] == [0, cols-1]
        assert len(result) == rows * cols
        
        # Bottom-left corner
        result = self.solution.spiralMatrixIII(rows, cols, rows-1, 0)
        assert result[0] == [rows-1, 0]
        assert len(result) == rows * cols
        
        # Bottom-right corner
        result = self.solution.spiralMatrixIII(rows, cols, rows-1, cols-1)
        assert result[0] == [rows-1, cols-1]
        assert len(result) == rows * cols
    
    # Performance tests
    def test_performance_medium_grid(self):
        """Test performance for medium-sized grids"""
        start_time = time.time()
        result = self.solution.spiralMatrixIII(20, 20, 10, 10)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Medium grid (20x20) should be fast, took {execution_time:.3f}s"
        assert len(result) == 400
    
    def test_performance_large_grid(self):
        """Test performance for larger grids"""
        start_time = time.time()
        result = self.solution.spiralMatrixIII(50, 50, 25, 25)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 2.0, f"Large grid (50x50) should complete in under 2s, took {execution_time:.3f}s"
        assert len(result) == 2500
    
    def test_performance_rectangular_grid(self):
        """Test performance for rectangular grids"""
        start_time = time.time()
        result = self.solution.spiralMatrixIII(30, 70, 15, 35)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 2.0, f"Rectangular grid (30x70) should be fast, took {execution_time:.3f}s"
        assert len(result) == 2100
    
    # Return type validation
    def test_return_type_structure(self):
        """Test that the return type is correctly structured"""
        test_cases = [(2, 3, 1, 1), (4, 5, 2, 2), (1, 1, 0, 0)]
        
        for rows, cols, rStart, cStart in test_cases:
            result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
            
            # Should return a list
            assert isinstance(result, list), f"Should return a list, got {type(result)}"
            
            # Each element should be a list with 2 integers
            for i, coord in enumerate(result):
                assert isinstance(coord, list), f"Coordinate {i} should be a list, got {type(coord)}"
                assert len(coord) == 2, f"Coordinate {i} should have 2 elements, got {len(coord)}"
                
                assert isinstance(coord[0], int), f"Row coordinate should be int, got {type(coord[0])}"
                assert isinstance(coord[1], int), f"Col coordinate should be int, got {type(coord[1])}"
    
    # Spiral pattern validation
    def test_spiral_expansion_pattern(self):
        """Test that the spiral follows the correct expansion pattern"""
        # For a 5x5 grid starting from center, the pattern should be:
        # Right 1, Down 1, Left 2, Up 2, Right 3, Down 3, Left 4, Up 4, etc.
        result = self.solution.spiralMatrixIII(5, 5, 2, 2)
        
        # Check that starting position is correct
        assert result[0] == [2, 2]
        
        # Verify we visit all 25 cells
        assert len(result) == 25
        
        # Check some key positions in the spiral
        expected_early_positions = [
            [2, 2],  # Start
            [2, 3],  # Right 1
            [3, 3],  # Down 1  
            [3, 2],  # Left 1
            [3, 1],  # Left 2
            [2, 1],  # Up 1
            [1, 1],  # Up 2
        ]
        
        for i, expected_pos in enumerate(expected_early_positions):
            assert result[i] == expected_pos, f"Position {i} should be {expected_pos}, got {result[i]}"
    
    # Parametrized tests
    @pytest.mark.parametrize("rows,cols", [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (2, 4), (4, 2)])
    def test_small_grids_parametrized(self, rows, cols):
        """Parametrized test for small grids"""
        # Test from each valid starting position
        for rStart in range(rows):
            for cStart in range(cols):
                result = self.solution.spiralMatrixIII(rows, cols, rStart, cStart)
                
                # Basic validations
                assert len(result) == rows * cols
                assert result[0] == [rStart, cStart]
                
                # Check all coordinates are valid
                for r, c in result:
                    assert 0 <= r < rows
                    assert 0 <= c < cols
                
                # Check uniqueness
                unique_coords = set(tuple(coord) for coord in result)
                assert len(unique_coords) == rows * cols


    # Combined tests for both problems
    def test_both_algorithms_consistency(self):
        """Test that both algorithms work correctly together"""
        # Test Spiral Matrix II
        matrix_result = self.solution.generateMatrix(3)
        expected_matrix = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        assert matrix_result == expected_matrix
        
        # Test Spiral Matrix III
        walk_result = self.solution.spiralMatrixIII(1, 4, 0, 0)
        expected_walk = [[0, 0], [0, 1], [0, 2], [0, 3]]
        assert walk_result == expected_walk


if __name__ == "__main__":
    """Run the tests when script is executed directly"""
    pytest.main([__file__, "-v", "--tb=short"])