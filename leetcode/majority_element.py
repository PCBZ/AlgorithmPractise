"""
LeetCode Problems #169 and #229: Majority Element I & II

URLs:
- #169: https://leetcode.com/problems/majority-element/
- #229: https://leetcode.com/problems/majority-element-ii/

Efficient solutions using Boyer-Moore voting algorithm for finding
majority elements (appearing > n/2 times or > n/3 times).
"""
from typing import List
from collections import Counter


class Solution:
    """Solution class for majority element problems using Boyer-Moore algorithm."""

    def majority_element(self, nums: List[int]) -> int:
        """
        Find the majority element that appears more than n/2 times.

        Uses Boyer-Moore voting algorithm to find the element in O(n) time
        and O(1) space. Guaranteed to find the majority element when it exists.

        Args:
            nums: Array of integers containing a majority element

        Returns:
            The majority element that appears more than n/2 times

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0

        candidate = nums[0]
        count = 1

        # Boyer-Moore voting phase
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = nums[i]
                    count = 1

        return candidate

    def majority_element_ii(self, nums: List[int]) -> List[int]:
        """
        Find all elements that appear more than n/3 times.

        Uses Boyer-Moore voting algorithm to find at most 2 candidates,
        then verifies which candidates actually appear > n/3 times.

        Args:
            nums: Array of integers

        Returns:
            List of elements appearing more than n/3 times

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return []

        # At most 2 elements can appear > n/3 times
        candidate1 = candidate2 = None
        count1 = count2 = 0

        # Boyer-Moore voting phase for 2 candidates
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Verification phase: check if candidates actually appear > n/3 times
        result = []
        threshold = len(nums) / 3
        if candidate1 is not None and nums.count(candidate1) > threshold:
            result.append(candidate1)
        if (candidate2 is not None and candidate2 != candidate1 and
                nums.count(candidate2) > threshold):
            result.append(candidate2)

        return result

    def majority_element_hashmap(self, nums: List[int]) -> int:
        """
        Alternative solution using hashmap for comparison.

        Args:
            nums: Array of integers

        Returns:
            The majority element

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        counts = Counter(nums)
        return max(counts, key=counts.get)

    def majority_element_ii_hashmap(self, nums: List[int]) -> List[int]:
        """
        Alternative solution using hashmap for comparison.

        Args:
            nums: Array of integers

        Returns:
            List of elements appearing more than n/3 times

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return []

        counts = Counter(nums)
        threshold = len(nums) / 3
        return [num for num, count in counts.items() if count > threshold]

    def majority_element_sorting(self, nums: List[int]) -> int:
        """
        Alternative solution using sorting for comparison.

        Args:
            nums: Array of integers

        Returns:
            The majority element

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0

        nums.sort()
        return nums[len(nums) // 2]


if __name__ == "__main__":
    solution = Solution()

    # Test majority element (appears > n/2 times)
    test_nums1 = [2, 2, 1, 1, 1, 2, 2]
    print(f"Majority element: {solution.majority_element(test_nums1)}")

    # Test majority elements (appear > n/3 times)
    test_nums2 = [1, 1, 3, 2, 2, 2, 3, 3, 1, 2, 1]
    print(f"Majority elements II: {solution.majority_element_ii(test_nums2)}")

    # Test with simpler case
    test_nums3 = [1, 2, 3, 1, 1]
    print(f"Majority elements II simple: {solution.majority_element_ii(test_nums3)}")
