"""
LeetCode 638: Shopping Offers

You are given an integer array price where price[i] is the price of the ith item.
There are special offers where you can pay special[i][n] for a bundle of items.
Return the lowest price to buy exactly the required items using optimal special offers.

URL: https://leetcode.com/problems/shopping-offers/
"""

from typing import List, Tuple
from functools import lru_cache


class Solution:  # pylint: disable=too-few-public-methods
    """
    Solution for Shopping Offers using DFS with memoization.

    Approach:
    1. Filter out unprofitable special offers
    2. Use DFS with LRU cache to explore all combinations
    3. For each state, try individual purchases and all valid special offers
    4. Return minimum cost across all options
    """

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:  # pylint: disable=invalid-name
        """
        Find minimum cost to buy exactly the required items using special offers.

        Args:
            price: List of individual item prices
            special: List of special offers, each containing item quantities and total cost
            needs: List of required quantities for each item

        Returns:
            Minimum cost to fulfill all needs

        Time: O(k^n) where k is max items in needs, n is number of items
        Space: O(k^n) for memoization cache
        """
        n = len(needs)

        # Filter out unprofitable special offers
        valid_specials = []
        for offer in special:
            individual_cost = sum(price[i] * offer[i] for i in range(n))
            if offer[n] < individual_cost:
                valid_specials.append(offer)

        @lru_cache(maxsize=None)
        def dfs(current_needs: Tuple[int, ...]) -> int:
            """
            Find minimum cost for current needs state using DFS.

            Args:
                current_needs: Tuple of remaining item quantities needed

            Returns:
                Minimum cost to fulfill current needs
            """
            needs_list = list(current_needs)

            # Buy all remaining items individually
            min_cost = sum(price[i] * needs_list[i] for i in range(n))

            # Try each valid special offer
            for offer in valid_specials:
                # Check if offer is applicable
                if all(offer[i] <= needs_list[i] for i in range(n)):
                    new_needs = tuple(needs_list[i] - offer[i] for i in range(n))
                    total_cost = offer[n] + dfs(new_needs)
                    min_cost = min(min_cost, total_cost)

            return min_cost

        return dfs(tuple(needs))


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Basic example
    price1 = [2, 5]
    special1 = [[3, 0, 5], [1, 2, 10]]
    needs1 = [3, 2]
    result1 = sol.shoppingOffers(price1, special1, needs1)
    print(f"Test 1: price={price1}, special={special1}, needs={needs1}")
    print(f"Result: {result1}")
    print()

    # Test case 2: No beneficial special offers
    price2 = [2, 3, 4]
    special2 = [[1, 1, 0, 4], [2, 2, 1, 9]]
    needs2 = [1, 2, 1]
    result2 = sol.shoppingOffers(price2, special2, needs2)
    print(f"Test 2: price={price2}, special={special2}, needs={needs2}")
    print(f"Result: {result2}")
    print()

    # Test case 3: Multiple good offers
    price3 = [2, 2]
    special3 = [[1, 1, 1], [1, 1, 2]]
    needs3 = [10, 10]
    result3 = sol.shoppingOffers(price3, special3, needs3)
    print(f"Test 3: price={price3}, special={special3}, needs={needs3}")
    print(f"Result: {result3}")
    print()

    # Test case 4: Single item
    price4 = [5]
    special4 = [[2, 8]]
    needs4 = [3]
    result4 = sol.shoppingOffers(price4, special4, needs4)
    print(f"Test 4: price={price4}, special={special4}, needs={needs4}")
    print(f"Result: {result4}")
