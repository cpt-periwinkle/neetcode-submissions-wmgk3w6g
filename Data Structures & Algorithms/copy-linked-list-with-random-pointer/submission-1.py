"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map original nodes → copied nodes
        # Initialize with {None: None} to handle edge cases cleanly
        # (so we don't need to check for None separately)
        old_to_copy = {None: None}

        # ---- Step 1: Create all nodes (without connections) ----
        curr = head
        while curr:
            # Create a copy of the current node (only value for now)
            copy = Node(curr.val)

            # Map original node to its copy
            old_to_copy[curr] = copy

            # Move to next node
            curr = curr.next

        # ---- Step 2: Assign next and random pointers ----
        curr = head
        while curr:
            # Get the copied version of current node
            copy = old_to_copy[curr]

            # Set 'next' pointer using the mapping
            # (curr.next might be None → handled by dictionary)
            copy.next = old_to_copy[curr.next]

            # Set 'random' pointer using the mapping
            copy.random = old_to_copy[curr.random]

            # Move forward
            curr = curr.next

        # Return the head of the copied list
        return old_to_copy[head]