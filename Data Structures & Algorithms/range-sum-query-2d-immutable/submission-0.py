class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.dp = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]

        for r in range(self.ROWS):
            for c in range(self.COLS):
                up_val = self.dp[r - 1][c] if r > 0 else 0
                left_val = self.dp[r][c - 1] if c > 0 else 0
                overlap_val = self.dp[r - 1][c - 1] if r > 0 and c > 0 else 0
                self.dp[r][c] = up_val + left_val + matrix[r][c] - overlap_val
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self.dp[row1 - 1][col2] if row1 > 0 else 0
        left = self.dp[row2][col1 - 1] if col1 > 0 else 0
        overlap = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] - up - left + overlap

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)