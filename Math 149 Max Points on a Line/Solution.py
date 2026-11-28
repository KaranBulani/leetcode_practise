'''
Time Complexity:  O(n^2)            (for 2 for loop)
Space Complexity: O(n)              (for count dictionary in the worst case every point from p1 has a distinct slope)

Instead of --> count = {}
           --> There’s no restriction or hint to Python or to IDEs/type checkers (like mypy) about what types the keys/values should be.

Can use    --> count: dict[float, int] = {}
           --> It doesn't enforce the type at runtime (Python doesn't throw an error), but tools like mypy will catch misuse during static analysis.
'''

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        # If there's at least one point, the minimum max on a line is 1
        res = 1

        # Iterate over each point p1 as the “anchor”
        for i in range(len(points)):
            p1 = points[i]
            # For each anchor, use a hashmap to count how many other points
            # share the same slope relative to p1
            count = {}

            # Compare to every subsequent point p2
            for j in range(i + 1, len(points)):
                p2 = points[j]

                # If x-coordinates are the same, it’s a vertical line → slope = ∞
                if p1[0] == p2[0]:
                    slope = float("inf")
                else:
                    # Compute slope = Δy / Δx
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                # Increment the number of points seen at this slope from p1
                count[slope] = 1 + count.get(slope, 0)

                # +1 to include the anchor point itself
                res = max(res, count[slope] + 1)

        return res

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