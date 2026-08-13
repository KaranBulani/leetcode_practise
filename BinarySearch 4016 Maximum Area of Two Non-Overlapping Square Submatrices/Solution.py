'''
1. What are we binary searching?

Suppose we ask:
> Can I place two non-overlapping valid squares of side k?

If the answer is True for k, then it must also be True for every smaller side length.
For example:
	k = 5  -> True
	k = 4  -> True
	k = 3  -> True
	k = 2  -> True
	k = 1  -> True

Therefore the answers look like:
	 True True True True False False False
					  ↑
				  maximum k

So binary search works.

####################################################################################################
2. How do we know whether a square is valid?

For a square with top-left corner (r, c) and side k, we need:
	mat[r][c] = 1
	mat[r][c+1] = 1
	...

Every cell must be 1.
Checking all k² cells for every square would be too expensive.
Instead, build a 2D prefix sum.

Define:		prefix[i][j]
as the sum of all cells in the rectangle from (0,0) to (i-1,j-1).

Then the sum of any square can be calculated in O(1).
For a square:		(r, c) -> (r+k-1, c+k-1)

its sum is:
	total = (
		prefix[r+k][c+k]
		- prefix[r][c+k]
		- prefix[r+k][c]
		+ prefix[r][c]
	)

If:
	total == k * k

then every cell in that square is 1.
####################################################################################################
3. The important part: detecting two non-overlapping squares

Suppose for a particular k, we find these valid top-left corners:\
	(1, 2)
	(2, 5)
	(5, 3)
	(7, 8)
We don't actually need to compare every pair.

We only need:
	min_row
	max_row
	min_col
	max_col

For the above:
	min_row = 1
	max_row = 7

	min_col = 2
	max_col = 8

Now ask:
Can they be separated vertically?

If:
	max_row - min_row >= k
then yes.

For example, if k = 3:
	square A starts at row 1
	square B starts at row 7

	difference = 7 - 1 = 6 >= 3
The two squares cannot overlap vertically.

####################################################################################################

Or can they be separated horizontally?

Similarly:
	max_col - min_col >= k

If this is true, we can choose the squares with the minimum and maximum columns, and they cannot overlap horizontally.

Therefore:
	return max_row - min_row >= k or max_col - min_col >= k

That's the entire trick.

####################################################################################################
4. Why don't we need to check every pair?

This is the clever part.

Suppose:
	max_row - min_row >= k

We know there exists:
	one valid square whose top-left row = min_row

and
	one valid square whose top-left row = max_row

Their vertical distance is at least k.

A square occupying rows: 	r ... r+k-1
and another starting at:		r+k ...
cannot share a row, so they definitely cannot share a cell.

The columns don't matter.
Same argument applies horizontally.
So we don't need to know the exact positions of all valid squares — just their extremes.

####################################################################################################
5. Complexity

Let:		m, n <= 500

Prefix sum
We visit every cell once:		O(mn)

can(k)
We examine every possible top-left corner:		O((m-k+1)(n-k+1))

which is at most:		O(mn)

Each square check is O(1) because of prefix sums.

Binary search
There are:		O(log(min(m,n)))	checks.

Therefore total:		O(mn log(min(m,n)))


With 500 × 500:
	250,000 × log₂(500)
	≈ 250,000 × 9
	≈ 2.25 million

which is easily manageable.

Space:		O(mn)	for the prefix sum.
'''

from typing import List
class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # Build 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                prefix[r + 1][c + 1] = (
                    mat[r][c]
                    + prefix[r][c + 1]
                    + prefix[r + 1][c]
                    - prefix[r][c]
                )

        def can(k):
            min_row = m
            max_row = -1
            min_col = n
            max_col = -1

            target = k * k

            # Try every possible top-left corner
            for r in range(m - k + 1):
                for c in range(n - k + 1):

                    # Sum of k x k square
                    total = (
                        prefix[r + k][c + k]
                        - prefix[r][c + k]
                        - prefix[r + k][c]
                        + prefix[r][c]
                    )

                    # This square consists entirely of 1s
                    if total == target:
                        min_row = min(min_row, r)
                        max_row = max(max_row, r)
                        min_col = min(min_col, c)
                        max_col = max(max_col, c)

            # No valid square, or only one position
            if max_row == -1:
                return False

            # Two valid squares can be separated vertically
            if max_row - min_row >= k:
                return True

            # Two valid squares can be separated horizontally
            if max_col - min_col >= k:
                return True

            return False

        # Binary search for maximum k
        low = 1
        high = min(m, n)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans * ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[1, 1, 1, 0],
             [1, 1, 1, 1],
             [0, 0, 1, 1]],
            4
        ),

        # Example 2
        (
            [[0, 1],
             [1, 0]],
            1
        ),

        # Example 3
        (
            [[0, 0],
             [0, 1]],
            0
        ),

        # Edge Case 1: Single cell
        (
            [[1]],
            0
        ),

        # Edge Case 2: Single row, two usable cells
        (
            [[1, 1]],
            1
        ),

        # Edge Case 3: Single column, two usable cells
        (
            [[1],
             [1]],
            1
        ),

        # Edge Case 4: Two separate 2x2 squares
        (
            [[1, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 1, 1],
             [0, 0, 1, 1]],
            4
        ),

        # Edge Case 5: Entire matrix is usable
        # Multiple 2x2 squares can be placed without overlap
        (
            [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]],
            4
        ),

        # Edge Case 6: Only one large square exists
        (
            [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]],
            1
        ),

        # Edge Case 7: Four isolated usable cells
        (
            [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]],
            1
        ),

        # Edge Case 8: Two horizontal 2x2 squares
        (
            [[1, 1, 1, 1],
             [1, 1, 1, 1]],
            4
        ),

        # Edge Case 9: Two vertical 2x2 squares
        (
            [[1, 1],
             [1, 1],
             [1, 1],
             [1, 1]],
            4
        ),

        # Edge Case 10: All zeros
        (
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            0
        ),
    ]

    for i, (mat, expected) in enumerate(test_cases, 1):
        result = solution.maxArea(mat)

        print(f"Test Case {i}:")
        print(f"Input:    {mat}")
        print(f"Expected: {expected}")
        print(f"Got:      {result}")
        print(f"PASS:     {result == expected}")
        print("-" * 50)