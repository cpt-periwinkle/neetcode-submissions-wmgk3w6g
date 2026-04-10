from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Edge case: empty grid
        if not grid:
            return 0

        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.grid = grid

        max_area = 0

        # Check every cell in the grid
        for r in range(self.ROWS):
            for c in range(self.COLS):
                # If we find unvisited land, compute this island's area
                if self.grid[r][c] == 1:
                    max_area = max(max_area, self.bfs(r, c))
        
        return max_area

    def bfs(self, r, c):
        # 4-directional movement: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        q = deque()
        q.append((r, c))

        # Mark starting land cell as visited
        self.grid[r][c] = 0

        # Starting cell already contributes area = 1
        area = 1

        while q:
            row, col = q.popleft()

            # Explore all 4 neighbors
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                # Skip out of bounds or water/visited cells
                if nr < 0 or nc < 0 or nr >= self.ROWS or nc >= self.COLS or self.grid[nr][nc] == 0:
                    continue

                # Valid land cell found, so include it in area
                area += 1
                q.append((nr, nc))

                # Mark visited so we don't process it again
                self.grid[nr][nc] = 0
        
        return area