"""
LeetCode 400: Nth Digit
https://leetcode.com/problems/nth-digit/

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
"""


class Solution:
    """Solution for Nth Digit problem."""

    def findNthDigit(self, n: int) -> int:  # pylint: disable=invalid-name
        """Find nth digit in sequence 1234567891011121314..."""
        digit_count = 1
        range_count = 9
        prev_total = 0

        # Find digit group
        while n > prev_total + digit_count * range_count:
            prev_total += digit_count * range_count
            digit_count += 1
            range_count *= 10

        # Find specific number and digit
        first_num_in_group = 10 ** (digit_count - 1)
        number_index = (n - prev_total - 1) // digit_count
        digit_offset = (n - prev_total - 1) % digit_count

        target_number = first_num_in_group + number_index
        return int(str(target_number)[digit_offset])


if __name__ == "__main__":
    solution = Solution()
    print(solution.findNthDigit(1000))
