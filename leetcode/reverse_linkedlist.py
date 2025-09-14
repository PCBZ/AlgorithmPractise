"""
LeetCode 206: Reverse Linked List
LeetCode 92: Reverse Linked List II

URL: https://leetcode.com/problems/reverse-linked-list/
URL: https://leetcode.com/problems/reverse-linked-list-ii/
"""
# pylint: disable=too-few-public-methods

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next_node=None):  # pylint: disable=redefined-builtin
        self.val = val
        self.next = next_node


class Solution:
    """Solutions for Reverse Linked List problems."""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  # pylint: disable=invalid-name
        """
        LeetCode 206: Reverse entire linked list.

        Time: O(n), Space: O(1)
        """
        prev = None
        current = head

        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp

        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  # pylint: disable=invalid-name
        """
        LeetCode 92: Reverse linked list between positions left and right.

        Time: O(n), Space: O(1)
        """
        # Create dummy node to handle edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        # Move to position before left
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing from left to right
        current = prev.next
        start = current
        reverse_prev = None

        for _ in range(right - left + 1):
            next_temp = current.next
            current.next = reverse_prev
            reverse_prev = current
            current = next_temp

        # Connect reversed section back
        prev.next = reverse_prev
        start.next = current

        return dummy.next


if __name__ == '__main__':
    sol = Solution()

    # Test LeetCode 206: Reverse entire list
    print("=== LeetCode 206: Reverse Linked List ===")
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = sol.reverseList(head1)
    print("Original: 1->2->3->4->5")
    print("Reversed: ", end="")
    while reversed_head:
        print(f"{reversed_head.val}", end="")
        if reversed_head.next:
            print("->", end="")
        reversed_head = reversed_head.next
    print()

    # Test LeetCode 92: Reverse between positions
    print("\n=== LeetCode 92: Reverse Linked List II ===")
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_between = sol.reverseBetween(head2, 2, 4)
    print("Original: 1->2->3->4->5")
    print("Reverse between positions 2-4: ", end="")
    while reversed_between:
        print(f"{reversed_between.val}", end="")
        if reversed_between.next:
            print("->", end="")
        reversed_between = reversed_between.next
    print()
