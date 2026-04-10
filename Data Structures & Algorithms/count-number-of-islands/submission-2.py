import collections
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid
        if not grid:
            return 0

        # Store grid and dimensions for easy access in bfs
        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        
        islands = 0  # This will count total islands
        
        # Traverse every cell in the grid
        for r in range(self.ROWS):
            for c in range(self.COLS):
                # If we find land, it's the start of a new island
                if self.grid[r][c] == "1":
                    self.bfs(r, c)  # Flood fill the entire island
                    islands += 1    # Increment island count
        
        return islands
                    
    def bfs(self, r, c):
        # Directions for moving up, down, left, right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Queue for BFS traversal
        q = collections.deque()
        q.append((r, c))
        
        # Mark starting cell as visited (sink the island)
        self.grid[r][c] = "0"

        # Process all connected land cells
        while q:
            row, col = q.popleft()
            
            # Explore all 4 directions
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                
                # Skip if:
                # 1. Out of bounds
                # 2. Already water (visited or originally water)
                if (nr < 0 or nc < 0 or 
                    nr >= self.ROWS or nc >= self.COLS or 
                    self.grid[nr][nc] == "0"):
                    continue
                
                # Add neighboring land to queue
                q.append((nr, nc))
                
                # Mark it as visited immediately to avoid re-processing
                self.grid[nr][nc] = "0"