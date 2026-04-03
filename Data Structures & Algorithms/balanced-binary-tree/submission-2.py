# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Assume tree is balanced unless we find a violation
        self.is_balanced = True

        # DFS returns subtree height while updating self.is_balanced
        self.dfs(root)

        return self.is_balanced

    def dfs(self, curr):
        # Base case:
        # Empty subtree has height 0
        if not curr:
            return 0
        
        # Recursively get heights of left and right subtrees
        left = self.dfs(curr.left)
        right = self.dfs(curr.right)

        # If the height difference is more than 1,
        # the tree is not height-balanced
        if abs(right - left) > 1:
            self.is_balanced = False

        # Return height of current subtree to parent
        return 1 + max(left, right)