"""
LeetCode Problem #315: Count of Smaller Numbers After Self

URL: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

Given an integer array nums, return an integer array counts where counts[i]
is the number of smaller elements to the right of nums[i].
"""
from typing import List


class TreeNode:
    """Binary Search Tree node for counting smaller elements."""

    def __init__(self, val):
        """
        Initialize a TreeNode.

        Args:
            val: The value of the node
        """
        self.val = val
        self.left = None
        self.right = None
        self.count = 1  # Count of nodes with this value
        self.left_size = 0  # Count of nodes in left subtree


class Solution:
    """Solution for counting smaller numbers after self using BST."""

    def countSmaller(self, number_list: List[int]) -> List[int]:
        """
        Count smaller numbers after each element using a BST approach.

        For each element, count how many elements to its right are smaller.
        Uses a Binary Search Tree built from right to left to efficiently
        count smaller elements.

        Args:
            number_list: List of integers

        Returns:
            List where each element is the count of smaller numbers to the right

        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(n) for the BST and result array
        """
        if not number_list:
            return []

        def insert_and_count(num: int, root: TreeNode) -> int:
            """
            Insert a number into BST and return count of smaller elements.

            Args:
                num: Number to insert
                root: Root of current subtree

            Returns:
                Count of smaller elements in the tree
            """
            if num < root.val:
                root.left_size += 1
                if not root.left:
                    root.left = TreeNode(num)
                    return 0
                return insert_and_count(num, root.left)
            if num > root.val:
                result = root.left_size + root.count
                if not root.right:
                    root.right = TreeNode(num)
                    return result
                return result + insert_and_count(num, root.right)
            # num == root.val
            root.count += 1
            return root.left_size

        # Process from right to left
        counts = [0]  # Last element has 0 smaller elements after it
        root = TreeNode(number_list[-1])
        n = len(number_list)

        for i in range(n - 2, -1, -1):
            count = insert_and_count(number_list[i], root)
            counts.insert(0, count)

        return counts


if __name__ == "__main__":
    test_nums = [2, 0, 1]
    solution = Solution()
    print(solution.countSmaller(test_nums))
