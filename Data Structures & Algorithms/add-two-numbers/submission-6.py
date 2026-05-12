# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0
        cur1, cur2, cur = l1, l2, dummy
        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            s = v1 + v2 + carry
            cur.next = ListNode(s % 10)
            carry = s // 10
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            cur =  cur.next

        return dummy.next

