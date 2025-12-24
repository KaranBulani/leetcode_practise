'''
####################################################################################################
########################################### My Solution ############################################
####################################################################################################

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        used = [[False] * col for _ in range(row)]
        self.res = False

        def backtrack(index: int, x: int, y: int):
            if self.res:
                return True

            if used[x][y]:
                return

            if board[x][y] != word[index]:
                return

            if index == len(word) - 1:
                self.res = True
                return

            used[x][y] = True

            #move up
            if x > 0:
                backtrack(index + 1, x - 1, y)
            #move down
            if x < row - 1:
                backtrack(index + 1, x + 1, y)
            #move left
            if y > 0:
                backtrack(index + 1, x, y - 1)
            #move right
            if y < col - 1:
                backtrack(index + 1, x, y + 1)

            used[x][y] = False

        #start backtracking through each char
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    backtrack(0, r, c)
                    if self.res:
                        return True
        return False

####################################################################################################
############################ ChatGPT Solution (Clubbed Used & direction ############################
####################################################################################################

Time complexity:  O(m × n × 3^L)						 		For each board we start backtrack

    1. Starting points
       * You may start DFS from every cell in the board: m × n

    2. DFS branching
       * From each cell, you can explore up to 4 directions.
       * After the first move, you cannot go back to the previous cell, so branching is effectively ≤ 3.

    3. Depth of recursion
       * Maximum depth = L (length of the word)

Space complexity: O(L) + O(mn)  		 						For Recursive Stack, used Array
'''

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        used = [[False] * col for _ in range(row)]
        self.res = False

        def backtrack(index: int, x: int, y: int):
            if self.res:
                return
            if board[x][y] != word[index]:
                return
            if index == len(word) - 1:
                self.res = True
                return

            used[x][y] = True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not used[nx][ny]:
                    backtrack(index + 1, nx, ny)

            used[x][y] = False

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    backtrack(0, r, c)
                    if self.res:
                        return True
        return False

if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    boards_and_words = [
        # Example 1
        (
            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],
            "ABCCED"
        ),
        # Example 2
        (
            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],
            "SEE"
        ),
        # Example 3
        (
            [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]],
            "ABCB"
        ),

        # ---- Additional edge cases ----

        # Single cell board, word matches
        ([["A"]], "A"),

        # Single cell board, word does not match
        ([["A"]], "B"),

        # Single row board
        ([["A", "B", "C", "D"]], "ABCD"),

        # Single column board
        ([["A"], ["B"], ["C"], ["D"]], "ABCD"),

        # Word requires revisiting a cell (not allowed)
        (
            [["A", "A", "A"],
             ["A", "B", "A"],
             ["A", "A", "A"]],
            "ABAA"
        ),

        # Word longer than total cells (impossible)
        (
            [["A", "B"],
             ["C", "D"]],
            "ABCDE"
        ),

        # Word with repeated letters but valid path
        (
            [["A", "B", "B", "A"]],
            "ABBA"
        ),

        # Larger grid with diagonal temptation (should not count)
        (
            [["A", "B", "C"],
             ["D", "E", "F"],
             ["G", "H", "I"]],
            "AEI"
        ),
    ]

    for i, (board, word) in enumerate(boards_and_words, 1):
        result = solution.exist(board, word)
        print(f"Test Case {i}: {result}")