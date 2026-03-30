class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # ---- Step 1: Binary search over rows ----
        # Goal: find the "possible row" (pos_row) where target could exist
        # Each row is sorted, and:
        # first element of a row > last element of previous row
        # → we can treat rows as sorted ranges

        row_left = 0
        row_right = rows - 1

        while row_left <= row_right:
            row_mid = row_left + (row_right - row_left) // 2

            # If target is greater than the largest element in this row,
            # it must be in a row below
            if target > matrix[row_mid][-1]:
                row_left = row_mid + 1

            # If target is smaller than the smallest element in this row,
            # it must be in a row above
            elif target < matrix[row_mid][0]:
                row_right = row_mid - 1

            # Otherwise, target lies within this row's range
            else:
                break

        # If no row satisfies the condition, target is not present
        if not (row_left <= row_right):
            return False

        # The row where target could possibly exist
        pos_row = row_mid

        # ---- Step 2: Binary search inside the selected row ----
        left = 0
        right = cols - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Standard binary search on the row
            if target > matrix[pos_row][mid]:
                left = mid + 1
            elif target < matrix[pos_row][mid]:
                right = mid - 1
            else:
                return True  # target found

        # Target not found in the possible row
        return False