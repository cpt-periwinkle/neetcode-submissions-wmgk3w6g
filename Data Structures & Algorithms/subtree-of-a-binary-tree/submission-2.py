# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is empty, it's always a subtree
        if not subRoot:
            return True
        
        # If root is empty but subRoot is not, cannot be a subtree
        if not root:
            return False

        # Check three possibilities:
        # 1. Trees match starting at current node
        # 2. Subtree exists in left subtree
        # 3. Subtree exists in right subtree
        return (
            self.sameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, p, q):
        # If both nodes are null, trees match
        if not p and not q:
            return True
        
        # If both nodes exist and values match,
        # recursively check left and right subtrees
        if p and q and p.val == q.val:
            return (
                self.sameTree(p.left, q.left) and
                self.sameTree(p.right, q.right)
            )

        # Otherwise, trees do not match
        return False