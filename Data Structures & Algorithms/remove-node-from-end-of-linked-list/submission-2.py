# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, cur = dummy, dummy.next
        dist = 1

        # Find the (n+1)-th node from the end
        while cur.next != None:
            if dist < n:
                dist += 1
            else:
                prev = prev.next
            cur = cur.next
        
        prev.next = prev.next.next
        return dummy.next