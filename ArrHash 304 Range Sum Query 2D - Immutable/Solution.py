'''
				0  0  0  0
	1 2 3	 	0  1  3  6
	4 5 6	->	0  5 12 21
	7 8 9       0 12 27 45

Time complexity:  O(n)					for prefix sum calculculation
Space complexity: O(n)					for prefix sum
'''
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            self.prefix = []
            return

        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (
                        matrix[r][c]
                        + self.prefix[r][c + 1]
                        + self.prefix[r + 1][c]
                        - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.prefix:
            return 0
        return (
                self.prefix[row2 + 1][col2 + 1]
                - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1]
                + self.prefix[row1][col1]
        )


if __name__ == "__main__":
    # Example from the problem statement
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(2, 1, 4, 3))  # Expected: 8
    print(obj.sumRegion(1, 1, 2, 2))  # Expected: 11
    print(obj.sumRegion(1, 2, 2, 4))  # Expected: 12

    print("\n--- Additional Edge Cases ---")

    # ✅ Single cell (smallest possible region)
    print(obj.sumRegion(0, 0, 0, 0))  # Expected: 3

    # ✅ Entire matrix
    print(obj.sumRegion(0, 0, 4, 4))  # Expected: 58

    # ✅ Single row
    print(obj.sumRegion(2, 0, 2, 4))  # Expected: 9  (1+2+0+1+5)

    # ✅ Single column
    print(obj.sumRegion(0, 1, 4, 1))  # Expected: 9  (0+6+2+1+0)

    # ✅ Top-left submatrix (corner region)
    print(obj.sumRegion(0, 0, 1, 1))  # Expected: 14 (3+0+5+6)

    # ✅ Region including negatives (test with new matrix)
    matrix2 = [
        [1, -1],
        [-1, 1]
    ]
    obj2 = NumMatrix(matrix2)
    print(obj2.sumRegion(0, 0, 1, 1))  # Expected: 0  (1-1-1+1)
    print(obj2.sumRegion(0, 1, 1, 1))  # Expected: 0  (-1+1)
    print(obj2.sumRegion(1, 0, 1, 0))  # Expected: -1

    # ✅ Larger random-style case
    matrix3 = [
        [2, 4, 6],
        [1, 3, 5],
        [7, 9, 11]
    ]
    obj3 = NumMatrix(matrix3)
    print(obj3.sumRegion(0, 0, 2, 2))  # Expected: 48 (sum of all)
    print(obj3.sumRegion(1, 1, 2, 2))  # Expected: 28 (3+5+9+11)
    print(obj3.sumRegion(0, 2, 2, 2))  # Expected: 22 (6+5+11)