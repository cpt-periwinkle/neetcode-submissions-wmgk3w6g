# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Initialize counter for "good" nodes
        self.count = 0

        # Start DFS from root, with initial max value = root's value
        self.dfs(root, root.val)

        # Return total number of good nodes found
        return self.count

    def dfs(self, node, maxVal):
        # Base case: if node is None, nothing to process
        if not node:
            return None
        
        # If current node's value is >= max value seen so far
        # on the path from root → this node, it's a "good" node
        if node.val >= maxVal:
            self.count += 1

            # Update maxVal since this node is now the new maximum
            maxVal = node.val

        # Recurse on left subtree with updated maxVal
        self.dfs(node.left, maxVal)

        # Recurse on right subtree with updated maxVal
        self.dfs(node.right, maxVal)