class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        for c in range(COLS):
            for r in range(ROWS):
                dfs(0, c)
                dfs(ROWS - 1, c)
                dfs(r, 0)
                dfs(r, COLS - 1)

        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        