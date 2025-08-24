'''
Very Similar to LC 300, LC 354

Time Complexity:  O(n^2)              	(for i, j)
Space Complexity: O(n)              	(for DP array)

Why it works?
  *  Sorting each cuboid handles rotations.
  *  Global sort ensures when we’re at i, any j < i is a valid “candidate below” if each dimension fits.
  *  The DP is exactly LIS on 3 keys, but we sum heights instead of counting length.
'''

from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Normalize rotations: sort dimensions within each cuboid
        for c in cuboids:
            c.sort()
        # Sort all cuboids to enable DP (nondecreasing by x,y,z)
        # First, it compares the first element of each sublist.
        # If those are equal, it moves on to the second element, and so on.
        cuboids.sort()

        n = len(cuboids)
        dp = [0] * n

        for i in range(n):
            # height contributed by this cuboid (its largest side after sorting)
            dp[i] = cuboids[i][2]
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                        cuboids[j][1] <= cuboids[i][1] and
                        cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        return max(dp)

if __name__ == "__main__":
    solution = Solution()

    # Example 1: From the problem statement
    cuboids1 = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]
    print(solution.maxHeight(cuboids1))  # Expected: 190

    # Example 2: From the problem statement
    cuboids2 = [[38, 25, 45], [76, 35, 3]]
    print(solution.maxHeight(cuboids2))  # Expected: 76

    # Example 3: From the problem statement
    cuboids3 = [[7, 11, 17], [7, 17, 11], [11, 7, 17],
                [11, 17, 7], [17, 7, 11], [17, 11, 7]]
    print(solution.maxHeight(cuboids3))  # Expected: 102

    # Edge Case 1: Single cuboid only
    cuboids4 = [[10, 20, 30]]
    print(solution.maxHeight(cuboids4))  # Expected: 30

    # Edge Case 2: All cuboids identical
    cuboids5 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    print(solution.maxHeight(cuboids5))  # Expected: 15

    # Edge Case 3: Cannot stack at all (different sizes)
    cuboids6 = [[10, 20, 30], [40, 50, 60]]
    print(solution.maxHeight(cuboids6))  # Expected: 60

    # Edge Case 4: Increasing dimensions (perfect stack)
    cuboids7 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    print(solution.maxHeight(cuboids7))  # Expected: 12

    # Edge Case 5: Max constraints (n = 100) - small repetitive pattern
    cuboids8 = [[100, 100, 100]] * 100
    print(solution.maxHeight(cuboids8))  # Expected: 10000