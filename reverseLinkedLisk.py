# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        p = head
        while p:
            temp_next = p.next
            p.next = prev
            prev = p
            p = temp_next
        return prev


if __name__ == '__main__':
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.reverseBetween(head)
    while head:
        print(head.val)
        head = head.next