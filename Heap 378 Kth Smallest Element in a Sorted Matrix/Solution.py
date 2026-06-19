'''
Approach 1: Min Heap

Idea
The matrix is sorted:
* Rows sorted left → right
* Columns sorted top → bottom
Put the first element of every row into a min heap.

Heap entry:		(value, row, col)

Pop the smallest element k-1 times.
Whenever you pop (val, r, c), push the next element in that row:		(r, c+1)
####################################################################################################

Complexity

Heap size ≤ n
Time:  O(k log n)
Space: O(n)

####################################################################################################
####################################################################################################
Approach 2 (Expected): Binary Search on Answer

Key Observation
	The answer must lie between matrix[0][0] and matrix[n-1][n-1]
	Suppose we guess: mid = 13

Can we determine:
	> How many numbers in the matrix are ≤ 13 ?
	If count ≥ k
	then answer is ≤ 13.
	Otherwise answer is > 13.
	This gives a monotonic condition ⇒ binary search.

####################################################################################################
Counting Numbers ≤ mid

Use the bottom-left corner.
Example:
1   5   9
10 11 13
12 13 15

Suppose: 	mid = 13
Start: 12 (bottom-left)

If value ≤ mid:
	Everything above it in that column is also ≤ mid.
    Add: row + 1 numbers.
    Move right.

Otherwise move up.

Count Function
	def countLessEqual(mid):
		row = n - 1
		col = 0
		count = 0

		while row >= 0 and col < n:

			if matrix[row][col] <= mid:
				count += row + 1
				col += 1
			else:
				row -= 1

		return count

Runs in: O(n)
####################################################################################################

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2

            count = 0
            row = n - 1
            col = 0

            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1
                else:
                    row -= 1

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left
####################################################################################################

Complexity

Let,
	n = matrix size
	V = maxVal - minVal

Binary search: O(log V)
Each count: O(n)

Total:
Time:  O(n log V)
Space: O(1)

'''
import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        heap = []
        for r in range(n):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        for _ in range(k - 1):
            val, r, c = heapq.heappop(heap)

            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(heap)[0]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic example
        (
            [[1,5,9],
             [10,11,13],
             [12,13,15]],
            8,
            13
        ),

        # Single element
        (
            [[-5]],
            1,
            -5
        ),

        # All elements same
        (
            [[2,2],
             [2,2]],
            3,
            2
        ),

        # k = 1 (smallest element)
        (
            [[1,3,5],
             [6,7,12],
             [11,14,14]],
            1,
            1
        ),

        # k = n*n (largest element)
        (
            [[1,3,5],
             [6,7,12],
             [11,14,14]],
            9,
            14
        ),

        # Negative numbers
        (
            [[-10,-5,0],
             [-3,1,4],
             [2,6,8]],
            5,
            1
        ),

        # Duplicates + sorted rows/cols
        (
            [[1,2,2],
             [2,3,3],
             [3,3,4]],
            6,
            3
        ),

        # Larger spread values
        (
            [[1,10,20],
             [2,15,30],
             [5,25,35]],
            7,
            25
        ),

        # Edge: k in middle with duplicates
        (
            [[1,2,3],
             [2,2,4],
             [3,5,6]],
            4,
            2
        ),

        # Edge: strictly increasing rows & cols
        (
            [[1,2,3],
             [4,5,6],
             [7,8,9]],
            5,
            5
        ),
    ]

    for i, (matrix, k, expected) in enumerate(test_cases, 1):
        result = solution.kthSmallest(matrix, k)
        print(f"Test Case {i}:")
        print(f"Input: matrix={matrix}, k={k}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"{'PASS' if result == expected else 'FAIL'}")
        print("-" * 50)