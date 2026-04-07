class MedianFinder:
    def __init__(self):
        # We maintain TWO heaps:
        #
        # small -> MAX heap (stores the smaller half of numbers)
        # large -> MIN heap (stores the larger half of numbers)
        #
        # Python only has a min heap, so:
        # - We simulate a max heap by pushing NEGATIVE values into `small`
        #
        # Invariant:
        # - All values in small <= all values in large
        # - Size difference between heaps is at most 1

        self.small, self.large = [], []  # small = max heap, large = min heap

    def addNum(self, num: int) -> None:
        # Step 1: Decide which heap to push into
        #
        # If num is greater than the smallest element in large,
        # it belongs to the larger half → push to large (min heap)
        #
        # Otherwise, it belongs to the smaller half → push to small (max heap)

        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # push negative to simulate max heap
            heapq.heappush(self.small, -1 * num)

        # Step 2: Rebalance heaps
        #
        # We want both heaps to have equal size OR differ by at most 1

        if len(self.small) > len(self.large) + 1:
            # Move top of small (max of smaller half) to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            # Move top of large (min of larger half) to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Case 1: small has more elements
        # Median is the max of smaller half
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # Case 2: large has more elements
        # Median is the min of larger half
        elif len(self.large) > len(self.small):
            return self.large[0]

        # Case 3: both heaps have equal size
        # Median is average of:
        # - max of small (convert back from negative)
        # - min of large
        return (-1 * self.small[0] + self.large[0]) / 2.0