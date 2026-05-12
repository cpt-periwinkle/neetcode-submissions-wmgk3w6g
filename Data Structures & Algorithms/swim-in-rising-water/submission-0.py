class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        min_heap = [(grid[0][0], 0, 0)]  # [time needed, row, col]
        visit = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return t

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    (nr, nc) in visit
                ):
                    continue

                new_time = max(t, grid[nr][nc])
                heapq.heappush(min_heap, (new_time, nr, nc))