"""
LeetCode Problem #166: Fraction to Recurring Decimal
URL: https://leetcode.com/problems/fraction-to-recurring-decimal/
"""


class Solution:
    """Solution for converting fraction to decimal with recurring pattern detection."""

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """Convert fraction to decimal string with repeating pattern in parentheses.

        Uses long division algorithm with remainder tracking to detect cycles.

        Args:
            numerator: The numerator of the fraction
            denominator: The denominator of the fraction

        Returns:
            String representation of the decimal, with repeating part in parentheses
        """
        result = []

        # Handle negative sign - XOR to check if signs differ
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')

        # Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)

        # Get integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))
        remainder = numerator % denominator

        # If no remainder, return integer result
        if remainder == 0:
            return "".join(result)

        # Start decimal part
        result.append('.')
        remainder_map = {}  # Track remainder positions for cycle detection

        # Perform long division
        while remainder != 0:
            # If we've seen this remainder before, we found a cycle
            if remainder in remainder_map:
                cycle_start = remainder_map[remainder]
                result.insert(cycle_start, '(')
                result.append(')')
                break

            # Record this remainder's position
            remainder_map[remainder] = len(result)

            # Continue long division
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return "".join(result)


if __name__ == "__main__":
    test_numerator = 4
    test_denominator = 333
    output = Solution().fractionToDecimal(test_numerator, test_denominator)
    print(f"Fraction {test_numerator}/{test_denominator} = {output}")
