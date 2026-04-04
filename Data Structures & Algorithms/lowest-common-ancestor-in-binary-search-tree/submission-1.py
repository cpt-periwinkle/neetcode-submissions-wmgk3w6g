# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  # ITERATIVE SOLUTION (BST specific)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root of the tree
        curr = root

        # Traverse the tree until we find the LCA
        while curr:
            # If both p and q are greater than current node,
            # then LCA must be in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # If both p and q are less than current node,
            # then LCA must be in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left

            else:
                # We have found the split point:
                # Either:
                # 1. p <= curr <= q OR q <= curr <= p
                # 2. One node is on left and the other is on right
                # 3. curr is equal to p or q
                # This makes curr the Lowest Common Ancestor
                return curr