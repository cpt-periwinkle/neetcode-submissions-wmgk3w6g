import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # ---------------- CORE IDEA ----------------
        # We want the kth largest element.
        #
        # Instead of sorting the entire array,
        # we keep track of only the k largest elements seen so far.
        #
        # We use a MIN HEAP of size k:
        # - The heap stores the k largest elements
        # - The smallest among them (heap[0]) is the kth largest overall

        # Initialize empty min heap
        min_heap = []
        heapq.heapify(min_heap)

        # ---------------- PROCESS EACH NUMBER ----------------
        for num in nums:
            # Add current number to heap
            heapq.heappush(min_heap, num)

            # If heap size exceeds k,
            # remove the smallest element
            #
            # This ensures:
            # → heap always contains ONLY the k largest elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # ---------------- RESULT ----------------
        # The root of the heap (smallest in heap)
        # is the kth largest element overall
        return min_heap[0]