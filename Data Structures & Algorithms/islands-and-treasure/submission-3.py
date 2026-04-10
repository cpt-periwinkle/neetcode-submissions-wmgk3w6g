from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Dimensions of the grid
        ROWS = len(grid)
        COLS = len(grid[0])

        # Queue for BFS (stores cells to process)
        q = deque()

        # Visited set to avoid revisiting cells
        visit = set()

        # Helper function to add valid neighboring cells
        def addLand(r, c):
            # Skip if:
            # 1. Out of bounds
            # 2. Already visited
            # 3. Wall (-1)
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visit or 
                grid[r][c] == -1):
                return
            
            # Add to queue for BFS expansion
            q.append([r, c])
            visit.add((r, c))

        # Step 1: Initialize BFS with ALL treasure cells (0s)
        # This is what makes it multi-source BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        # Distance from nearest treasure
        dist = 0

        # Step 2: BFS level-by-level
        while q:
            # Process one "layer" at a time
            # All nodes in this layer have the same distance
            for i in range(len(q)):
                r, c = q.popleft()

                # Assign the shortest distance to this cell
                grid[r][c] = dist

                # Expand in 4 directions
                addLand(r + 1, c)
                addLand(r - 1, c)
                addLand(r, c + 1)
                addLand(r, c - 1)
            
            # After finishing one layer, increase distance
            dist += 1