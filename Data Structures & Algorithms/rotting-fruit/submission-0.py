from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # Queue stores all currently rotten oranges.
        # These are the oranges that will spread rot in the current minute.
        q = deque()

        minutes = 0
        fresh = 0

        def makeRotten(r, c):
            nonlocal fresh

            # Skip if:
            # 1. Out of bounds
            # 2. Not a fresh orange
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return

            # Turn fresh orange rotten
            grid[r][c] = 2
            fresh -= 1

            # This orange will spread rot in the next minute
            q.append((r, c))

        # First pass:
        # - add all initially rotten oranges to the queue
        # - count total fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Multi-source BFS:
        # all rotten oranges spread at the same time
        # each level of BFS = 1 minute
        while q and fresh > 0:
            # Process exactly one "minute" worth of rotten oranges
            for _ in range(len(q)):
                r, c = q.popleft()

                # Try to rot the 4 neighboring fresh oranges
                makeRotten(r + 1, c)
                makeRotten(r - 1, c)
                makeRotten(r, c + 1)
                makeRotten(r, c - 1)

            # After finishing one full BFS layer, one minute has passed
            minutes += 1

        # If fresh oranges are still left, they were unreachable
        if fresh > 0:
            return -1

        return minutes