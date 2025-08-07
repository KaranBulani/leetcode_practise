'''
Time Complexity:  O(log rows + log column)              (for both Binary Search)
Space Complexity: O(1)                                  (for Variables, indexes)
'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1

        #Get which row might have target
        low, high = 0, ROWS
        mid = 0
        while low <= high:
            mid = (high + low)//2
            if matrix[mid][0] <= target <= matrix[mid][COLS]:
                break
            elif target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][COLS]:
                low = mid + 1

        #Check if value is present on that row
        low, high = 0, COLS
        new_row = mid
        while low <= high:
            mid = (high + low)//2
            if matrix[new_row][mid] == target:
                return True
            elif matrix[new_row][mid] > target:
                high = mid - 1
            elif matrix[new_row][mid] < target:
                low = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()

    # Each tuple is: (matrix, target, expected_result)
    test_cases = [
        # Prompt examples
        (
            [[1,3,5,7],
             [10,11,16,20],
             [23,30,34,60]],
            3,
            True
        ),
        (
            [[1,3,5,7],
             [10,11,16,20],
             [23,30,34,60]],
            13,
            False
        ),

        # Single-cell matrix
        ([[1]], 1, True),
        ([[1]], 2, False),

        # Single row
        ([[-5, -3, 0, 2]], 0, True),
        ([[-5, -3, 0, 2]], 3, False),

        # Single column
        ([[1], [3], [5]], 5, True),
        ([[1], [3], [5]], 2, False),

        # First & last elements
        (
            [[2, 4, 6],
             [8, 10, 12]],
            2,
            True
        ),
        (
            [[2, 4, 6],
             [8, 10, 12]],
            12,
            True
        ),

        # Non-existent values around the gaps
        (
            [[1, 2, 3],
             [5, 6, 7],
             [9, 10, 11]],
            4,
            False
        )
    ]

    for matrix, target, expected in test_cases:
        result = solution.searchMatrix(matrix, target)
        print(f"matrix={matrix}, target={target} -> {result} (expected: {expected})")