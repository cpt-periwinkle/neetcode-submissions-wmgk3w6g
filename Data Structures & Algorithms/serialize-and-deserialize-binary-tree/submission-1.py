# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Codec:
    
    # ---------------- SERIALIZATION ----------------
    # Goal: Convert tree → string using BFS (level-order traversal)
    def serialize(self, root: Optional[TreeNode]) -> str:
        # Edge case: empty tree
        if not root:
            return "N"
        
        # Queue will store actual TreeNode objects (NOT values)
        q = deque([root])
        
        # This will store the serialized output
        res = []

        # Standard BFS traversal
        while q:
            node = q.popleft()

            if not node:
                # Use "N" to represent null nodes (important to preserve structure)
                res.append("N")
            else:
                # Store current node value
                res.append(str(node.val))

                # Push children into queue (even if they are None)
                # This ensures structure is preserved
                q.append(node.left)
                q.append(node.right)

        # Convert list → comma-separated string
        return ",".join(res)
        
    
    # ---------------- DESERIALIZATION ----------------
    # Goal: Convert string → tree using BFS
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split string into list
        vals = data.split(",")
        
        # If tree was empty
        if vals == ["N"]:
            return None

        # First value is always root
        root = TreeNode(int(vals[0]))
        
        # Queue to reconstruct tree level-by-level
        q = deque([root])
        
        # Pointer to track position in vals list
        index = 1

        # Process nodes level by level
        while q:
            node = q.popleft()

            # ---- LEFT CHILD ----
            # Check bounds AND ensure it's not null
            if index < len(vals) and vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1  # Move pointer

            # ---- RIGHT CHILD ----
            if index < len(vals) and vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1  # Move pointer
        
        return root