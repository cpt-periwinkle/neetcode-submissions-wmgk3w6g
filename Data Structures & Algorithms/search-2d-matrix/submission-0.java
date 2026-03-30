class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = rowSearch(matrix, 0, matrix.length - 1, matrix[0].length - 1, target);
        if (row == -1)  {
            return false;
        }
        return colSearch(0, matrix[row].length - 1, matrix[row], target);
    }

    private static int rowSearch(int[][] matrix, int top, int bottom, int cols, int target)  {
        while (true)    {
            if (top > bottom)   {
                return -1;
            }
            int midRow = top + (bottom - top)/2;
            if (target >= matrix[midRow][0] && target <= matrix[midRow][cols])  {
                return midRow;
            } else if (target < matrix[midRow][0]) {
                return rowSearch(matrix, top, midRow - 1, cols, target);
            } else if (target > matrix[midRow][cols])   {
                return rowSearch(matrix, midRow + 1, bottom, cols, target);
            }
        }
    }

    private static boolean colSearch(int lb, int ub, int[] solnArr, int target) {
        while (true)    {
            if (lb > ub)   {
                return false;
            }
            int mid = lb + (ub - lb)/2;
            if (solnArr[mid] == target)  {
                return true;
            } else if (target < solnArr[mid]) {
                return colSearch(lb, mid - 1, solnArr, target);
            } else  {
                return colSearch(mid + 1, ub, solnArr, target);
            }
        }
    }
}
