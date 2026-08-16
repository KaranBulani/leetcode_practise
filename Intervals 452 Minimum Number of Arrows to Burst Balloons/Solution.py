'''
### Key idea

    If we sort balloons by their end coordinate, we can always shoot an arrow at the end of the first balloon.
    That arrow will burst every subsequent balloon whose start is <= arrow_position.

    If we encounter a balloon with: 	start > arrow_position
    then the current arrow cannot burst it, so we need another arrow.

### Example
    points = [[10,16],[2,8],[1,6],[7,12]]
    Sort by ending point:
        [1,6]
        [2,8]
        [7,12]
        [10,16]

    Start with:
        arrow_position = 6
        arrows = 1
    * [2,8] → 2 <= 6 → already burst
    * [7,12] → 7 > 6 → need another arrow at 12
    * [10,16] → 10 <= 12 → already burst

    Therefore:		answer = 2

### Why sort by end?
    The important greedy choice is:
    > When we need an arrow, place it as far left as possible while still bursting the current balloon.

    For the first balloon after sorting, its right endpoint is the best position. Putting the arrow anywhere further right could make us lose the ability to burst future balloons.

### Complexity
    Sorting dominates:
        Time:  O(n log n)
        Space: O(1) auxiliary space

    The distinction from 435. Non-overlapping Intervals is that here we're counting how many groups of overlapping intervals we need, rather than how many intervals to remove.

'''

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_position = points[0][1]

        for start, end in points[1:]:
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows

if __name__ == "__main__":
    solution = Solution()

    # ---------------------------------------------------------
    # Diverse examples from the question
    # ---------------------------------------------------------

    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    # Expected: 4
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)


    # ---------------------------------------------------------
    # Requested test cases
    # ---------------------------------------------------------

    points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    # Expected: 3
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[0, 10], [20, 30], [40, 50], [60, 70]]
    # Expected: 4
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[-10, -5], [-7, 0], [2, 5], [7, 10]]
    # Expected: 4
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[100, 200], [150, 250], [180, 220], [210, 230]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[-50, -40], [-30, -20], [-10, 0], [10, 20], [30, 40]]
    # Expected: 5
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[500, 510], [520, 530], [540, 550], [560, 570], [580, 590]]
    # Expected: 5
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    # Expected: 3
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]
    # Expected: 5
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)


    # ---------------------------------------------------------
    # Edge cases
    # ---------------------------------------------------------

    points = []
    # Expected: 0
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[-2147483646, -2147483645],
              [2147483646, 2147483647]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    # Expected: 4
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[1, 2]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)

    points = [[2, 3], [2, 3]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)


    # ---------------------------------------------------------
    # Additional useful edge cases
    # ---------------------------------------------------------

    # All balloons completely overlapping
    points = [[1, 10], [2, 9], [3, 8], [4, 7], [5, 6]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)

    # Same start, different ends
    points = [[1, 2], [1, 5], [1, 10], [1, 20]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)

    # Same end, different starts
    points = [[1, 10], [2, 10], [5, 10], [8, 10]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)

    # Chain of overlapping intervals where one arrow cannot burst all
    points = [[1, 4], [2, 5], [3, 6], [7, 10]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    # Negative and positive coordinates with overlap
    points = [[-10, 0], [-5, 5], [0, 10], [5, 15]]
    # Expected: 2
    result = solution.findMinArrowShots(points)
    print(result)

    # One large interval covering all others
    points = [[0, 100], [10, 20], [30, 40], [50, 60], [70, 80]]
    # Expected: 4
    result = solution.findMinArrowShots(points)
    print(result)

    # Exact touching boundaries
    points = [[1, 2], [2, 2], [2, 3]]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)

    # Large number of overlapping balloons
    points = [[i, i + 100] for i in range(0, 1000, 10)]
    # Expected: 1
    result = solution.findMinArrowShots(points)
    print(result)