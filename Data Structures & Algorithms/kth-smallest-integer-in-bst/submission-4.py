# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: # Iterative DFS
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack is used to simulate recursion (DFS)
        stack = []

        # Start traversal from root
        curr = root

        # Continue while there are nodes to process:
        # - curr handles downward traversal
        # - stack handles backtracking
        while curr or stack:

            # Go as far left as possible
            # (this ensures we process smallest elements first in BST)
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Pop the next node to process
            # (this is the next smallest element)
            curr = stack.pop()

            # Decrement k since we've visited one more node
            k -= 1

            # If this is the k-th visited node, return its value
            if k == 0:
                return curr.val

            # Move to the right subtree
            # (after processing current node, we explore larger elements)
            curr = curr.right