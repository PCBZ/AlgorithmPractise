"""
LeetCode Problem #592: Fraction Addition and Subtraction
URL: https://leetcode.com/problems/fraction-addition-and-subtraction/
"""
from math import gcd
from functools import reduce


def lcm(a, b):
    """Calculate least common multiple of two numbers."""
    return a * b // gcd(a, b)


class Solution:
    """Solution for fraction addition and subtraction."""

    def fractionAddition(self, expression_str: str) -> str:
        """Add and subtract fractions in the given expression.

        Parse the expression to extract numerators and denominators,
        then compute the result using common denominator approach.

        Args:
            expression_str: String containing fraction expression like "1/3-1/2"

        Returns:
            String representation of the result fraction in lowest terms
        """
        numerators, denominators = [], []
        sign = 1
        current_number = ''

        # Parse the expression character by character
        for idx, char in enumerate(expression_str):
            if char in ('+', '-'):
                # Found operator, save previous denominator if exists
                if current_number:
                    denominators.append(int(current_number))
                    current_number = ""
                # Set sign for next numerator
                sign = -1 if char == "-" else 1
            elif char == '/':
                # Found fraction bar, save numerator with sign
                numerators.append(int(current_number) * sign)
                current_number = ''
            else:
                # Build current number digit by digit
                current_number += char

            # Handle last denominator at end of expression
            if idx == len(expression_str) - 1:
                denominators.append(int(current_number))

        # Calculate LCM of all denominators
        common_denominator = reduce(lcm, denominators)

        # Convert all fractions to common denominator
        adjusted_numerators = [
            num * common_denominator // denominators[i]
            for i, num in enumerate(numerators)
        ]

        # Sum all numerators
        total_numerator = sum(adjusted_numerators)

        # Reduce to lowest terms using GCD
        result_gcd = gcd(abs(total_numerator), common_denominator)
        final_numerator = total_numerator // result_gcd
        final_denominator = common_denominator // result_gcd

        return f"{final_numerator}/{final_denominator}"


if __name__ == "__main__":
    test_expression = "1/3-1/2"
    result = Solution().fractionAddition(test_expression)
    print(f"Expression: {test_expression}")
    print(f"Result: {result}")
