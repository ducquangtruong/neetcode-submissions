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
        # Idea: Make a mapping old node -> new node
        newHead = Node(head.val)
        oldToNew = {
            None: None,
            head: newHead
        }

        cur1, cur2 = head, newHead
        while cur1:
            if cur1.next not in oldToNew:
                newNext = Node(cur1.next.val)
                oldToNew[cur1.next] = newNext
            cur2.next = oldToNew[cur1.next]
            if cur1.random not in oldToNew:
                newRandom = Node(cur1.random.val)
                oldToNew[cur1.random] = newRandom
            cur2.random = oldToNew[cur1.random]
            cur1, cur2 = cur1.next, cur2.next
        
        return newHead