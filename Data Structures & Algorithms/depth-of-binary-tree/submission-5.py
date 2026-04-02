# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # RECURSIVE DFS SOLUTION!
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case:
        # If the node is None, it contributes 0 to the depth
        # (empty tree has height 0)
        if not root:
            return 0
        
        # Recursively compute the depth of left and right subtrees
        # Then take the maximum of both (since depth = longest path)
        # Add 1 for the current node
        return 1 + max(
            self.maxDepth(root.left),   # depth of left subtree
            self.maxDepth(root.right)   # depth of right subtree
        )