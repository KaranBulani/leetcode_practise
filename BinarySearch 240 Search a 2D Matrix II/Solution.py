'''
Approach 1 — Binary Search each row

Since every row is sorted, perform binary search on every row.

    For each row: O(log n)
    There are m rows.

    Overall: O(m log n)
    Space: O(1)

class Solution:
    def binary_search(self, row, target):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        for row in matrix:
            if target < row[0] or target > row[-1]:
                continue
            if self.binary_search(row, target):
                return True
        return False

####################################################################################################

Approach 2 — Staircase Search

This is the intended solution.
Start from:		top-right

Example
	1   4   7  11
	2   5   8  12
	3   6   9  16
	10  13  14 17

				^
			 start

Why top-right?
Because from here,
* left becomes smaller
* down becomes larger
You always eliminate an entire row or column.

Suppose target = 6
		11
	6 < 11
	← move left

Now
		7
	6 < 7
	← move left

Now
		4
	6 > 4
	↓
	move down

Now
	5
	↓

Now
	6

Found


### Why does this work?

At position (r,c):

If
	matrix[r][c] > target

everything below is even bigger.
		7
		8
		9
		10
So the whole column can be discarded.
Move left.

If
	matrix[r][c] < target

everything left is even smaller.
1 2 3 4
      ^
So the whole row can be discarded.
Move down.

Every move removes either
* one row
* or one column

Maximum moves: m + n

Time: O(m+n)
Space: O(1)
'''
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            5,
            True
        ),

        # Example 2
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ],
            20,
            False
        ),

        # Single element (found)
        (
            [[5]],
            5,
            True
        ),

        # Single element (not found)
        (
            [[5]],
            10,
            False
        ),

        # Single row (found)
        (
            [[1, 3, 5, 7, 9]],
            7,
            True
        ),

        # Single row (not found)
        (
            [[1, 3, 5, 7, 9]],
            8,
            False
        ),

        # Single column (found)
        (
            [
                [2],
                [4],
                [6],
                [8]
            ],
            6,
            True
        ),

        # Single column (not found)
        (
            [
                [2],
                [4],
                [6],
                [8]
            ],
            5,
            False
        ),

        # Target is smallest element
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            1,
            True
        ),

        # Target is largest element
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            9,
            True
        ),

        # Target smaller than all elements
        (
            [
                [5, 6],
                [7, 8]
            ],
            1,
            False
        ),

        # Target larger than all elements
        (
            [
                [5, 6],
                [7, 8]
            ],
            100,
            False
        ),

        # Negative numbers
        (
            [
                [-10, -5, -1],
                [-8, -3, 2],
                [-6, 0, 5]
            ],
            -3,
            True
        ),

        # Negative numbers (not found)
        (
            [
                [-10, -5, -1],
                [-8, -3, 2],
                [-6, 0, 5]
            ],
            4,
            False
        ),

        # Rectangular matrix (more rows)
        (
            [
                [1, 4],
                [2, 5],
                [3, 6],
                [7, 8]
            ],
            7,
            True
        ),

        # Rectangular matrix (more columns)
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8]
            ],
            6,
            True
        ),

        # Target absent but within value range
        (
            [
                [1, 3, 5],
                [2, 4, 6],
                [7, 8, 9]
            ],
            10,
            False
        ),

        # Larger matrix
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ],
            11,
            True
        ),
    ]

    for i, (matrix, target, expected) in enumerate(test_cases, 1):
        result = solution.searchMatrix(matrix, target)
        print(f"Test Case {i}:")
        print(f"Target   = {target}")
        print(f"Expected = {expected}")
        print(f"Got      = {result}")
        print(f"Passed   = {result == expected}")
        print("-" * 50)