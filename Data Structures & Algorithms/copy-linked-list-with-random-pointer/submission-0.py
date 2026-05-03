"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newHead = Node(head.val)
        hashMap = {}
        cur1, cur2 = head, newHead
        while cur1:
            hashMap[cur1] = cur2
            cur1 = cur1.next
            if cur1:
                cur2.next = Node(cur1.val)
                cur2 = cur2.next

        cur1, cur2 = head, newHead
        while cur1:
            if cur1.random:
                cur2.random = hashMap[cur1.random]
            cur1 = cur1.next
            cur2 = cur2.next

        return newHead