'''
Problem

Given intervals where intervals[i] = [start, end], merge all overlapping intervals.
Example:
	Input:
	[[1,3],[2,6],[8,10],[15,18]]

	Output:
	[[1,6],[8,10],[15,18]]

####################################################################################################
Step 1: Observe
Suppose the intervals are already sorted by their starting point.
	[1,3]
	[2,6]
	[8,10]
	[15,18]
Compare every interval with the previous merged interval.

Current merged interval		[1,3]
Next interval		[2,6]
Since		2 <= 3
they overlap.

Merged interval becomes		[1,6]

Next
		[8,10]
	8 > 6
No overlap.
Add it separately.

####################################################################################################
Step 2: What if intervals aren't sorted?

Example
		[[8,10],[1,3],[2,6]]

Without sorting, you cannot know whether an interval that should merge has already appeared.
So the first step must always be sorting by start time.

####################################################################################################
Step 3: Algorithm

1. Sort intervals by start.
2. Create answer list.
3. Add first interval.
4. For every remaining interval:
   * If overlap:
     * Update end.
   * Else:
     * Append new interval.


####################################################################################################
Edge Cases

1. [[1,4],[5,6]]
No overlap
Output	[[1,4],[5,6]]

2. [[1,4],[4,5]]
Since 4 <= 4 they overlap.
Output [[1,5]]

3. [[1,10],[2,3],[4,5]]
Output [[1,10]]

4. [[1,4]]
Output [[1,4]]

####################################################################################################
Complexity

Sorting takes:
* Time: O(n log n)

Merging requires one pass:
* Time: O(n)

Overall:
* Time: O(n log n)
* Space: O(n) (for the output; ignoring the output itself, the extra working space is O(1) aside from the sort implementation).
'''

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ==========================
        # Examples from Question
        # ==========================
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]]
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]]
        ),
        (
            [[4, 7], [1, 4]],
            [[1, 7]]
        ),

        # ==========================
        # Basic Edge Cases
        # ==========================
        (
            [[1, 2]],
            [[1, 2]]
        ),
        (
            [[1, 1]],
            [[1, 1]]
        ),

        # ==========================
        # Already Merged
        # ==========================
        (
            [[1, 2], [3, 4], [5, 6]],
            [[1, 2], [3, 4], [5, 6]]
        ),

        # ==========================
        # Completely Overlapping
        # ==========================
        (
            [[1, 10], [2, 3], [4, 5], [6, 8]],
            [[1, 10]]
        ),

        # ==========================
        # Same Intervals
        # ==========================
        (
            [[2, 5], [2, 5], [2, 5]],
            [[2, 5]]
        ),

        # ==========================
        # Chain Merging
        # ==========================
        (
            [[1, 2], [2, 3], [3, 4], [4, 5]],
            [[1, 5]]
        ),

        # ==========================
        # Nested Intervals
        # ==========================
        (
            [[1, 10], [2, 6], [3, 5], [7, 9]],
            [[1, 10]]
        ),

        # ==========================
        # Unsorted Input
        # ==========================
        (
            [[8, 10], [1, 3], [15, 18], [2, 6]],
            [[1, 6], [8, 10], [15, 18]]
        ),

        # ==========================
        # Multiple Merge Groups
        # ==========================
        (
            [[1, 4], [2, 3], [6, 8], [7, 10], [12, 15]],
            [[1, 4], [6, 10], [12, 15]]
        ),

        # ==========================
        # End Touching Start
        # ==========================
        (
            [[1, 5], [5, 8], [8, 10]],
            [[1, 10]]
        ),

        # ==========================
        # Zero-Length Intervals
        # ==========================
        (
            [[1, 1], [1, 2], [3, 3]],
            [[1, 2], [3, 3]]
        ),

        # ==========================
        # Large Range Covers Others
        # ==========================
        (
            [[0, 10000], [1, 2], [9999, 10000]],
            [[0, 10000]]
        ),

        # ==========================
        # Mixed Complex Case
        # ==========================
        (
            [[6, 8], [1, 9], [2, 4], [4, 7]],
            [[1, 9]]
        ),
    ]

    for i, (intervals, expected) in enumerate(test_cases, 1):
        result = solution.merge([interval[:] for interval in intervals])  # Copy to avoid mutation
        print(f"Test Case {i}")
        print("Input    :", intervals)
        print("Expected :", expected)
        print("Output   :", result)
        print("PASS" if result == expected else "FAIL")
        print("-" * 60)