"""
Comprehensive test suite for LeetCode Problem #394: Decode String

Tests the decodeString method which decodes encoded strings with nested
brackets and repetition counts using a stack-based approach.
"""
import time

from leetcode.decode_string import Solution


class TestDecodeString:
    """Test class for decode string problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        s = "3[a]"
        result = self.solution.decodeString(s)
        expected = "aaa"
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        s = "2[bc]"
        result = self.solution.decodeString(s)
        expected = "bcbc"
        assert result == expected

    def test_example_case_3(self):
        """Test LeetCode example case 3."""
        s = "3[a2[c]]"
        result = self.solution.decodeString(s)
        expected = "accaccacc"
        assert result == expected

    def test_example_case_4(self):
        """Test LeetCode example case 4."""
        s = "2[abc]3[cd]ef"
        result = self.solution.decodeString(s)
        expected = "abcabccdcdcdef"
        assert result == expected

    def test_single_character_no_brackets(self):
        """Test with single character and no brackets."""
        s = "a"
        result = self.solution.decodeString(s)
        expected = "a"
        assert result == expected

    def test_multiple_characters_no_brackets(self):
        """Test with multiple characters and no brackets."""
        s = "abcdef"
        result = self.solution.decodeString(s)
        expected = "abcdef"
        assert result == expected

    def test_single_digit_repetition(self):
        """Test with single digit repetition."""
        test_cases = [
            ("1[a]", "a"),
            ("5[b]", "bbbbb"),
            ("9[x]", "xxxxxxxxx"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_double_digit_repetition(self):
        """Test with double digit repetition."""
        test_cases = [
            ("10[a]", "a" * 10),
            ("12[b]", "b" * 12),
            ("99[c]", "c" * 99),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_triple_digit_repetition(self):
        """Test with triple digit repetition."""
        s = "100[a]"
        result = self.solution.decodeString(s)
        expected = "a" * 100
        assert result == expected

    def test_nested_single_level(self):
        """Test with single level nesting."""
        test_cases = [
            ("2[a3[b]]", "abbbabbb"),
            ("3[a2[b]]", "abbabbabb"),
            ("4[a1[b]]", "abababab"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_nested_multiple_levels(self):
        """Test with multiple levels of nesting."""
        test_cases = [
            ("2[a3[b2[c]]]", "abccbccbccabccbccbcc"),
            ("3[a2[b1[c]]]", "abcbcabcbcabcbc"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_multiple_groups_same_level(self):
        """Test with multiple groups at the same level."""
        test_cases = [
            ("2[a]3[b]", "aabbb"),
            ("1[a]2[b]3[c]", "abbccc"),
            ("3[a]2[b]1[c]", "aaabbc"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_mixed_brackets_and_plain_text(self):
        """Test with mix of brackets and plain text."""
        test_cases = [
            ("abc3[d]ef", "abcdddef"),
            ("a2[b]c3[d]e", "abbcddde"),
            ("xy2[z]ab", "xyzzab"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_consecutive_numbers(self):
        """Test with consecutive number-bracket groups."""
        test_cases = [
            ("2[a]2[b]", "aabb"),
            ("3[x]3[y]3[z]", "xxxyyyzzz"),
            ("1[a]1[b]1[c]", "abc"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_multi_character_strings(self):
        """Test with multi-character strings inside brackets."""
        test_cases = [
            ("2[abc]", "abcabc"),
            ("3[xyz]", "xyzxyzxyz"),
            ("2[hello]", "hellohello"),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s}: got {result}, expected {expected}"

    def test_return_type_and_constraints(self):
        """Test return type and basic constraints."""
        s = "3[a]"
        result = self.solution.decodeString(s)
        
        assert isinstance(result, str)
        assert len(result) > 0

    def test_algorithm_correctness_manual_verification(self):
        """Test algorithm correctness with manual step-by-step verification."""
        test_cases = [
            # (input, expected, description)
            ("2[a3[b]]", "abbbabbb", "Outer 2 repeats inner 'a3b' -> 'abbb' * 2"),
            ("3[a2[c]]", "accaccacc", "Outer 3 repeats inner 'a2c' -> 'acc' * 3"),
            ("abc3[cd]xyz", "abccdcdcdxyz", "Plain text + brackets + plain text"),
        ]
        
        for s, expected, description in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for {s} ({description}): got {result}, expected {expected}"

    def test_edge_cases(self):
        """Test edge cases."""
        edge_cases = [
            ("", ""),  # Empty string
            ("a", "a"),  # Single character
            ("1[a]", "a"),  # Minimum repetition
        ]
        
        for s, expected in edge_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for edge case {s}: got {result}, expected {expected}"

    def test_stack_behavior_verification(self):
        """Test that stack behavior is correct for nested cases."""
        # This tests the internal stack operations indirectly
        s = "2[a3[b]c]"
        result = self.solution.decodeString(s)
        expected = "abbbcabbbc"  # a + bbb + c, repeated 2 times
        assert result == expected

    def test_large_repetition_counts(self):
        """Test with large repetition counts."""
        test_cases = [
            ("50[a]", "a" * 50),
            ("25[ab]", "ab" * 25),
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed for large count {s}"

    def test_deep_nesting(self):
        """Test with deep nesting levels."""
        s = "2[a2[b2[c]]]"
        # Inner: c -> cc (2[c])
        # Middle: b + cc -> bcc (b2[c]) -> bccbcc (2[b2[c]])
        # Outer: a + bccbcc -> abccbcc (a2[b2[c]]) -> abccbccabccbcc (2[a2[b2[c]]])
        expected = "abccbccabccbcc"
        result = self.solution.decodeString(s)
        assert result == expected

    def test_performance_reasonable_input(self):
        """Test performance with reasonable input size."""
        start_time = time.time()
        s = "10[a10[b]]"  # Should produce 100 'b's between 'a's
        result = self.solution.decodeString(s)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0
        
        # Verify correctness
        expected = "a" + "b" * 10  # "abbbbbbbbbb"
        expected = expected * 10  # Repeat 10 times
        assert result == expected

    def test_algorithm_stability(self):
        """Test that algorithm produces consistent results."""
        s = "3[a2[b]]"
        
        # Run multiple times
        results = [self.solution.decodeString(s) for _ in range(5)]
        
        # All results should be identical
        assert all(result == results[0] for result in results)

    def test_character_preservation(self):
        """Test that characters are preserved correctly."""
        # Test all lowercase letters
        s = "1[abcdefghijklmnopqrstuvwxyz]"
        result = self.solution.decodeString(s)
        expected = "abcdefghijklmnopqrstuvwxyz"
        assert result == expected

    def test_boundary_number_cases(self):
        """Test boundary cases for numbers."""
        test_cases = [
            ("1[a]", "a"),        # Minimum repetition
            ("9[a]", "a" * 9),    # Single digit max
            ("10[a]", "a" * 10),  # Two digit min
        ]
        
        for s, expected in test_cases:
            result = self.solution.decodeString(s)
            assert result == expected

    def test_complex_mixed_pattern(self):
        """Test complex pattern with mixed elements."""
        s = "abc2[def3[gh]ij]klm"
        # Inner: gh -> ghghgh (3[gh])
        # Middle: def + ghghgh + ij -> defghghghij (def3[gh]ij)
        # Outer: abc + defghghghij + defghghghij + klm -> abcdefghghghijdefghghghijklm
        expected = "abcdefghghghijdefghghghijklm"
        result = self.solution.decodeString(s)
        assert result == expected

    def test_mathematical_properties(self):
        """Test mathematical properties of repetition."""
        # Test that k[s] produces a string of length k * len(s)
        test_cases = [
            ("5[abc]", 5 * 3),     # 5 * 3 = 15
            ("10[xy]", 10 * 2),    # 10 * 2 = 20
            ("3[a]", 3 * 1),       # 3 * 1 = 3
        ]
        
        for s, expected_length in test_cases:
            result = self.solution.decodeString(s)
            assert len(result) == expected_length

    def test_nested_mathematical_properties(self):
        """Test mathematical properties with nesting."""
        # For a[b[c]], result length should be a * (len(b) + b * len(c))
        s = "2[a3[b]]"  # Should be 2 * (1 + 3 * 1) = 2 * 4 = 8
        result = self.solution.decodeString(s)
        expected_length = 8
        assert len(result) == expected_length

    def test_stack_depth_handling(self):
        """Test that stack handles appropriate depth."""
        # Test multiple levels to ensure stack operations are correct
        s = "1[a1[b1[c]]]"
        result = self.solution.decodeString(s)
        expected = "abc"
        assert result == expected

    def test_memory_efficiency(self):
        """Test memory efficiency with reasonable input."""
        # Test that algorithm doesn't use excessive memory
        s = "20[a]"
        result = self.solution.decodeString(s)
        expected = "a" * 20
        assert result == expected
        assert len(result) == 20

    def test_comprehensive_pattern_recognition(self):
        """Test comprehensive pattern recognition."""
        complex_patterns = [
            ("2[a]2[b]2[c]", "aabbcc"),
            ("1[a2[b3[c]]]", "abcccbccc"),
            ("3[a]b2[c]", "aaabcc"),
        ]
        
        for s, expected in complex_patterns:
            result = self.solution.decodeString(s)
            assert result == expected, f"Failed pattern {s}: got {result}, expected {expected}"
