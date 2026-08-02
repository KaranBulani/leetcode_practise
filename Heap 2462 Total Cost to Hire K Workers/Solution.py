'''
####################################################################################################
Time complexity:
Building Heap: O(2 * candidates) array traversal * Log( 2 * candidates) heap push

Actually getting answers: k times heappop + k times heappush
                         2 * k ( log( 2 * candidates))

( O(2 * candidates) + 2 * k ) * log ( 2 * candidates)

Space complexity:
Heap = O(2 * candidates)
'''
import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        left = 0
        right = n - 1

        # (cost, side)
        # side = 0 -> worker came from left pool
        # side = 1 -> worker came from right pool
        heap = []

        # Initialize the heap with up to 'candidates' workers
        # from both ends without overlapping.
        while left <= right and left < candidates:
            heapq.heappush(heap, (costs[left], 0))
            left += 1

            if left <= right:
                heapq.heappush(heap, (costs[right], 1))
                right -= 1

        total_cost = 0

        for _ in range(k):
            cost, side = heapq.heappop(heap)
            total_cost += cost

            # Refill from the same side from which the worker was hired.
            if left <= right:
                if side == 0:
                    heapq.heappush(heap, (costs[left], 0))
                    left += 1
                else:
                    heapq.heappush(heap, (costs[right], 1))
                    right -= 1

        return total_cost

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # =========================
        # Examples from question
        # =========================
        {
            "costs": [18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75],
            "k": 13,
            "candidates": 23,
            "expected": 223,
        },
        {
            "costs": [17, 12, 10, 2, 7, 2, 11, 20, 8],
            "k": 3,
            "candidates": 4,
            "expected": 11,
        },
        {
            "costs": [1, 2, 4, 1],
            "k": 3,
            "candidates": 3,
            "expected": 4,
        },

        # =========================
        # Single element
        # =========================
        {
            "costs": [5],
            "k": 1,
            "candidates": 1,
            "expected": 5,
        },

        # =========================
        # Hire everyone
        # =========================
        {
            "costs": [4, 2, 8, 1, 6],
            "k": 5,
            "candidates": 2,
            "expected": 21,
        },

        # =========================
        # candidates = 1
        # =========================
        {
            "costs": [5, 4, 3, 2, 1],
            "k": 3,
            "candidates": 1,
            "expected": 6,
        },
        {
            "costs": [1, 2, 3, 4, 5],
            "k": 3,
            "candidates": 1,
            "expected": 6,
        },

        # =========================
        # candidates >= n
        # =========================
        {
            "costs": [8, 3, 5, 1, 7],
            "k": 2,
            "candidates": 5,
            "expected": 4,
        },

        # =========================
        # Overlapping windows
        # =========================
        {
            "costs": [6, 5, 4, 3, 2, 1],
            "k": 4,
            "candidates": 4,
            "expected": 10,
        },
        {
            "costs": [9, 1, 8, 2, 7, 3, 6],
            "k": 4,
            "candidates": 4,
            "expected": 12,
        },

        # =========================
        # All equal values
        # =========================
        {
            "costs": [5, 5, 5, 5, 5],
            "k": 3,
            "candidates": 2,
            "expected": 15,
        },

        # =========================
        # Tie-breaking by index
        # =========================
        {
            "costs": [2, 1, 3, 1, 2],
            "k": 2,
            "candidates": 2,
            "expected": 2,
        },
        {
            "costs": [4, 1, 1, 4],
            "k": 2,
            "candidates": 2,
            "expected": 2,
        },

        # =========================
        # Middle element eventually exposed
        # =========================
        {
            "costs": [10, 9, 1, 9, 10],
            "k": 3,
            "candidates": 1,
            "expected": 20,
        },

        # =========================
        # Random looking cases
        # =========================
        {
            "costs": [7, 4, 6, 2, 9, 1, 8, 3],
            "k": 5,
            "candidates": 3,
            "expected": 17,
        },
        {
            "costs": [100, 1, 100, 1, 100],
            "k": 2,
            "candidates": 2,
            "expected": 2,
        },
        {
            "costs": [3, 8, 2, 7, 4, 6, 1, 5],
            "k": 4,
            "candidates": 2,
            "expected": 11,
        },

        # =========================
        # Large candidates causing full overlap
        # =========================
        {
            "costs": [9, 8, 7, 6, 5, 4],
            "k": 3,
            "candidates": 6,
            "expected": 15,
        },

        # =========================
        # Minimum costs at both ends
        # =========================
        {
            "costs": [1, 9, 9, 9, 1],
            "k": 2,
            "candidates": 1,
            "expected": 2,
        },

        # =========================
        # Increasing then decreasing
        # =========================
        {
            "costs": [1, 2, 3, 4, 3, 2, 1],
            "k": 5,
            "candidates": 2,
            "expected": 9,
        },
    ]

    for i, tc in enumerate(test_cases, 1):
        result = solution.totalCost(tc["costs"], tc["k"], tc["candidates"])
        status = "PASS" if result == tc["expected"] else "FAIL"

        print(f"Test Case {i}: {status}")
        print(f"Costs      : {tc['costs']}")
        print(f"k          : {tc['k']}")
        print(f"Candidates : {tc['candidates']}")
        print(f"Expected   : {tc['expected']}")
        print(f"Got        : {result}")
        print("-" * 60)