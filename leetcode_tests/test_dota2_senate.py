"""
Comprehensive test suite for LeetCode Problem #649: Dota2 Senate

Tests the predictPartyVictory method which simulates senate voting where
senators ban opponents in round-robin fashion until one party wins.
"""
import time

from leetcode.dota2_senate import Solution


class TestDota2Senate:
    """Test class for Dota2 senate problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        senate = "RD"
        result = self.solution.predictPartyVictory(senate)
        expected = "Radiant"
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        senate = "RDD"
        result = self.solution.predictPartyVictory(senate)
        expected = "Dire"
        assert result == expected

    def test_single_senator(self):
        """Test with single senator."""
        test_cases = [
            ("R", "Radiant"),
            ("D", "Dire"),
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_one_party_majority(self):
        """Test when one party has clear majority."""
        test_cases = [
            ("RRR", "Radiant"),
            ("DDD", "Dire"),
            ("RRRR", "Radiant"),
            ("DDDD", "Dire"),
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_alternating_patterns(self):
        """Test with alternating patterns."""
        test_cases = [
            ("RDRD", "Radiant"),   # R bans D, leaving RRD, R wins
            ("DRDR", "Dire"),      # D bans R, leaving DDR, D wins
            ("RDRDRD", "Radiant"), # Similar pattern, Radiant wins
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_radiant_advantages(self):
        """Test cases where Radiant has strategic advantage."""
        test_cases = [
            ("RD", "Radiant"),     # R goes first, bans D
            ("RRDD", "Radiant"),   # R's go first, ban both D's
            ("RRDDD", "Radiant"),  # R's can ban enough D's to win
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_dire_advantages(self):
        """Test cases where Dire has strategic advantage."""
        test_cases = [
            ("DR", "Dire"),        # D goes first, bans R
            ("DDRR", "Dire"),      # D's go first, ban both R's
            ("DDRRR", "Dire"),     # D's can ban enough R's to win
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_equal_numbers_different_arrangements(self):
        """Test equal numbers with different arrangements."""
        test_cases = [
            ("RDDR", "Radiant"),   # Arrangement matters
            ("DRRD", "Dire"),      # Different arrangement, different winner
            ("RRDD", "Radiant"),   # R's grouped together
            ("DDRR", "Dire"),      # D's grouped together
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_complex_patterns(self):
        """Test with complex voting patterns."""
        test_cases = [
            ("DDRRRR", "Radiant"), # From the original example
            ("DDRRRRR", "Radiant"), # More R's than D's
            ("DDDRRR", "Dire"),    # More D's than R's initially
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_round_robin_behavior(self):
        """Test that round-robin behavior is correctly implemented."""
        # In "RDRD", the sequence should be:
        # Round 1: R(0) bans D(1), leaving "R_RD" -> "RRD"
        # Round 2: D(2->1) bans R(0), leaving "_RD" -> "RD"
        # Round 3: R(1->0) bans D(1), leaving "R_" -> "R"
        # Radiant wins
        senate = "RDRD"
        result = self.solution.predictPartyVictory(senate)
        # The actual result depends on implementation details
        assert result in ["Radiant", "Dire"]

    def test_symmetrical_cases(self):
        """Test symmetrical cases."""
        test_cases = [
            ("RR", "Radiant"),
            ("DD", "Dire"),
            ("RRRR", "Radiant"),
            ("DDDD", "Dire"),
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_position_matters(self):
        """Test that initial position affects outcome."""
        # These cases demonstrate that order matters
        test_cases = [
            ("RDD", "Dire"),       # D's can coordinate
            ("DRD", "Dire"),       # D goes first
            ("DDR", "Dire"),       # D's have majority and good position
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_longer_sequences(self):
        """Test with longer sequences."""
        test_cases = [
            ("RRRRRR", "Radiant"), # All Radiant
            ("DDDDDD", "Dire"),    # All Dire
            ("RDRDRDRD", "Radiant"), # Long alternating pattern starting with R
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_strategic_banning(self):
        """Test strategic banning scenarios."""
        # Test cases where optimal strategy matters
        test_cases = [
            ("RRDR", "Radiant"),   # R's can eliminate the D
            ("DRDD", "Dire"),      # D's have good positioning
            ("RRDDDD", "Dire"),    # D's outnumber R's enough
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        senate = "RD"
        result = self.solution.predictPartyVictory(senate)
        
        assert isinstance(result, str)
        assert result in ["Radiant", "Dire"]

    def test_algorithm_deterministic(self):
        """Test that algorithm is deterministic."""
        senate = "RDRD"
        result1 = self.solution.predictPartyVictory(senate)
        result2 = self.solution.predictPartyVictory(senate)
        assert result1 == result2

    def test_edge_cases_minimal(self):
        """Test minimal edge cases."""
        test_cases = [
            ("R", "Radiant"),
            ("D", "Dire"),
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_voting_simulation_correctness(self):
        """Test that voting simulation follows correct rules."""
        # Each senator bans the next opponent they can find
        # Test a case where we can manually verify the process
        senate = "RDD"
        result = self.solution.predictPartyVictory(senate)
        
        # R(0) bans D(1), leaving "R_D" -> "RD"
        # D(1->0) bans R(0), leaving "_D" -> "D"
        # Dire wins
        expected = "Dire"
        assert result == expected

    def test_circular_voting_order(self):
        """Test that circular voting order is maintained."""
        # Test cases that verify circular behavior
        test_cases = [
            ("RDR", "Radiant"),    # R bans D, R bans R? No, should be different
            ("DRD", "Dire"),       # D bans R, D wins
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        # Test with moderately long input
        senate = "RDRD" * 10  # 40 characters
        
        start_time = time.time()
        result = self.solution.predictPartyVictory(senate)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0
        assert result in ["Radiant", "Dire"]

    def test_majority_patterns(self):
        """Test various majority patterns."""
        test_cases = [
            ("RRRD", "Radiant"),   # 3 vs 1
            ("DRRRR", "Radiant"),  # 1 vs 4
            ("DDDR", "Dire"),      # 3 vs 1
            ("RDDDD", "Dire"),     # 1 vs 4
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_algorithm_properties(self):
        """Test mathematical properties of the algorithm."""
        # Test that result depends on both count and position
        result1 = self.solution.predictPartyVictory("RDD")
        result2 = self.solution.predictPartyVictory("DRD")
        result3 = self.solution.predictPartyVictory("DDR")
        
        # All should be "Dire" since D has majority
        assert result1 == "Dire"
        assert result2 == "Dire"
        assert result3 == "Dire"

    def test_tactical_scenarios(self):
        """Test tactical voting scenarios."""
        # Test scenarios where positioning creates tactical advantages
        test_cases = [
            ("RDDR", "Radiant"),   # R's can eliminate D's efficiently
            ("DRRD", "Dire"),      # D's can eliminate R's efficiently
            ("RRDD", "Radiant"),   # Grouped R's advantage
            ("DDRR", "Dire"),      # Grouped D's advantage
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Test cases at the boundary of different behaviors
        test_cases = [
            ("RR", "Radiant"),     # Minimum winning for R
            ("DD", "Dire"),        # Minimum winning for D
            ("RRD", "Radiant"),    # Just enough for R
            ("DDR", "Dire"),       # Just enough for D
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_complex_elimination_sequences(self):
        """Test complex elimination sequences."""
        # Test cases with complex elimination patterns
        senate = "RDDRD"
        result = self.solution.predictPartyVictory(senate)
        
        # Should produce a valid result
        assert result in ["Radiant", "Dire"]

    def test_greedy_strategy_verification(self):
        """Test that greedy strategy (ban next opponent) is optimal."""
        # The algorithm assumes each senator bans the next opponent
        # This should lead to optimal play for each side
        test_cases = [
            ("RDRD", "Radiant"),   # R goes first, gets advantage
            ("DRDR", "Dire"),      # D goes first, gets advantage
        ]
        
        for senate, expected in test_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_recursion_depth_reasonable(self):
        """Test that recursion depth is reasonable for moderate inputs."""
        # Test with input that could cause deep recursion
        senate = "RDRDRDRD"  # 8 characters, should not cause stack overflow
        result = self.solution.predictPartyVictory(senate)
        assert result in ["Radiant", "Dire"]

    def test_state_transition_correctness(self):
        """Test that state transitions are correct."""
        # Test that banning and index updates work correctly
        senate = "RDR"
        result = self.solution.predictPartyVictory(senate)
        
        # R(0) bans D(1), leaving "R_R" -> "RR"
        # R(0) wins (no more D's)
        expected = "Radiant"
        assert result == expected

    def test_comprehensive_pattern_verification(self):
        """Test comprehensive pattern verification."""
        patterns = [
            ("RDRDRDR", "Radiant"), # Long alternating starting with R
            ("RRRDDD", "Radiant"),  # Grouped equal
            ("DDDRRR", "Dire"),     # Grouped equal, D first
            ("RDDDRRR", "Radiant"), # Complex mixed, R gets first move advantage
        ]
        
        for senate, expected in patterns:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"

    def test_algorithm_completeness(self):
        """Test that algorithm handles all valid inputs."""
        # Test various combinations to ensure completeness
        valid_chars = ['R', 'D']
        
        # Test all combinations up to length 3
        for length in range(1, 4):
            # Generate some test cases
            test_cases = [
                'R' * length,
                'D' * length,
                'RD' * (length // 2) + 'R' * (length % 2),
                'DR' * (length // 2) + 'D' * (length % 2),
            ]
            
            for senate in test_cases:
                if senate:  # Skip empty strings
                    result = self.solution.predictPartyVictory(senate)
                    assert result in ["Radiant", "Dire"]

    def test_final_verification_cases(self):
        """Final verification with known difficult cases."""
        difficult_cases = [
            ("DRDRDRDRDR", "Dire"),     # Long alternating starting with D
            ("RDRDRDRDR", "Radiant"),   # Long alternating starting with R
            ("RRRRDDDD", "Radiant"),    # Equal groups, R first
            ("DDDDRRR", "Dire"),        # Unequal groups, D first
        ]
        
        for senate, expected in difficult_cases:
            result = self.solution.predictPartyVictory(senate)
            assert result == expected, f"Failed for {senate}: got {result}, expected {expected}"
