class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, HashSet<Character>> rows = new HashMap<>();
        Map<Integer, HashSet<Character>> cols = new HashMap<>();
        Map<String, HashSet<Character>> square = new HashMap<>();
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                String squareKey = Math.floor(r / 3) + "," + Math.floor(c / 3);
                if (!rows.containsKey(r))  {
                    rows.put(r, new HashSet<>());
                }
                if (!cols.containsKey(c))  {
                    cols.put(c, new HashSet<>());
                }
                if (!square.containsKey(squareKey))    {
                    square.put(squareKey, new HashSet<>());
                }
                if ((rows.get(r)).contains(board[r][c]) || (cols.get(c)).contains(board[r][c])
                        || (square.get(squareKey)).contains(board[r][c]))   {
                    return false;
                }
                rows.get(r).add(board[r][c]);
                cols.get(c).add(board[r][c]);
                square.get(squareKey).add(board[r][c]);
            }
        }
        return true;
    }
}
