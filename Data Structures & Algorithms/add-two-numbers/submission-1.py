# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        dummy = ListNode()
        cur = dummy
        carry = 0
        while cur1 and cur2:
            total = cur1.val + cur2.val + carry
            cur.next = ListNode(total % 10)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
            carry = total // 10
        
        while cur1:
            total = cur1.val + carry
            cur.next = ListNode(total % 10)
            carry = total // 10
            cur1 = cur1.next
            cur = cur.next
        while cur2:
            total = cur2.val + carry
            cur.next = ListNode(total % 10)
            carry = total // 10
            cur2 = cur2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next