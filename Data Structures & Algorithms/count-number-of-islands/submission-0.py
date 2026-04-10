class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        islands = 0
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if grid[r][c] == "1":
                    self.bfs(r, c)
                    islands += 1
        return islands
                    
    def bfs(self, r, c):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = collections.deque()
        q.append((r, c))
        self.grid[r][c] = "0"

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if (nr < 0 or nc < 0 or nr >= self.ROWS or nc >= self.COLS or self.grid[nr][nc] == "0"):
                    continue
                q.append((nr, nc))
                self.grid[nr][nc] = "0"
