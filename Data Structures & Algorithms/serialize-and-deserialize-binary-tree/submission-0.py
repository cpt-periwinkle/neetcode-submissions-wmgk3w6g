# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # ---------------- SERIALIZATION ----------------
    # Goal: Convert tree → string
    def serialize(self, root: Optional[TreeNode]) -> str:
        # This list will store values in preorder traversal
        self.res = []
        
        # Start DFS traversal
        self.serialDfs(root)
        
        # Convert list to comma-separated string
        return ",".join(self.res)

    def serialDfs(self, node):
        # If node is null, add a marker ("N") to preserve structure
        if not node:
            self.res.append("N")
            return
        
        # Add current node value
        self.res.append(str(node.val))
        
        # Recurse on left subtree
        self.serialDfs(node.left)
        
        # Recurse on right subtree
        self.serialDfs(node.right)
        
        # NOTE:
        # This is PREORDER traversal: root → left → right
        # Example:
        #     1
        #    / \
        #   2   3
        #
        # Serialized: "1,2,N,N,3,N,N"


    # ---------------- DESERIALIZATION ----------------
    # Goal: Convert string → tree
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Split string into list of values
        self.vals = data.split(",")
        
        # Pointer to track current position in list
        self.i = 0
        
        # Rebuild tree using DFS
        return self.deserialDfs()

    def deserialDfs(self):
        # If current value is "N", it's a null node
        if self.vals[self.i] == "N":
            self.i += 1  # Move pointer forward
            return None
        
        # Create node with current value
        node = TreeNode(int(self.vals[self.i]))
        self.i += 1  # Move pointer forward
        
        # Recursively build left subtree
        node.left = self.deserialDfs()
        
        # Recursively build right subtree
        node.right = self.deserialDfs()
        
        return node