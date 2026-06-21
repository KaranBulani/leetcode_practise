'''
Approach: Two Heaps + Lazy Deletion

Maintain:
* small → max heap (stores smaller half)
* large → min heap (stores larger half)
* delayed → hashmap for lazy deletion of elements that left the window

The top of:
* small = median when k is odd
* small and large tops = median when k is even
####################################################################################################

Complexity

For each window movement:
* Insert: O(log k)
* Remove (lazy deletion): O(log k)
* Median lookup: O(1)

Overall:
* Time: O(n log k)
* Space: O(k)

'''
from collections import defaultdict
import heapq


class Solution:
    def medianSlidingWindow(self, nums, k):

        small = []      # max heap
        large = []      # min heap

        delayed = defaultdict(int)

        small_size = 0      # valid elements
        large_size = 0

        def prune_small():
            while small and delayed[small[0]]:
                num = small[0]
                delayed[num] -= 1
                heapq.heappop_max(small)

        def prune_large():
            while large and delayed[large[0]]:
                num = large[0]
                delayed[num] -= 1
                heapq.heappop(large)

        def rebalance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                prune_small()

                num = heapq.heappop_max(small)
                heapq.heappush(large, num)

                small_size -= 1
                large_size += 1

                prune_small()

            elif small_size < large_size:
                prune_large()

                num = heapq.heappop(large)
                heapq.heappush_max(small, num)

                large_size -= 1
                small_size += 1

                prune_large()

        def add_num(num):
            nonlocal small_size, large_size

            if not small or num <= small[0]:
                heapq.heappush_max(small, num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            rebalance()

        def remove_num(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= small[0]:
                small_size -= 1

                if num == small[0]:
                    prune_small()
            else:
                large_size -= 1

                if large and num == large[0]:
                    prune_large()

            rebalance()

        def get_median():
            prune_small()

            if k % 2:
                return float(small[0])

            prune_large()
            return (small[0] + large[0]) / 2

        # build first window
        for i in range(k):
            add_num(nums[i])

        ans = [get_median()]

        # slide window
        for i in range(k, len(nums)):
            add_num(nums[i])
            remove_num(nums[i - k])

            ans.append(get_median())

        return ans

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "nums": [1, 3, -1, -3, 5, 3, 6, 7],
            "k": 3,
            "expected": [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
        },

        # Example 2
        {
            "nums": [1, 2, 3, 4, 2, 3, 1, 4, 2],
            "k": 3,
            "expected": [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
        },

        # k = 1 (every element is its own median)
        {
            "nums": [5, -2, 7, 1],
            "k": 1,
            "expected": [5.0, -2.0, 7.0, 1.0]
        },

        # Entire array is one window
        {
            "nums": [4, 1, 7, 2, 5],
            "k": 5,
            "expected": [4.0]
        },

        # Even k
        {
            "nums": [1, 2, 3, 4],
            "k": 2,
            "expected": [1.5, 2.5, 3.5]
        },

        # All duplicates
        {
            "nums": [2, 2, 2, 2, 2],
            "k": 3,
            "expected": [2.0, 2.0, 2.0]
        },

        # Negative numbers only
        {
            "nums": [-5, -1, -3, -4, -2],
            "k": 3,
            "expected": [-3.0, -3.0, -3.0]
        },

        # Mix of positive and negative
        {
            "nums": [-1, 5, 13, 8, 2, 3, 3],
            "k": 4,
            "expected": [6.5, 6.5, 5.5, 3.0]
        },

        # Increasing sequence
        {
            "nums": [1, 2, 3, 4, 5, 6],
            "k": 3,
            "expected": [2.0, 3.0, 4.0, 5.0]
        },

        # Decreasing sequence
        {
            "nums": [6, 5, 4, 3, 2, 1],
            "k": 3,
            "expected": [5.0, 4.0, 3.0, 2.0]
        },

        # Repeated values around median
        {
            "nums": [1, 4, 2, 3, 2, 2, 5],
            "k": 3,
            "expected": [2.0, 3.0, 2.0, 2.0, 2.0]
        },

        # Large values (32-bit boundaries)
        {
            "nums": [2147483647, 2147483647, -2147483648, -2147483648],
            "k": 2,
            "expected": [2147483647.0, -0.5, -2147483648.0]
        },

        # Even window with duplicates
        {
            "nums": [1, 1, 1, 1, 1],
            "k": 4,
            "expected": [1.0, 1.0]
        },

        # Alternating values
        {
            "nums": [1, 10, 1, 10, 1, 10],
            "k": 3,
            "expected": [1.0, 10.0, 1.0, 10.0]
        },
    ]

    for i, test in enumerate(test_cases, start=1):
        nums = test["nums"]
        k = test["k"]
        expected = test["expected"]

        result = solution.medianSlidingWindow(nums, k)

        print(f"\nTest Case {i}")
        print(f"nums     = {nums}")
        print(f"k        = {k}")
        print(f"expected = {expected}")
        print(f"result   = {result}")
        print(f"PASS     = {result == expected}")