'''
####################################################################################################
Idea

For each point (x, y): 					distance^2 = x^2 + y^2
We use the squared distance because sqrt does not affect ordering.

Maintain a max heap of size k:
* If heap size < k → insert point.
* Otherwise:
  * If current point is closer than the farthest point in the heap, remove the farthest and insert the current point.
At the end, the heap contains the k closest points.

####################################################################################################
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x * x + y * y

            if len(heap) < k:
                heapq.heappush(heap, (-dist, x, y))
            elif dist < -heap[0][0]:
                heapq.heapreplace(heap, (-dist, x, y))

        return [[x, y] for _, x, y in heap]
####################################################################################################

from typing import List

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)

        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent][0] >= self.heap[i][0]:
                break

            self.heap[parent], self.heap[i] = \
                self.heap[i], self.heap[parent]

            i = parent

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return maximum

    def heapify_down(self, i):
        n = len(self.heap)

        while True:
            largest = i

            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = \
                self.heap[largest], self.heap[i]

            i = largest

    def replace_root(self, item):
        self.heap[0] = item
        self.heapify_down(0)

    def __len__(self):
        return len(self.heap)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = MaxHeap()

        for x, y in points:
            dist = x * x + y * y

            if len(heap) < k:
                heap.push((dist, x, y))

            elif dist < heap.heap[0][0]:
                heap.replace_root((dist, x, y))

        return [[x, y] for dist, x, y in heap.heap]

####################################################################################################
Complexity

	Let:  n = len(points)

	For each point:
	* Heap insertion/replacement = O(log k)

	Therefore:
	* Time: O(n log k)
	* Space: O(k)

####################################################################################################
Alternative: Heapify All Points
You can also build a min heap of all distances and pop k times.

####################################################################################################
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(x*x + y*y, x, y) for x, y in points]
        heapq.heapify(heap)

        ans = []

        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])

        return ans

####################################################################################################
Complexity
	* Heapify: O(n)
	* Pop k times: O(k log n)

	Total:
	* Time: O(n + k log n)
	* Space: O(n)


'''
from typing import List

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)

        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent][0] >= self.heap[i][0]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return maximum

    def heapify_down(self, i):
        n = len(self.heap)

        while True:
            largest = i

            left = 2 * i + 1
            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            right = 2 * i + 2
            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]

            i = largest

    def replace_root(self, item):
        self.heap[0] = item
        self.heapify_down(0)

    def __len__(self):
        return len(self.heap)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = MaxHeap()

        for x, y in points:
            dist = x * x + y * y

            if len(heap) < k:
                heap.push((dist, x, y))

            elif dist < heap.heap[0][0]:
                heap.replace_root((dist, x, y))

        return [[x, y] for dist, x, y in heap.heap]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "points": [[1, 3], [-2, 2]],
            "k": 1,
            "expected": [[-2, 2]]
        },

        # Example 2
        {
            "points": [[3, 3], [5, -1], [-2, 4]],
            "k": 2,
            "expected": [[3, 3], [-2, 4]]
        },

        # Single point
        {
            "points": [[7, -8]],
            "k": 1,
            "expected": [[7, -8]]
        },

        # k == number of points
        {
            "points": [[1, 2], [2, 1], [-1, -1]],
            "k": 3,
            "expected": [[1, 2], [2, 1], [-1, -1]]
        },

        # Origin included
        {
            "points": [[0, 0], [5, 5], [1, 1]],
            "k": 1,
            "expected": [[0, 0]]
        },

        # Negative coordinates
        {
            "points": [[-5, -4], [-2, -1], [-10, -10]],
            "k": 2,
            "expected": [[-2, -1], [-5, -4]]
        },

        # Points on axes
        {
            "points": [[0, 5], [3, 0], [0, 2], [7, 0]],
            "k": 2,
            "expected": [[0, 2], [3, 0]]
        },

        # Large values
        {
            "points": [[10000, 10000], [1, 1], [-9999, -9999]],
            "k": 1,
            "expected": [[1, 1]]
        },

        # Mix of positive and negative coordinates
        {
            "points": [[4, 4], [-1, -1], [2, 2], [-3, 3]],
            "k": 2,
            "expected": [[-1, -1], [2, 2]]
        },

        # Closest point not first in input
        {
            "points": [[100, 100], [50, 50], [1, 2]],
            "k": 1,
            "expected": [[1, 2]]
        }
    ]

    for i, test in enumerate(test_cases, start=1):
        result = solution.kClosest(test["points"], test["k"])

        print(f"\nTest Case {i}")
        print(f"Points   : {test['points']}")
        print(f"k        : {test['k']}")
        print(f"Result   : {result}")
        print(f"Expected : {test['expected']}")