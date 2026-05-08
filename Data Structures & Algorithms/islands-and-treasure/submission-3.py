class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        q = deque()


        def add_land(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] < 0:
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])
        
        dist = 0
        while q:
            curr_len = len(q)
            for i in range(curr_len):
                r, c = q.popleft()
                grid[r][c] = dist
                add_land(r + 1, c)
                add_land(r - 1, c)
                add_land(r, c + 1)
                add_land(r, c - 1)
            dist += 1
