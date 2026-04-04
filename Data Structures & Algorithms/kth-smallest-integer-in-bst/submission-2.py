# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #EASIER RECURSIVE SOLUTION
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.dfs(root)
        return self.arr[k - 1]

    def dfs(self, node):
        if not node:
            return None
        
        self.dfs(node.left)
        self.arr.append(node.val)
        self.dfs(node.right)