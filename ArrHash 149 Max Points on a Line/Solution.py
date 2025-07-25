'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

149. Max Points on a Line

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # From prompt
        ([[1,1],[2,2],[3,3]], 3),
        ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),

        # Minimal input
        ([[0,0]], 1),                         # only one point

        # Two points always lie on a line
        ([[0,0],[1,1]], 2),

        # Vertical line
        ([[-1,2],[-1,-3],[-1,0],[5,5]], 3),   # three with x == -1

        # Horizontal line
        ([[2,5],[-1,5],[0,5],[3,4]], 3),      # three with y == 5

        # Mixed positive & negative
        ([[-2,-2],[-1,-1],[0,0],[1,1],[2,2],[2,1]], 5),

        # No three collinear except trivial pairs
        ([[0,0],[1,2],[2,5],[3,7]], 2),
    ]

    for i, (points, expected) in enumerate(test_cases, start=1):
        result = solution.maxPoints(points)
        print(f"Case {i}: points = {points}")
        print(f"  → expected = {expected}, got = {result}")
        print("-" * 60)