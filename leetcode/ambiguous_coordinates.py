"""
Ambiguous Coordinates - LeetCode Problem Solution
Source: https://leetcode.com/problems/ambiguous-coordinates/description/

Given a string representing parentheses and digits, return all possible
interpretations as coordinate pairs with possible decimal points.
"""

from typing import List


class Solution:
    """
    Solution class for the Ambiguous Coordinates problem.

    Generates all valid coordinate interpretations by placing decimal points
    in different positions while avoiding invalid number formats.
    """

    def ambiguousCoordinates(self, coordinate_str: str) -> List[str]:
        """
        Generate all possible coordinate interpretations.

        Args:
            coordinate_str: String in format "(digits)" to interpret as coordinates

        Returns:
            List of strings representing all valid coordinate interpretations
        """
        def get_possibles(t: str) -> List[str]:
            """Generate all valid number representations for a digit string."""
            res = []
            if t == format(float(t), "f").rstrip("0").rstrip("."):
                res.append(t)
            for i in range(len(t) - 1):
                n_t = t[:i+1] + "." + t[i+1:]
                if n_t == format(float(n_t), "f").rstrip("0").rstrip("."):
                    res.append(n_t)
            return res

        # Remove parentheses
        coordinate_str = coordinate_str[1:-1]
        res = []
        n = len(coordinate_str)

        # Try all possible splits between x and y coordinates
        for i in range(n - 1):
            for num1 in get_possibles(coordinate_str[:i+1]):
                for num2 in get_possibles(coordinate_str[i+1:]):
                    res.append(f"({num1}, {num2})")

        return res


if __name__ == "__main__":
    test_str = "(0000001)"
    print(Solution().ambiguousCoordinates(test_str))
    # test_str = "(00011)"
    # print(Solution().ambiguousCoordinates(test_str))
    # test_str = "(0123)"
    # print(Solution().ambiguousCoordinates(test_str))
    # test_str = "(100)"
    # print(Solution().ambiguousCoordinates(test_str))
