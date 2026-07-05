'''
### Idea

We process all building boundaries from left to right.

For each building [L, R, H]:
* Create a start event (L, -H, R)
* Create an end event (R, 0, 0) (used only to trigger heap cleanup never pushed on heap)

Why negative height?
* Taller buildings come first when multiple buildings start at the same x.
* Starts naturally come before ends because -H < 0.

####################################################################################################
### Algorithm

Maintain a max heap storing (-height, right)

The heap contains all currently active buildings.

For every event:
1. Remove every building whose right <= current_x.
2. If it is a start event, push it into the heap.
3. Current skyline height is -height_of_heap_top

(or 0 if heap empty)
If this height differs from previous height, record a key point.

####################################################################################################
# Example

Input
[
    [2,9,10],
    [3,7,15],
    [5,12,12]
]

Events become
(2,-10,9)
(3,-15,7)
(5,-12,12)
(7,0,0)
(9,0,0)
(12,0,0)   --


Processing

| x  | Heap Max | Skyline   |
| -- | -------- | --------- |
| 2  | 10       | [2,10]    |
| 3  | 15       | [3,15]    |
| 5  | 15       | No change |
| 7  | 12       | [7,12]    |
| 9  | 12       | No change |
| 12 | 0        | [12,0]    |

Result
[
    [2,10],
    [3,15],
    [7,12],
    [12,0]
]

####################################################################################################
# Why do we remove before inserting?

Suppose a building ends at x=7 and another starts at x=7.

Removing expired buildings first ensures buildings ending at 7 are no longer active. Then inserting the new building correctly reflects the skyline immediately to the right of x=7, matching the problem definition where buildings cover the interval [left, right).

####################################################################################################
# Time Complexity
* Creating events: O(n)
* Sorting events: O(n log n)
* Each building is pushed once and popped once from the heap: O(n log n)

Overall:
Time: O(n log n)
Space: O(n)
'''
from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = []

        for left, right, height in buildings:
            events.append((left, -height, right)) #start
            events.append((right, 0, 0)) #end
        # if 2 building start together, higher building comes first, -height with asc makes taller building come 1st
        # if 2 building end together, then smaller building should come first, but end in this approach never get inserted due to 0 height
        # if start, end come together then we want to make sure start process first, hence -ve height for start

        events.sort()

        heap = [(0, float("inf"))]      # (-height, right)
        answer = []

        for x, neg_height, right in events:

            # Remove expired buildings
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Start of building, automatically excludes ends because their height is 0
            if neg_height:
                heapq.heappush(heap, (neg_height, right))

            current_height = -heap[0][0]

            if not answer or answer[-1][1] != current_height:
                answer.append([x, current_height])

        return answer
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # --------------------------------------------------
        # Example 1
        (
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        ),

        # Example 2
        (
            [[0, 2, 3], [2, 5, 3]],
            [[0, 3], [5, 0]]
        ),

        # --------------------------------------------------
        # Single building
        (
            [[1, 5, 10]],
            [[1, 10], [5, 0]]
        ),

        # Two non-overlapping buildings
        (
            [[1, 3, 4], [5, 7, 6]],
            [[1, 4], [3, 0], [5, 6], [7, 0]]
        ),

        # Completely overlapping, second taller
        (
            [[2, 9, 10], [2, 9, 15]],
            [[2, 15], [9, 0]]
        ),

        # Completely overlapping, first taller
        (
            [[2, 9, 15], [2, 9, 10]],
            [[2, 15], [9, 0]]
        ),

        # Building completely inside another (shorter)
        (
            [[1, 10, 10], [3, 7, 5]],
            [[1, 10], [10, 0]]
        ),

        # Building completely inside another (taller)
        (
            [[1, 10, 5], [3, 7, 12]],
            [[1, 5], [3, 12], [7, 5], [10, 0]]
        ),

        # Same start, different heights
        (
            [[2, 6, 8], [2, 4, 12], [2, 5, 10]],
            [[2, 12], [4, 10], [5, 8], [6, 0]]
        ),

        # Same end, different heights
        (
            [[1, 6, 6], [2, 6, 10], [3, 6, 8]],
            [[1, 6], [2, 10], [6, 0]]
        ),

        # Multiple touching buildings (same height)
        (
            [[1, 3, 5], [3, 6, 5], [6, 8, 5]],
            [[1, 5], [8, 0]]
        ),

        # Multiple touching buildings (different heights)
        (
            [[1, 3, 5], [3, 6, 7], [6, 8, 4]],
            [[1, 5], [3, 7], [6, 4], [8, 0]]
        ),

        # Staircase increasing
        (
            [[1, 5, 2], [2, 6, 4], [3, 7, 6]],
            [[1, 2], [2, 4], [3, 6], [7, 0]]
        ),

        # Staircase decreasing
        (
            [[1, 7, 6], [2, 6, 4], [3, 5, 2]],
            [[1, 6], [7, 0]]
        ),

        # Complex overlap
        (
            [[1, 4, 4], [2, 6, 6], [5, 8, 5], [7, 9, 8]],
            [[1, 4], [2, 6], [6, 5], [7, 8], [9, 0]]
        ),

        # Large gap between buildings
        (
            [[1, 2, 3], [10, 12, 4]],
            [[1, 3], [2, 0], [10, 4], [12, 0]]
        ),

        # Many identical buildings
        (
            [[1, 5, 7], [1, 5, 7], [1, 5, 7]],
            [[1, 7], [5, 0]]
        ),

        # Nested buildings with increasing heights
        (
            [[1, 10, 2], [2, 9, 4], [3, 8, 6], [4, 7, 8]],
            [[1, 2], [2, 4], [3, 6], [4, 8], [7, 6], [8, 4], [9, 2], [10, 0]]
        ),

        # Nested buildings with decreasing heights
        (
            [[1, 10, 8], [2, 9, 6], [3, 8, 4], [4, 7, 2]],
            [[1, 8], [10, 0]]
        ),

        # Long building interrupted by taller ones
        (
            [[1, 10, 5], [2, 3, 8], [4, 5, 9], [6, 7, 10]],
            [[1, 5], [2, 8], [3, 5], [4, 9], [5, 5], [6, 10], [7, 5], [10, 0]]
        ),
    ]

    for idx, (buildings, expected) in enumerate(test_cases, 1):
        result = solution.getSkyline(buildings)

        print(f"\nTest Case {idx}")
        print("Buildings :", buildings)
        print("Expected  :", expected)
        print("Got       :", result)
        print("PASS" if result == expected else "FAIL")