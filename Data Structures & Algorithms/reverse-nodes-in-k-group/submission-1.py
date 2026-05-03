# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, start, end = dummy, head, head
        dist = 0
        while end:
            end = end.next
            dist += 1
            if dist == k:
                self.reverseGroup(prev, start, end)
                prev, start, end = start, end, end
                dist = 0
        return dummy.next

    def reverseGroup(self, pre, start, end):
        prev, cur = pre, start
        while cur != end:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
        pre.next = prev
        start.next = end