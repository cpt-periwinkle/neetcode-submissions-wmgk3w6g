class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Min heap stores:
        # (minimum time required to reach this cell, row, col)
        #
        # We start at (0,0).
        # If grid[0][0] = 5, then water must rise to at least 5
        # before we can even stand there.
        min_heap = [(grid[0][0], 0, 0)]

        # Tracks cells whose minimum required time
        # has already been finalized.
        visit = set()

        # 4-directional movement
        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while min_heap:

            # Always process the cell with the currently smallest
            # required water level first.
            #
            # This is Dijkstra's algorithm.
            t, r, c = heapq.heappop(min_heap)

            # A cell may appear multiple times in the heap
            # through different paths.
            #
            # Once we process it the first time,
            # we already know the optimal/minimum time to reach it.
            if (r, c) in visit:
                continue

            visit.add((r, c))

            # If we reached the bottom-right corner,
            # the current time is the minimum possible answer.
            #
            # Dijkstra guarantees this because we pop
            # cells in increasing time order.
            if r == ROWS - 1 and c == COLS - 1:
                return t

            # Explore neighboring cells
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Skip invalid coordinates or already finalized cells
                if (
                    nr < 0 or nc < 0 or
                    nr >= ROWS or nc >= COLS or
                    (nr, nc) in visit
                ):
                    continue

                # To move into the neighbor:
                #
                # - We already needed time t to reach current cell
                # - Neighbor cell itself may require a higher water level
                #
                # So the required time becomes the maximum of the two.
                new_time = max(t, grid[nr][nc])

                # Add candidate path into the heap
                heapq.heappush(min_heap, (new_time, nr, nc))