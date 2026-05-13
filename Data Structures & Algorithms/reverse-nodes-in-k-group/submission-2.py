# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        
        dummy = ListNode(-1, head)
        left, right = dummy, dummy.next
        dist = 1

        while right:
            if dist < k:
                right = right.next
                dist += 1
            else:
                start, end = left.next, right.next
                end_prev = self.reverse(start, end)
                left.next, start.next = end_prev, end
                left, right = start, end
                dist = 1
        
        return dummy.next
    
    def reverse(self, start, end):
        prev, cur = None, start
        while cur != end and cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev