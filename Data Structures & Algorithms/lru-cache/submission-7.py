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
        prev, nxt = self.end.prev, self.end
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

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
            self.remove(self.keyStore[key])
        node = Node(key, value)
        self.insert(node)
        self.keyStore[key] = node
        if len(self.keyStore) > self.capacity:
            node = self.start.next
            self.remove(node)
            del self.keyStore[node.key]
