from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseLinkList(head: Optional[ListNode]) -> Optional[ListNode]:
            p = head
            q = head.next
            while q:
                temp = q.next
                q.next = p
                p = q
                q = temp
            head.next = None
            return p

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        reversed_second = reverseLinkList(second)
        p, q = head, reversed_second
        while p and q:
            temp = q.next
            q.next = p.next
            p.next = q
            p = q.next
            q = temp
        if q: 
            p.next = q
        return head

        
        

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
        
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().reorderList(head)
    print(list_to_array(head)) # [1, 5, 2, 4, 3]