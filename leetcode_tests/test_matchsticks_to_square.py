"""
Test module for matchsticks to square problem (LeetCode #473).

Comprehensive test cases covering backtracking algorithm,
edge cases, and optimization strategies.
"""
import pytest
from leetcode.matchsticks_to_square import Solution


class TestMatchsticksToSquare:
    """Test class for matchsticks to square problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_cases(self):
        """Test LeetCode example cases."""
        test_cases = [
            ([1, 1, 2, 2, 2], True),  # Can form square with sides of length 2
            ([3, 3, 3, 3, 4], False),  # Cannot form square (total=16, not divisible by 4 evenly)
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_edge_cases(self):
        """Test edge cases."""
        test_cases = [
            ([], False),  # Empty array
            ([1], False),  # Single matchstick
            ([1, 2], False),  # Too few matchsticks
            ([1, 1, 1], False),  # Three matchsticks
            ([5, 5, 5, 5], True),  # Perfect square case
            ([1, 1, 1, 1], True),  # Minimum valid square
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_impossible_cases(self):
        """Test cases where forming a square is impossible."""
        test_cases = [
            ([1, 2, 3, 4, 5], False),  # Total=15, not divisible by 4
            ([1, 1, 1, 6], False),  # One stick too long (6 > 9/4=2.25)
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7], False),  # One stick too long
            ([2, 2, 2, 2, 2, 2], False),  # Total=12, but cannot arrange properly
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_valid_square_cases(self):
        """Test cases where forming a square is possible."""
        test_cases = [
            ([2, 2, 2, 2], True),  # Simple square
            ([1, 1, 1, 1, 2, 2, 2, 2], True),  # Mixed lengths, total 12, sides of 3
            ([1, 2, 1, 2, 1, 2, 1, 2], True),  # Each side gets [1,2,1], total 12, sides of 3  
            ([1, 1, 1, 1, 1, 1, 1, 1], True),  # All small sticks, total 8, sides of 2
            ([4, 4, 4, 4], True),  # Large square
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_complex_arrangements(self):
        """Test complex arrangements requiring backtracking."""
        test_cases = [
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),  # 12 unit sticks -> sides of 3
            ([2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1], True),  # Mixed pattern, total 16, sides of 4
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], False),  # 11 units + 1 two-unit = 13, not divisible by 4
            ([4, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),  # One large + many small, total 16, sides of 4
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_mathematical_properties(self):
        """Test mathematical properties of valid squares."""
        # Total length must be divisible by 4
        assert not self.solution.makesquare([1, 2, 3])  # Total = 6
        assert not self.solution.makesquare([1, 1, 1, 1, 1])  # Total = 5

        # No single stick can be longer than side length
        assert not self.solution.makesquare([1, 1, 1, 9])  # 9 > 12/4 = 3
        assert not self.solution.makesquare([8, 1, 1, 1, 1])  # 8 > 12/4 = 3

    def test_backtracking_efficiency(self):
        """Test that backtracking works efficiently with pruning."""
        # Cases designed to test pruning effectiveness
        test_cases = [
            ([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], False),  # Large stick that can't fit
            ([3, 3, 3, 3, 3, 3, 3, 3], True),  # Even distribution, total 24, sides of 6
            ([5, 5, 5, 5], True),  # Simple case, total 20, sides of 5
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_optimized_implementation_consistency(self):
        """Test that optimized implementation gives same results."""
        test_cases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
            [5, 5, 5, 5],
            [1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2],
            [1, 2, 1, 2, 1, 2, 1, 2],
        ]

        for matchsticks in test_cases:
            result1 = self.solution.makesquare(matchsticks)
            result2 = self.solution.makesquare_optimized(matchsticks)
            assert result1 == result2, f"Inconsistent results for {matchsticks}: basic={result1}, optimized={result2}"

    def test_iterative_implementation_consistency(self):
        """Test that iterative implementation gives same results for small inputs."""
        # Note: iterative approach is exponential, so test only small cases
        test_cases = [
            [1, 1, 2, 2, 2],
            [3, 3, 3, 3, 4],
            [5, 5, 5, 5],
            [1, 1, 1, 1],
            [2, 2, 2, 2],
        ]

        for matchsticks in test_cases:
            if len(matchsticks) <= 10:  # Only test small cases for iterative
                result1 = self.solution.makesquare(matchsticks)
                result2 = self.solution.makesquare_iterative(matchsticks)
                assert result1 == result2, f"Inconsistent results for {matchsticks}: backtrack={result1}, iterative={result2}"

    def test_duplicate_matchsticks(self):
        """Test cases with duplicate matchstick lengths."""
        test_cases = [
            ([2, 2, 2, 2], True),
            ([3, 3, 3, 3], True),
            ([1, 1, 1, 1, 1, 1, 1, 1], True),  # 8 sticks of length 1 -> sides of 2
            ([2, 2, 2, 2, 2, 2, 2, 2], True),  # 8 sticks of length 2 -> sides of 4
            ([5, 5, 5, 5, 5], False),  # Total = 25, not divisible by 4
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_large_matchstick_values(self):
        """Test with larger matchstick values."""
        test_cases = [
            ([100, 100, 100, 100], True),
            ([50, 50, 50, 50, 50, 50, 50, 50], True),  # Sides of 200
            ([1000, 1, 1, 1, 1], False),  # 1000 > 1004/4 = 251
            ([250, 250, 250, 250], True),
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        # Minimum case
        assert self.solution.makesquare([1, 1, 1, 1])

        # Correct boundary tests
        assert not self.solution.makesquare([1, 1, 2, 2])  # Total 6, not divisible by 4
        assert self.solution.makesquare([2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1])  # Total 16, sides of 4

    def test_sorting_independence(self):
        """Test that result is independent of input order."""
        base_sticks = [1, 2, 3, 2]
        import itertools

        # Test different permutations
        for perm in list(itertools.permutations(base_sticks))[:6]:  # Test first 6 permutations
            result = self.solution.makesquare(list(perm))
            # All permutations should give same result
            expected = self.solution.makesquare(base_sticks)
            assert result == expected, f"Permutation {perm} gave different result"

    def test_stress_cases(self):
        """Test cases that stress the backtracking algorithm."""
        # Case with many possibilities to explore
        matchsticks = [1] * 16  # 16 sticks of length 1, sides of 4 each
        assert self.solution.makesquare(matchsticks)

        # Case with forced early termination
        matchsticks = [1] * 15 + [8]  # 15 ones + one 8, total 23, not divisible by 4
        assert not self.solution.makesquare(matchsticks)

    def test_algorithm_correctness_verification(self):
        """Verify algorithm correctness with manual verification."""
        # Case 1: [1,1,2,2,2] -> True
        # Total = 8, side = 2
        # Possible arrangement: sides = [2,2], [2], [1,1], [2]
        matchsticks = [1, 1, 2, 2, 2]
        assert self.solution.makesquare(matchsticks)

        # Case 2: [3,3,3,3,4] -> False  
        # Total = 16, side = 4
        # Cannot fit the 4-length stick anywhere since each side should be exactly 4
        # Actually, wait - each side IS 4, so the stick of length 4 takes up one entire side
        # The remaining [3,3,3,3] has total 12, need to distribute into 3 sides of 4 each
        # That's impossible since 3+3 = 6 > 4
        matchsticks = [3, 3, 3, 3, 4]
        assert not self.solution.makesquare(matchsticks)

    def test_performance_characteristics(self):
        """Test performance characteristics."""
        # Test that algorithm completes in reasonable time for moderate input
        matchsticks = [1] * 12 + [2] * 6  # Total = 24, sides of 6
        result = self.solution.makesquare(matchsticks)
        assert isinstance(result, bool)  # Should complete and return boolean

        # Test early termination on impossible cases
        matchsticks = [1] * 100 + [1000]  # Clearly impossible
        assert not self.solution.makesquare(matchsticks)

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        test_cases = [
            # Minimum valid inputs
            ([1, 1, 1, 1], True),
            
            # Single large stick cases
            ([2, 1, 1, 1, 1, 1, 1], True),  # Total 8, sides of 2
            ([2, 2, 2, 2], True),  # Total 8, sides of 2
            ([6, 1, 1], False),  # Total 8, but 6 > 2
            
            # Exact fit cases
            ([4, 4, 4, 4], True),
            ([2, 2, 2, 2, 2, 2, 2, 2], True),
            
            # Near miss cases
            ([1, 1, 1, 2, 2, 2, 2], False),  # Total 11
            ([1, 1, 1, 1, 1, 1, 1], False),  # Total 7
        ]

        for matchsticks, expected in test_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"

    def test_final_verification_cases(self):
        """Final verification with additional challenging cases."""
        challenging_cases = [
            ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], True),  # 16 ones -> sides of 4
            ([2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], True),  # Mixed sizes
            ([3, 3, 4, 4, 5, 5], False),  # Total 24, sides of 6, but arrangement impossible
            ([6, 6, 6, 6], True),  # Simple large square
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),  # Total 55, not divisible by 4
        ]

        for matchsticks, expected in challenging_cases:
            result = self.solution.makesquare(matchsticks)
            assert result == expected, f"Failed for {matchsticks}: got {result}, expected {expected}"
