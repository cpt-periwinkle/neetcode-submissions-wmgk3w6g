class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board
        self.word = word

        # path keeps track of cells used in the CURRENT DFS path
        # This ensures we don't reuse the same cell in one word construction
        self.path = set()

        # Try starting the word from every cell
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.dfs(r, c, 0):
                    return True
        return False

    def dfs(self, r, c, i):
        # If we've matched all characters in the word, success
        if i == len(self.word):
            return True

        # Invalid conditions:
        # - out of bounds
        # - character mismatch
        # - cell already used in current path
        if (
            r < 0 or c < 0 or
            r >= self.ROWS or c >= self.COLS or
            self.board[r][c] != self.word[i] or
            (r, c) in self.path
        ):
            return False

        # ---- CHOOSE ----
        # We "take" this cell as part of our current path
        # Mark it as visited so we don't reuse it in THIS path
        self.path.add((r, c))

        # ---- EXPLORE ----
        # Try all 4 directions to match the next character
        res = (
            self.dfs(r + 1, c, i + 1) or
            self.dfs(r - 1, c, i + 1) or
            self.dfs(r, c + 1, i + 1) or
            self.dfs(r, c - 1, i + 1)
        )

        # ---- BACKTRACK (UN-CHOOSE) ----
        # Remove the cell from path AFTER exploring
        # This is the key idea:
        # - The cell should only be blocked for THIS recursive path
        # - Other paths should still be able to use it
        #
        # Without this step:
        # - once a cell is used, it would remain blocked forever
        # - and we would incorrectly miss valid paths
        self.path.remove((r, c))

        return res