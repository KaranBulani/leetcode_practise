'''
The key observation is that we place exactly one queen per row, so we only need to track:

- cols → columns already occupied
- pos_diag → row + col diagonals
- neg_diag → row - col diagonals

####################################################################################################

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        ans = 0

        def dfs(row: int):
            nonlocal ans

            # Successfully placed queens in all rows
            if row == n:
                ans += 1
                return

            for col in range(n):
                # Check if this position is attacked
                if col in cols:
                    continue

                if row + col in pos_diag:
                    continue

                if row - col in neg_diag:
                    continue

                # Place queen
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                dfs(row + 1)

                # Backtrack
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

        dfs(0)

        return ans


####################################################################################################
How the diagonal sets work

For a cell (row, col):
	↘ diagonal: row - col
	↙ diagonal: row + col

For example, consider:
	. Q . .
	. . . Q
	Q . . .
	. . Q .

The queen at (0,1) has:
	row - col = -1
	row + col = 1


Any other cell with the same value would lie on the same diagonal.

So checking:
	row + col in pos_diag
	row - col in neg_diag
is enough to determine whether a queen can attack diagonally.

####################################################################################################
Why row doesn't need a set

We deliberately recurse like this:
	dfs(row + 1)

That means each recursive call handles exactly one row.
Therefore, when we're at row, all previous rows already contain exactly one queen.

So there is no need for:
	rows = set()


This is a common simplification compared with a solution that loops over both row and col.

####################################################################################################

Backtracking flow

For n = 4:
	row 0
	 ├── col 0
	 │    ├── row 1 ...
	 │    └── ...
	 ├── col 1
	 │    └── row 1
	 │         └── ...
	 ├── col 2
	 │    └── ...
	 └── col 3
		  └── ...


Whenever we place a queen:
	cols.add(col)
	pos_diag.add(row + col)
	neg_diag.add(row - col)

we explore that choice.

After returning:
cols.remove(col)
pos_diag.remove(row + col)
neg_diag.remove(row - col)

we undo the choice, allowing the next column to be tried.

For n = 4, the search finds exactly 2 valid configurations, so:


Input: 4
Output: 2


####################################################################################################

Complexity

There are roughly n! possible ways to place one queen in each row/column, with pruning from the diagonal checks.

- Time: O(n!) approximately
    We place one queen per row.
    - Row 1 → n choices
    - Row 2 → at most n-1 choices
    - Row 3 → at most n-2 choices
    - ...
    - Last row → 1 choice

    So the worst-case search tree is:
        n × (n-1) × (n-2) × ... × 1 = n!

    Each position check is O(1) because we use sets for columns and diagonals.

- Space: O(n) for the three sets + O(n) recursion stack → O(n)
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # row + col
        neg_diag = set()  # row - col

        def dfs(row: int) -> int:
            # One complete valid solution
            if row == n:
                return 1

            total = 0
            for col in range(n):
                if col in cols:
                    continue
                if row + col in pos_diag:
                    continue
                if row - col in neg_diag:
                    continue

                # Place queen
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)

                total += dfs(row + 1)

                # Backtrack
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)

            return total
        return dfs(0)

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # n, expected_answer
        # Given examples
        (4, 2),
        (1, 1),
        # Additional edge cases
        (2, 0),
        (3, 0),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
        (9, 352),
    ]

    for n, expected in test_cases:
        result = solution.totalNQueens(n)
        print(
            f"n = {n} | "
            f"Expected = {expected} | "
            f"Got = {result} | "
            f"{'PASS' if result == expected else 'FAIL'}"
        )