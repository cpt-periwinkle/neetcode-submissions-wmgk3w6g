# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # RECURSIVE SOLUTION (BST specific)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case:
        # If root is None, or either node is missing (defensive check),
        # we cannot find an LCA
        if not root or not p or not q:
            return None
        
        # If BOTH p and q are smaller than root,
        # then LCA must be in the left subtree
        # (because of BST property: left < root < right)
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If BOTH p and q are greater than root,
        # then LCA must be in the right subtree
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            # We found the split point:
            # Either:
            # 1. p and q are on different sides of root
            # 2. One of them IS the root
            # This makes root the Lowest Common Ancestor
            return root