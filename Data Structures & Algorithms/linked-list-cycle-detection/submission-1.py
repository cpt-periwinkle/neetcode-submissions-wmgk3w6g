# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers:
        # 'slow' moves one step at a time
        # 'fast' moves two steps at a time
        slow = head
        fast = head

        # Traverse the list while fast pointer can move
        # If fast reaches the end → no cycle
        while fast and fast.next:

            # Move pointers
            fast = fast.next.next   # moves 2 steps
            slow = slow.next        # moves 1 step

            # If there is a cycle, fast will eventually meet slow
            if fast == slow:
                return True

        # If we exit the loop, fast reached the end → no cycle
        return False