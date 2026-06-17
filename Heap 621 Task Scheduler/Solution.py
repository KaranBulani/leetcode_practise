'''
### Idea

* Count the frequency of each task.
* Put frequencies into a max heap.
* Process tasks in cycles of length n + 1.
* In each cycle:
  * Execute up to n + 1 different tasks.
  * Decrease their frequencies.
  * Push unfinished tasks back into the heap.
* If tasks remain after a cycle, any unused slots in the cycle become idle time.

####################################################################################################

### Why the cycle length is n + 1?

After executing a task, we must wait n intervals before executing the same task again.
So within a window of n + 1 slots, a task can appear at most once. We greedily fill these slots with the most frequent remaining tasks to minimize idle time. This is exactly what the max heap helps us do.

####################################################################################################

## Dry Run

tasks = [A,A,A,B,B,B], n = 2

Heap = [-3, -3]

Cycle 1:
	pop A -> -2
	pop B -> -2
	time = 2
	cycle left = 1

	push back [-2,-2]
	heap not empty => add 1 idle

	time = 3

Cycle 2:
	pop A -> -1
	pop B -> -1
	time = 5
	cycle left = 1

	push back [-1,-1]
	heap not empty => add idle

	time = 6

Cycle 3:
	pop A
	pop B
	time = 8

	heap empty => no idle

Answer = 8
####################################################################################################

## Complexity Analysis
Let:
* N = len(tasks)
* K = number of unique tasks (at most 26)

### Time Complexity
* Building frequency map: O(N)
* Heap operations: each task occurrence is popped/pushed once.

Overall: O(N log K)
Since K ≤ 26, this is effectively O(N).

### Space Complexity
O(K) - for the frequency map and heap.

'''
from collections import Counter
from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = list(freq.values())
        heapq.heapify_max(max_heap)

        time = 0
        while max_heap:
            temp = []
            i = 0
            while i < n + 1 and max_heap:
                curr_max = heapq.heappop_max(max_heap)
                if curr_max > 1:
                    temp.append(curr_max - 1)
                time += 1
                i += 1

            if temp:
                # add buffer time iff there are sometime to add in next slot
                # if nothing in next slot then no need to add buffer
                time += (n + 1 - i)

            for count in temp:
                heapq.heappush_max(max_heap, count)
            temp = []

        return time

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        (
            ["A", "A", "A", "B", "B", "B"],
            2,
            "Expected: ?"
        ),
        (
            ["A", "C", "A", "B", "D", "B"],
            1,
            "Expected: ?"
        ),
        (
            ["A", "A", "A", "B", "B", "B"],
            3,
            "Expected: ?"
        ),

        # Edge Case: Single task
        (
            ["A"],
            5,
            "Expected: ?"
        ),

        # Edge Case: No cooldown
        (
            ["A", "A", "A", "B", "B", "B"],
            0,
            "Expected: ?"
        ),

        # All tasks unique
        (
            ["A", "B", "C", "D", "E", "F"],
            3,
            "Expected: ?"
        ),

        # Only one task type
        (
            ["A", "A", "A", "A"],
            2,
            "Expected: ?"
        ),

        # One dominant task
        (
            ["A", "A", "A", "A", "B", "C"],
            2,
            "Expected: ?"
        ),

        # Multiple task types with same frequency
        (
            ["A", "A", "A", "B", "B", "B", "C", "C", "C"],
            2,
            "Expected: ?"
        ),

        # Cooldown larger than distinct tasks
        (
            ["A", "A", "B", "B"],
            5,
            "Expected: ?"
        ),

        # Large frequency gap
        (
            ["A"] * 7 + ["B"] + ["C"],
            2,
            "Expected: ?"
        ),

        # Many tasks can fill idle slots
        (
            ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D"],
            2,
            "Expected: ?"
        ),

        # Two task types, high cooldown
        (
            ["A", "A", "A", "B", "B", "B"],
            4,
            "Expected: ?"
        ),

        # Maximum variety
        (
            list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            100,
            "Expected: ?"
        ),

        # Heavy tie for max frequency
        (
            ["A"] * 4 + ["B"] * 4 + ["C"] * 4,
            2,
            "Expected: ?"
        ),
    ]

    for i, (tasks, n, expected) in enumerate(test_cases, start=1):
        result = solution.leastInterval(tasks, n)
        print(f"Test Case {i}")
        print(f"tasks = {tasks}")
        print(f"n = {n}")
        print(f"Output   : {result}")
        print(f"{expected}")
        print("-" * 60)