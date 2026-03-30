class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Binary search to find the correct row
        row_left = 0
        row_right = rows - 1
        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2

            if target > matrix[row_mid][-1]:
                row_left = row_mid + 1
            elif target < matrix[row_mid][0]:
                row_right = row_mid - 1
            else:
                break

        # If no valid row found
        if not (row_left <= row_right):
            return False

        # Row is determined
        pos_row = row_mid

        # Binary search inside the row
        left, right = 0, cols - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target > matrix[pos_row][mid]:
                left = mid + 1
            elif target < matrix[pos_row][mid]:
                right = mid - 1
            else:
                return True

        return False