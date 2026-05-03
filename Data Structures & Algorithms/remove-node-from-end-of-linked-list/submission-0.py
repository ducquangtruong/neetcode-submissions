# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        start.next = head
        prev, cur = start, head
        prev.next = head
        dist = 0
        while dist < n and cur:
            cur = cur.next
            dist += 1
        while cur:
            prev = prev.next
            cur = cur.next
        prev.next = prev.next.next
        return start.next