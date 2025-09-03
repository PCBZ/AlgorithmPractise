"""
LeetCode Problem #56: Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

URL: https://leetcode.com/problems/merge-intervals/

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) excluding the output array
"""
from typing import List


class Solution:
    """Solution for merging overlapping intervals."""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge all overlapping intervals.

        Args:
            intervals: List of intervals [start, end]

        Returns:
            List of merged non-overlapping intervals
        """
        if not intervals:
            return []

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged[-1]

            # If current interval overlaps with the last merged interval
            if current[0] <= last_merged[1]:
                # Merge by extending the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval to result
                merged.append(current)

        return merged


if __name__ == '__main__':
    TEST_INTERVALS = [[1, 4], [0, 4]]
    print(Solution().merge(TEST_INTERVALS))
