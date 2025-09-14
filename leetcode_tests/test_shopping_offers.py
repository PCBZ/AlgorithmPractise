"""
Comprehensive test suite for LeetCode 638: Shopping Offers.
"""

import pytest
from leetcode.shopping_offers import Solution


class TestShoppingOffers:
    """Test cases for the Shopping Offers problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    # Basic Examples
    def test_example_1(self):
        """Test example 1: Basic case with beneficial offers."""
        price = [2, 5]
        special = [[3, 0, 5], [1, 2, 10]]
        needs = [3, 2]
        # Optimal: use offer [3,0,5] once (5), then buy [0,2] individually (0*2 + 2*5 = 10)
        # Total: 5 + 10 = 15
        # Alternative: individual purchase would be 3*2 + 2*5 = 16
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 14  # Actually optimal is to use [1,2,10] once + [2,0] individually = 10 + 4 = 14

    def test_example_2(self):
        """Test example 2: No beneficial special offers."""
        price = [2, 3, 4]
        special = [[1, 1, 0, 4], [2, 2, 1, 9]]
        needs = [1, 2, 1]
        # Individual cost: 1*2 + 2*3 + 1*4 = 12
        # Special offers are not better than individual purchases
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 11  # Optimal combination

    # Edge Cases
    def test_empty_needs(self):
        """Test with no items needed."""
        price = [2, 5]
        special = [[3, 0, 5]]
        needs = [0, 0]
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 0

    def test_single_item(self):
        """Test with single item type."""
        price = [5]
        special = [[2, 8]]
        needs = [3]
        # Can use special offer once (2 items for 8) + 1 individual (5)
        # Total: 8 + 5 = 13 vs individual 3*5 = 15
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 13

    def test_no_special_offers(self):
        """Test with no special offers."""
        price = [2, 3, 4]
        special = []
        needs = [1, 2, 3]
        # Only individual purchases: 1*2 + 2*3 + 3*4 = 20
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 20

    def test_single_need(self):
        """Test with only one item needed."""
        price = [10, 5]
        special = [[1, 1, 12]]
        needs = [1, 0]
        # Individual: 1*10 = 10 vs special: not applicable since needs[1] = 0
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 10

    # Special Offer Validation
    def test_expensive_special_offers(self):
        """Test with special offers more expensive than individual purchases."""
        price = [2, 2]
        special = [[1, 1, 10]]  # More expensive than individual: 1*2 + 1*2 = 4 < 10
        needs = [2, 2]
        # Should ignore expensive offer and buy individually: 2*2 + 2*2 = 8
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 8

    def test_mixed_offer_quality(self):
        """Test with mix of good and bad special offers."""
        price = [3, 3]
        special = [[1, 1, 5], [1, 1, 10], [2, 0, 4]]  # First and third are good, second is bad
        needs = [2, 2]
        # Best strategy: use [2,0,4] once + [0,2] individually = 4 + 6 = 10
        # Or: use [1,1,5] twice = 10
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 10

    # Complex Combinations
    def test_multiple_offer_usage(self):
        """Test using the same offer multiple times."""
        price = [2, 2]
        special = [[1, 1, 1]]  # Very good offer
        needs = [5, 5]
        # Use the offer 5 times: 5 * 1 = 5
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 5

    def test_partial_offer_usage(self):
        """Test where offers can't fully satisfy needs."""
        price = [1, 1, 1]
        special = [[2, 2, 0, 3]]  # Buy 2 of first two items for 3
        needs = [3, 3, 1]
        # Use offer once (2,2,0 for 3) + individual (1,1,1 for 3) = 6
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 6

    def test_optimal_combination(self):
        """Test finding optimal combination of offers and individual purchases."""
        price = [2, 3, 1]
        special = [[1, 2, 0, 7], [0, 1, 1, 3]]
        needs = [2, 3, 2]
        # Need to find the optimal combination
        result = self.solution.shoppingOffers(price, special, needs)
        assert result <= 2*2 + 3*3 + 2*1  # Should be better than individual purchases

    # Large Scale Tests
    def test_large_needs(self):
        """Test with larger need quantities."""
        price = [1] * 6
        special = [[1, 1, 1, 1, 1, 1, 4]]  # Buy 6 items for 4 (vs 6 individually)
        needs = [10, 10, 10, 10, 10, 10]
        # Should use the offer multiple times
        result = self.solution.shoppingOffers(price, special, needs)
        expected_individual = sum(needs)  # 60
        assert result < expected_individual

    def test_many_special_offers(self):
        """Test with many special offers."""
        price = [2, 2]
        special = [[1, 1, 1], [1, 0, 1], [0, 1, 1], [2, 2, 3]]
        needs = [3, 3]
        # Should find the optimal combination among many offers
        result = self.solution.shoppingOffers(price, special, needs)
        assert result <= 3*2 + 3*2  # Should be better than individual

    # Edge Cases with Zero Values
    def test_zero_price_items(self):
        """Test with zero-price items."""
        price = [0, 5]
        special = [[1, 1, 3]]
        needs = [2, 1]
        # Individual: 2*0 + 1*5 = 5 vs special: 3 + remaining individual = 3 + 0 = 3
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 3

    def test_zero_cost_special_offer(self):
        """Test with zero-cost special offer."""
        price = [5, 5]
        special = [[1, 1, 0]]  # Free offer!
        needs = [2, 2]
        # Use free offer twice
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 0

    def test_zero_items_in_offer(self):
        """Test special offers that include zero of some items."""
        price = [3, 4, 5]
        special = [[0, 1, 2, 7], [1, 0, 1, 6]]
        needs = [1, 2, 2]
        result = self.solution.shoppingOffers(price, special, needs)
        expected_individual = 1*3 + 2*4 + 2*5  # 21
        assert result <= expected_individual

    # Performance and Stress Tests
    def test_maximum_constraints(self):
        """Test with maximum problem constraints."""
        # LeetCode constraints: at most 6 items, needs[i] <= 10
        price = [1, 2, 3, 4, 5, 6]
        special = [
            [1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 2],
            [1, 1, 1, 1, 1, 1, 15]
        ]
        needs = [5, 5, 5, 5, 5, 5]
        result = self.solution.shoppingOffers(price, special, needs)
        # Should complete efficiently and find optimal solution
        assert isinstance(result, int)
        assert result > 0

    def test_deep_recursion_case(self):
        """Test case that might cause deep recursion."""
        price = [1, 1]
        special = [[1, 0, 0]]  # Very cheap partial offer
        needs = [10, 1]
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 1  # Use special offer 10 times + 1 individual

    # Special Mathematical Cases
    def test_exactly_divisible_needs(self):
        """Test where needs are exactly divisible by offers."""
        price = [5, 5]
        special = [[2, 2, 8]]
        needs = [6, 6]
        # Use offer 3 times: 3 * 8 = 24 vs individual: 6*5 + 6*5 = 60
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 24

    def test_prime_number_needs(self):
        """Test with prime number needs (harder to optimize)."""
        price = [2, 3]
        special = [[2, 2, 5]]
        needs = [7, 7]  # Prime number
        # Can use offer 3 times (6,6 for 15) + individual (1,1 for 5) = 20
        # vs individual: 7*2 + 7*3 = 35
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 20

    # Boundary Value Tests
    def test_minimum_values(self):
        """Test with minimum possible values."""
        price = [1]
        special = [[1, 1]]
        needs = [1]
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 1

    def test_offer_equals_individual_cost(self):
        """Test where special offer cost equals individual cost."""
        price = [3, 3]
        special = [[1, 1, 6]]  # Same cost as individual: 1*3 + 1*3 = 6
        needs = [2, 2]
        # Either approach should give same result
        result = self.solution.shoppingOffers(price, special, needs)
        assert result == 12

    # Greedy vs Optimal Tests
    def test_greedy_trap(self):
        """Test case where greedy approach fails."""
        price = [1, 1, 1]
        special = [[1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
        needs = [2, 2, 2]
        # Greedy might not find optimal solution
        result = self.solution.shoppingOffers(price, special, needs)
        individual_cost = sum(needs[i] * price[i] for i in range(len(needs)))
        assert result <= individual_cost


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])