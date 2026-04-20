import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # ---------------- CORE IDEA ----------------
        # We want the k points closest to the origin (0,0).
        #
        # Distance formula:
        # sqrt(x^2 + y^2)
        #
        # But we DO NOT need sqrt because:
        # → sqrt is monotonic (order doesn't change)
        # → so we can just use (x^2 + y^2)
        #
        # We use a MIN HEAP where:
        # (distance_squared, point)
        #
        # Heap always gives us the smallest distance first.

        # Initialize empty min heap
        min_heap = []
        heapq.heapify(min_heap)

        # This will store the final k closest points
        res = []

        # ---------------- BUILD HEAP ----------------
        for point in points:
            # Compute squared distance from origin
            distance_sq = (point[0] ** 2) + (point[1] ** 2)

            # Push into heap
            # Heap is ordered by first value → distance_sq
            heapq.heappush(min_heap, (distance_sq, point))

        # ---------------- EXTRACT K CLOSEST ----------------
        for _ in range(k):
            # Pop the smallest distance point
            val = heapq.heappop(min_heap)

            # val = (distance_sq, point)
            # We only need the point
            res.append(val[1])

        # Return k closest points
        return res