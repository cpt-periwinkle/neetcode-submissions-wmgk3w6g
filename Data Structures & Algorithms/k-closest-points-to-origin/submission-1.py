import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_heap = []
        heapq.heapify(points_heap)
        res = []

        for i, point in enumerate(points):
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            heapq.heappush(points_heap, (distance, point))

        for i in range(k):
            val = heapq.heappop(points_heap)
            res.append(val[1])

        return res