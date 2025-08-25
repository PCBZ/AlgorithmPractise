"""
LeetCode Problem #649: Dota2 Senate

URL: https://leetcode.com/problems/dota2-senate/

Simulate senate voting where senators ban opponents in round-robin fashion.
Example: "RD" -> "Radiant" (R bans D, R wins)
"""
from typing import List


class Solution:
    """Solution for predicting Dota2 senate victory using simulation."""

    def predictPartyVictory(self, senate_string: str) -> str:
        """
        Predict which party wins the senate voting.

        Senators vote in round-robin order, each banning the next
        opponent they encounter. The party with remaining senators wins.

        Args:
            senate_string: String of 'R' (Radiant) and 'D' (Dire) senators

        Returns:
            "Radiant" if Radiant wins, "Dire" if Dire wins
        """
        def simulate_victory(senators: List[str], current_index: int) -> str:
            """Recursively simulate the voting process."""
            if 'R' not in senators:
                return 'Dire'
            if 'D' not in senators:
                return 'Radiant'

            n = len(senators)
            current_senator = senators[current_index]

            # Find next opponent to ban
            for i in range(current_index + 1, current_index + n):
                target_index = i % n
                if senators[target_index] != current_senator:
                    break

            # Remove the banned senator
            del senators[target_index]

            # Calculate next senator's index
            if target_index < current_index:
                next_index = current_index % (n - 1)
            else:
                next_index = (current_index + 1) % (n - 1)

            return simulate_victory(senators, next_index)

        return simulate_victory(list(senate_string), 0)


if __name__ == "__main__":
    test_senate = "DDRRRR"
    print(Solution().predictPartyVictory(test_senate))
