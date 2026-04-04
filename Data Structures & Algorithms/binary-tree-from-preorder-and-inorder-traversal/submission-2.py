# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Dummy node so the real root can be stored at head.right
        head = TreeNode(None)

        # curr points to the current node being expanded
        curr = head

        # i scans preorder (next node to create)
        # j scans inorder (next node whose left side is done)
        i, j, n = 0, 0, len(preorder)

        while i < n and j < n:
            # Create the next preorder node as curr.right.
            # Preserve old curr.right as a temporary thread.
            curr.right = TreeNode(preorder[i], right=curr.right)
            curr = curr.right
            i += 1

            # Keep building left children until current node matches
            # the next inorder value. That means we've reached the
            # leftmost unfinished node for this subtree.
            while i < n and curr.val != inorder[j]:
                # Create left child and temporarily use its right pointer
                # as a thread back to the current node.
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1

            # We have now matched one inorder node
            j += 1

            # Follow temporary right threads upward while the ancestor
            # values also match the next inorder values.
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right       # threaded ancestor
                curr.right = None       # remove temporary thread
                curr = prev             # move back up
                j += 1

        # Real tree root is stored at head.right
        return head.right