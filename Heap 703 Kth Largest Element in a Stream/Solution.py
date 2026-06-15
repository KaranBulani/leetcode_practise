'''

from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


'''
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]

        self.heapify()

        while len(self.heap) > k:
            self.pop()

    def heapify(self):
        n = len(self.heap)
        # we want to skip leaf nodes from heapify
        # so we start from last node's parent which would be the 1st node which is not leaf
        # last node's index is n-1 where n = len(nums), parent would be (i - 1) // 2
        # (n-1 - 1) // 2    ->      n//2 - 1
        # this n//2 - 1 assumes n = len(nums) not len(nums) - 1

        for i in range((n // 2) - 1, -1, -1):
            self.sift_down(i)

    def sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[parent] <= self.heap[index]:
                break

            self.heap[parent], self.heap[index] = (
                self.heap[index],
                self.heap[parent]
            )

            index = parent

    def sift_down(self, index):
        n = len(self.heap)

        while True:
            smallest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

    def push(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()
        self.sift_down(0)

        return minimum

    def add(self, val: int) -> int:
        self.push(val)

        if len(self.heap) > self.k:
            self.pop()

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == "__main__":
    print("===== Test Case 1 (Example 1) =====")
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    print(kthLargest.add(3))  # Expected:
    print(kthLargest.add(5))  # Expected:
    print(kthLargest.add(10))  # Expected:
    print(kthLargest.add(9))  # Expected:
    print(kthLargest.add(4))  # Expected:

    print("\n===== Test Case 2 (Example 2) =====")
    kthLargest = KthLargest(4, [7, 7, 7, 7, 8, 3])

    print(kthLargest.add(2))  # Expected:
    print(kthLargest.add(10))  # Expected:
    print(kthLargest.add(9))  # Expected:
    print(kthLargest.add(9))  # Expected:

    print("\n===== Test Case 3 (Empty Initial Array) =====")
    kthLargest = KthLargest(1, [])

    print(kthLargest.add(-3))  # Expected:
    print(kthLargest.add(-2))  # Expected:
    print(kthLargest.add(-4))  # Expected:
    print(kthLargest.add(0))  # Expected:
    print(kthLargest.add(4))  # Expected:

    print("\n===== Test Case 4 (k = 1) =====")
    kthLargest = KthLargest(1, [5, 2, 10])

    print(kthLargest.add(3))  # Expected:
    print(kthLargest.add(20))  # Expected:
    print(kthLargest.add(1))  # Expected:

    print("\n===== Test Case 5 (All Duplicates) =====")
    kthLargest = KthLargest(3, [5, 5, 5, 5])

    print(kthLargest.add(5))  # Expected:
    print(kthLargest.add(5))  # Expected:
    print(kthLargest.add(5))  # Expected:

    print("\n===== Test Case 6 (Negative Numbers) =====")
    kthLargest = KthLargest(2, [-10, -7, -5])

    print(kthLargest.add(-8))  # Expected:
    print(kthLargest.add(-1))  # Expected:
    print(kthLargest.add(-20))  # Expected:

    print("\n===== Test Case 7 (k = len(nums) + 1 Initially) =====")
    kthLargest = KthLargest(5, [4, 2, 8, 6])

    print(kthLargest.add(10))  # Expected:
    print(kthLargest.add(1))  # Expected:
    print(kthLargest.add(7))  # Expected:

    print("\n===== Test Case 8 (Increasing Stream) =====")
    kthLargest = KthLargest(3, [1, 2, 3])

    print(kthLargest.add(4))  # Expected:
    print(kthLargest.add(5))  # Expected:
    print(kthLargest.add(6))  # Expected:

    print("\n===== Test Case 9 (Decreasing Stream) =====")
    kthLargest = KthLargest(3, [10, 9, 8])

    print(kthLargest.add(7))  # Expected:
    print(kthLargest.add(6))  # Expected:
    print(kthLargest.add(5))  # Expected: