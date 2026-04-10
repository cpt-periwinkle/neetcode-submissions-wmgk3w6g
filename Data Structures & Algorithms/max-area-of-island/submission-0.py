class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.grid = grid

        max_area = 0

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.grid[r][c] == 1:
                    max_area = max(max_area, self.bfs(r, c))
        
        return max_area

    def bfs(self, r, c):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        q.append((r, c))
        self.grid[r][c] = 0
        area = 1

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
                if nr < 0 or nc < 0 or nr >= self.ROWS or nc >= self.COLS or self.grid[nr][nc] == 0:
                    continue
                area += 1
                q.append((nr, nc))
                self.grid[nr][nc] = 0
        
        return area
