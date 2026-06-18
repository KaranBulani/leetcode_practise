'''

Intuition

To efficiently find the median after every insertion:
* Max Heap (small) → stores the smaller half of numbers.
* Min Heap (large) → stores the larger half of numbers.

We maintain:
* Every element in small ≤ every element in large
* Heap sizes differ by at most 1

Then:
* Odd count → median is the root of the larger heap.
* Even count → median is average of both roots.

####################################################################################################
Complexity

addNum
Heap insertion/removal: O(log n)

findMedian
Just peek heap tops: O(1)

Space
O(n)

####################################################################################################
                                            ## Follow-up 1

### If all numbers are in range [0, 100]

You don't need heaps.

Maintain:
	count = [0] * 101
	n = 0

For every addNum(num):
	count[num] += 1
	n += 1


To find median:
* Walk through count
* Accumulate frequencies
* Find the middle position(s)

Example:

	nums = [1, 3, 3, 5]
	count:
	1 -> 1
	3 -> 2
	5 -> 1

Median positions:
	n = 4
	left = 2
	right = 3

Traverse counts until reaching those positions.

### Complexity
	addNum      O(1)
	findMedian  O(101) = O(1)
	space       O(101) = O(1)
Since the range is fixed, scanning 101 numbers is constant time.

                                            ## Follow-up 2

### If 99% of numbers are in range [0, 100]
Now we can't use only a frequency array because some values may be:
	-1000
	5000
	100000

A good optimization:
	count[0..100]

for the common numbers.

And store outliers separately:
	small = values < 0
	large = values > 100

Along with:
	inside_count
	outside_low_count
	outside_high_count

### Finding median

Suppose:
	10,000,000 numbers total
	9,900,000 in [0,100]
	100,000 outside

Median position:
	k = n // 2

Check:

#### Case 1
Median lies among numbers < 0 Search only in small.

#### Case 2
Median lies in [0,100]
This will happen most of the time.

Just scan:
	count[0]
	count[1]
	...
	count[100]
which is only 101 entries.

#### Case 3
Median lies among numbers > 100
Search only in large.

### Complexity
	addNum      O(1) for most numbers
	findMedian  O(101 + outliers_near_median)
Much faster than maintaining all numbers in heaps when almost every value is inside a tiny fixed range.

### What interviewers usually expect

For [0,100]:
> Use a counting array of size 101 and compute median from cumulative frequencies.

For 99% in [0,100]:
> Still use the counting array for the common values and keep numbers outside the range in separate data structures. When finding the median, first determine whether it falls below 0, within [0,100], or above 100, then search only that region.

This demonstrates that you recognized and exploited the small bounded domain, which is exactly what the follow-up is testing.
'''
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []  # for big numbers
        self.max_heap = []  # for small numbers

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                min_val = heapq.heappop(self.min_heap)
                heapq.heappush_max(self.max_heap, min_val)
            else:
                max_val = heapq.heappop_max(self.max_heap)
                heapq.heappush(self.min_heap, max_val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]

        return (self.min_heap[0] + self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == "__main__":
    median_finder = MedianFinder()

    test_cases = [
        # Example from question
        {
            "operations": ["addNum", "addNum", "findMedian", "addNum", "findMedian"],
            "values": [1, 2, None, 3, None],
            "expected": [None, None, 1.5, None, 2.0]
        },

        # Single element
        {
            "operations": ["addNum", "findMedian"],
            "values": [5, None],
            "expected": [None, 5.0]
        },

        # Two elements (even count)
        {
            "operations": ["addNum", "addNum", "findMedian"],
            "values": [5, 10, None],
            "expected": [None, None, 7.5]
        },

        # Numbers added in increasing order
        {
            "operations": ["addNum", "addNum", "addNum", "addNum", "findMedian"],
            "values": [1, 2, 3, 4, None],
            "expected": [None, None, None, None, 2.5]
        },

        # Numbers added in decreasing order
        {
            "operations": ["addNum", "addNum", "addNum", "addNum", "findMedian"],
            "values": [10, 9, 8, 7, None],
            "expected": [None, None, None, None, 8.5]
        },

        # Negative numbers
        {
            "operations": ["addNum", "addNum", "addNum", "findMedian"],
            "values": [-5, -1, -3, None],
            "expected": [None, None, None, -3.0]
        },

        # Mix of positive and negative
        {
            "operations": ["addNum", "addNum", "addNum", "addNum", "findMedian"],
            "values": [-10, 20, -30, 40, None],
            "expected": [None, None, None, None, 5.0]
        },

        # Duplicates
        {
            "operations": ["addNum", "addNum", "addNum", "addNum", "findMedian"],
            "values": [7, 7, 7, 7, None],
            "expected": [None, None, None, None, 7.0]
        },

        # Median changes after every insertion
        {
            "operations": [
                "addNum", "findMedian",
                "addNum", "findMedian",
                "addNum", "findMedian",
                "addNum", "findMedian"
            ],
            "values": [2, None, 1, None, 5, None, 7, None],
            "expected": [None, 2.0, None, 1.5, None, 2.0, None, 3.5]
        },

        # Extreme values
        {
            "operations": ["addNum", "addNum", "findMedian"],
            "values": [-100000, 100000, None],
            "expected": [None, None, 0.0]
        }
    ]

    for idx, test in enumerate(test_cases, start=1):
        print(f"\n===== Test Case {idx} =====")

        median_finder = MedianFinder()
        outputs = []

        for op, val in zip(test["operations"], test["values"]):
            if op == "addNum":
                median_finder.addNum(val)
                outputs.append(None)
            else:
                outputs.append(median_finder.findMedian())

        print("Expected :", test["expected"])
        print("Your Output:", outputs)