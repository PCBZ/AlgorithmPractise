"""
LeetCode 148: Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (constant space)?

URL: https://leetcode.com/problems/sort-list/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    """Definition for singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Solution using merge sort algorithm."""
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort linked list using merge sort (divide and conquer).

        Time: O(n log n), Space: O(log n) due to recursion stack
        """
        # Base case: empty list or single node
        if not head or not head.next:
            return head

        # Find middle using slow/fast pointers (Floyd's algorithm)
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Split list into two halves
        second = slow
        prev.next = None  # Break the connection

        # Recursively sort both halves
        sorted_first = self.sortList(head)
        sorted_second = self.sortList(second)

        # Merge the two sorted halves
        dummy = ListNode(-1)
        p, q = sorted_first, sorted_second
        k = dummy
        while p and q:
            if p.val < q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        if p:
            k.next = p
        if q:
            k.next = q
        return dummy.next

    def merge_lists(self, list1: Optional[ListNode],
                   list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Helper method to merge two sorted linked lists (for testing compatibility).
        This uses the same merge logic as in sortList method.
        """
        dummy = ListNode(-1)
        p, q = list1, list2
        k = dummy
        while p and q:
            if p.val < q.val:
                k.next = p
                p = p.next
            else:
                k.next = q
                q = q.next
            k = k.next
        if p:
            k.next = p
        if q:
            k.next = q
        return dummy.next


# Helper functions for testing and examples
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Convert linked list to array for easy display."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Aliases for test compatibility
def list_to_array(head):
    """Convert linked list to array (alias for compatibility)."""
    return linked_list_to_array(head)


def array_to_list(values):
    """Convert array to linked list (alias for compatibility)."""
    return create_linked_list(values)


def print_linked_list(head, description=""):
    """Print linked list in a readable format."""
    values = linked_list_to_array(head)
    if description:
        print(f"{description}: {values}")
    else:
        print(values)


if __name__ == "__main__":
    solution = Solution()

    print("LeetCode 148: Sort List - Examples and Test Cases")
    print("=" * 60)

    # Example 1: LeetCode example [4,2,1,3]
    print("\n📝 Example 1: Standard unsorted list")
    input1 = [4, 2, 1, 3]
    head1 = create_linked_list(input1)
    print(f"Input:  {input1}")
    sorted_head1 = solution.sortList(head1)
    output1 = linked_list_to_array(sorted_head1)
    print(f"Output: {output1}")
    print("Explanation: The linked list is sorted in ascending order")

    # Example 2: LeetCode example [-1,5,3,4,0]
    print("\n📝 Example 2: List with negative numbers")
    input2 = [-1, 5, 3, 4, 0]
    head2 = create_linked_list(input2)
    print(f"Input:  {input2}")
    sorted_head2 = solution.sortList(head2)
    output2 = linked_list_to_array(sorted_head2)
    print(f"Output: {output2}")
    print("Explanation: Negative numbers are sorted to the beginning")

    # Example 3: Empty list
    print("\n📝 Example 3: Empty list edge case")
    input3 = []
    head3 = create_linked_list(input3)
    print(f"Input:  {input3}")
    sorted_head3 = solution.sortList(head3)
    output3 = linked_list_to_array(sorted_head3)
    print(f"Output: {output3}")
    print("Explanation: Empty list remains empty")

    # Example 4: Single element
    print("\n📝 Example 4: Single element")
    input4 = [42]
    head4 = create_linked_list(input4)
    print(f"Input:  {input4}")
    sorted_head4 = solution.sortList(head4)
    output4 = linked_list_to_array(sorted_head4)
    print(f"Output: {output4}")
    print("Explanation: Single element list is already sorted")

    # Example 5: Two elements
    print("\n📝 Example 5: Two elements needing swap")
    input5 = [2, 1]
    head5 = create_linked_list(input5)
    print(f"Input:  {input5}")
    sorted_head5 = solution.sortList(head5)
    output5 = linked_list_to_array(sorted_head5)
    print(f"Output: {output5}")
    print("Explanation: Two elements are swapped to correct order")

    # Example 6: Already sorted
    print("\n📝 Example 6: Already sorted list")
    input6 = [1, 2, 3, 4, 5]
    head6 = create_linked_list(input6)
    print(f"Input:  {input6}")
    sorted_head6 = solution.sortList(head6)
    output6 = linked_list_to_array(sorted_head6)
    print(f"Output: {output6}")
    print("Explanation: Already sorted list remains unchanged")

    # Example 7: Reverse sorted
    print("\n📝 Example 7: Reverse sorted list")
    input7 = [5, 4, 3, 2, 1]
    head7 = create_linked_list(input7)
    print(f"Input:  {input7}")
    sorted_head7 = solution.sortList(head7)
    output7 = linked_list_to_array(sorted_head7)
    print(f"Output: {output7}")
    print("Explanation: Completely reverses the order")

    # Example 8: Duplicates
    print("\n📝 Example 8: List with duplicate values")
    input8 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    head8 = create_linked_list(input8)
    print(f"Input:  {input8}")
    sorted_head8 = solution.sortList(head8)
    output8 = linked_list_to_array(sorted_head8)
    print(f"Output: {output8}")
    print("Explanation: Duplicates are kept together in sorted order")

    # Example 9: Large numbers and zeros
    print("\n📝 Example 9: Mix of large numbers and zeros")
    input9 = [0, 1000, 0, -1000, 500]
    head9 = create_linked_list(input9)
    print(f"Input:  {input9}")
    sorted_head9 = solution.sortList(head9)
    output9 = linked_list_to_array(sorted_head9)
    print(f"Output: {output9}")
    print("Explanation: Large range of values sorted correctly")

    # Example 10: All same elements
    print("\n📝 Example 10: All elements are the same")
    input10 = [7, 7, 7, 7, 7]
    head10 = create_linked_list(input10)
    print(f"Input:  {input10}")
    sorted_head10 = solution.sortList(head10)
    output10 = linked_list_to_array(sorted_head10)
    print(f"Output: {output10}")
    print("Explanation: All identical elements remain in same order")

    print("\n" + "=" * 60)
    print("✅ All examples completed successfully!")
    print("Algorithm: Merge Sort with O(n log n) time complexity")
    print("Space: O(log n) due to recursion stack")
