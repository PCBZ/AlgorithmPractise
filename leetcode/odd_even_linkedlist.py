"""
LeetCode Problem: https://leetcode.com/problems/odd-even-linked-list/
328. Odd Even Linked List

Group odd-indexed nodes together, then even-indexed nodes.
Maintain relative order within each group. O(1) space, O(n) time.
"""

from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val: int = 0, next_node: Optional['ListNode'] = None):
        self.val = val
        self.next = next_node


class Solution:
    """Solution for LeetCode Problem 328: Odd Even Linked List."""

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Group odd/even nodes. Time: O(n), Space: O(1)"""
        if not head or not head.next:
            return head

        # Split chains
        odd_head = head
        even_head = head.next
        odd_tail = odd_head
        even_tail = even_head

        # Separate nodes
        current = even_head.next
        is_odd_position = True

        while current:
            if is_odd_position:
                odd_tail.next = current
                odd_tail = current
            else:
                even_tail.next = current
                even_tail = current

            current = current.next
            is_odd_position = not is_odd_position

        # Connect chains
        odd_tail.next = even_head
        even_tail.next = None

        return odd_head


def create_linked_list(node_values: list[int]) -> Optional[ListNode]:
    """Create linked list from values."""
    if not node_values:
        return None

    head = ListNode(node_values[0])
    current = head
    for val in node_values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def print_linked_list(list_head: Optional[ListNode]) -> None:
    """Print linked list values."""
    output_values = []
    current = list_head
    while current:
        output_values.append(str(current.val))
        current = current.next
    print(" -> ".join(output_values) if output_values else "Empty list")


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4, 5],      # Expected: [1, 3, 5, 2, 4]
        [2, 1, 3, 5, 6, 4, 7], # Expected: [2, 3, 6, 7, 1, 5, 4]
        [1],                   # Expected: [1]
        [1, 2],                # Expected: [1, 2]
        [],                    # Expected: []
    ]

    for i, test_values in enumerate(test_cases):
        test_head = create_linked_list(test_values)
        print(f"Test case {i+1}: {test_values}")
        result = solution.oddEvenList(test_head)
        print("Result: ", end="")
        print_linked_list(result)
        print()
