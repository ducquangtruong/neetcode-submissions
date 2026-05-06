class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # Dummy node
        self.head = ListNode()
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.head.next
        while index > 0 and curr != None:
            curr = curr.next
            index -= 1
        if index > 0:
            return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = ListNode(val)
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        prev, curr = self.head, self.head.next
        while index > 0 and curr != None:
            prev = prev.next
            curr = curr.next
            index -= 1
        
        prev.next = curr.next
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        return res
