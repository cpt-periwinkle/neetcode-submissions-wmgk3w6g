class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        time = 0
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        def make_rotten(r, c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return
            grid[r][c] = 2
            fresh -= 1
            q.append([r, c])

        while q and fresh > 0:
            curr_len = len(q)
            for _ in range(curr_len):
                r, c = q.popleft()
                make_rotten(r + 1, c)
                make_rotten(r - 1, c)
                make_rotten(r, c + 1)
                make_rotten(r, c - 1)
            time += 1
        
        return -1 if fresh > 0 else time
        