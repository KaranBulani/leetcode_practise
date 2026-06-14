'''
Since we always need the two heaviest stones, a max heap is the natural data structure.

### Approach
1. Build a max heap from the input array.
2. Repeatedly:
   * Extract the largest stone y.
   * Extract the second largest stone x.
   * If y != x, insert y - x back into the heap.
3. Continue until there is at most one stone left.
4. Return the remaining stone or 0.

### Time Complexity
* Build heap: O(n)
* Each smash:
  * 2 pops + at most 1 push = O(log n)
* Total: O(n log n)

### Space Complexity
* Heap: O(n)

### Code
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)  # largest
            x = -heapq.heappop(max_heap)  # second largest

            if y != x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0
'''
from typing import List

class MaxHeap:
    def __init__(self, nums=None):
        self.heap = nums if nums else []
        self.heapify()

    def heapify(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent] >= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent],
            )
            index = parent

    def sift_down(self, index):
        n = len(self.heap)

        while True:
            largest = index

            left = 2 * index + 1
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            right = 2 * index + 2
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index],
            )
            index = largest

    def push(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return maximum

    def __len__(self):
        return len(self.heap)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap(stones)

        while len(max_heap) > 1:
            y = max_heap.pop()  # largest
            x = max_heap.pop()  # second largest

            if y != x:
                max_heap.push(y - x)

        return max_heap.pop() if len(max_heap) == 1 else 0

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example cases
        ([2,7,4,1,8,1], 1),
        ([1], 1),

        # Edge cases
        ([1,1], 0),                  # both destroy
        ([10,10,10,10], 0),          # all equal even count
        ([10,10,10], 10),            # odd count same numbers

        # Increasing order
        ([1,2,3,4,5], 1),

        # Decreasing order
        ([9,7,5,3,1], 1),

        # Large difference
        ([1000,1], 999),

        # Multiple reductions
        ([31,26,33,21,40], 9),

        # Many duplicates
        ([5,5,5,5,5,5], 0),

        # Single heavy survives
        ([50,40,30,20,10], 10),

        # Random mixed
        ([8,3,5,2,9,1,7], 1),

        # Another tricky one
        ([2,2,3,3,4,4], 0),

        # All same odd count
        ([7,7,7,7,7], 7),
    ]

    for i, (stones, expected) in enumerate(test_cases):
        result = solution.lastStoneWeight(stones[:])  # use copy to avoid mutation issues
        print(f"Test Case {i+1}:")
        print(f"Input: {stones}")
        print(f"Expected: {expected}, Got: {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)