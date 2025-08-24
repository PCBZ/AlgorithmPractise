"""
Test cases for Boats to Save People problem.
"""

import os
import sys

# Add the leetcode directory to the path for importing
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'leetcode'))

import pytest
from boats_to_save_people import Solution


class TestBoatsToSavePeople:
    """Test class for Boats to Save People solution."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def test_example_case_1(self):
        """Test the first example case."""
        # [1,5,3,5] with limit 7
        # After sorting: [1,3,5,5]
        # Boat 1: 1+5=6 <= 7 (take both)
        # Boat 2: 3+5=8 > 7, take 5 only
        # Boat 3: 3 only
        # Total: 3 boats
        people = [1, 5, 3, 5]
        limit = 7
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_example_case_2(self):
        """Test the second example case."""
        # [3,2,2,1] with limit 3
        # After sorting: [1,2,2,3]
        # Boat 1: 1+3=4 > 3, take 3 only
        # Boat 2: 1+2=3 <= 3 (take both)
        # Boat 3: 2 only
        # Total: 3 boats
        people = [3, 2, 2, 1]
        limit = 3
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_example_case_3(self):
        """Test the third example case."""
        # [3,5,3,4] with limit 5
        # After sorting: [3,3,4,5]
        # Boat 1: 3+5=8 > 5, take 5 only
        # Boat 2: 3+4=7 > 5, take 4 only
        # Boat 3: 3+3=6 > 5, take 3 only
        # Boat 4: 3 only
        # Total: 4 boats
        people = [3, 5, 3, 4]
        limit = 5
        assert self.solution.numRescueBoats(people, limit) == 4
    
    def test_single_person(self):
        """Test with a single person."""
        people = [5]
        limit = 10
        assert self.solution.numRescueBoats(people, limit) == 1
    
    def test_two_people_can_share(self):
        """Test with two people who can share a boat."""
        people = [2, 3]
        limit = 5
        assert self.solution.numRescueBoats(people, limit) == 1
    
    def test_two_people_cannot_share(self):
        """Test with two people who cannot share a boat."""
        people = [4, 5]
        limit = 6
        assert self.solution.numRescueBoats(people, limit) == 2
    
    def test_all_people_same_weight_can_pair(self):
        """Test when all people have same weight and can pair."""
        people = [2, 2, 2, 2]
        limit = 4
        assert self.solution.numRescueBoats(people, limit) == 2
    
    def test_all_people_same_weight_cannot_pair(self):
        """Test when all people have same weight and cannot pair."""
        people = [3, 3, 3, 3]
        limit = 5
        assert self.solution.numRescueBoats(people, limit) == 4
    
    def test_minimum_weight_people(self):
        """Test with people having minimum weight (1)."""
        people = [1, 1, 1, 1]
        limit = 2
        assert self.solution.numRescueBoats(people, limit) == 2
    
    def test_maximum_weight_people(self):
        """Test when people have maximum possible weight equal to limit."""
        people = [5, 5, 5]
        limit = 5
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_optimal_pairing(self):
        """Test optimal pairing strategy."""
        # [1,2,3,4,5] with limit 6
        # After sorting: [1,2,3,4,5]
        # Boat 1: 1+5=6 <= 6 (take both)
        # Boat 2: 2+4=6 <= 6 (take both)
        # Boat 3: 3 only
        # Total: 3 boats
        people = [1, 2, 3, 4, 5]
        limit = 6
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_no_pairing_possible(self):
        """Test when no pairing is possible."""
        people = [5, 5, 5, 5]
        limit = 8
        assert self.solution.numRescueBoats(people, limit) == 4
    
    def test_large_limit(self):
        """Test with very large limit allowing all pairings."""
        people = [1, 2, 3, 4, 5, 6]
        limit = 10
        # All pairs: (1,6), (2,5), (3,4) = 3 boats
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_edge_case_empty_list(self):
        """Test with empty people list."""
        people = []
        limit = 5
        assert self.solution.numRescueBoats(people, limit) == 0
    
    def test_alternating_weights(self):
        """Test with alternating light and heavy weights."""
        people = [1, 10, 1, 10, 1, 10]
        limit = 11
        # After sorting: [1,1,1,10,10,10]
        # Pairs: (1,10), (1,10), (1,10) = 3 boats
        assert self.solution.numRescueBoats(people, limit) == 3
    
    @pytest.mark.parametrize("people,limit,expected", [
        ([1, 5, 3, 5], 7, 3),
        ([3, 2, 2, 1], 3, 3),
        ([3, 5, 3, 4], 5, 4),
        ([1, 2], 3, 1),
        ([5, 5], 6, 2),
        ([1, 1, 1, 1], 2, 2),
        ([1, 2, 3, 4, 5], 6, 3),
    ])
    def test_parametrized_cases(self, people, limit, expected):
        """Parametrized test for multiple input-output pairs."""
        assert self.solution.numRescueBoats(people, limit) == expected
    
    def test_greedy_strategy_verification(self):
        """Test to verify the greedy strategy works optimally."""
        # The greedy approach: always try to pair lightest with heaviest
        people = [1, 4, 4, 5]
        limit = 5
        # After sorting: [1,4,4,5]
        # Boat 1: 1+5=6 > 5, take 5 only
        # Boat 2: 1+4=5 <= 5 (take both)
        # Boat 3: 4 only
        # Total: 3 boats
        assert self.solution.numRescueBoats(people, limit) == 3
    
    def test_return_type(self):
        """Test that the function returns an integer."""
        people = [1, 2, 3]
        limit = 5
        result = self.solution.numRescueBoats(people, limit)
        assert isinstance(result, int)
    
    def test_non_negative_result(self):
        """Test that the result is always non-negative."""
        test_cases = [
            ([1, 2, 3], 5),
            ([5, 5, 5], 5),
            ([], 10),
            ([1], 2)
        ]
        for people, limit in test_cases:
            result = self.solution.numRescueBoats(people, limit)
            assert result >= 0
    
    def test_result_bounds(self):
        """Test that result is within expected bounds."""
        # Number of boats should never exceed number of people
        test_cases = [
            ([1, 2, 3, 4], 5),
            ([5, 5, 5], 5),
            ([1, 1, 1, 1], 2)
        ]
        for people, limit in test_cases:
            result = self.solution.numRescueBoats(people, limit)
            assert result <= len(people)
            # Should be at least ceil(len(people)/2) boats
            assert result >= (len(people) + 1) // 2
    
    def test_input_modification(self):
        """Test that the original input list is modified (sorted)."""
        people = [5, 1, 3, 2]
        limit = 6
        original_people = people.copy()
        self.solution.numRescueBoats(people, limit)
        # The function should sort the input list
        assert people != original_people
        assert sorted(original_people) == people
    
    def test_large_input(self):
        """Test with a larger input to verify efficiency."""
        # Generate a larger test case
        people = list(range(1, 101))  # [1, 2, ..., 100]
        limit = 101
        result = self.solution.numRescueBoats(people, limit)
        # Should be able to pair most people optimally
        assert result == 50  # Each pair sums to 101


if __name__ == "__main__":
    # Run tests if script is executed directly
    pytest.main([__file__, "-v"])
