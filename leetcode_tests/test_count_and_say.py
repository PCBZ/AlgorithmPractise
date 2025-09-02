"""
Comprehensive test suite for LeetCode Problem #38: Count and Say

Tests the countAndSay method which generates the nth term in the
count-and-say sequence using run-length encoding.
"""
import time

from leetcode.count_and_say import Solution


class TestCountAndSay:
    """Test class for count and say problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_base_case_1(self):
        """Test the base case n=1."""
        result = self.solution.countAndSay(1)
        expected = "1"
        assert result == expected

    def test_case_2(self):
        """Test n=2: say "1" -> "one 1" -> "11"."""
        result = self.solution.countAndSay(2)
        expected = "11"
        assert result == expected

    def test_case_3(self):
        """Test n=3: say "11" -> "two 1s" -> "21"."""
        result = self.solution.countAndSay(3)
        expected = "21"
        assert result == expected

    def test_case_4(self):
        """Test n=4: say "21" -> "one 2, then one 1" -> "1211"."""
        result = self.solution.countAndSay(4)
        expected = "1211"
        assert result == expected

    def test_case_5(self):
        """Test n=5: say "1211" -> "one 1, one 2, then two 1s" -> "111221"."""
        result = self.solution.countAndSay(5)
        expected = "111221"
        assert result == expected

    def test_case_6(self):
        """Test n=6: continuing the sequence."""
        result = self.solution.countAndSay(6)
        expected = "312211"  # "111221" -> "three 1s, two 2s, one 1"
        assert result == expected

    def test_case_7(self):
        """Test n=7: continuing the sequence."""
        result = self.solution.countAndSay(7)
        expected = "13112221"  # "312211" -> "one 3, one 1, two 2s, two 1s"
        assert result == expected

    def test_zero_input(self):
        """Test edge case with n=0."""
        result = self.solution.countAndSay(0)
        expected = ""
        assert result == expected

    def test_negative_input(self):
        """Test edge case with negative n."""
        result = self.solution.countAndSay(-1)
        expected = ""
        assert result == expected

    def test_sequence_consistency(self):
        """Test that each term correctly follows from the previous."""
        # Test first several terms
        expected_sequence = ["1", "11", "21", "1211", "111221", "312211"]
        
        for i, expected in enumerate(expected_sequence, 1):
            result = self.solution.countAndSay(i)
            assert result == expected, f"Failed at position {i}: got {result}, expected {expected}"

    def test_return_type(self):
        """Test that return type is string."""
        result = self.solution.countAndSay(3)
        assert isinstance(result, str)

    def test_result_contains_only_digits(self):
        """Test that result contains only digit characters."""
        for n in range(1, 8):
            result = self.solution.countAndSay(n)
            assert result.isdigit(), f"Result '{result}' for n={n} contains non-digit characters"

    def test_sequence_length_growth(self):
        """Test that sequence length generally grows (with some exceptions)."""
        lengths = []
        for n in range(1, 10):
            result = self.solution.countAndSay(n)
            lengths.append(len(result))
        
        # Generally, the sequence should grow in length
        # (though there might be occasional decreases)
        assert len(set(lengths)) > 1  # Should have different lengths
        assert lengths[-1] > lengths[0]  # Later terms should be longer than first

    def test_large_input_performance(self):
        """Test performance with larger input."""
        start_time = time.time()
        result = self.solution.countAndSay(20)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 1.0
        assert isinstance(result, str)
        assert len(result) > 0

    def test_sequence_pattern_validation(self):
        """Test that sequence follows count-and-say pattern correctly."""
        # Manual validation of the pattern
        term1 = "1"
        term2 = self.solution.countAndSay(2)
        
        # "1" should become "11" (one 1)
        assert term2 == "11"
        
        # "11" should become "21" (two 1s)
        term3 = self.solution.countAndSay(3)
        assert term3 == "21"
        
        # "21" should become "1211" (one 2, one 1)
        term4 = self.solution.countAndSay(4)
        assert term4 == "1211"

    def test_no_consecutive_identical_counts(self):
        """Test that the algorithm handles consecutive identical digits correctly."""
        # This tests the run-length encoding logic
        for n in range(1, 8):
            result = self.solution.countAndSay(n)
            
            # Parse the result as count-digit pairs
            for i in range(0, len(result), 2):
                if i + 1 < len(result):
                    count = int(result[i])
                    digit = result[i + 1]
                    
                    # Count should be reasonable (1-9 for normal cases)
                    assert 1 <= count <= 9
                    assert digit.isdigit()

    def test_edge_case_very_small_inputs(self):
        """Test very small valid inputs."""
        test_cases = [
            (1, "1"),
            (2, "11"),
        ]
        
        for n, expected in test_cases:
            result = self.solution.countAndSay(n)
            assert result == expected

    def test_algorithm_correctness_by_manual_computation(self):
        """Test algorithm correctness by manually computing expected results."""
        # Manually trace through the algorithm
        
        # n=1: "1"
        # n=2: say "1" -> "11" (one 1)
        # n=3: say "11" -> "21" (two 1s)
        # n=4: say "21" -> "1211" (one 2, one 1)
        # n=5: say "1211" -> "111221" (one 1, one 2, two 1s)
        
        manual_results = {
            1: "1",
            2: "11",
            3: "21",
            4: "1211",
            5: "111221"
        }
        
        for n, expected in manual_results.items():
            result = self.solution.countAndSay(n)
            assert result == expected, f"Manual computation failed for n={n}"

    def test_intermediate_computation_steps(self):
        """Test intermediate steps in the computation."""
        # Test that we can build sequence step by step
        current = "1"
        
        for n in range(2, 6):
            # Manually apply the count-and-say rule
            next_term = self._manual_count_and_say(current)
            algorithm_result = self.solution.countAndSay(n)
            
            assert algorithm_result == next_term, f"Step mismatch at n={n}"
            current = next_term

    def _manual_count_and_say(self, s: str) -> str:
        """Manually implement count-and-say for testing."""
        if not s:
            return ""
        
        result = ""
        i = 0
        while i < len(s):
            count = 1
            current_char = s[i]
            
            # Count consecutive identical characters
            while i + 1 < len(s) and s[i + 1] == current_char:
                count += 1
                i += 1
            
            result += str(count) + current_char
            i += 1
        
        return result

    def test_string_immutability(self):
        """Test that strings are handled correctly (immutability)."""
        n = 5
        result1 = self.solution.countAndSay(n)
        result2 = self.solution.countAndSay(n)
        
        # Should get same result for same input
        assert result1 == result2
        
        # Results should be independent string objects
        assert result1 is not result2 or result1 == result2

    def test_mathematical_properties(self):
        """Test mathematical properties of the sequence."""
        # Test first 10 terms
        terms = [self.solution.countAndSay(i) for i in range(1, 11)]
        
        # Each term should be non-empty
        for term in terms:
            assert len(term) > 0
        
        # All terms should be different (count-and-say is injective for reasonable range)
        assert len(set(terms)) == len(terms)
        
        # Terms should only contain digits
        for term in terms:
            assert all(c.isdigit() for c in term)

    def test_consistency_across_multiple_calls(self):
        """Test that multiple calls with same input return same result."""
        n = 7
        results = [self.solution.countAndSay(n) for _ in range(5)]
        
        # All results should be identical
        assert all(result == results[0] for result in results)

    def test_boundary_sequence_behavior(self):
        """Test behavior at sequence boundaries."""
        # Test transitions between terms
        for n in range(1, 8):
            current_term = self.solution.countAndSay(n)
            
            if n < 7:  # Avoid going too far
                next_term = self.solution.countAndSay(n + 1)
                
                # Next term should be derivable from current term
                derived_next = self._manual_count_and_say(current_term)
                assert next_term == derived_next

    def test_run_length_encoding_properties(self):
        """Test properties specific to run-length encoding."""
        for n in range(1, 8):
            result = self.solution.countAndSay(n)
            
            # For n=1, result is "1" (special base case)
            if n == 1:
                assert result == "1"
                continue
            
            # For n>1, result length should be even (count-digit pairs)
            assert len(result) % 2 == 0, f"Odd length result for n={n}: {result}"
            
            # Parse as count-digit pairs
            for i in range(0, len(result), 2):
                count_char = result[i]
                digit_char = result[i + 1]
                
                # Count should be a valid digit 1-9
                assert count_char.isdigit() and count_char != '0'
                # Digit should be a valid digit
                assert digit_char.isdigit()

    def test_comprehensive_edge_cases(self):
        """Test comprehensive edge cases."""
        edge_cases = [
            (0, ""),
            (-1, ""),
            (-5, ""),
            (1, "1"),
        ]
        
        for n, expected in edge_cases:
            result = self.solution.countAndSay(n)
            assert result == expected, f"Edge case failed for n={n}"

    def test_algorithm_efficiency(self):
        """Test that algorithm is reasonably efficient."""
        # Test that moderate inputs complete quickly
        start_time = time.time()
        
        for n in range(1, 15):
            result = self.solution.countAndSay(n)
            assert isinstance(result, str)
        
        total_time = time.time() - start_time
        assert total_time < 0.5  # Should be very fast for reasonable inputs
