# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Result list to store values level by level
        res = []

        # Initialize queue for BFS (level-order traversal)
        q = collections.deque()
        q.append(root)

        # Process nodes level by level
        while q:
            # Number of nodes in the current level
            qLen = len(q)

            # List to store values of current level
            level = []

            # Iterate through all nodes in current level
            for i in range(qLen):
                node = q.popleft()

                # Only process valid (non-null) nodes
                if node:
                    # Add current node's value to this level
                    level.append(node.val)

                    # Add children to queue for next level
                    q.append(node.left)
                    q.append(node.right)

            # Only add non-empty levels to result
            if level:
                res.append(level)

        return res