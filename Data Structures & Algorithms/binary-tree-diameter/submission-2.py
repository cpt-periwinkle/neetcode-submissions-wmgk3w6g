# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This will store the maximum diameter found so far
        self.maxD = 0

        # Run DFS to compute heights and update diameter
        self.dfs(root)

        return self.maxD

    def dfs(self, root: Optional[TreeNode]) -> int:
        # Base case: height of null node = 0
        if not root:
            return 0

        # Recursively get height of left and right subtrees
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # Diameter at this node = left height + right height
        # (longest path passing through this node)
        self.maxD = max(self.maxD, left + right)

        # Return height of current node to parent
        # height = 1 + max(left subtree, right subtree)
        return 1 + max(left, right)