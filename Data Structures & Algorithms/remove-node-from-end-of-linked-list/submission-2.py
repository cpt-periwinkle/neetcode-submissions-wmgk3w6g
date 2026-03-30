# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node pointing to head
        # This helps handle edge cases (like removing the head itself)
        dummy = ListNode(0, head)

        # 'left' will end up pointing to the node BEFORE the one we remove
        left = dummy

        # 'right' is used to create a gap of n nodes ahead of 'left'
        right = head

        # Move 'right' n steps ahead
        # This creates a fixed gap of n between left and right
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until 'right' reaches the end
        # At this point:
        # - 'right' is None (end of list)
        # - 'left' is just before the node to delete
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        # (i.e., skip the next node)
        left.next = left.next.next

        # Return the new head (skip dummy)
        return dummy.next