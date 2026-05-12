class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def _insert(self, node):
        prev = self.right.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.right
        self.right.prev = node

    def _remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)
        
        if len(self.cache) > self.cap:
            lru = self.left.nxt
            rem_key = lru.key
            self._remove(lru)
            del self.cache[rem_key]