# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree has depth 0
        if not root:
            return 0

        level = 0  # This will track the number of levels (depth)

        # Initialize queue for BFS with the root node
        q = deque([root])

        # Process the tree level by level
        while q:
            # Number of nodes at current level
            level_size = len(q)

            # Process all nodes in the current level
            for i in range(level_size):
                node = q.popleft()

                # Add children of current node to queue (next level)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # After processing one full level, increment depth
            level += 1
        
        return level