from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        odd, even = dummy1, dummy2
        p, q = odd, even
        t, is_odd = head, True
        while t:
            if is_odd:
                p.next = t
                p = p.next
            else:
                q.next = t
                q = q.next
            is_odd = not is_odd
            t = t.next
        p.next = even.next
        q.next = None
        return odd.next

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = Solution().oddEvenList(head)
    while head:
        print(head.val)
        head = head.next