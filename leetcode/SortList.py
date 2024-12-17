from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        slow = fast = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        second = slow
        prev.next = None
        sorted_first = self.sortList(head)
        sorted_second = self.sortList(second)

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

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
        
if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_res = Solution().sortList(head)
    print(list_to_array(sorted_res)) # [1, 2, 3, 4]