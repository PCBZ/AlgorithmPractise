"""
LeetCode Problem #436: Find Right Interval
URL: https://leetcode.com/problems/find-right-interval/
"""
from typing import List


class Solution:
    """Solution for finding right intervals."""

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """Find the right interval for each interval."""
        n = len(intervals)

        # Create list of (start_time, original_index) pairs
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort()  # Sort by start time

        result = []
        for interval in intervals:
            end_time = interval[1]

            # Binary search for smallest start >= end_time
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if starts[mid][0] >= end_time:
                    right = mid
                else:
                    left = mid + 1

            # Check if found
            if left < n:
                result.append(starts[left][1])
            else:
                result.append(-1)

        return result


if __name__ == "__main__":
    # Example usage
    test_intervals = [[1, 2]]
    solution = Solution()
    right_intervals = solution.findRightInterval(test_intervals)
    print(f"Right intervals: {right_intervals}")
