# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Start DFS from the root.
        # The initial maximum value on the path is root.val itself.
        return self.dfs(root, root.val)
        
    def dfs(self, node, maxVal):
        # Base case:
        # If there is no node, it contributes 0 good nodes.
        if not node:
            return 0
        
        # res will store the number of good nodes
        # found in the subtree rooted at this node.
        res = 0

        # A node is "good" if its value is greater than or equal to
        # the maximum value seen so far on the path from root to this node.
        if node.val >= maxVal:
            res = 1
        
        # Update the maximum value seen on this path before going to children.
        # This updated max is passed down independently to left and right.
        maxVal = max(maxVal, node.val)

        # Count good nodes in the left subtree
        res += self.dfs(node.left, maxVal)

        # Count good nodes in the right subtree
        res += self.dfs(node.right, maxVal)

        # Return total good nodes in this subtree
        return res