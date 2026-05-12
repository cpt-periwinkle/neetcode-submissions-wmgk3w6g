# Node for doubly linked list
# Stores key as well so we can delete from hashmap in O(1) during eviction
class Node:
    def __init__(self, key, value):
        self.key = key          # needed to remove from hashmap
        self.val = value        # actual value
        self.prev = None        # pointer to previous node
        self.next = None        # pointer to next node


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node (O(1) lookup)

        # Dummy nodes to avoid edge-case checks (empty list, single node, etc.)
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        # Initialize empty doubly linked list: left <-> right
        self.left.next = self.right
        self.right.prev = self.left


    # Remove a node from the doubly linked list in O(1)
    def _remove(self, node):
        prev = node.prev
        nxt = node.next

        # Bypass the node
        prev.next = nxt
        nxt.prev = prev


    # Insert node at the MRU position (right side)
    def _insert(self, node):
        prev = self.right.prev   # last real node
        nxt = self.right         # dummy right

        # Insert node between prev and right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    # Get value and mark as recently used
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # Move node to MRU position
            self._remove(node)
            self._insert(node)

            return node.val

        return -1  # key not found


    # Insert or update key
    def put(self, key: int, value: int) -> None:

        # If key exists, remove old node (we'll reinsert updated one)
        if key in self.cache:
            self._remove(self.cache[key])

        # Create new node and insert into hashmap + DLL
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        # If capacity exceeded, evict LRU (leftmost real node)
        if len(self.cache) > self.cap:
            lru = self.left.next   # first real node = least recently used
            self._remove(lru)
            del self.cache[lru.key]