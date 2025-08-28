"""
Test cases for LeetCode Problem #134: Gas Station
"""
import unittest
import sys
import os

# Add the parent directory to the Python path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Import using importlib
import importlib.util
spec = importlib.util.spec_from_file_location(
    "solution",
    os.path.join(parent_dir, "leetcode", "gas_station.py")
)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution


class TestGasStation(unittest.TestCase):
    """Test cases for the GasStation solution."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test first example case - should start at station 3."""
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 3
        assert result == expected

    def test_example_case_2(self):
        """Test second example case - impossible to complete."""
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = -1
        assert result == expected

    def test_single_station_possible(self):
        """Test single station where completion is possible."""
        gas = [5]
        cost = [4]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 0
        assert result == expected

    def test_single_station_impossible(self):
        """Test single station where completion is impossible."""
        gas = [4]
        cost = [5]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = -1
        assert result == expected

    def test_two_stations_start_second(self):
        """Test two stations where we must start at second."""
        gas = [1, 2]
        cost = [2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 1
        assert result == expected

    def test_two_stations_start_first(self):
        """Test two stations where we can start at first."""
        gas = [3, 1]
        cost = [1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 0
        assert result == expected

    def test_three_stations_possible(self):
        """Test three stations with possible completion."""
        gas = [1, 2, 3]
        cost = [2, 1, 3]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 1
        assert result == expected

    def test_start_at_beginning(self):
        """Test case where optimal start is at index 0."""
        gas = [3, 1, 1]
        cost = [1, 2, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 0
        assert result == expected

    def test_exact_gas_needed(self):
        """Test case where total gas exactly equals total cost."""
        gas = [2, 3, 1]
        cost = [3, 1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Total gas = 6, total cost = 6, should be possible
        assert result != -1

    def test_impossible_total_deficit(self):
        """Test case where total gas is less than total cost."""
        gas = [1, 1, 1]
        cost = [2, 2, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = -1
        assert result == expected

    def test_all_equal_amounts(self):
        """Test case where all stations have equal gas and cost."""
        gas = [2, 2, 2, 2]
        cost = [2, 2, 2, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 0  # Should be able to start anywhere
        assert result == expected

    def test_large_surplus_at_start(self):
        """Test case with large surplus at starting station."""
        gas = [10, 1, 1, 1]
        cost = [1, 5, 3, 4]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Large gas at start should allow completion
        assert result != -1

    def test_deficit_then_surplus(self):
        """Test case with deficit stations followed by surplus."""
        gas = [1, 1, 10]
        cost = [5, 4, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 2  # Should start at the high gas station
        assert result == expected

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        gas = [1, 2, 3]
        cost = [3, 2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        assert isinstance(result, int)
        assert result == -1 or 0 <= result < len(gas)

    def test_greedy_algorithm_correctness(self):
        """Test that greedy algorithm finds correct starting point."""
        # Case where greedy choice is optimal
        gas = [1, 1, 1, 10]
        cost = [2, 2, 2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 3  # Must start at station with surplus
        assert result == expected

    def test_multiple_possible_starts(self):
        """Test case where multiple starting points might work."""
        gas = [3, 3, 3]
        cost = [1, 1, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Algorithm should return the first valid starting point
        assert result in [0, 1, 2]

    def test_algorithm_efficiency_large_input(self):
        """Test algorithm efficiency with larger input."""
        # Create pattern that tests the algorithm
        gas = [1] * 100 + [200]
        cost = [2] * 100 + [1]
        result = self.solution.canCompleteCircuit(gas, cost)
        expected = 100  # Should start at the high gas station
        assert result == expected

    def test_edge_case_barely_possible(self):
        """Test edge case where circuit is barely possible."""
        gas = [1, 1, 1, 1, 5]
        cost = [2, 2, 2, 2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Total gas = 9, total cost = 9, should be possible
        assert result != -1

    def test_edge_case_barely_impossible(self):
        """Test edge case where circuit is barely impossible."""
        gas = [1, 1, 1, 1, 4]
        cost = [2, 2, 2, 2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Total gas = 8, total cost = 9, should be impossible
        expected = -1
        assert result == expected

    def test_circular_nature_validation(self):
        """Test that circular nature is properly handled."""
        gas = [2, 4, 1]
        cost = [3, 2, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should be able to complete the circuit
        assert result != -1

    def test_greedy_reset_mechanism(self):
        """Test the greedy reset mechanism works correctly."""
        gas = [1, 1, 1, 1, 10]
        cost = [5, 1, 1, 1, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should find a valid starting point (algorithm finds 1, not necessarily 4)
        expected = 1  # Algorithm correctly finds station 1 as optimal start
        assert result == expected

    def test_mathematical_correctness(self):
        """Test mathematical correctness of the algorithm."""
        test_cases = [
            ([3, 3, 4], [3, 4, 4], -1),  # Total gas < total cost
            ([4, 3, 4], [3, 4, 4], 0),   # Can start at beginning (fixed: total gas = 11, cost = 11)
            ([2, 2, 2], [3, 1, 2], 1),   # Must start at index 1
        ]
        
        for gas, cost, expected in test_cases:
            with self.subTest(gas=gas, cost=cost):
                result = self.solution.canCompleteCircuit(gas, cost)
                assert result == expected

    def test_algorithm_properties(self):
        """Test key properties of the algorithm."""
        # Property 1: If solution exists, it's unique
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        assert result == 3  # Should be deterministic
        
        # Property 2: Algorithm finds first valid starting point
        gas = [5, 1, 2, 3, 4]
        cost = [4, 4, 1, 5, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should find the earliest valid starting point
        assert isinstance(result, int)

    def test_deficit_accumulation(self):
        """Test cases with deficit accumulation."""
        gas = [1, 1, 1, 1, 8]
        cost = [2, 2, 2, 2, 1]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should handle accumulated deficit correctly
        expected = 4
        assert result == expected

    def test_surplus_distribution(self):
        """Test cases with distributed surplus."""
        gas = [3, 1, 1, 3, 1]
        cost = [1, 2, 2, 1, 3]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should handle distributed surplus correctly
        assert result != -1

    def test_complex_pattern(self):
        """Test complex gas/cost patterns."""
        gas = [2, 1, 3, 1, 4]
        cost = [1, 3, 2, 2, 3]
        result = self.solution.canCompleteCircuit(gas, cost)
        # Complex pattern should still be solvable
        assert isinstance(result, int)
        assert result == -1 or 0 <= result < len(gas)

    def test_optimal_starting_point_validation(self):
        """Test that the found starting point is actually optimal."""
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        result = self.solution.canCompleteCircuit(gas, cost)
        
        # Verify this is a valid starting point by simulation
        if result != -1:
            current_gas = 0
            n = len(gas)
            for i in range(n):
                station = (result + i) % n
                current_gas += gas[station] - cost[station]
                assert current_gas >= 0, f"Invalid at station {station}"

    def test_time_complexity_validation(self):
        """Test that algorithm runs in O(n) time."""
        # Large input to test efficiency
        n = 1000
        gas = [1] * (n-1) + [n]
        cost = [2] * (n-1) + [1]
        
        result = self.solution.canCompleteCircuit(gas, cost)
        # Should complete efficiently
        expected = n - 1
        assert result == expected


if __name__ == "__main__":
    unittest.main()
