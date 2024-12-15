from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        p = head
        while p:
            new_node = Node(p.val)
            node_map[p] = new_node
            p = p.next
        dummy = Node(-1)
        prev = dummy
        p = head
        while p:
            prev.next = node_map[p]
            if p.random:
                node_map[p].random = node_map[p.random]
            p = p.next
            prev = prev.next
        return dummy.next

if __name__ == "__main__":
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    sol = Solution()
    cloned_head = sol.copyRandomList(node1)
    p = cloned_head
    while p:
        if p.random:
            print(p.val, p.random.val)
        else:
            print(p.val, None)
        p = p.next