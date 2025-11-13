'''
Time complexity:                O(9^81)  					For each 81 spots we can fit 1-9.
                                → ~10⁷⁷ tries

Practical Time complexity:      Due to pruning as some spots are already filled
                                O(branching_factor^empty_cells)
                                where branching_factor is usually 1–3, not 9.

Space complexity:               Board: O(81) → O(1)
                                Sets → 9 row, column, box with each having 9 digits
                                       27 sets × 9 digits = 243 ≈ O(1)
                                Recursion Stack: At most 81 calls deep O(81) = O(1)
'''

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        '''
        (0, 0) -> 0   (0, 1) -> 0   (0, 2) -> 0   (0, 3) -> 1   (0, 4) -> 1   (0, 5) -> 1   (0, 6) -> 2   (0, 7) -> 2   (0, 8) -> 2
        (1, 0) -> 0   (1, 1) -> 0   (1, 2) -> 0   (1, 3) -> 1   (1, 4) -> 1   (1, 5) -> 1   (1, 6) -> 2   (1, 7) -> 2   (1, 8) -> 2
        (2, 0) -> 0   (2, 1) -> 0   (2, 2) -> 0   (2, 3) -> 1   (2, 4) -> 1   (2, 5) -> 1   (2, 6) -> 2   (2, 7) -> 2   (2, 8) -> 2
        (3, 0) -> 3   (3, 1) -> 3   (3, 2) -> 3   (3, 3) -> 4   (3, 4) -> 4   (3, 5) -> 4   (3, 6) -> 5   (3, 7) -> 5   (3, 8) -> 5
        (4, 0) -> 3   (4, 1) -> 3   (4, 2) -> 3   (4, 3) -> 4   (4, 4) -> 4   (4, 5) -> 4   (4, 6) -> 5   (4, 7) -> 5   (4, 8) -> 5
        (5, 0) -> 3   (5, 1) -> 3   (5, 2) -> 3   (5, 3) -> 4   (5, 4) -> 4   (5, 5) -> 4   (5, 6) -> 5   (5, 7) -> 5   (5, 8) -> 5
        (6, 0) -> 6   (6, 1) -> 6   (6, 2) -> 6   (6, 3) -> 7   (6, 4) -> 7   (6, 5) -> 7   (6, 6) -> 8   (6, 7) -> 8   (6, 8) -> 8
        (7, 0) -> 6   (7, 1) -> 6   (7, 2) -> 6   (7, 3) -> 7   (7, 4) -> 7   (7, 5) -> 7   (7, 6) -> 8   (7, 7) -> 8   (7, 8) -> 8
        (8, 0) -> 6   (8, 1) -> 6   (8, 2) -> 6   (8, 3) -> 7   (8, 4) -> 7   (8, 5) -> 7   (8, 6) -> 8   (8, 7) -> 8   (8, 8) -> 8
        '''
        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        # Initialize sets
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_index(r, c)].add(val)

        def backtrack(i):
            if i == len(empties):
                return True  # solved

            r, c = empties[i]
            b = box_index(r, c)

            for d in '123456789':
                # tries to place all digits in current spot
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:

                    # place digit
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(i + 1):
                        return True

                    # undo (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
            # if no digits were possible then some mistake at prev level, return false and try something else
            return False

        backtrack(0)


if __name__ == "__main__":
    solution = Solution()

    # Example 1: From LeetCode problem statement
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print("Before solving (Example 1):")
    for row in board1:
        print(row)

    solution.solveSudoku(board1)

    print("\nAfter solving (Example 1):")
    for row in board1:
        print(row)
    print("\nExpected final board (for manual check):")
    print('[["5","3","4","6","7","8","9","1","2"],')
    print(' ["6","7","2","1","9","5","3","4","8"],')
    print(' ["1","9","8","3","4","2","5","6","7"],')
    print(' ["8","5","9","7","6","1","4","2","3"],')
    print(' ["4","2","6","8","5","3","7","9","1"],')
    print(' ["7","1","3","9","2","4","8","5","6"],')
    print(' ["9","6","1","5","3","7","2","8","4"],')
    print(' ["2","8","7","4","1","9","6","3","5"],')
    print(' ["3","4","5","2","8","6","1","7","9"]]')

    # Edge Case: Almost empty Sudoku (but still valid partial structure)
    board2 = [
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".","3",".","8","5"],
        [".",".","1",".","2",".",".",".","."],
        [".",".",".","5",".","7",".",".","."],
        [".",".","4",".",".",".","1",".","."],
        [".","9",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","7","3"],
        [".",".","2",".","1",".",".",".","."],
        [".",".",".",".","4",".",".",".","9"]
    ]

    print("\nBefore solving (Edge Case):")
    for row in board2:
        print(row)

    solution.solveSudoku(board2)

    print("\nAfter solving (Edge Case):")
    for row in board2:
        print(row)
    print("\nExpected: Should result in a valid 9x9 solved Sudoku grid with digits 1–9 in each row, column, and sub-box.")