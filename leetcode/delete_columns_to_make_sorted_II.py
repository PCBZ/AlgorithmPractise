"""
LeetCode #955: Delete Columns to Make Sorted II
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

We're given an array of N strings (each string has the same length), and we need to choose columns
to delete from the grid such that the remaining grid is lexicographically sorted.

Algorithm: Use a greedy approach with a sorted_flag array to track which adjacent rows are already
in sorted order to avoid unnecessary column deletions.

Time Complexity: O(m * n) where m is number of strings and n is string length
Space Complexity: O(m) for the sorted_flag array
"""

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        """
        Find minimum number of columns to delete to make rows lexicographically sorted.
        
        Args:
            strs: List of strings of equal length
            
        Returns:
            Minimum number of columns to delete
            
        Example:
            strs = ["ca", "bb", "ac"]
            After deleting column 0: ["a", "b", "c"] - sorted
            Return: 1
        """
        m, n = len(strs), len(strs[0])  # m strings, each of length n
        ans = 0  # Count of deleted columns
        sorted_flag = [False] * (m - 1)  # Track which adjacent pairs are sorted
        
        for i in range(n):  # Check each column
            need_delete = False
            
            # Check if current column breaks lexicographic order
            for j in range(m - 1):
                if not sorted_flag[j] and strs[j][i] > strs[j + 1][i]:
                    need_delete = True
                    break
            
            if need_delete:
                ans += 1
                continue  # Skip to next column
                
            # Update sorted_flag: mark pairs as sorted if current char is smaller
            for j in range(m - 1):
                if strs[j][i] < strs[j + 1][i]:
                    sorted_flag[j] = True
                    
        return ans


if __name__ == "__main__":
    test_strs = ["ca", "bb", "ac"]
    print(Solution().minDeletionSize(test_strs))