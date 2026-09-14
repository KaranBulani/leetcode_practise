'''
Approach: One-pass

Since intervals is already:
* sorted by start time
* non-overlapping

We divide the intervals into 3 groups:
1. Intervals completely before newInterval
2. Intervals that overlap with newInterval
3. Intervals completely after newInterval

The key overlap condition is:				interval[0] <= newInterval[1]
while processing the overlapping region.

####################################################################################################

class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval

        for curr_start, curr_end in intervals:

            # 1. Current interval is completely before newInterval
            if curr_end < start:
                result.append([curr_start, curr_end])

            # 2. Current interval is completely after newInterval
            elif curr_start > end:
                result.append([start, end])

                # From here onward, all remaining intervals
                # are also after newInterval.
                result.extend(intervals[intervals.index([curr_start, curr_end]) :])
                return result

            # 3. Overlapping intervals
            else:
                start = min(start, curr_start)
                end = max(end, curr_end)

        # Add newInterval if it wasn't added yet
        result.append([start, end])

        return result

However, don't use the above implementation in an interview/LeetCode submission because intervals.index() makes the complexity worse.

####################################################################################################

Clean optimal solution
    provided in main function

####################################################################################################

Example
	intervals  = [[1,3], [6,9]]
	newInterval = [2,5]

First:
	[1,3]

overlaps with [2,5]:
	start = min(2, 1) = 1
	end   = max(5, 3) = 5

	merged = [1,5]

Then [6,9] is after the merged interval.

Result:
		[[1,5], [6,9]]

####################################################################################################

Why the overlap condition works

For:
		while i < n and intervals[i][0] <= end:

we know that:
		current_start <= new_end

So the current interval could overlap/touch the new interval.

And before this loop, we've already removed all intervals satisfying:
		intervals[i][1] < start

Therefore, anything remaining either overlaps or comes after the new interval.

####################################################################################################

Complexity
		Time:  O(n)
		Space: O(n)   # result array

The important pattern to remember is:
		# Before
		while ...:
			result.append(...)

		# Overlap
		while ...:
			start = min(...)
			end = max(...)

		# After
		while ...:
			result.append(...)

This 3-phase pattern is the cleanest way to solve Insert Interval.

####################################################################################################
####################################### bisect_left solution #######################################
####################################################################################################

bisect_left can be used here, and it's a good exercise because Python compares lists lexicographically.

For example:
	[1, 7] < [2, 5]   # True
	[2, 9] < [2, 5]   # False

So we can use bisect_left to find where newInterval would be inserted.

####################################################################################################

Bisect-based solution


from bisect import bisect_left

class Solution:
    def insert(self, intervals, newInterval):
        # Find insertion position based on [start, end]
        i = bisect_left(intervals, newInterval)

        # Merge with intervals to the left if they overlap
        if i > 0 and intervals[i - 1][1] >= newInterval[0]:
            i -= 1
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

        # Merge with intervals to the right
        j = i

        while j < len(intervals) and intervals[j][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[j][0])
            newInterval[1] = max(newInterval[1], intervals[j][1])
            j += 1

        return intervals[:i] + [newInterval] + intervals[j:]


####################################################################################################

But there's an important problem

bisect_left(intervals, newInterval) compares the entire lists, not just their start values.

Suppose:
	intervals = [[1, 3], [6, 9]]
	newInterval = [2, 5]

Then:
	bisect_left(intervals, [2, 5])

returns:
			1

That's useful here.

But consider:
		intervals = [[1, 10], [20, 30]]
		newInterval = [1, 5]

bisect_left returns 0 because:
		[1, 5] < [1, 10]

That's actually fine.

The bigger issue is that we want to bisect based only on interval[0], whereas bisect_left on a list of lists considers both start and end.

####################################################################################################

## A cleaner bisect solution

We can create a separate list containing only the starts:

from bisect import bisect_left

class Solution:
    def insert(self, intervals, newInterval):
        starts = [interval[0] for interval in intervals]

        i = bisect_left(starts, newInterval[0])

        # Merge intervals on the left
        if i > 0 and intervals[i - 1][1] >= newInterval[0]:
            i -= 1

        # Merge intervals on the right
        j = i

        start, end = newInterval

        while j < len(intervals) and intervals[j][0] <= end:
            start = min(start, intervals[j][0])
            end = max(end, intervals[j][1])
            j += 1

        return intervals[:i] + [[start, end]] + intervals[j:]

####################################################################################################

Example
	intervals = [[1, 3], [6, 9]]
	newInterval = [2, 5]

We construct:
		starts = [1, 6]

Then:
		bisect_left([1, 6], 2)

gives:
		1

So we initially think:
			   i
			   ↓
		[1,3] [6,9]

But [1,3] overlaps [2,5] because:
		3 >= 2

Therefore:
		i -= 1

Now:
		 i
		 ↓
		[1,3] [6,9]

Merge [1,3]:
		[1,5]

Then [6,9] doesn't overlap because:
		6 > 5

Result:
		[[1, 5], [6, 9]]

####################################################################################################

One thing to remember

For this problem, bisect is useful for finding the approximate insertion position, but it doesn't eliminate the need to scan overlapping intervals.

So:
		bisect → find where newInterval belongs
				  ↓
		scan   → merge overlaps
				  ↓
		slice  → construct result

Also, the starts = [...] construction itself costs O(n), so the overall complexity remains O(n).

'''
class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval
        i = 0
        n = len(intervals)

        # 1. Add intervals completely before newInterval
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        # Add the merged interval
        result.append([start, end])

        # 3. Add intervals completely after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # --------------------------------------------------
        # Official Examples
        # --------------------------------------------------

        (
            [[1,5]],
            [0,0],
            [[1, 5], [6, 8]]
        ),

        (
            [[1, 5]],
            [6, 8],
            [[1, 5], [6, 8]]
        ),

        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]]
        ),

        (
            [[1,2],[6,9]],
            [2, 5],
            [[1, 5], [6, 9]]
        ),

        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]]
        ),

        # --------------------------------------------------
        # Empty input
        # --------------------------------------------------

        (
            [],
            [5, 7],
            [[5, 7]]
        ),

        # --------------------------------------------------
        # New interval before everything
        # --------------------------------------------------

        (
            [[5, 7], [10, 12]],
            [1, 3],
            [[1, 3], [5, 7], [10, 12]]
        ),

        # New interval after everything
        (
            [[1, 3], [5, 7]],
            [10, 12],
            [[1, 3], [5, 7], [10, 12]]
        ),

        # --------------------------------------------------
        # New interval completely inside an existing gap
        # --------------------------------------------------

        (
            [[1, 3], [10, 12]],
            [5, 7],
            [[1, 3], [5, 7], [10, 12]]
        ),

        # --------------------------------------------------
        # New interval completely inside existing interval
        # --------------------------------------------------

        (
            [[1, 10]],
            [3, 5],
            [[1, 10]]
        ),

        # --------------------------------------------------
        # New interval completely covers everything
        # --------------------------------------------------

        (
            [[2, 4], [6, 8], [10, 12]],
            [1, 15],
            [[1, 15]]
        ),

        # --------------------------------------------------
        # Overlap from the left
        # --------------------------------------------------

        (
            [[5, 7], [10, 12]],
            [3, 6],
            [[3, 7], [10, 12]]
        ),

        # Overlap from the right
        (
            [[1, 3], [5, 7]],
            [6, 10],
            [[1, 3], [5, 10]]
        ),

        # --------------------------------------------------
        # Touching intervals
        # Since sharing a point means overlapping
        # --------------------------------------------------

        (
            [[1, 3], [7, 9]],
            [3, 7],
            [[1, 9]]
        ),

        (
            [[1, 3], [7, 9]],
            [3, 5],
            [[1, 5], [7, 9]]
        ),

        (
            [[1, 3], [7, 9]],
            [5, 7],
            [[1, 3], [5, 9]]
        ),

        # --------------------------------------------------
        # Merge multiple intervals
        # --------------------------------------------------

        (
            [[1, 2], [4, 5], [7, 8], [10, 12]],
            [2, 10],
            [[1, 12]]
        ),

        # --------------------------------------------------
        # Single interval
        # --------------------------------------------------

        (
            [[5, 10]],
            [1, 3],
            [[1, 3], [5, 10]]
        ),

        (
            [[5, 10]],
            [12, 15],
            [[5, 10], [12, 15]]
        ),

        (
            [[5, 10]],
            [7, 8],
            [[5, 10]]
        ),

        (
            [[5, 10]],
            [3, 7],
            [[3, 10]]
        ),

        (
            [[5, 10]],
            [8, 15],
            [[5, 15]]
        ),

        # --------------------------------------------------
        # Single-point intervals
        # --------------------------------------------------

        (
            [[1, 1], [3, 3], [5, 5]],
            [2, 2],
            [[1, 1], [2, 2], [3, 3], [5, 5]]
        ),

        (
            [[1, 1], [3, 3], [5, 5]],
            [1, 5],
            [[1, 5]]
        ),

        # --------------------------------------------------
        # New interval is exactly equal to an existing one
        # --------------------------------------------------

        (
            [[1, 3], [6, 9]],
            [1, 3],
            [[1, 3], [6, 9]]
        ),

        (
            [[1, 3], [6, 9]],
            [6, 9],
            [[1, 3], [6, 9]]
        ),

        # --------------------------------------------------
        # Large values
        # --------------------------------------------------

        (
            [[0, 100], [200, 500], [1000, 100000]],
            [50, 1000],
            [[0, 1000], [1000, 100000]]
        ),
    ]

    # --------------------------------------------------
    # Run tests
    # --------------------------------------------------

    for i, (intervals, new_interval, expected) in enumerate(test_cases, 1):
        result = solution.insert(intervals, new_interval)

        status = "PASS" if result == expected else "FAIL"

        print(f"Test {i:02}: {status}")

        if status == "FAIL":
            print(f"  Input:    intervals={intervals}, newInterval={new_interval}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            print()