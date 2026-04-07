import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python only has a MIN heap, so we simulate a MAX heap
        # by storing negative values
        stones_heap = [-n for n in stones]

        # Convert list into a heap in O(n) time
        heapq.heapify(stones_heap)

        # Keep smashing stones until at most one remains
        while len(stones_heap) > 1:
            # Pop the two largest stones
            # (negate because we stored them as negatives)
            val1 = -heapq.heappop(stones_heap)  # largest
            val2 = -heapq.heappop(stones_heap)  # second largest

            # If they are not equal, push the difference back
            # This represents the remaining stone after smashing
            if val1 != val2:
                # Push negative again to maintain max heap behavior
                heapq.heappush(stones_heap, -(val1 - val2))

        # If no stones remain, return 0
        if not stones_heap:
            return 0

        # Otherwise, return the weight of the last remaining stone
        # (convert back from negative)
        return -stones_heap[0]