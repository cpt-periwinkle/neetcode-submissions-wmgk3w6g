# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case:
        # If the current node is None, there's nothing to invert
        if not root:
            return None
        
        # Swap the left and right children of the current node
        # This is the key operation of inversion
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Recursively invert the left subtree
        # (which was originally the right subtree before swapping)
        self.invertTree(root.left)
        
        # Recursively invert the right subtree
        # (which was originally the left subtree before swapping)
        self.invertTree(root.right)

        # Return the root of the modified (inverted) tree
        return root