class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # (r // 3, c // 3) -> Each box is an index, with each box having a coordinate with a 0, 1, 2 creating tuple

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in cols[c] or val in rows[r] or val in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                key = (r//3, c//3)
                squares[key].add(val)

        return True
