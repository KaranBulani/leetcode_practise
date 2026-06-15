'''
### Idea
* The heap stores the k largest elements seen so far.
* The smallest element in this heap (heap[0]) is the kth largest overall.
* If the heap grows beyond size k, remove the minimum.

### Complexity
* Time: O(n log k)
* Space: O(k)

## Solution using heapq

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

## Without heapq (implement Min Heap manually)
'''
from typing import List

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return minimum

    def _bubble_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2

            if self.heap[parent] <= self.heap[idx]:
                break

            self.heap[parent], self.heap[idx] = (
                self.heap[idx],
                self.heap[parent]
            )

            idx = parent

    def _bubble_down(self, idx):
        n = len(self.heap)

        while True:
            smallest = idx

            left = 2 * idx + 1
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            right = 2 * idx + 2
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[idx]
            )

            idx = smallest

    def peek(self):
        return self.heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = MinHeap()

        for num in nums:
            heap.push(num)

            if len(heap.heap) > k:
                heap.pop()

        return heap.peek()

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        {
            "nums": [3, 2, 1, 5, 6, 4],
            "k": 2,
            "expected": 5,
        },
        {
            "nums": [3, 2, 3, 1, 2, 4, 5, 5, 6],
            "k": 4,
            "expected": 4,
        },

        # Single element
        {
            "nums": [10],
            "k": 1,
            "expected": 10,
        },

        # Already sorted ascending
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 1,
            "expected": 5,
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "k": 5,
            "expected": 1,
        },

        # Already sorted descending
        {
            "nums": [5, 4, 3, 2, 1],
            "k": 3,
            "expected": 3,
        },

        # All duplicates
        {
            "nums": [7, 7, 7, 7, 7],
            "k": 3,
            "expected": 7,
        },

        # Duplicates mixed
        {
            "nums": [5, 5, 5, 3, 3, 1],
            "k": 2,
            "expected": 5,
        },
        {
            "nums": [5, 5, 5, 3, 3, 1],
            "k": 4,
            "expected": 3,
        },

        # Negative numbers
        {
            "nums": [-1, -2, -3, -4, -5],
            "k": 2,
            "expected": -2,
        },

        # Mixed positive and negative
        {
            "nums": [-10, 5, 3, -2, 8, 0],
            "k": 3,
            "expected": 3,
        },

        # k = 1 (largest element)
        {
            "nums": [8, 2, 4, 9, 1],
            "k": 1,
            "expected": 9,
        },

        # k = len(nums) (smallest element)
        {
            "nums": [8, 2, 4, 9, 1],
            "k": 5,
            "expected": 1,
        },

        # Many repeated largest values
        {
            "nums": [9, 9, 9, 8, 7, 6],
            "k": 3,
            "expected": 9,
        },

        # Zeroes
        {
            "nums": [0, 0, 0, 0, 0],
            "k": 4,
            "expected": 0,
        },

        # Extremes from constraints
        {
            "nums": [-10000, 10000],
            "k": 1,
            "expected": 10000,
        },
        {
            "nums": [-10000, 10000],
            "k": 2,
            "expected": -10000,
        },
    ]

    for i, test in enumerate(test_cases, start=1):
        result = solution.findKthLargest(test["nums"], test["k"])

        print(f"Test Case {i}")
        print(f"nums     = {test['nums']}")
        print(f"k        = {test['k']}")
        print(f"expected = {test['expected']}")
        print(f"result   = {result}")
        print(f"PASS     = {result == test['expected']}")
        print("-" * 50)