from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        p = head
        while p:
            if p.next and p.val == p.next.val:
                while p.next and p.val == p.next.val:
                    p = p.next
                prev.next = p.next
            else:
                prev = prev.next
            p = p.next
        return dummy.next

            
if __name__ == '__main__':
    # begin
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    head = s.deleteDuplicates(head)
    while head:
        print(head.val)
        head = head.next