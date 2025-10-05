"""
LeetCode #907: Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/

Given an array of integers arr, find the sum of min(b), where b ranges over every
contiguous subarray of arr. Since the answer may be large, return it modulo 10^9 + 7.

Algorithm: Use monotonic stack to find nearest smaller elements on left and right
for each element. For each element, calculate how many subarrays it's the minimum of.
Time: O(N), Space: O(N)
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        Calculate sum of minimums of all subarrays using monotonic stack.
        
        For each element arr[i], we find:
        - left_less[i]: nearest smaller element index on the left
        - right_less[i]: nearest smaller element index on the right
        
        Then arr[i] is minimum in (i - left_less[i]) * (right_less[i] - i) subarrays.
        """
        n = len(arr)
        MOD = 10**9 + 7
        
        # Find nearest smaller element indices
        left_less = [-1] * n   # Index of nearest smaller element on left
        right_less = [n] * n   # Index of nearest smaller element on right
        
        # Use monotonic increasing stack to find left boundaries
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left_less[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Use monotonic increasing stack to find right boundaries
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Calculate sum of contributions
        result = 0
        for i in range(n):
            # Number of subarrays where arr[i] is minimum
            left_count = i - left_less[i]
            right_count = right_less[i] - i
            contribution = (arr[i] * left_count * right_count) % MOD
            result = (result + contribution) % MOD
            
        return result


if __name__ == "__main__":
    test_cases = [
        ([3, 1, 2, 4], 17),
        ([11, 81, 94, 43, 3], 444),
        ([1], 1),
        ([1, 2, 3, 4, 5], 35),
        ([5, 4, 3, 2, 1], 35),
        ([2, 9, 7, 8, 3, 4, 6, 1], 117),
    ]
    
    sol = Solution()
    for arr, expected in test_cases:
        result = sol.sumSubarrayMins(arr)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {arr}")
        print(f"   Output: {result} (Expected: {expected})\n")