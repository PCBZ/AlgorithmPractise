"""
Test cases for LeetCode 60: Permutation Sequence
Testing both mathematical and brute force approaches.
"""

import pytest
from leetcode.permutation_sequence import Solution


class TestPermutationSequence:
    """Test cases for Permutation Sequence problem."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    # Example test cases from LeetCode
    def test_example_1(self):
        """Test n=3, k=3 -> '213'."""
        assert self.solution.getPermutation(3, 3) == "213"
    
    def test_example_2(self):
        """Test n=4, k=9 -> '2314'."""
        assert self.solution.getPermutation(4, 9) == "2314"
    
    def test_example_3(self):
        """Test n=3, k=1 -> '123'."""
        assert self.solution.getPermutation(3, 1) == "123"
    
    # Edge cases
    def test_single_element(self):
        """Test with n=1."""
        assert self.solution.getPermutation(1, 1) == "1"
    
    def test_first_permutation(self):
        """Test first permutation for various n values."""
        assert self.solution.getPermutation(2, 1) == "12"
        assert self.solution.getPermutation(3, 1) == "123"
        assert self.solution.getPermutation(4, 1) == "1234"
        assert self.solution.getPermutation(5, 1) == "12345"
    
    def test_last_permutation(self):
        """Test last permutation for various n values."""
        assert self.solution.getPermutation(2, 2) == "21"  # 2! = 2
        assert self.solution.getPermutation(3, 6) == "321"  # 3! = 6
        assert self.solution.getPermutation(4, 24) == "4321"  # 4! = 24
    
    # Systematic tests for n=3
    def test_all_permutations_n3(self):
        """Test all 6 permutations for n=3."""
        expected = ["123", "132", "213", "231", "312", "321"]
        for k in range(1, 7):  # 1-indexed
            result = self.solution.getPermutation(3, k)
            assert result == expected[k-1], f"Failed for n=3, k={k}"
    
    # Systematic tests for n=4 (selected cases)
    def test_n4_selected_cases(self):
        """Test selected cases for n=4 to verify correctness."""
        test_cases = [
            (4, 1, "1234"),   # First
            (4, 6, "1432"),   # End of first group
            (4, 7, "2134"),   # Start of second group
            (4, 12, "2431"),  # End of second group
            (4, 13, "3124"),  # Start of third group
            (4, 18, "3421"),  # End of third group
            (4, 19, "4123"),  # Start of fourth group
            (4, 24, "4321"),  # Last
        ]
        
        for n, k, expected in test_cases:
            result = self.solution.getPermutation(n, k)
            assert result == expected, f"Failed for n={n}, k={k}"
    
    # Larger values
    def test_larger_values(self):
        """Test with larger n values."""
        # n=5 test cases
        assert self.solution.getPermutation(5, 1) == "12345"
        assert self.solution.getPermutation(5, 24) == "15432"  # End of first group (24 permutations each)
        assert self.solution.getPermutation(5, 25) == "21345"  # Start of second group
        assert self.solution.getPermutation(5, 120) == "54321"  # Last permutation (5! = 120)
        
        # n=6 selected cases
        assert self.solution.getPermutation(6, 1) == "123456"
        assert self.solution.getPermutation(6, 720) == "654321"  # Last (6! = 720)
    
    # Boundary tests
    def test_boundaries(self):
        """Test boundary conditions."""
        # Second to last permutation
        assert self.solution.getPermutation(3, 5) == "312"
        assert self.solution.getPermutation(4, 23) == "4312"
        
        # Second permutation
        assert self.solution.getPermutation(3, 2) == "132"
        assert self.solution.getPermutation(4, 2) == "1243"
    
    # Consistency tests between both methods
    @pytest.mark.parametrize("n,k", [
        (1, 1), (2, 1), (2, 2), (3, 1), (3, 3), (3, 6),
        (4, 1), (4, 9), (4, 15), (4, 24), (5, 1), (5, 60), (5, 120)
    ])
    def test_consistency_between_methods(self, n, k):
        """Test that both mathematical and brute force methods give same results."""
        efficient_result = self.solution.getPermutation(n, k)
        brute_force_result = self.solution.getPermutationBruteForce(n, k)
        assert efficient_result == brute_force_result, \
            f"Methods disagree for n={n}, k={k}: {efficient_result} vs {brute_force_result}"
    
    # Pattern verification
    def test_lexicographic_order_pattern(self):
        """Verify that results follow lexicographic order."""
        n = 4
        previous_result = ""
        
        for k in range(1, 13):  # Test first half of permutations
            current_result = self.solution.getPermutation(n, k)
            if previous_result:
                assert current_result > previous_result, \
                    f"Lexicographic order violated: {previous_result} should come before {current_result}"
            previous_result = current_result
    
    # Performance comparison insight (not actual performance test)
    def test_algorithm_properties(self):
        """Test that algorithm properties hold."""
        # Mathematical approach should work for reasonable sizes
        result = self.solution.getPermutation(8, 20000)
        assert len(result) == 8
        assert all(c in "12345678" for c in result)
        assert len(set(result)) == 8  # All digits unique
    
    # Error handling (if implemented)
    def test_mathematical_precision(self):
        """Test mathematical precision for edge cases."""
        # Test middle permutations for various sizes
        test_cases = [
            (4, 12),  # Middle of 4! = 24
            (5, 60),  # Middle of 5! = 120
            (6, 360), # Middle of 6! = 720
        ]
        
        for n, k in test_cases:
            result = self.solution.getPermutation(n, k)
            # Basic validation
            assert len(result) == n
            assert len(set(result)) == n
            digits = set(str(i) for i in range(1, n + 1))
            assert set(result) == digits


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
