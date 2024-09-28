import java.util.HashSet;

class Solution36 {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] rowSet = new HashSet[9];
        HashSet<Character>[] colSet = new HashSet[9];
        HashSet<Character>[] squareSet = new HashSet[9];

        // Initialize the sets for rows, columns, and squares
        for (int i = 0; i < 9; i++) {
            rowSet[i] = new HashSet<>();
            colSet[i] = new HashSet<>();
            squareSet[i] = new HashSet<>();
        }

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char value = board[row][col];

                if (value == '.') {
                    continue; // Skip empty cells
                }

                // Check row, column, and 3x3 square for duplicates
                if (rowSet[row].contains(value) || colSet[col].contains(value) || squareSet[(row / 3) * 3 + (col / 3)].contains(value)) {
                    return false;
                }

                // Add the value to the corresponding sets
                rowSet[row].add(value);
                colSet[col].add(value);
                squareSet[(row / 3) * 3 + (col / 3)].add(value);
            }
        }
        return true; // The board is valid
    }

    public static void main(String[] args) {
        Solution36 solution = new Solution36();

        char[][] board = {
                {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
                {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
                {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
                {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
                {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
                {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
                {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
                {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
                {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };

        boolean result = solution.isValidSudoku(board);
        System.out.println(result);  // Should print true or false
    }
}
