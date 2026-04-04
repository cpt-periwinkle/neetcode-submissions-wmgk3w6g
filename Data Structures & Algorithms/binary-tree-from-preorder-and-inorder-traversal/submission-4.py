# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case:
        # If traversal lists are empty, there is no subtree to build
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is always the root
        root = TreeNode(preorder[0])

        # Find the root in inorder traversal
        # Everything to the left is the left subtree
        # Everything to the right is the right subtree
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree
        # preorder[1:mid+1] contains exactly the left subtree nodes
        # inorder[:mid] contains left subtree inorder traversal
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        # Recursively build the right subtree
        # preorder[mid+1:] contains right subtree nodes
        # inorder[mid+1:] contains right subtree inorder traversal
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # Return the root of this subtree
        return root