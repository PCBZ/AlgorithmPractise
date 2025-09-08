"""
LeetCode 131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

URL: https://leetcode.com/problems/palindrome-partitioning/
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str) -> bool:
            return s == s[::-1]
        n = len(s)
        def backTrace(s: str, start: int, path: List[str]):
            if start == n:
                res.append(path[:])
            for end in range(start+1, n+1):
                substr = s[start:end]
                if isPalindrome(substr):
                    path.append(substr)
                    backTrace(s, end, path)
                    path.pop()
        res = []
        backTrace(s, 0, [])
        return res

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1: Basic case with multiple palindrome possibilities
    s1 = "aab"
    result1 = solution.partition(s1)
    print(f"Input: '{s1}' -> Output: {result1}")
    
    # Example 2: Single character
    s2 = "a"
    result2 = solution.partition(s2)
    print(f"Input: '{s2}' -> Output: {result2}")
    
    # Example 3: String that is itself a palindrome
    s3 = "aba"
    result3 = solution.partition(s3)
    print(f"Input: '{s3}' -> Output: {result3}")
    
    # Example 4: All same characters
    s4 = "aaa"
    result4 = solution.partition(s4)
    print(f"Input: '{s4}' -> Output: {result4}")
    
    # Example 5: No palindromes except single characters
    s5 = "abc"
    result5 = solution.partition(s5)
    print(f"Input: '{s5}' -> Output: {result5}")

