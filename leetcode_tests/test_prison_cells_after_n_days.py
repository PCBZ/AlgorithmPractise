"""
Test suite for LeetCode #957: Prison Cells After N Days
"""

import pytest
import time

from leetcode.prison_cells_after_n_days import Solution


class TestPrisonCellsAfterNDays:
    """Comprehensive test suite for Prison Cells After N Days problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # LeetCode Examples
    def test_example_1_leetcode(self):
        """Test LeetCode Example 1: [0,1,0,1,1,0,0,1], n=7 -> [0,0,1,1,0,0,0,0]"""
        cells = [0,1,0,1,1,0,0,1]
        n = 7
        expected = [0,0,1,1,0,0,0,0]
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_example_2_leetcode(self):
        """Test LeetCode Example 2: [1,0,0,1,0,0,1,0], n=1000000000 -> [0,0,1,1,1,1,1,0]"""
        cells = [1,0,0,1,0,0,1,0]
        n = 1000000000
        expected = [0,0,1,1,1,1,1,0]
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Edge Cases
    def test_n_zero(self):
        """Test with n=0 (no days)."""
        cells = [1,0,1,0,1,0,1,0]
        n = 0
        expected = [1,0,1,0,1,0,1,0]  # Should remain unchanged
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_n_one(self):
        """Test with n=1 (single day)."""
        cells = [1,0,1,0,1,0,1,0]
        n = 1
        expected = [0,1,1,1,1,1,1,0]  # Correct expected result
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_all_zeros(self):
        """Test with all cells initially empty."""
        cells = [0,0,0,0,0,0,0,0]
        n = 5
        expected = [0,1,0,1,1,0,1,0]  # Correct expected result after 5 days
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_all_ones(self):
        """Test with all cells initially occupied."""
        cells = [1,1,1,1,1,1,1,1]
        n = 1
        expected = [0,1,1,1,1,1,1,0]  # First/last become 0, middle stay 1
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_alternating_pattern(self):
        """Test with alternating pattern."""
        cells = [1,0,1,0,1,0,1,0]
        n = 2
        expected = [0,0,1,1,1,1,0,0]  # Correct expected result after 2 days
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Cycle Detection Tests
    def test_cycle_detection_small(self):
        """Test cycle detection with small numbers."""
        cells = [0,1,0,1,1,0,0,1]
        
        # Test multiple days to verify cycle occurs within reasonable range
        results = []
        for n in range(1, 30):  # Test more days to find cycles
            result = self.solution.prisonAfterNDays(cells[:], n)
            results.append(result)
        
        # Check that we eventually get repeating patterns
        assert len(set(tuple(r) for r in results)) < len(results), "Should have cycles"
    
    def test_cycle_length_properties(self):
        """Test properties of cycle lengths."""
        cells = [1,0,1,1,0,1,0,1]
        
        # Since first and last cells always become 0 after day 1,
        # we only have 2^6 = 64 possible states for middle 6 cells
        # So cycle length should be at most 64
        
        seen_states = set()
        current = cells[:]
        day = 0
        
        while day < 100:  # More than enough to find cycle
            state = tuple(current)
            if state in seen_states:
                break
            seen_states.add(state)
            current = self.solution.prisonAfterNDays(current, 1)
            day += 1
        
        assert day < 64, f"Cycle should be found within 64 days, but took {day}"
    
    def test_large_n_efficiency(self):
        """Test that large N values are handled efficiently."""
        cells = [1,0,1,0,1,0,1,0]
        n = 10**9
        
        start_time = time.time()
        result = self.solution.prisonAfterNDays(cells, n)
        end_time = time.time()
        
        execution_time = end_time - start_time
        assert execution_time < 0.1, f"Large N should be fast due to cycle detection: {execution_time:.3f}s"
        assert len(result) == 8, "Result should have 8 cells"
        assert all(cell in [0, 1] for cell in result), "All cells should be 0 or 1"
    
    # Specific Pattern Tests
    def test_symmetric_pattern(self):
        """Test with symmetric initial pattern."""
        cells = [1,0,1,1,1,1,0,1]
        n = 3
        result = self.solution.prisonAfterNDays(cells, n)
        
        # Verify result is valid
        assert len(result) == 8, "Should have 8 cells"
        assert result[0] == 0 and result[7] == 0, "First and last should be 0"
    
    def test_middle_cells_only(self):
        """Test pattern affecting only middle cells."""
        cells = [0,1,0,0,0,1,0,0]
        n = 1
        expected = [0,1,0,1,0,1,0,0]  # Correct expected result
        result = self.solution.prisonAfterNDays(cells, n)
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_no_changes_pattern(self):
        """Test pattern that results in no changes."""
        cells = [0,1,0,1,0,1,0,0]
        n = 1
        result = self.solution.prisonAfterNDays(cells, n)
        
        # After applying rules, first and last become 0
        expected = [0,1,1,1,1,1,0,0]  # Correct expected result
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Progressive Evolution Tests
    def test_step_by_step_evolution(self):
        """Test step-by-step evolution for small n."""
        cells = [1,1,0,0,0,0,1,1]
        
        # Day 1
        day1 = self.solution.prisonAfterNDays(cells[:], 1)
        assert day1[0] == 0 and day1[7] == 0, "First and last should be 0"
        
        # Day 2
        day2 = self.solution.prisonAfterNDays(cells[:], 2)
        
        # Verify consistency
        day1_to_day2 = self.solution.prisonAfterNDays(day1, 1)
        assert day2 == day1_to_day2, "Sequential application should match direct calculation"
    
    def test_multiple_n_values(self):
        """Test same initial state with different n values."""
        cells = [0,1,1,0,0,1,1,0]
        
        results = {}
        for n in [1, 2, 3, 5, 8, 13, 21]:
            results[n] = self.solution.prisonAfterNDays(cells[:], n)
        
        # Verify all results are valid
        for n, result in results.items():
            assert len(result) == 8, f"Day {n}: should have 8 cells"
            assert result[0] == 0 and result[7] == 0, f"Day {n}: first and last should be 0"
    
    # Boundary Tests
    def test_maximum_n(self):
        """Test with maximum reasonable n value."""
        cells = [1,0,1,0,1,0,1,0]
        n = 2**31 - 1  # Large number
        
        result = self.solution.prisonAfterNDays(cells, n)
        assert len(result) == 8, "Should handle large n"
        assert all(isinstance(cell, int) and cell in [0, 1] for cell in result)
    
    # Performance Tests
    def test_performance_various_patterns(self):
        """Test performance with various initial patterns."""
        patterns = [
            [1,0,0,0,0,0,0,1],
            [0,1,1,1,1,1,1,0],
            [1,0,1,0,1,0,1,0],
            [0,0,1,1,1,1,0,0],
            [1,1,0,0,0,0,1,1]
        ]
        
        for cells in patterns:
            start_time = time.time()
            result = self.solution.prisonAfterNDays(cells, 1000000)
            end_time = time.time()
            
            execution_time = end_time - start_time
            assert execution_time < 0.1, f"Should be fast for pattern {cells}: {execution_time:.3f}s"
            assert len(result) == 8, "Should have 8 cells"
    
    # Validation Tests
    def test_input_preservation(self):
        """Test that input array is not modified."""
        cells = [1,0,1,0,1,0,1,0]
        original = cells[:]
        
        self.solution.prisonAfterNDays(cells, 5)
        
        assert cells == original, "Input array should not be modified"
    
    def test_return_type(self):
        """Test that function returns correct type."""
        cells = [1,0,1,0,1,0,1,0]
        result = self.solution.prisonAfterNDays(cells, 3)
        
        assert isinstance(result, list), f"Expected list, got {type(result)}"
        assert len(result) == 8, f"Expected length 8, got {len(result)}"
        assert all(isinstance(cell, int) and cell in [0, 1] for cell in result), "All elements should be 0 or 1"
    
    def test_edge_cell_behavior(self):
        """Test that edge cells always become 0 after first day."""
        test_cases = [
            [1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1]
        ]
        
        for cells in test_cases:
            result = self.solution.prisonAfterNDays(cells, 1)
            assert result[0] == 0, f"First cell should be 0 for {cells}"
            assert result[7] == 0, f"Last cell should be 0 for {cells}"


if __name__ == "__main__":
    pytest.main([__file__])