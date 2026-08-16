'''
The key idea is Greedy + Sorting.

We want to remove the minimum number of intervals so that the remaining intervals don't overlap.

Instead of thinking:
> "Which intervals should I remove?"

think:
> "Which intervals should I keep?"

For two overlapping intervals, we should keep the one that ends earlier, because it leaves more room for future intervals.

Greedy strategy

1. Sort intervals by their end time.
2. Keep track of the end of the last interval we accepted.
3. For every interval:
   * If start >= previous_end, it doesn't overlap → keep it.
   * Otherwise, it overlaps → remove it.

### Example
intervals = [[1,2], [2,3], [1,3]]

Sort by end:
[1,2]
[2,3]
[1,3]

Process:
[1,2] → keep
[2,3] → keep     (2 >= 2)
[1,3] → remove   (1 < 2)

Answer: 1

### Why sorting by end works

Suppose we have:
[1,10]
[2,3]
Both can't be kept.

If we keep [1,10]:
1 -------- 10
we have very little room for subsequent intervals.

If we keep [2,3]:
  2 -- 3
we have much more room.

So when intervals overlap, the interval with the smaller end is always the better one to keep.

### Complexity

Sorting: O(n log n)
Single pass: O(n)

Overall:
Time:  O(n log n)
Space: O(1) auxiliary

The important greedy pattern to remember is:
> For interval scheduling problems, sorting by ending time and keeping the earliest-finishing interval is often the optimal strategy.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prev_end = float("-inf")
        removals = 0

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                removals += 1

        return removals


if __name__ == "__main__":
    solution = Solution()

    # DiverseExamplesFromQuestion
    test_cases = [
        # Example 1
        {
            "intervals": [[1, 2], [2, 3], [3, 4], [1, 3]],
            "expected": 1
        },

        # Example 2
        {
            "intervals": [[1, 2], [1, 2], [1, 2]],
            "expected": 2
        },

        # Example 3
        {
            "intervals": [[1, 2], [2, 3]],
            "expected": 0
        },

        # Single interval
        {
            "intervals": [[1, 2]],
            "expected": 0
        },

        # Two completely overlapping intervals
        {
            "intervals": [[1, 5], [2, 3]],
            "expected": 1
        },

        # Two identical intervals
        {
            "intervals": [[1, 5], [1, 5]],
            "expected": 1
        },

        # Intervals touching at endpoints are allowed
        {
            "intervals": [[1, 2], [2, 3], [3, 4], [4, 5]],
            "expected": 0
        },

        # One large interval overlapping many smaller intervals
        {
            "intervals": [[1, 10], [2, 3], [3, 4], [4, 5], [5, 6]],
            "expected": 1
        },

        # Multiple overlapping intervals
        {
            "intervals": [[1, 3], [2, 4], [3, 5], [4, 6]],
            "expected": 2
        },

        # Same start, different end
        {
            "intervals": [[1, 4], [1, 3], [1, 2]],
            "expected": 2
        },

        # Same end, different start
        {
            "intervals": [[1, 5], [2, 5], [3, 5]],
            "expected": 2
        },

        # Negative values
        {
            "intervals": [[-5, -3], [-4, -2], [-2, 0]],
            "expected": 1
        },

        # Completely separate intervals
        {
            "intervals": [[1, 2], [5, 6], [10, 20]],
            "expected": 0
        },

        # Nested intervals
        {
            "intervals": [[1, 10], [2, 9], [3, 8], [4, 7]],
            "expected": 3
        },

        # Chain of overlapping intervals
        {
            "intervals": [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]],
            "expected": 2
        },

        # Unsorted input
        {
            "intervals": [[5, 7], [1, 2], [3, 4], [2, 3]],
            "expected": 0
        },

        # All intervals overlap at the same region
        {
            "intervals": [[1, 4], [2, 5], [3, 6], [2, 4], [1, 5]],
            "expected": 3
        },

        # Boundary values from constraints
        {
            "intervals": [[-50000, -49999], [49999, 50000]],
            "expected": 0
        },
    ]

    # Run all test cases
    for i, test_case in enumerate(test_cases, 1):
        intervals = test_case["intervals"]
        expected = test_case["expected"]

        result = solution.eraseOverlapIntervals(intervals)

        print(
            f"Test Case {i}: "
            f"result = {result}, "
            f"expected = {expected}, "
            f"{'PASS' if result == expected else 'FAIL'}"
        )