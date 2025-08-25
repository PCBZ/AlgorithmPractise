"""
LeetCode Problem #204: Count Primes

URL: https://leetcode.com/problems/count-primes/

Given an integer n, return the number of prime numbers that are less than n.

A prime number is a natural number greater than 1 that has no positive divisors 
other than 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, 13, ...
"""


class Solution:
    """Solution for counting prime numbers using Sieve of Eratosthenes."""

    def countPrimes(self, number_limit: int) -> int:
        """
        Count prime numbers less than n using Sieve of Eratosthenes.

        The Sieve of Eratosthenes is an ancient algorithm for finding all
        prime numbers up to a given limit. It works by iteratively marking
        the multiples of each prime as composite.

        Args:
            number_limit: Upper limit (exclusive) for counting primes

        Returns:
            Number of prime numbers less than number_limit
        """
        if number_limit <= 2:
            return 0

        # Initialize all numbers as potentially prime
        is_prime = [True] * number_limit
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        count = 0
        for i in range(2, number_limit):
            if is_prime[i]:
                count += 1
                # Mark all multiples of i as composite
                # Start from i*i as smaller multiples already marked
                for multiple in range(i * i, number_limit, i):
                    is_prime[multiple] = False

        return count


if __name__ == "__main__":
    # Example test case
    test_n = 10
    solution = Solution()
    print(solution.countPrimes(test_n))
