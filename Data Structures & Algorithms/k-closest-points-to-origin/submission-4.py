import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for x, y in points:
            dist_sq = -((x ** 2) + (y ** 2))
            heapq.heappush(max_heap, [dist_sq, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        while max_heap:
            dist, x, y = heapq.heappop(max_heap)
            res.append([x, y])
        
        return res