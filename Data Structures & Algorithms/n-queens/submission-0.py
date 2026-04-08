class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # col keeps track of which columns already have queens
        col = set()

        # Positive diagonal is identified by (r + c)
        # All cells on the same top-left to bottom-right diagonal
        # share the same value of (r + c)
        posDiag = set()

        # Negative diagonal is identified by (r - c)
        # All cells on the same top-right to bottom-left diagonal
        # share the same value of (r - c)
        negDiag = set()

        res = []

        # Start with an empty board
        board = [["."] * n for _ in range(n)]

        def dfs(r):
            # Base case:
            # If we've placed queens in all rows, we found one valid board
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # Try placing a queen in every column of the current row
            for c in range(n):
                # A queen cannot be placed if:
                # 1. that column already has a queen
                # 2. that positive diagonal already has a queen
                # 3. that negative diagonal already has a queen
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # ---- CHOOSE ----
                # Place queen at (r, c) and mark column/diagonals as occupied
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to the next row
                dfs(r + 1)

                # ---- BACKTRACK (UNDO CHOICE) ----
                # Remove queen and unmark its column/diagonals
                # so we can try another column in this row
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        dfs(0)
        return res