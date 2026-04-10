"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        self.og_clone_map = {}
        return self.dfs(node)

    def dfs(self, node):
        if node in self.og_clone_map:
            return self.og_clone_map[node]
        copy = Node(node.val)
        self.og_clone_map[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(self.dfs(n))
        return copy