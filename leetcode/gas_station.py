"""
LeetCode Problem #134: Gas Station
URL: https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    """Solution for finding the starting gas station to complete circuit."""

    def canCompleteCircuit(self, gas_amounts: List[int], travel_costs: List[int]) -> int:
        """Find starting gas station index to complete the circuit.

        Use greedy approach: if we can't reach next station from current start,
        try starting from the next station instead.

        Args:
            gas_amounts: List of gas amounts at each station
            travel_costs: List of gas costs to travel to next station

        Returns:
            Starting station index, or -1 if impossible
        """
        n = len(gas_amounts)
        total_gas = sum(gas_amounts)
        total_cost = sum(travel_costs)

        # If total gas < total cost, impossible to complete circuit
        if total_gas < total_cost:
            return -1

        # Greedy approach: find the starting point
        current_gas = 0
        start_station = 0

        for i in range(n):
            # Add gas from current station and subtract cost to next station
            current_gas += gas_amounts[i] - travel_costs[i]

            # If we can't reach next station from current start
            if current_gas < 0:
                # Reset and try starting from next station
                current_gas = 0
                start_station = i + 1

        return start_station


if __name__ == "__main__":
    test_gas = [1, 2, 3, 4, 5]
    test_cost = [3, 4, 5, 1, 2]
    result = Solution().canCompleteCircuit(test_gas, test_cost)
    print(f"Gas: {test_gas}")
    print(f"Cost: {test_cost}")
    print(f"Starting station: {result}")
