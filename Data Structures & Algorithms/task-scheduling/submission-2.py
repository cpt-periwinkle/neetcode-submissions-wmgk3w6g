class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        max_heap = [-i for i in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque() # (count, time)

        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                total = 1 + heapq.heappop(max_heap)
                if total:
                    q.append([total, time + n])
        
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time