# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Store the best path sum found anywhere in the tree
        self.res = root.val

        # Run DFS to compute path sums
        self.dfs(root)

        # Return the global maximum path sum
        return self.res

    def dfs(self, root):
        # Base case:
        # A null node contributes 0 to a path
        if not root:
            return 0
        
        # Recursively get the best path sum from left and right subtrees
        leftMax = self.dfs(root.left)
        rightMax = self.dfs(root.right)

        # Ignore negative paths since they would reduce the total sum
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # Best path passing through the current node:
        # left branch + current node + right branch
        # Update the global answer if this path is better
        self.res = max(self.res, root.val + leftMax + rightMax)

        # Return the best single branch that can extend upward to parent
        # We can only choose one side when going upward
        return root.val + max(leftMax, rightMax)