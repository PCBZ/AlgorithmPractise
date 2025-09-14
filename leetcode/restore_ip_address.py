"""
LeetCode 93: Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses
that can be obtained from s. You can return them in any order.

URL: https://leetcode.com/problems/restore-ip-addresses/
"""

from typing import List


class Solution:  # pylint: disable=too-few-public-methods
    """Solution for Restore IP Addresses using backtracking."""

    def restoreIpAddresses(self, s: str) -> List[str]:  # pylint: disable=invalid-name
        """
        Find all valid IP addresses from given string using backtracking.
        
        Time: O(3^4) = O(81), Space: O(1) excluding output
        """
        def is_valid_segment(segment: str) -> bool:
            """Check if segment is valid for IP address."""
            if not segment:
                return False

            # No leading zeros except "0"
            if len(segment) > 1 and segment[0] == '0':
                return False

            # Must be 0-255
            try:
                return 0 <= int(segment) <= 255
            except ValueError:
                return False

        def backtrack(start: int, segments: List[str]) -> None:
            """Backtrack to find all valid IP combinations."""
            # Base case: 4 segments and all chars used
            if len(segments) == 4:
                if start == len(s):
                    result.append('.'.join(segments))
                return

            # Try segment lengths 1, 2, 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                segment = s[start:start + length]
                if is_valid_segment(segment):
                    segments.append(segment)
                    backtrack(start + length, segments)
                    segments.pop()

        result = []
        backtrack(0, [])
        return result


if __name__ == "__main__":
    sol = Solution()

    # "25525511135" -> ["255.255.11.135","255.255.111.35"]
    result1 = sol.restoreIpAddresses("25525511135")
    print(f"Test 1: {result1}")

    # "0000" -> ["0.0.0.0"]
    result2 = sol.restoreIpAddresses("0000")
    print(f"Test 2: {result2}")

    # "101023" -> ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    result3 = sol.restoreIpAddresses("101023")
    print(f"Test 3: {result3}")

    # "1111" -> ["1.1.1.1"]
    result4 = sol.restoreIpAddresses("1111")
    print(f"Test 4: {result4}")
