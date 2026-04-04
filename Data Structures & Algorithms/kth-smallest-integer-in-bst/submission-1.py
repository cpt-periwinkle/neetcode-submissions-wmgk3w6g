# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # cnt tracks how many nodes we still need to skip
        # before reaching the k-th smallest
        self.cnt = k

        # index will store the answer when we find the k-th node
        self.index = root.val

        # Perform inorder DFS (sorted order in BST)
        self.dfs(root)

        # Return the k-th smallest value
        return self.index


    def dfs(self, node):
        # Base case: no node to process
        if not node:
            return
        
        # Traverse left subtree first (smaller values)
        self.dfs(node.left)

        # Visit current node → decrement counter
        self.cnt -= 1

        # If this is the k-th node in inorder traversal
        if self.cnt == 0:
            # Store the result
            self.index = node.val
            return  # Stop further unnecessary processing
        
        # Traverse right subtree (larger values)
        self.dfs(node.right)