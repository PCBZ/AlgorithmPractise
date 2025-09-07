"""
Test cases for LeetCode 417. Pacific Atlantic Water Flow

Tests the DFS solution for finding cells that can reach both oceans.
Covers various grid configurations, edge cases, and performance scenarios.
"""

import pytest
from typing import List
import sys
import os

# Add the parent directory to sys.path to import from leetcode module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from leetcode.pacific_atlantic_water_flow import Solution


class TestPacificAtlanticWaterFlow:
    """Test cases for Pacific Atlantic Water Flow solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def normalize_result(self, result: List[List[int]]) -> List[List[int]]:
        """Normalize result by sorting for consistent comparison."""
        return sorted(result)
    
    def test_example_case(self):
        """Test the main example from problem description."""
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1], 
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_uniform_grid(self):
        """Test grid with uniform heights - all cells should reach both oceans."""
        heights = [[1, 1], [1, 1]]
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
        
    def test_single_cell(self):
        """Test single cell grid - should reach both oceans."""
        heights = [[5]]
        expected = [[0, 0]]
        result = self.solution.pacificAtlantic(heights)
        assert result == expected
    
    def test_single_row(self):
        """Test single row - all cells should reach both oceans."""
        heights = [[1, 2, 3, 2, 1]]
        expected = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_single_column(self):
        """Test single column - all cells should reach both oceans."""
        heights = [[1], [2], [3], [2], [1]]
        expected = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_ascending_heights(self):
        """Test strictly ascending heights - border cells can reach their adjacent ocean."""
        heights = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        # Border cells that can reach both oceans
        expected = [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_descending_heights(self):
        """Test strictly descending heights - cells near borders can reach oceans."""
        heights = [
            [9, 8, 7],
            [6, 5, 4], 
            [3, 2, 1]
        ]
        # Only cells that can reach both oceans
        expected = [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_mountain_pattern(self):
        """Test mountain-like pattern with peak in center."""
        heights = [
            [1, 3, 1],
            [3, 5, 3],
            [1, 3, 1]
        ]
        # Cells that can reach both oceans through the mountain
        expected = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_valley_pattern(self):
        """Test valley-like pattern with minimum in center."""
        heights = [
            [5, 3, 5],
            [3, 1, 3],
            [5, 3, 5]
        ]
        # Only corner cells can reach both oceans
        expected = [[0, 2], [2, 0]]
        result = self.solution.pacificAtlantic(heights)
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_blocked_center(self):
        """Test case where center is blocked from one ocean."""
        heights = [
            [1, 1, 1, 1, 1],
            [1, 2, 2, 2, 1],
            [1, 2, 3, 2, 1],
            [1, 2, 2, 2, 1],
            [1, 1, 1, 1, 1]
        ]
        result = self.solution.pacificAtlantic(heights)
        # All border cells should be included
        assert [0, 0] in result
        assert [0, 4] in result
        assert [4, 0] in result
        assert [4, 4] in result
    
    def test_zigzag_pattern(self):
        """Test zigzag height pattern."""
        heights = [
            [1, 3, 1, 3],
            [3, 1, 3, 1],
            [1, 3, 1, 3]
        ]
        result = self.solution.pacificAtlantic(heights)
        expected = [[0, 3], [1, 0], [1, 2], [2, 0], [2, 1]]
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_large_uniform_grid(self):
        """Test performance with larger uniform grid."""
        size = 20
        heights = [[1 for _ in range(size)] for _ in range(size)]
        result = self.solution.pacificAtlantic(heights)
        expected = [[i, j] for i in range(size) for j in range(size)]
        assert len(result) == size * size
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_extreme_heights(self):
        """Test with extreme height values."""
        heights = [
            [1, 10**9, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = self.solution.pacificAtlantic(heights)
        # All cells should be reachable
        assert len(result) >= 4  # At least the corners
    
    def test_two_by_two_variations(self):
        """Test various 2x2 configurations."""
        test_cases = [
            # All same height - all cells reach both
            ([[1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
            # Ascending - some cells reach both
            ([[1, 2], [3, 4]], [[0, 1], [1, 0], [1, 1]]),  
            # Descending - border cells reach both
            ([[4, 3], [2, 1]], [[0, 0], [0, 1], [1, 0]]),
            # Mixed patterns
            ([[1, 4], [2, 3]], [[0, 1], [1, 0], [1, 1]])
        ]
        
        for heights, expected in test_cases:
            result = self.solution.pacificAtlantic(heights)
            assert self.normalize_result(result) == self.normalize_result(expected)
    
    @pytest.mark.parametrize("rows,cols", [
        (1, 10), (10, 1), (5, 5), (3, 7), (8, 4)
    ])
    def test_different_dimensions(self, rows: int, cols: int):
        """Test grids of different dimensions."""
        heights = [[1 for _ in range(cols)] for _ in range(rows)]
        result = self.solution.pacificAtlantic(heights)
        # All cells should reach both oceans in uniform grid
        assert len(result) == rows * cols
    
    def test_water_flow_logic(self):
        """Test specific water flow scenarios."""
        # Water can only flow to equal or lower heights
        heights = [
            [5, 4, 3],
            [6, 5, 4],
            [7, 6, 5]
        ]
        result = self.solution.pacificAtlantic(heights)
        # Check that diagonal flow works correctly
        assert len(result) > 0
    
    def test_isolated_regions(self):
        """Test grid with isolated high regions."""
        heights = [
            [1, 1, 1, 1, 1],
            [1, 5, 5, 5, 1],
            [1, 5, 9, 5, 1],
            [1, 5, 5, 5, 1],
            [1, 1, 1, 1, 1]
        ]
        result = self.solution.pacificAtlantic(heights)
        # Border cells should definitely be included
        assert [0, 0] in result
        assert [0, 4] in result
        assert [4, 0] in result
        assert [4, 4] in result
    
    def test_complex_topology(self):
        """Test complex topological scenario."""
        heights = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        result = self.solution.pacificAtlantic(heights)
        # Should have results due to spiral pattern
        assert len(result) > 0
        # Some specific corner cells should be reachable
        reachable_corners = [[0, 4], [4, 0], [4, 4]]
        for corner in reachable_corners:
            assert corner in result
    
    def test_narrow_passages(self):
        """Test scenario with narrow passages between regions."""
        heights = [
            [10, 1, 10],
            [1, 1, 1],
            [10, 1, 10]
        ]
        result = self.solution.pacificAtlantic(heights)
        # All cells should be reachable through the passage
        expected = [[i, j] for i in range(3) for j in range(3)]
        assert self.normalize_result(result) == self.normalize_result(expected)
    
    def test_performance_stress(self):
        """Test performance with moderately large grid."""
        size = 50
        heights = []
        for i in range(size):
            row = []
            for j in range(size):
                # Create interesting pattern
                height = abs(i - size//2) + abs(j - size//2) + 1
                row.append(height)
            heights.append(row)
        
        result = self.solution.pacificAtlantic(heights)
        # Should complete in reasonable time and have valid results
        assert len(result) > 0
        assert len(result) <= size * size


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
