# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node simplifies edge cases (especially when head changes after reversal)
        dummy = ListNode(0, head)
        
        # groupPrev always points to the node BEFORE the current group
        groupPrev = dummy

        while True:
            # Find the kth node from groupPrev
            # This marks the end of the current group
            kth = self._getKth(groupPrev, k)

            # If fewer than k nodes remain, stop (no reversal)
            if not kth:
                break

            # Node after the kth node (start of next group)
            groupNext = kth.next
            
            # Reverse the group:
            # prev starts from groupNext so that the reversed group connects correctly
            prev = kth.next
            curr = groupPrev.next  # first node in current group

            # Reverse nodes in the current group
            # Stop when we reach the node after the group
            while curr != groupNext:
                tmp = curr.next      # store next node
                curr.next = prev     # reverse pointer
                prev = curr          # move prev forward
                curr = tmp           # move curr forward

            # After reversal:
            # prev = new head of reversed group (which is kth)
            # groupPrev.next was the old head (now the tail)

            # Store the start of group (which becomes tail after reversal)
            tmp = groupPrev.next

            # Connect previous part to the new head (kth)
            groupPrev.next = kth

            # Move groupPrev to the end of the reversed group
            # (which is the old head)
            groupPrev = tmp
        
        return dummy.next


    def _getKth(self, curr, k):
        # Move k steps ahead from curr
        # Returns the kth node OR None if not enough nodes
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr