# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Store traversals on self so helper method can access them
        self.preorder = preorder
        self.inorder = inorder

        # preIdx points to the next node to create from preorder
        self.preIdx = 0

        # inIdx points to the current position in inorder
        self.inIdx = 0

        # Start building with no upper boundary
        return self.dfs(float("inf"))

    def dfs(self, limit):
        # If we have used all preorder elements, no more nodes remain
        if self.preIdx >= len(self.preorder):
            return None

        # If inorder has reached the current boundary,
        # this subtree is finished
        if self.inorder[self.inIdx] == limit:
            self.inIdx += 1
            return None

        # Create the current root from preorder
        root = TreeNode(self.preorder[self.preIdx])
        self.preIdx += 1

        # Build the left subtree first
        # Left subtree stops when inorder reaches root.val
        root.left = self.dfs(root.val)

        # Build the right subtree next
        # Right subtree stops when inorder reaches the parent's boundary
        root.right = self.dfs(limit)

        return root