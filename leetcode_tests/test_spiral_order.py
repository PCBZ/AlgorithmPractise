"""
Comprehensive test suite for LeetCode 54: Spiral Matrix

This module contains extensive test cases to validate the spiral matrix traversal
algorithm, including edge cases, performance tests, and validation tests.
"""

import pytest
import time

from leetcode.spiral_order import Solution


class TestSpiralOrder:
    """Test class for Spiral Matrix (LeetCode 54)"""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Basic functionality tests from LeetCode examples
    def test_example_1_leetcode(self):
        """Test LeetCode example 1: 3x3 matrix"""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_2_leetcode(self):
        """Test LeetCode example 2: 3x4 matrix"""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge cases
    def test_single_element(self):
        """Test single element matrix"""
        matrix = [[42]]
        result = self.solution.spiralOrder(matrix)
        expected = [42]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_single_row(self):
        """Test single row matrices"""
        test_cases = [
            ([[1]], [1]),
            ([[1, 2]], [1, 2]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5])
        ]
        
        for matrix, expected in test_cases:
            result = self.solution.spiralOrder(matrix)
            assert result == expected, f"For matrix {matrix}: expected {expected}, got {result}"
    
    def test_single_column(self):
        """Test single column matrices"""
        test_cases = [
            ([[1]], [1]),
            ([[1], [2]], [1, 2]),
            ([[1], [2], [3]], [1, 2, 3]),
            ([[1], [2], [3], [4]], [1, 2, 3, 4])
        ]
        
        for matrix, expected in test_cases:
            result = self.solution.spiralOrder(matrix)
            assert result == expected, f"For matrix {matrix}: expected {expected}, got {result}"
    
    def test_2x2_matrix(self):
        """Test 2x2 matrix"""
        matrix = [[1, 2], [3, 4]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 4, 3]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_2x3_matrix(self):
        """Test 2x3 matrix"""
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 6, 5, 4]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_3x2_matrix(self):
        """Test 3x2 matrix"""
        matrix = [[1, 2], [3, 4], [5, 6]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 4, 6, 5, 3]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_larger_square_matrix(self):
        """Test larger square matrices"""
        # 4x4 matrix
        matrix = [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]
        ]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_larger_rectangular_matrix(self):
        """Test larger rectangular matrix"""
        matrix = [
            [1,  2,  3,  4,  5],
            [6,  7,  8,  9,  10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Property validation tests
    def test_all_elements_present(self):
        """Test that all matrix elements are present in result"""
        test_matrices = [
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3, 4], [5, 6, 7, 8]],
            [[1], [2], [3], [4], [5]],
            [[1, 2, 3, 4, 5]],
            [[1, 2], [3, 4], [5, 6]]
        ]
        
        for matrix in test_matrices:
            result = self.solution.spiralOrder(matrix)
            
            # Flatten matrix to get all elements
            all_elements = [val for row in matrix for val in row]
            
            # Check same length
            assert len(result) == len(all_elements), f"Result length mismatch for matrix {matrix}"
            
            # Check same elements (account for potential duplicates)
            all_elements.sort()
            result_sorted = sorted(result)
            assert result_sorted == all_elements, f"Elements mismatch for matrix {matrix}"
    
    def test_result_length(self):
        """Test that result length equals matrix size"""
        test_cases = [
            ([[1]], 1),
            ([[1, 2, 3]], 3),
            ([[1], [2], [3]], 3),
            ([[1, 2], [3, 4]], 4),
            ([[1, 2, 3], [4, 5, 6]], 6),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
        ]
        
        for matrix, expected_length in test_cases:
            result = self.solution.spiralOrder(matrix)
            assert len(result) == expected_length, f"Expected length {expected_length}, got {len(result)}"
    
    def test_spiral_order_correctness(self):
        """Test that elements are visited in correct spiral order"""
        # Test a specific matrix where we can verify the exact order
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        result = self.solution.spiralOrder(matrix)
        
        # The spiral order should visit: right edge first, then follow spiral
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_negative_numbers(self):
        """Test matrix with negative numbers"""
        matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        result = self.solution.spiralOrder(matrix)
        expected = [-1, -2, -3, -6, -9, -8, -7, -4, -5]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_mixed_positive_negative(self):
        """Test matrix with mixed positive and negative numbers"""
        matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, -2, 3, -6, 9, -8, 7, -4, 5]
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_duplicate_elements(self):
        """Test matrix with duplicate elements"""
        matrix = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]
        result = self.solution.spiralOrder(matrix)
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 2]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Performance tests
    def test_performance_medium_matrix(self):
        """Test performance for medium-sized matrices"""
        # Create 10x10 matrix
        matrix = []
        counter = 1
        for i in range(10):
            row = []
            for j in range(10):
                row.append(counter)
                counter += 1
            matrix.append(row)
        
        start_time = time.time()
        result = self.solution.spiralOrder(matrix)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 1.0, f"Medium matrix (10x10) should be fast, took {execution_time:.3f}s"
        assert len(result) == 100
    
    def test_performance_large_matrix(self):
        """Test performance for larger matrices"""
        # Create 50x20 matrix
        matrix = []
        counter = 1
        for i in range(50):
            row = []
            for j in range(20):
                row.append(counter)
                counter += 1
            matrix.append(row)
        
        start_time = time.time()
        result = self.solution.spiralOrder(matrix)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 2.0, f"Large matrix (50x20) should complete in under 2s, took {execution_time:.3f}s"
        assert len(result) == 1000
    
    # Return type validation
    def test_return_type(self):
        """Test that return type is List[int]"""
        test_matrices = [
            [[1]],
            [[1, 2], [3, 4]],
            [[1, 2, 3], [4, 5, 6]]
        ]
        
        for matrix in test_matrices:
            result = self.solution.spiralOrder(matrix)
            
            # Should return a list
            assert isinstance(result, list), f"Should return a list, got {type(result)}"
            
            # Each element should be an integer
            for i, val in enumerate(result):
                assert isinstance(val, int), f"Element {i} should be int, got {type(val)}"
    
    # Edge case boundary tests
    def test_matrix_bounds_constraints(self):
        """Test matrices within problem constraints"""
        # Test minimum size (1x1)
        matrix = [[1]]
        result = self.solution.spiralOrder(matrix)
        assert result == [1]
        
        # Test maximum values in constraints (-100 to 100)
        matrix = [[-100, 0, 100]]
        result = self.solution.spiralOrder(matrix)
        assert result == [-100, 0, 100]
    
    # Spiral pattern validation for specific cases
    def test_spiral_layers(self):
        """Test that spiral correctly handles multiple layers"""
        # 5x5 matrix to test multiple layers
        matrix = [
            [1,  2,  3,  4,  5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        result = self.solution.spiralOrder(matrix)
        
        # Should traverse layer by layer
        # Outer layer: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
        # Next layer: 17,18,19,20,21,22,23,24
        # Center: 25
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25]
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Parametrized tests
    @pytest.mark.parametrize("m,n", [(1, 1), (1, 2), (2, 1), (2, 2), (3, 3), (2, 4), (4, 2)])
    def test_small_matrices_parametrized(self, m, n):
        """Parametrized test for small matrices"""
        # Create m×n matrix with sequential numbers
        matrix = []
        counter = 1
        for i in range(m):
            row = []
            for j in range(n):
                row.append(counter)
                counter += 1
            matrix.append(row)
        
        result = self.solution.spiralOrder(matrix)
        
        # Basic validations
        assert len(result) == m * n
        
        # Check all elements are present
        all_elements = [val for row in matrix for val in row]
        assert sorted(result) == sorted(all_elements)
        
        # Check return type
        assert isinstance(result, list)
        assert all(isinstance(x, int) for x in result)


if __name__ == "__main__":
    """Run the tests when script is executed directly"""
    pytest.main([__file__, "-v", "--tb=short"])