"""
LeetCode 486. Predict the Winner
Given an integer array nums, return true if Player 1 can win the game.

URL: https://leetcode.com/problems/predict-the-winner/
"""

from typing import List


class Solution:
    """Solution for Predict the Winner using recursive game theory."""

    def predictTheWinner(self, nums: List[int]) -> bool:
        """Determine if Player 1 can win the game with optimal play."""

        def helper(cur_nums: List[int], sum1: int, sum2: int, is_player1: bool) -> bool:
            """Recursive helper to simulate optimal game play."""
            # Base case: no numbers left
            if not cur_nums:
                return sum1 >= sum2

            # Base case: one number left
            if len(cur_nums) == 1:
                if is_player1:
                    return sum1 + cur_nums[0] >= sum2
                return sum1 < cur_nums[0] + sum2

            # Try taking from both ends
            nums_left = cur_nums[1:]  # Take first element
            nums_right = cur_nums[:-1]  # Take last element

            if is_player1:
                # Player 1 wins if either choice leads to opponent not winning
                take_first = not helper(nums_left, sum1 + cur_nums[0], sum2, False)
                take_last = not helper(nums_right, sum1 + cur_nums[-1], sum2, False)
                return take_first or take_last
            # Player 2 wins if either choice leads to opponent not winning
            take_first = not helper(nums_left, sum1, sum2 + cur_nums[0], True)
            take_last = not helper(nums_right, sum1, sum2 + cur_nums[-1], True)
            return take_first or take_last

        return helper(nums, 0, 0, True)


if __name__ == "__main__":
    solution = Solution()

    # Example 1: [1, 5, 2]
    nums1 = [1, 5, 2]
    result1 = solution.predictTheWinner(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print("Explanation: Player 1 can choose 2, then Player 2 must choose 1, then Player 1 gets 5.")
    print("Player 1: 2 + 5 = 7, Player 2: 1. Player 1 wins.")
    print()

    # Example 2: [1, 5, 233, 7]
    nums2 = [1, 5, 233, 7]
    result2 = solution.predictTheWinner(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print("Explanation: Player 1 cannot guarantee a win with optimal play.")
    print()

    # Example 3: [1, 1]
    nums3 = [1, 1]
    result3 = solution.predictTheWinner(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print("Explanation: Both players get equal scores, Player 1 wins ties.")
    print()
