# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0, head)
        left, right = start, head
        dist = 0

        while dist < n:
            right = right.next
            dist += 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return start.next