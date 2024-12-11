# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        p = prev.next
        start = p
        rear = None
        for _ in range(right - left + 1):
            temp = p.next
            p.next = rear
            rear = p
            p = temp
        
        prev.next = rear
        start.next = p

        return dummy.next

if __name__ == '__main__':
    # begin
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.reverseBetween(head, 2, 4)
    while head:
        print(head.val)
        head = head.next