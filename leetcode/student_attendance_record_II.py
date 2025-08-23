"""
Student Attendance Record II - Dynamic Programming Solution.

This module contains a solution to determine the number of possible attendance 
records of length n that would be considered rewardable.
"""


class Solution:
    """Solution class for Student Attendance Record II problem."""

    def checkRecord(self, days: int) -> int:
        """
        Calculate number of rewardable attendance records.
        
        A student can be rewarded if:
        - The student was absent ('A') for strictly fewer than 2 days total
        - The student was never late ('L') for 3 or more consecutive days
        
        Args:
            days: The length of the attendance record
            
        Returns:
            Number of possible rewardable attendance records
        """
        MOD = 10**9 + 7
        # dp[day][absence][late]
        dp = [[[0] * 3 for _ in range(2)] for _ in range(days + 1)]
        dp[0][0][0] = 1
        for day in range(1, days + 1):
            for absence in range(2):
                for late in range(3):
                    prev_day = dp[day - 1][absence][late]
                    if prev_day == 0:
                        continue
                    # add present
                    dp[day][absence][0] = (dp[day][absence][0] + prev_day) % MOD
                    # add absence
                    if absence == 0:
                        dp[day][absence + 1][0] = (dp[day][absence + 1][0] + prev_day) % MOD
                    # add late
                    if late < 2:
                        dp[day][absence][late + 1] = (dp[day][absence][late + 1] + prev_day) % MOD

        return sum(dp[days][absence][late] for absence in range(2) for late in range(3)) % MOD


if __name__ == "__main__":
    test_days = 2
    print(Solution().checkRecord(test_days))  # Example usage
