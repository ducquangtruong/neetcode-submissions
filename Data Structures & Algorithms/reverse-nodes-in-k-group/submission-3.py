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
        groupPrev, ptr = dummy, dummy.next
        dist = 1

        while ptr:
            if dist < k:
                ptr = ptr.next
                dist += 1
            else:
                groupPrevNext, groupNext = groupPrev.next, ptr.next
                preGroupNext = self.reverse(groupPrevNext, groupNext)
                groupPrev.next, groupPrevNext.next = preGroupNext, groupNext
                groupPrev, ptr = groupPrevNext, groupNext
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