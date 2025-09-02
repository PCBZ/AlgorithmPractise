"""
LeetCode Problem #421: Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
where 0 <= i <= j < n.

URL: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

Time Complexity: O(n * 31) = O(n)
Space Complexity: O(n * 31) = O(n)
"""
from typing import List


class TrieNode:
    """Node for Trie data structure to store binary representation of numbers."""

    def __init__(self):
        """Initialize a new TrieNode."""
        self.left = None  # For bit 0
        self.right = None  # For bit 1


class Solution:
    """Solution for finding maximum XOR of two numbers in an array using Trie."""

    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        Find the maximum XOR of two numbers in the array.

        Uses a Trie to store binary representations of numbers and greedily
        construct the maximum XOR by choosing opposite bits when possible.

        Args:
            nums: List of integers to find maximum XOR from

        Returns:
            Maximum XOR value possible from any two numbers in the array
        """
        root = TrieNode()

        def add_number(num: int) -> None:
            """Add a number to the Trie in binary representation."""
            node = root
            for i in range(30, -1, -1):  # 31 bits (30 to 0)
                digit = (num >> i) & 1
                if digit == 0:
                    if not node.left:
                        node.left = TrieNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = TrieNode()
                    node = node.right

        def find_max_xor_with(num: int) -> int:
            """Find maximum XOR of num with any number in the Trie."""
            node = root
            result = 0
            for i in range(30, -1, -1):
                digit = (num >> i) & 1
                # Try to go in opposite direction for maximum XOR
                if digit == 0:
                    if node.right:  # Prefer bit 1 for maximum XOR
                        node = node.right
                        result = (result << 1) + 1
                    else:
                        node = node.left
                        result = result << 1
                else:
                    if node.left:  # Prefer bit 0 for maximum XOR
                        node = node.left
                        result = (result << 1) + 1
                    else:
                        node = node.right
                        result = result << 1
            return result

        max_xor = 0
        # First add all numbers to the Trie
        for num in nums:
            add_number(num)

        # Then find maximum XOR for each number
        for num in nums:
            max_xor = max(max_xor, find_max_xor_with(num))

        return max_xor


if __name__ == '__main__':
    test_nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR(test_nums))  # Expected: 28
