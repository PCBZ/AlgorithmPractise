"""
LeetCode 143: Reorder List

Given the head of a singly linked list L0 → L1 → … → Ln-1 → Ln,
reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

URL: https://leetcode.com/problems/reorder-list/
"""

from typing import Optional


class ListNode:  # pylint: disable=too-few-public-methods
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):  # pylint: disable=redefined-builtin
        self.val = val
        self.next = next


class Solution:  # pylint: disable=too-few-public-methods
    """Solution for Reorder List using three-step approach."""

    def reorderList(self, head: Optional[ListNode]) -> None:  # pylint: disable=invalid-name
        """
        Reorder list in-place using three-step approach.
        
        Algorithm:
        1. Find middle of list using slow/fast pointers
        2. Reverse the second half of the list
        3. Merge the two halves alternately
        
        Time: O(n), Space: O(1)
        """
        if not head or not head.next:
            return

        # Step 1: Find middle using slow/fast pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split list and reverse second half
        second_half = slow.next
        slow.next = None
        reversed_second = self._reverse_list(second_half)

        # Step 3: Merge two halves alternately
        first_half = head
        while first_half and reversed_second:
            first_next = first_half.next
            second_next = reversed_second.next

            first_half.next = reversed_second
            reversed_second.next = first_next

            first_half = first_next
            reversed_second = second_next

    def _reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Reverse a linked list and return new head."""
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


def list_to_array(head: Optional[ListNode]) -> list:
    """Convert linked list to array for testing purposes."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # Test case 1: [1,2,3,4,5] -> [1,5,2,4,3]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList(head1)
    print(f"Test 1: {list_to_array(head1)}")

    # Test case 2: [1,2,3,4] -> [1,4,2,3]
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    Solution().reorderList(head2)
    print(f"Test 2: {list_to_array(head2)}")

    # Test case 3: [1,2] -> [1,2]
    head3 = ListNode(1, ListNode(2))
    Solution().reorderList(head3)
    print(f"Test 3: {list_to_array(head3)}")

    # Test case 4: [1] -> [1]
    head4 = ListNode(1)
    Solution().reorderList(head4)
    print(f"Test 4: {list_to_array(head4)}")
