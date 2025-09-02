"""
Comprehensive test suite for LeetCode Problem #115: Distinct Subsequences

Tests the numDistinct method which counts the number of distinct subsequences
of string s that equal string t using dynamic programming.
"""
import time

from leetcode.distinct_subsequence import Solution


class TestDistinctSubsequences:
    """Test class for distinct subsequences problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        source = "rabbbit"
        target = "rabbit"
        result = self.solution.numDistinct(source, target)
        expected = 3
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        source = "babgbag"
        target = "bag"
        result = self.solution.numDistinct(source, target)
        expected = 5
        assert result == expected

    def test_empty_strings(self):
        """Test with empty strings."""
        test_cases = [
            ("", "", 1),      # Empty target can be formed in 1 way
            ("a", "", 1),     # Empty target can be formed in 1 way
            ("abc", "", 1),   # Empty target can be formed in 1 way
            ("", "a", 0),     # Non-empty target cannot be formed from empty source
            ("", "abc", 0),   # Non-empty target cannot be formed from empty source
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_identical_strings(self):
        """Test with identical source and target strings."""
        test_cases = [
            ("a", "a", 1),
            ("ab", "ab", 1),
            ("abc", "abc", 1),
            ("hello", "hello", 1),
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_target_longer_than_source(self):
        """Test when target is longer than source."""
        test_cases = [
            ("a", "ab", 0),
            ("ab", "abc", 0),
            ("short", "longer", 0),
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_no_subsequence_possible(self):
        """Test when no subsequence is possible."""
        test_cases = [
            ("abc", "xyz", 0),
            ("hello", "world", 0),
            ("aaa", "b", 0),
            ("123", "456", 0),
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_single_character_patterns(self):
        """Test with single character patterns."""
        test_cases = [
            ("a", "a", 1),
            ("aa", "a", 2),     # Two ways to choose 'a'
            ("aaa", "a", 3),    # Three ways to choose 'a'
            ("aaaa", "a", 4),   # Four ways to choose 'a'
            ("abcd", "a", 1),   # One way to choose 'a'
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_repeated_characters_in_source(self):
        """Test with repeated characters in source."""
        test_cases = [
            ("aab", "ab", 2),     # Two ways: a[1]b, a[2]b (using different 'a's)
            ("aaab", "ab", 3),    # Three ways to choose 'a'
            ("abab", "ab", 3),    # Three ways: a[1]b[1], a[1]b[2], a[2]b[2]
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_repeated_characters_in_target(self):
        """Test with repeated characters in target."""
        test_cases = [
            ("abb", "bb", 1),     # Only one way to get "bb"
            ("abbb", "bb", 3),    # Three ways to choose 2 'b's from 3 'b's
            ("abbbb", "bb", 6),   # C(4,2) = 6 ways to choose 2 'b's from 4 'b's
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_complex_patterns(self):
        """Test with complex patterns."""
        test_cases = [
            ("abcabc", "abc", 4),  # Multiple ways to form "abc"
            ("aabbc", "abc", 4),   # Four ways to choose chars
            ("xyzabc", "abc", 1),  # Only one way at the end
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_mathematical_combinations(self):
        """Test cases that follow combinatorial patterns."""
        # When we have n identical characters and need to choose k,
        # the result should be C(n,k) if other constraints are satisfied
        test_cases = [
            ("aaaa", "aa", 6),    # C(4,2) = 6
            ("bbbbb", "bb", 10),  # C(5,2) = 10
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_prefix_suffix_patterns(self):
        """Test with prefix and suffix patterns."""
        test_cases = [
            ("abcdef", "ace", 1),   # One subsequence
            ("abcabc", "ac", 3),    # Three ways to choose 'a' and 'c'
            ("prefixsuffix", "fix", 5),  # Five ways to form "fix"
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_dynamic_programming_correctness(self):
        """Test that DP solution is working correctly."""
        # Test a case where we can manually verify the DP table
        source = "aba"
        target = "ab"
        result = self.solution.numDistinct(source, target)
        expected = 1  # Only one way: a[1]b[2]
        assert result == expected

    def test_order_preservation(self):
        """Test that subsequence order is preserved."""
        test_cases = [
            ("abc", "acb", 0),    # Order matters - can't form "acb" from "abc"
            ("abc", "cab", 0),    # Order matters
            ("abcba", "aba", 2),  # Two ways: a[1]b[2]a[5], a[1]b[4]a[5]
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_large_counts(self):
        """Test cases that produce large counts."""
        # Test case where many combinations are possible
        source = "aaabaaaba"
        target = "aaba"
        result = self.solution.numDistinct(source, target)
        
        # This should produce a reasonable count > 1
        assert result > 1
        assert isinstance(result, int)

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        source = "a" * 20 + "b" * 20
        target = "a" * 5 + "b" * 5
        
        start_time = time.time()
        result = self.solution.numDistinct(source, target)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0
        assert result > 0

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        source = "abc"
        target = "ab"
        result = self.solution.numDistinct(source, target)
        
        assert isinstance(result, int)
        assert result >= 0

    def test_algorithm_properties(self):
        """Test mathematical properties of the algorithm."""
        # Test deterministic behavior
        source = "abcabc"
        target = "abc"
        result1 = self.solution.numDistinct(source, target)
        result2 = self.solution.numDistinct(source, target)
        assert result1 == result2

    def test_boundary_conditions(self):
        """Test boundary conditions."""
        test_cases = [
            ("a", "a", 1),        # Minimal equal case
            ("ab", "a", 1),       # Target is prefix
            ("ab", "b", 1),       # Target is suffix
            ("abc", "c", 1),      # Target is last character
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_case_sensitivity(self):
        """Test that algorithm is case sensitive."""
        test_cases = [
            ("aA", "a", 1),       # Case sensitive
            ("Aa", "A", 1),       # Case sensitive
            ("aA", "A", 1),       # Case sensitive
            ("Aa", "a", 1),       # Case sensitive
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_consecutive_vs_non_consecutive(self):
        """Test difference between consecutive and non-consecutive subsequences."""
        test_cases = [
            ("abcd", "ac", 1),    # Non-consecutive subsequence
            ("aacc", "ac", 4),    # Four ways to form "ac"
            ("acac", "ac", 3),    # Three ways: a[1]c[2], a[1]c[4], a[3]c[4]
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_dp_table_properties(self):
        """Test properties of the DP table indirectly."""
        # Test that longer source always gives >= count of shorter source
        # when target is the same
        target = "ab"
        
        count1 = self.solution.numDistinct("ab", target)
        count2 = self.solution.numDistinct("aabb", target)
        count3 = self.solution.numDistinct("aaabbb", target)
        
        assert count1 <= count2 <= count3

    def test_manual_verification_cases(self):
        """Test cases with manually verified results."""
        # Manually verify "rabbbit" -> "rabbit"
        # r-a-b-b-b-i-t can form "rabbit" by:
        # 1. r-a-b[1]-b[2]-i-t (skip b[3])
        # 2. r-a-b[1]-b[3]-i-t (skip b[2]) 
        # 3. r-a-b[2]-b[3]-i-t (skip b[1])
        source = "rabbbit"
        target = "rabbit"
        result = self.solution.numDistinct(source, target)
        expected = 3
        assert result == expected

    def test_edge_case_all_same_characters(self):
        """Test with all same characters."""
        test_cases = [
            ("aaaa", "aa", 6),    # C(4,2) = 6
            ("bbbb", "b", 4),     # 4 ways to choose 1 'b' from 4
            ("cccc", "ccc", 4),   # C(4,3) = 4
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_alternating_patterns(self):
        """Test with alternating character patterns."""
        test_cases = [
            ("abab", "ab", 3),    # a[1]b[2], a[1]b[4], a[3]b[4]
            ("ababa", "aba", 4),  # Multiple ways to form "aba"
            ("bacab", "ab", 2),   # Two ways to get "ab"
        ]
        
        for source, target, expected in test_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"

    def test_stress_test_small(self):
        """Small stress test to ensure robustness."""
        sources = ["abcdefg", "aabbccdd", "abcabc", "xyzzyx"]
        targets = ["ace", "abc", "ab", "xyz"]
        
        for source in sources:
            for target in targets:
                result = self.solution.numDistinct(source, target)
                assert isinstance(result, int)
                assert result >= 0

    def test_memory_efficiency(self):
        """Test that algorithm handles reasonable inputs efficiently."""
        # Test with moderately sized inputs
        source = "abcdef" * 5  # 30 characters
        target = "ace"
        
        result = self.solution.numDistinct(source, target)
        assert isinstance(result, int)
        assert result > 0  # Should find at least some subsequences

    def test_correctness_verification(self):
        """Final correctness verification with known results."""
        verified_cases = [
            ("distinct", "dis", 1),
            ("programming", "gram", 2), 
            ("abcdefghijk", "ace", 1),
            ("aabbcc", "abc", 8),
        ]
        
        for source, target, expected in verified_cases:
            result = self.solution.numDistinct(source, target)
            assert result == expected, f"Failed for ({source}, {target}): got {result}, expected {expected}"
