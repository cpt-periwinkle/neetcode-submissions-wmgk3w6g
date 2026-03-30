# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # ---- Step 1: Find the middle of the list ----
        # 'slow' moves 1 step, 'fast' moves 2 steps
        # When fast reaches end, slow will be at the middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # ---- Step 2: Split the list into two halves ----
        # First half: head → ... → slow
        # Second half: slow.next → ...
        second = slow.next
        slow.next = None  # break the list into two parts

        # ---- Step 3: Reverse the second half ----
        # We reverse so we can merge from both ends
        prev = None
        while second:
            nxt = second.next        # store next node
            second.next = prev       # reverse pointer
            prev = second            # move prev forward
            second = nxt             # move second forward

        # After this:
        # prev = head of reversed second half

        # ---- Step 4: Merge the two halves ----
        # Merge in alternating order:
        # first → second → first → second ...
        first = head
        second = prev

        while second:
            # Store next pointers before modifying links
            nxt1 = first.next
            nxt2 = second.next

            # Link nodes alternately
            first.next = second
            second.next = nxt1

            # Move both pointers forward
            first = nxt1
            second = nxt2