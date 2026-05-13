# Idea: Doubly-linked list
class Node:
    def __init__(self, key = -1, val = -1, prev = None, next = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.start, self.end = Node(), Node()
        self.start.next, self.end.prev = self.end, self.start

        self.keyStore = {}
        self.capacity = capacity
    
    def insert(self, node: Node):
        prev = self.end.prev
        prev.next, self.end.prev = node, node
        node.next, node.prev = self.end, prev
        self.keyStore[node.key] = node
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.keyStore[node.key]

    def get(self, key: int) -> int:
        val = -1
        if key in self.keyStore:
            node = self.keyStore[key]
            val = node.val
            self.remove(node)
            self.insert(node)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keyStore:
            node = Node(key, value)
            self.remove(self.keyStore[key])
            self.insert(node)
            return
        if len(self.keyStore) == self.capacity:
            self.remove(self.start.next)
        self.insert(Node(key, value))
