# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion -> SUBOPTIMAL, BUT GOOD FOR LEARNING

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case:
        # If the list is empty, return None
        if not head:
            return None

        # Initialize newHead as current node
        # This will eventually become the last node of original list
        newHead = head

        # If there is a next node, recursively reverse the rest of the list
        if head.next:
            # Reverse everything after current node
            newHead = self.reverseList(head.next)

            # After recursion:
            # head -> next node
            # next node is now at the end of reversed sublist

            # Reverse the link:
            # Make next node point back to current node
            head.next.next = head

        # Break the original forward link to avoid cycle
        head.next = None

        # Return the new head of the reversed list
        return newHead
    