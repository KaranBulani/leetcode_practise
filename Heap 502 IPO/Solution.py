'''
The key observation:

* At any point, you can only start projects whose capital[i] <= current_capital.
* Among all currently available projects, you should always pick the one with the maximum profit.
* As your capital increases, more projects become available.

This naturally suggests:
1. Sort projects by required capital.
2. Use a max heap to store profits of all projects currently affordable.
3. Repeat at most k times:
   * Add all newly affordable projects into the heap.
   * Pick the project with maximum profit.
   * Add its profit to capital.
   * If no project is affordable, stop.

####################################################################################################
Example

    k = 2
    w = 0

    capital = [0,1,1]
    profits = [1,2,3]


Sorted projects:		[(0,1), (1,2), (1,3)]


Initial capital = 0

Round 1
    * Affordable: (0,1)
    * Heap = [1]
    * Take profit 1
    * Capital = 1

Round 2
    * Newly affordable: (1,2), (1,3)
    * Heap = [3,2]
    * Take profit 3
    * Capital = 4

Answer = 4

####################################################################################################

Why Greedy Works

Suppose your current capital is w.
Among all projects you can currently do:		capital[i] <= w
choosing anything except the highest profit cannot help.

If profits are:		2, 5, 8

and you choose 2 instead of 8, your future capital is always smaller, meaning you can never unlock more projects than choosing 8 would.

Therefore:

> Whenever multiple projects are available, taking the maximum profit is always optimal.

The heap efficiently gives us that project.

####################################################################################################
Complexity

Sorting:    	    	O(n log n)

Each project:
* pushed once
* popped at most once
Heap work:  			O(n log n)

Total:			        O(n log n)

Space:      	    	O(n)
'''
from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))

        max_heap = []
        i = 0
        n = len(projects)

        while k > 0:

            # Add all affordable projects
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # No project can be started
            if not max_heap:
                break

            # Pick most profitable project
            w += -heapq.heappop(max_heap)

            k -= 1

        return w

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {
            "name": "Example 1",
            "k": 2,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [0, 1, 1],
            "expected": 4,
        },
        {
            "name": "Example 2",
            "k": 3,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [0, 1, 2],
            "expected": 6,
        },

        # Only one project available
        {
            "name": "Single Project",
            "k": 1,
            "w": 0,
            "profits": [5],
            "capital": [0],
            "expected": 5,
        },

        # Cannot start any project
        {
            "name": "No Affordable Project",
            "k": 3,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [1, 2, 3],
            "expected": 0,
        },

        # k larger than number of projects
        {
            "name": "k Greater Than n",
            "k": 10,
            "w": 0,
            "profits": [1, 2, 3],
            "capital": [0, 0, 0],
            "expected": 6,
        },

        # All projects immediately available
        {
            "name": "All Available Initially",
            "k": 2,
            "w": 100,
            "profits": [5, 20, 10, 1],
            "capital": [0, 10, 50, 99],
            "expected": 130,
        },

        # Must unlock larger profit projects gradually
        {
            "name": "Progressive Unlock",
            "k": 3,
            "w": 0,
            "profits": [1, 2, 100],
            "capital": [0, 1, 3],
            "expected": 103,
        },

        # Multiple projects with same capital requirement
        {
            "name": "Same Capital Requirement",
            "k": 2,
            "w": 1,
            "profits": [5, 1, 10, 3],
            "capital": [1, 1, 1, 1],
            "expected": 16,
        },

        # Zero profit projects
        {
            "name": "Zero Profit Projects",
            "k": 4,
            "w": 2,
            "profits": [0, 0, 5, 10],
            "capital": [0, 1, 2, 7],
            "expected": 17,
        },

        # Capital grows enough to unlock everything
        {
            "name": "Chain Unlock",
            "k": 4,
            "w": 1,
            "profits": [2, 3, 5, 20],
            "capital": [1, 3, 6, 11],
            "expected": 31,
        },

        # All profits zero
        {
            "name": "All Zero Profits",
            "k": 5,
            "w": 10,
            "profits": [0, 0, 0],
            "capital": [0, 5, 10],
            "expected": 10,
        },

        # Large initial capital
        {
            "name": "Huge Initial Capital",
            "k": 3,
            "w": 1000,
            "profits": [100, 200, 300, 400],
            "capital": [0, 100, 200, 300],
            "expected": 1900,
        },

        # Need to choose best profits among many affordable projects
        {
            "name": "Choose Highest Profit First",
            "k": 2,
            "w": 1,
            "profits": [1, 100, 50, 25],
            "capital": [1, 1, 1, 1],
            "expected": 151,
        },

        # k = 1
        {
            "name": "Only One Selection Allowed",
            "k": 1,
            "w": 2,
            "profits": [1, 5, 10],
            "capital": [0, 2, 3],
            "expected": 7,
        },

        # Capital exactly matches requirements
        {
            "name": "Exact Capital Match",
            "k": 3,
            "w": 2,
            "profits": [2, 3, 4],
            "capital": [2, 4, 7],
            "expected": 11,
        },
    ]

    for idx, tc in enumerate(test_cases, 1):
        result = solution.findMaximizedCapital(
            tc["k"],
            tc["w"],
            tc["profits"],
            tc["capital"]
        )

        status = "PASS" if result == tc["expected"] else "FAIL"

        print(f"Test {idx}: {tc['name']}")
        print(f"Expected: {tc['expected']}")
        print(f"Got     : {result}")
        print(f"Status  : {status}")
        print("-" * 50)