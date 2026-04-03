# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.dfs(root)

        return self.is_balanced

    def dfs(self, curr):
        if not curr:
            return 0
        
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)
        diff = abs(right - left)

        if diff > 1:
            self.is_balanced = False

        return 1 + max(left, right)
        