"""
LeetCode Problem #138: Copy List with Random Pointer

URL: https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n
brand new nodes, where each new node has its value set to the value of its
corresponding original node. Both the next and random pointers of the new
nodes should point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.
"""
from typing import Optional


class Node:
    """Definition for a Node in the linked list with random pointer."""

    def __init__(self, x: int, next_node: 'Node' = None, random: 'Node' = None):
        """
        Initialize a Node.

        Args:
            x: The value of the node
            next_node: The next node in the list
            random: A random pointer to any node in the list or None
        """
        self.val = int(x)
        self.next = next_node
        self.random = random


class Solution:
    """Solution for copying a linked list with random pointers."""

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Create a deep copy of the linked list with random pointers.

        Uses a hash map to track the mapping between original and copied nodes.

        Args:
            head: The head of the original linked list

        Returns:
            The head of the deep copied linked list

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for the hash map
        """
        if not head:
            return None

        # First pass: create all nodes and store mapping
        node_map = {}
        current = head
        while current:
            new_node = Node(current.val)
            node_map[current] = new_node
            current = current.next

        # Second pass: connect next and random pointers
        dummy = Node(-1)
        prev = dummy
        current = head
        while current:
            prev.next = node_map[current]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next
            prev = prev.next

        return dummy.next


if __name__ == "__main__":
    # Create test linked list: 7->13->11->10->1
    # Random pointers: 13->7, 11->1, 10->11, 1->7
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    # Connect next pointers
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Connect random pointers
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    # Test the solution
    solution = Solution()
    cloned_head = solution.copyRandomList(node1)

    # Print the cloned list
    current_node = cloned_head
    while current_node:
        if current_node.random:
            print(f"Node {current_node.val} -> Random: {current_node.random.val}")
        else:
            print(f"Node {current_node.val} -> Random: None")
        current_node = current_node.next
