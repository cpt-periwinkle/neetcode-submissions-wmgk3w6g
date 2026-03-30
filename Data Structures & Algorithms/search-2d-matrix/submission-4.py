class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1
        pos_row = []

        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2
            if (matrix[row_mid][0] > target):
                row_right = row_mid - 1
            elif (matrix[row_mid][-1] < target):
                row_left = row_mid + 1
            else:
                pos_row = matrix[row_mid]
                break

        if not pos_row:
            return False

        left = 0
        right = len(pos_row) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (pos_row[mid] > target):
                right = mid - 1
            elif (pos_row[mid] < target):
                left = mid + 1
            else:
                return True

        return False