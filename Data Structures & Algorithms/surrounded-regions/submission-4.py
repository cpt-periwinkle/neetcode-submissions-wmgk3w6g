from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Dimensions of the board
        ROWS = len(board)
        COLS = len(board[0])

        # DFS to mark all 'O's connected to border as safe
        def dfs(r, c):
            # Stop if:
            # - Out of bounds
            # - Not an 'O' (either 'X' or already visited 'T')
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            
            # Mark current cell as temporary safe
            board[r][c] = "T"

            # Explore all 4 directions
            dfs(r + 1, c)   # down
            dfs(r - 1, c)   # up
            dfs(r, c + 1)   # right
            dfs(r, c - 1)   # left

        # Step 1: Start DFS from border cells
        # Traverse left and right borders
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r, 0)  # left border
            if board[r][COLS - 1] == "O":
                dfs(r, COLS - 1)  # right border

        # Traverse top and bottom borders
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)  # top border
            if board[ROWS - 1][c] == "O":
                dfs(ROWS - 1, c)  # bottom border

        # Step 2 & 3: Flip and restore in one pass
        for c in range(COLS):
            for r in range(ROWS):
                # If still 'O', it's surrounded → capture it
                if board[r][c] == "O":
                    board[r][c] = "X"
                # If 'T', it was safe → restore it
                if board[r][c] == "T":
                    board[r][c] = "O"