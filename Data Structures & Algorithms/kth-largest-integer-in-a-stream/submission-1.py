import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # ---------------- CORE IDEA ----------------
        # We DO NOT store all elements.
        # Instead, we only keep the k LARGEST elements seen so far.
        #
        # We use a MIN HEAP of size k:
        # - The heap always contains the k largest elements
        # - The smallest among them (heap[0]) is the kth largest overall
        #
        # Example:
        # nums = [4,5,8,2], k = 3
        # We only care about top 3 → [4,5,8]
        # min_heap = [4,5,8]
        # kth largest = 4 (smallest in heap)

        self.min_heap = nums
        self.k = k

        # Convert list into a min heap
        heapq.heapify(self.min_heap)

        # If we have more than k elements,
        # remove the smallest until size becomes k
        #
        # This ensures:
        # → heap ALWAYS stores ONLY the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        # Add the new value into the heap
        heapq.heappush(self.min_heap, val)

        # If heap grows beyond size k,
        # remove the smallest element
        #
        # Why?
        # Because we only want to keep the k largest elements
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root of the heap (smallest element in heap)
        # is the kth largest element overall
        return self.min_heap[0]