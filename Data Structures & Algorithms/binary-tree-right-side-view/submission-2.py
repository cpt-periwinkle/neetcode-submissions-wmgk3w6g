# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the tree is empty, there is no right-side view
        if not root:
            return []

        # Initialize queue for BFS (level-order traversal)
        q = deque([root])

        # Result list to store the rightmost node of each level
        res = []

        # Process the tree level by level
        while q:
            # Number of nodes in the current level
            level_size = len(q)

            # Iterate through all nodes in this level
            for i in range(level_size):
                node = q.popleft()

                # If this is the last node in the current level,
                # it is visible from the right side
                if i == level_size - 1:
                    res.append(node.val)
                
                # Add left and right children to queue for next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        # Return the collected right-side view
        return res