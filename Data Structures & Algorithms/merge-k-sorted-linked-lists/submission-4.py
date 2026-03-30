# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: empty input
        if not lists or len(lists) == 0:
            return None
        
        # Repeatedly merge lists in pairs (divide and conquer)
        # Each iteration reduces number of lists by half
        while len(lists) > 1:
            merged = []

            # Merge pairs of lists: (l0,l1), (l2,l3), ...
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # If there is no pair, l2 stays None
                l2 = None
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]

                # Merge two sorted lists and store result
                merged.append(self._mergeLists(l1, l2))
            
            # Replace old list with merged results
            lists = merged
        
        # Only one fully merged list remains
        return lists[0]


    def _mergeLists(self, l1, l2):
        # Dummy node simplifies edge cases (empty result list)
        dummy = ListNode()
        tail = dummy  # tail always points to last node in merged list

        # Merge two sorted linked lists
        while l1 and l2:
            # Pick smaller value node and attach to result
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next  # move pointer in l1
            else:
                tail.next = l2
                l2 = l2.next  # move pointer in l2
            
            tail = tail.next  # advance tail

        # Attach remaining nodes (only one of these will exist)
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        # Return merged list (skip dummy node)
        return dummy.next