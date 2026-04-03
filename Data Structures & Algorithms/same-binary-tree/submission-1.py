# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same_tree = True
        self.dfs(p, q)
        return self.same_tree

    def dfs(self, p, q):
        # If one is null and the other is not, trees differ
        if p is None or q is None:
            if p != q:
                self.same_tree = False
            return
        
        # If values differ, trees differ
        if p.val != q.val:
            self.same_tree = False
            return

        self.dfs(p.left, q.left)
        self.dfs(p.right, q.right)