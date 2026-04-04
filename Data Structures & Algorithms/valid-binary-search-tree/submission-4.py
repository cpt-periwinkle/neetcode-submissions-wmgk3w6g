# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Start with the widest possible range
        # Any node must lie between (-∞, +∞)
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, left, right):
        # Base case: empty subtree is valid
        if not node:
            return True
        
        # Check if current node violates BST property
        # It must strictly lie between left and right bounds
        if not (left < node.val < right):
            return False

        # Recursively validate:
        # Left subtree → values must be < current node
        # Right subtree → values must be > current node
        return (
            self.valid(node.left, left, node.val) and
            self.valid(node.right, node.val, right)
        )