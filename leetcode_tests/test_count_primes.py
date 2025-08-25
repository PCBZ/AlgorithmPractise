"""
Comprehensive test suite for LeetCode Problem #204: Count Primes

Tests the countPrimes method which counts prime numbers less than n
using the Sieve of Eratosthenes algorithm.
"""
import os
import sys
import time
import math

# Add the parent directory to sys.path to import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from leetcode.count_primes import Solution


class TestCountPrimes:
    """Test class for count primes problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example case 1."""
        n = 10
        result = self.solution.countPrimes(n)
        expected = 4  # Primes < 10: 2, 3, 5, 7
        assert result == expected

    def test_example_case_2(self):
        """Test LeetCode example case 2."""
        n = 0
        result = self.solution.countPrimes(n)
        expected = 0  # No primes < 0
        assert result == expected

    def test_example_case_3(self):
        """Test LeetCode example case 3."""
        n = 1
        result = self.solution.countPrimes(n)
        expected = 0  # No primes < 1
        assert result == expected

    def test_small_cases(self):
        """Test small input cases."""
        test_cases = [
            (2, 0),   # No primes < 2
            (3, 1),   # Primes < 3: 2
            (4, 2),   # Primes < 4: 2, 3
            (5, 2),   # Primes < 5: 2, 3
            (6, 3),   # Primes < 6: 2, 3, 5
            (7, 3),   # Primes < 7: 2, 3, 5
            (8, 4),   # Primes < 8: 2, 3, 5, 7
        ]
        
        for n, expected in test_cases:
            result = self.solution.countPrimes(n)
            assert result == expected, f"countPrimes({n}) = {result}, expected {expected}"

    def test_medium_cases(self):
        """Test medium-sized input cases."""
        test_cases = [
            (10, 4),   # Primes < 10: 2, 3, 5, 7
            (20, 8),   # Primes < 20: 2, 3, 5, 7, 11, 13, 17, 19
            (30, 10),  # Primes < 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
            (50, 15),  # First 15 primes are < 50
            (100, 25), # 25 primes < 100
        ]
        
        for n, expected in test_cases:
            result = self.solution.countPrimes(n)
            assert result == expected, f"countPrimes({n}) = {result}, expected {expected}"

    def test_prime_boundaries(self):
        """Test cases around prime number boundaries."""
        # Test around first few primes
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        
        for i, prime in enumerate(primes):
            # Count of primes < prime should be i
            result = self.solution.countPrimes(prime)
            assert result == i, f"countPrimes({prime}) = {result}, expected {i}"
            
            # Count of primes < prime+1 should be i+1
            result = self.solution.countPrimes(prime + 1)
            assert result == i + 1, f"countPrimes({prime + 1}) = {result}, expected {i + 1}"

    def test_algorithm_correctness_brute_force_comparison(self):
        """Test algorithm correctness by comparing with brute force approach."""
        def is_prime_brute_force(num):
            """Check if a number is prime using brute force."""
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
        
        def count_primes_brute_force(n):
            """Count primes using brute force method."""
            return sum(1 for i in range(2, n) if is_prime_brute_force(i))
        
        # Test for smaller values where brute force is feasible
        test_values = [0, 1, 2, 5, 10, 20, 50, 100]
        
        for n in test_values:
            sieve_result = self.solution.countPrimes(n)
            brute_force_result = count_primes_brute_force(n)
            assert sieve_result == brute_force_result, f"Mismatch for n={n}: sieve={sieve_result}, brute_force={brute_force_result}"

    def test_edge_cases(self):
        """Test edge cases."""
        edge_cases = [
            (0, 0),
            (1, 0),
            (2, 0),
            (-1, 0),  # Negative input
        ]
        
        for n, expected in edge_cases:
            result = self.solution.countPrimes(n)
            assert result == expected, f"countPrimes({n}) = {result}, expected {expected}"

    def test_return_type(self):
        """Test that return type is integer."""
        result = self.solution.countPrimes(10)
        assert isinstance(result, int)
        assert result >= 0  # Count should be non-negative

    def test_mathematical_properties(self):
        """Test mathematical properties of primes."""
        # Prime counting function π(n) is non-decreasing
        prev_count = 0
        for n in range(1, 51):
            current_count = self.solution.countPrimes(n)
            assert current_count >= prev_count, f"π({n}) = {current_count} < π({n-1}) = {prev_count}"
            prev_count = current_count

    def test_specific_known_values(self):
        """Test specific known values of prime counting function."""
        known_values = [
            (100, 25),    # π(100) = 25
            (200, 46),    # π(200) = 46
            (500, 95),    # π(500) = 95
            (1000, 168),  # π(1000) = 168
        ]
        
        for n, expected in known_values:
            result = self.solution.countPrimes(n)
            assert result == expected, f"π({n}) = {result}, expected {expected}"

    def test_performance_larger_input(self):
        """Test performance with larger input."""
        start_time = time.time()
        result = self.solution.countPrimes(10000)
        end_time = time.time()
        
        # Should complete within reasonable time
        assert end_time - start_time < 1.0
        
        # Verify known result
        assert result == 1229  # π(10000) = 1229

    def test_sieve_efficiency(self):
        """Test that the sieve is more efficient than naive approach."""
        # This is more of a performance test
        n = 5000
        
        start_time = time.time()
        result = self.solution.countPrimes(n)
        sieve_time = time.time() - start_time
        
        # Sieve should be very fast
        assert sieve_time < 0.5
        assert result == 669  # π(5000) = 669

    def test_memory_efficiency(self):
        """Test memory efficiency with reasonable input."""
        # Test that algorithm doesn't crash with larger inputs
        try:
            result = self.solution.countPrimes(50000)
            assert isinstance(result, int)
            assert result > 0
        except MemoryError:
            # If memory is limited, this is acceptable
            pass

    def test_algorithm_stability(self):
        """Test that algorithm produces consistent results."""
        n = 100
        
        # Run multiple times
        results = [self.solution.countPrimes(n) for _ in range(5)]
        
        # All results should be identical
        assert all(result == results[0] for result in results)

    def test_boundary_optimization(self):
        """Test the i*i optimization in the sieve."""
        # The algorithm should start marking multiples from i*i
        # This is tested implicitly, but we verify correctness
        test_cases = [
            (49, 15),   # 49 = 7^2, should handle this correctly
            (121, 30),  # 121 = 11^2
            (169, 39),  # 169 = 13^2
        ]
        
        for n, expected in test_cases:
            result = self.solution.countPrimes(n)
            assert result == expected

    def test_comprehensive_small_range(self):
        """Test comprehensive coverage of small range."""
        # Manual verification for first 30 numbers
        # Primes < 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
        expected_counts = [
            0,  # n=0
            0,  # n=1
            0,  # n=2
            1,  # n=3: [2]
            2,  # n=4: [2, 3]
            2,  # n=5: [2, 3]
            3,  # n=6: [2, 3, 5]
            3,  # n=7: [2, 3, 5]
            4,  # n=8: [2, 3, 5, 7]
            4,  # n=9: [2, 3, 5, 7]
            4,  # n=10: [2, 3, 5, 7]
            4,  # n=11: [2, 3, 5, 7]
            5,  # n=12: [2, 3, 5, 7, 11]
            5,  # n=13: [2, 3, 5, 7, 11]
            6,  # n=14: [2, 3, 5, 7, 11, 13]
            6,  # n=15: [2, 3, 5, 7, 11, 13]
            6,  # n=16: [2, 3, 5, 7, 11, 13]
            6,  # n=17: [2, 3, 5, 7, 11, 13]
            7,  # n=18: [2, 3, 5, 7, 11, 13, 17]
            7,  # n=19: [2, 3, 5, 7, 11, 13, 17]
            8,  # n=20: [2, 3, 5, 7, 11, 13, 17, 19]
        ]
        
        for n, expected in enumerate(expected_counts):
            result = self.solution.countPrimes(n)
            assert result == expected, f"countPrimes({n}) = {result}, expected {expected}"

    def test_large_primes_accuracy(self):
        """Test accuracy for larger prime counts."""
        # Test some larger known values
        large_test_cases = [
            (2000, 303),   # π(2000) = 303
            (3000, 430),   # π(3000) = 430
        ]
        
        for n, expected in large_test_cases:
            result = self.solution.countPrimes(n)
            assert result == expected, f"π({n}) = {result}, expected {expected}"

    def test_algorithmic_complexity(self):
        """Test that algorithm runs in expected time complexity."""
        # Test increasing sizes to verify O(n log log n) behavior
        sizes = [1000, 2000, 4000]
        times = []
        
        for size in sizes:
            start_time = time.time()
            self.solution.countPrimes(size)
            end_time = time.time()
            times.append(end_time - start_time)
        
        # All should complete quickly (actual complexity testing would be more sophisticated)
        assert all(t < 0.5 for t in times)

    def test_sieve_correctness_properties(self):
        """Test specific properties of Sieve of Eratosthenes."""
        # Test that multiples are correctly marked
        n = 50
        result = self.solution.countPrimes(n)
        
        # Should correctly identify first 15 primes < 50
        assert result == 15
        
        # Test that algorithm handles perfect squares correctly
        perfect_squares = [4, 9, 16, 25, 36, 49]
        for square in perfect_squares:
            # All perfect squares > 1 should be composite
            result = self.solution.countPrimes(square + 1)
            assert result >= 0  # Basic sanity check

    def test_input_validation_behavior(self):
        """Test behavior with various input types."""
        # Test with negative numbers
        assert self.solution.countPrimes(-5) == 0
        
        # Test with zero
        assert self.solution.countPrimes(0) == 0
        
        # Test with very small positive numbers
        assert self.solution.countPrimes(1) == 0
        assert self.solution.countPrimes(2) == 0
