"""
LeetCode Problem #57: Insert Interval
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals sorted by start time,
insert a new interval and merge any overlapping intervals.
"""

from typing import List


class Solution:
    """Solution for Insert Interval problem."""

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Insert and merge overlapping intervals.
        Time: O(n), Space: O(1)
        """
        result = []

        for interval in intervals:
            if interval[1] < new_interval[0]:
                # No overlap - add interval
                result.append(interval)
            elif interval[0] > new_interval[1]:
                # No overlap - add new_interval and switch
                result.append(new_interval)
                new_interval = interval
            else:
                # Overlap - merge intervals
                new_interval[0] = min(interval[0], new_interval[0])
                new_interval[1] = max(interval[1], new_interval[1])

        result.append(new_interval)
        return result


if __name__ == '__main__':
    test_intervals = [[1, 3], [6, 9]]
    test_new_interval = [2, 5]
    print(Solution().insert(test_intervals, test_new_interval))  # [[1,5],[6,9]]
