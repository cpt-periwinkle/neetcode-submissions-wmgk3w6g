class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases (like empty list)
        # It acts as a fixed starting point for the merged list
        dummy = ListNode()

        # 'tail' always points to the last node in the merged list
        tail = dummy

        # Traverse both lists while neither is exhausted
        while list1 and list2:

            # Compare current values and attach the smaller node
            if list1.val <= list2.val:
                tail.next = list1        # attach node from list1
                list1 = list1.next       # move list1 forward
            else:
                tail.next = list2        # attach node from list2
                list2 = list2.next       # move list2 forward

            # Move tail forward to the newly added node
            tail = tail.next

        # At this point, one of the lists is exhausted
        # Attach the remaining nodes (already sorted)
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the head of the merged list (skip dummy node)
        return dummy.next