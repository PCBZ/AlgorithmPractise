"""
LeetCode Problem #875: Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, and she can decide
her bananas-per-hour eating speed k. Each hour, she chooses a pile and eats k bananas.
If the pile has less than k bananas, she eats all and won't eat more bananas during that hour.
Return the minimum integer k such that she can eat all bananas within h hours.
"""

from typing import List
import math


class Solution:
    """Solution for Koko Eating Bananas problem."""

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find minimum eating speed using binary search.
        Time: O(n log max_pile), Space: O(1)
        """
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_needed = sum(math.ceil(pile / mid) for pile in piles)

            if hours_needed <= h:
                right = mid  # Try slower speed
            else:
                left = mid + 1  # Need faster speed

        return left


if __name__ == "__main__":
    test_piles = [30, 11, 23, 4, 20]
    test_h = 5
    print(Solution().minEatingSpeed(test_piles, test_h))
