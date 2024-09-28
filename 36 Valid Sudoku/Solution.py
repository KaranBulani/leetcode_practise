'''
Time Complexity: O(1) or O(n) where n is row*column which is indeed 81
Space Complexity: O(3n) Every element is part of row/col/sqw

if not using defaultdict(set) can use below
rows, columns, square = {}, {}, {}
if r not in rows:
    rows[r] = set()
if c not in columns:
    columns[c] = set()
if (r//3, c//3) not in square:
    square[(r//3, c//3)] = set()
'''
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sqr_dict = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in row_dict[row] or board[row][col] in col_dict[col] or board[row][col] in sqr_dict[(row//3,col//3)]:
                    return False
                row_dict[row].add(board[row][col])
                col_dict[col].add(board[row][col])
                sqr_dict[(row//3,col//3)].add(board[row][col])
        return True

if __name__ == "__main__":
    solution = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    board1 =[["8", "3", ".", ".", "7", ".", ".", ".", "."]
           , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
           , [".", "9", "8", ".", ".", ".", ".", "6", "."]
           , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
           , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
           , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
           , [".", "6", ".", ".", ".", ".", "2", "8", "."]
           , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
           , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    result = solution.isValidSudoku(board)
    print(result)