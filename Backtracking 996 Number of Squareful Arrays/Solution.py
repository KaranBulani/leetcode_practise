'''
Time complexity: O(n * n!)

n!
 * Number of permutations = nPr = n! / (n−r)!
   3P3 = 3!
   But n! counts how many complete permutations exist, NOT how much work is done to build them.
n
 * To build each permutation:
   We need to make n recursive decisions.
So it can be said that for each n! permutation we had to go through n steps, making it O(n * n!)

Space complexity: O(n * n!)

Recursion stack
* Depth = n
  → O(n)

currPath
* Size up to n
  → O(n)

numCounter
* Stores up to n distinct elements
  → O(n)

res
* You store all valid squareful permutations
  Worst case: all permutations are valid
  Number of permutations = n!
  Each permutation costs O(n) space
'''
import math
from typing import List
from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        numCounter = Counter(nums)
        res = []
        currPath = []

        def dfs(start: int):
            if start == len(nums):
                res.append(currPath.copy())

            for num in numCounter:
                # Check if current num will form squareful
                squareful = num + currPath[-1] if currPath else 0
                k = int(math.sqrt(squareful))

                if not k * k == squareful:
                    continue

                if numCounter[num] > 0:
                    currPath.append(num)
                    numCounter[num] -= 1

                    dfs(start + 1)

                    currPath.pop()
                    numCounter[num] += 1

        dfs(0)
        return len(res)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples from the problem
        [1, 17, 8],
        [2, 2, 2],

        # Single element (always squareful)
        [0],
        [1],
        [999999999],

        # Two elements
        [1, 3],  # 1 + 3 = 4 (perfect square)
        [1, 2],  # 1 + 2 = 3 (not a perfect square)

        # Duplicate-heavy inputs
        [1, 1, 1],
        [2, 2, 3, 3],
        [8, 8, 8],

        # Mixed values
        [1, 8, 17, 8],
        [0, 1, 4],
        [4, 5, 6],

        # Larger permutations
        [1, 1, 8, 8],
        [2, 3, 6, 7],
        [18, 7, 11],

        # Edge values
        [0, 0, 0],
        [10 ** 9, 10 ** 9],
        [10 ** 9, 1, 999999999],

        # Stress-style small but branching
        [1, 4, 9, 16],
        [2, 7, 9, 16]
    ]

    for i, nums in enumerate(test_cases, 1):
        result = solution.numSquarefulPerms(nums)
        print(f"Test case {i}: nums = {nums}")
        print(f"Output: {result}")
        print("-" * 50)