# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify building the result list
        # Avoids handling special case for the head
        dummy = ListNode()

        # 'curr' points to the last node in the result list
        curr = dummy

        # Carry value from previous digit addition
        carry = 0

        # Continue while there are nodes in l1 or l2, or a remaining carry
        while l1 or l2 or carry:

            # Default values (in case one list is shorter)
            v1 = 0
            v2 = 0

            # Extract values from current nodes if they exist
            if l1:
                v1 = l1.val
            if l2:
                v2 = l2.val
            
            # Compute sum of current digits + carry
            val = v1 + v2 + carry

            # Update carry (tens place)
            carry = val // 10

            # Current digit to store (ones place)
            val = val % 10

            # Create a new node with the computed digit
            curr.next = ListNode(val)

            # Move result pointer forward
            curr = curr.next

            # Move input lists forward (if they exist)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the head of the result list (skip dummy node)
        return dummy.next
