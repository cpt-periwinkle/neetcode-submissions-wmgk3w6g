# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 'prev' will point to the previous node (initially None)
        prev = None

        # 'curr' starts at the head of the list
        curr = head

        # Traverse the list
        while curr:
            # Store next node before breaking the link
            nxt = curr.next

            # Reverse the current node's pointer
            curr.next = prev

            # Move 'prev' and 'curr' one step forward
            prev = curr
            curr = nxt

        # At the end, 'prev' will be the new head of the reversed list
        return prev