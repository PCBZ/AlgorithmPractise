"""
Next Greater Element Problems - LeetCode Solutions

LeetCode #496: Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/

LeetCode #503: Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/

LeetCode #556: Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/

Comprehensive solutions for all Next Greater Element variants.
"""

from typing import List


class NextGreaterElementSolutions:
    """Solutions for Next Greater Element problems I, II, and III."""

    def next_greater_element_i(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find next greater element for nums1 elements in nums2.

        Time: O(n + m), Space: O(n)
        """
        next_greater_map = {}
        stack = []

        # Build next greater mapping for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_map[stack.pop()] = num
            stack.append(num)

        # Build result for nums1
        result = []
        for num in nums1:
            result.append(next_greater_map.get(num, -1))

        return result

    def next_greater_element_ii(self, nums: List[int]) -> List[int]:
        """
        Find next greater element in circular array.

        Time: O(n), Space: O(n)
        """
        n = len(nums)
        result = [-1] * n
        stack = []

        # Process array twice to handle circular nature
        for i in range(2 * n):
            curr_idx = i % n
            curr_val = nums[curr_idx]

            # Pop elements from stack that have found their next greater
            while stack and nums[stack[-1]] < curr_val:
                result[stack.pop()] = curr_val

            # Only add indices from first pass
            if i < n:
                stack.append(curr_idx)

        return result

    def next_greater_element_iii(self, n: int) -> int:
        """
        Find next greater element with same digits.

        Time: O(d log d), Space: O(d) where d is number of digits
        """
        digits = list(str(n))
        length = len(digits)

        # Find rightmost character smaller than its next character
        pivot = -1
        for i in range(length - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                pivot = i
                break

        # If no such character exists, no greater number possible
        if pivot == -1:
            return -1

        # Find smallest character on right of pivot greater than pivot
        successor = -1
        for i in range(length - 1, pivot, -1):
            if digits[i] > digits[pivot]:
                successor = i
                break

        # Swap pivot and successor
        digits[pivot], digits[successor] = digits[successor], digits[pivot]

        # Sort characters after pivot in ascending order
        digits[pivot + 1:] = sorted(digits[pivot + 1:])

        # Convert back to integer
        result = int(''.join(digits))

        # Check for 32-bit integer overflow
        return result if result <= 2**31 - 1 else -1


if __name__ == "__main__":
    solution = NextGreaterElementSolutions()

    # Test Next Greater Element I
    print("=== Next Greater Element I ===")
    NUMS1 = [4, 1, 2]
    NUMS2 = [1, 3, 4, 2]
    RESULT1 = solution.next_greater_element_i(NUMS1, NUMS2)
    print(f"nums1: {NUMS1}, nums2: {NUMS2}")
    print(f"Result: {RESULT1}")

    # Test Next Greater Element II
    print("\n=== Next Greater Element II ===")
    NUMS = [1, 2, 1]
    RESULT2 = solution.next_greater_element_ii(NUMS)
    print(f"nums: {NUMS}")
    print(f"Result: {RESULT2}")

    # Test Next Greater Element III
    print("\n=== Next Greater Element III ===")
    N = 12
    RESULT3 = solution.next_greater_element_iii(N)
    print(f"n: {N}")
    print(f"Result: {RESULT3}")

    N2 = 21
    RESULT4 = solution.next_greater_element_iii(N2)
    print(f"n: {N2}")
    print(f"Result: {RESULT4}")
