class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for a, b, t in times:
            edges[a].append((b, t))

        min_heap = [(0, k)]
        visited = set()
        total_time = 0

        while min_heap:
            t1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue

            visited.add(n1)

            # Since this is the shortest confirmed time to reach n1,
            # the answer must be at least this large.
            total_time = t1

            for n2, t2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (t1 + t2, n2))

        return total_time if len(visited) == n else -1