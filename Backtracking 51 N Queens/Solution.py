'''
Time complexity:  O(n!) 					because for each row, you can choose up to N columns (minus constraints).
Space complexity: O(n^2) + O(n) 			for board + recursion stack
'''

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["."] * n for _ in range(n)]  # Step 1: initialize empty n×n board
        res = []

        cols = set()  # columns with queens
        diag1 = set()  # main diagonals (r - c) ↘ or ↖
        diag2 = set()  # anti-diagonals (r + c) ↙ or ↗

        def backtrack(r: int):
            # Step 3: base case — all queens placed
            if r == n:
                # convert board to list of strings and save
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                # Step 4: check if cell is attacked
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue  # skip attacked cell

                # Place queen
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = "Q"

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack (remove queen)
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
                board[r][c] = "."

        backtrack(0)
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1: Small standard case (from question)
    n = 4
    result = solution.solveNQueens(n)
    print(f"Input: n = {n}")
    print("Output:", result)
    # Expected (any order):
    # [[".Q..","...Q","Q...","..Q."],
    #  ["..Q.","Q...","...Q",".Q.."]]

    print("-" * 80)

    # Example 2: Smallest possible board (edge case)
    n = 1
    result = solution.solveNQueens(n)
    print(f"Input: n = {n}")
    print("Output:", result)
    # Expected:
    # [["Q"]]

    print("-" * 80)

    # Example 3: No possible solution (odd edge)
    n = 2
    result = solution.solveNQueens(n)
    print(f"Input: n = {n}")
    print("Output:", result)
    # Expected:
    # []  (no valid arrangement)

    print("-" * 80)

    # Example 4: Another no-solution edge
    n = 3
    result = solution.solveNQueens(n)
    print(f"Input: n = {n}")
    print("Output:", result)
    # Expected:
    # []  (no valid arrangement)

    print("-" * 80)

    # Example 5: Slightly larger test
    n = 5
    result = solution.solveNQueens(n)
    print(f"Input: n = {n}")
    print("Number of solutions:", len(result))
    # Expected count (not layout): 10
    # Actual board layouts depend on your implementation order.