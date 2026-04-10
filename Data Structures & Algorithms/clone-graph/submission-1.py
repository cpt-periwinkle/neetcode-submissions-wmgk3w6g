"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case: empty graph
        if not node:
            return None
        
        # Map to store: original node -> cloned node
        # This is the key to handling cycles and avoiding duplicate copies
        self.og_clone_map = {}
        
        # Start DFS from the given node
        return self.dfs(node)

    def dfs(self, node):
        # If we've already cloned this node, return the clone
        # This prevents infinite recursion in cyclic graphs
        if node in self.og_clone_map:
            return self.og_clone_map[node]
        
        # Create a copy of the current node (without neighbors yet)
        copy = Node(node.val)
        
        # Store it in the map BEFORE exploring neighbors
        # Important: this breaks cycles
        self.og_clone_map[node] = copy
        
        # Now recursively clone all neighbors
        for n in node.neighbors:
            # Append the cloned neighbor to this node's neighbors
            copy.neighbors.append(self.dfs(n))
        
        # Return the fully built clone of this node
        return copy