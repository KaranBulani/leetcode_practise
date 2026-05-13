'''
1. Observation

We need to select jobs such that:
* Jobs do not overlap
* If one job ends at time X, another can start at time X
* We want maximum total profit

Each job has:
* start
* end
* profit

A brute force idea would be:
* For every job:
  * Take it
  * Skip it
But after taking a job, we must jump to the next non-overlapping job.

This creates overlapping subproblems:
* “Maximum profit starting from job i”
That strongly suggests Dynamic Programming.
####################################################################################################

2. Simulation

Example:
startTime = [1,2,3,3]
endTime   = [3,4,5,6]
profit    = [50,10,40,70]

Create jobs and sort by start time:
jobs = [
    (1,3,50),
    (2,4,10),
    (3,5,40),
    (3,6,70)
]

Suppose we are at job 0 → (1,3,50)

We have 2 choices:

	Choice 1: Skip current job
	Move to next job: dfs(1)

	Choice 2: Take current job
	Profit gained: 50

Now we must find the next job whose:
start >= 3

That is index 2.
So: 50 + dfs(2)

Final recurrence:
dfs(i) = max(
    skip current job,
    take current job + next compatible job
)
####################################################################################################

3. Recursion

Define:

dfs(i)      > Maximum profit we can make starting from index i

Base Case
    If no jobs remain:

    if i >= n:
        return 0

Recursive Choices
At every index:

1. Skip current job
    skip = dfs(i + 1)

2. Take current job
    Current profit:	jobs[i][2]

    Then jump to next non-overlapping job.

    We use binary search to find first job with:
    start >= current_end
    next_index = binary_search(current_end)

    Then:
    take = current_profit + dfs(next_index)

Recurrence Relation
dfs(i) = max(skip, take)
####################################################################################################

4. Dynamic Programming

The same states repeat many times.

Example:
	dfs(3)
	may be reached from multiple paths.
	So we cache results.

State i
Only current index matters.

Transition
dp[i] = max(
    dfs(i + 1),
    profit[i] + dfs(next_index)
)
####################################################################################################
                                            Top-Down DP
####################################################################################################
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        def binary_search(target: int) -> int:
            low = 0
            high = n - 1
            ans = n
            while low <= high:
                mid = (low + high) // 2
                if starts[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        memo = {}
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]

            # Skip current job
            skip = dfs(i + 1)

            # Take current job
            start, end, gain = jobs[i]
            next_index = binary_search(end)
            take = gain + dfs(next_index)
            memo[i] = max(skip, take)

            return memo[i]

        return dfs(0)
####################################################################################################
                                            BOTTOM-UP DP
####################################################################################################
Idea

Instead of solving from front → back recursively,
we solve from:  n - 1 → 0
because future states must already be known.

Transition
    dp[i] = max(
        dp[i + 1],
        profit[i] + dp[next_index]
    )

from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        starts = [job[0] for job in jobs]
        n = len(jobs)

        def binary_search(target: int) -> int:
            low = 0
            high = n - 1

            ans = n
            while low <= high:
                mid = (low + high) // 2
                if starts[mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1

            return ans

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            start, end, gain = jobs[i]
            next_index = binary_search(end)

            skip = dp[i + 1]
            take = gain + dp[next_index]
            dp[i] = max(skip, take)
        return dp[0]

####################################################################################################
Time Complexity

For each job:
* Binary search → O(log n)
* State computed once
Total:	O(n log n)

Space Complexity

O(n) for memoization + recursion stack.
'''

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70],
            "expected": 120
        },

        # Example 2
        {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60],
            "expected": 150
        },

        # Example 3
        {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4],
            "expected": 6
        },

        # Non-overlapping chain (take all)
        {
            "startTime": [1, 3, 5, 7],
            "endTime": [3, 5, 7, 9],
            "profit": [20, 30, 25, 50],
            "expected": 125
        },

        # Completely overlapping jobs (take max profit one)
        {
            "startTime": [1, 1, 1, 1],
            "endTime": [5, 5, 5, 5],
            "profit": [10, 40, 30, 20],
            "expected": 40
        },

        # Jobs touching endpoints are allowed
        {
            "startTime": [1, 2, 3],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 7],
            "expected": 18
        },

        # Better to skip one large interval
        {
            "startTime": [1, 2, 3, 4],
            "endTime": [10, 3, 4, 5],
            "profit": [100, 40, 40, 40],
            "expected": 120
        },

        # Single job
        {
            "startTime": [5],
            "endTime": [10],
            "profit": [99],
            "expected": 99
        },

        # Unsorted input
        {
            "startTime": [4, 2, 1, 6],
            "endTime": [6, 5, 3, 9],
            "profit": [70, 20, 50, 60],
            "expected": 180
        },

        # Choosing smaller compatible jobs beats one big job
        {
            "startTime": [1, 2, 3, 4],
            "endTime": [5, 3, 4, 6],
            "profit": [50, 20, 20, 70],
            "expected": 110
        },

        # Large gap between jobs
        {
            "startTime": [1, 100],
            "endTime": [2, 101],
            "profit": [10, 20],
            "expected": 30
        },

        # Same start, different end/profit
        {
            "startTime": [1, 1, 1, 4],
            "endTime": [2, 3, 4, 5],
            "profit": [20, 50, 70, 60],
            "expected": 80
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.jobScheduling(
            test["startTime"],
            test["endTime"],
            test["profit"]
        )

        print(f"Test Case {i}")
        print(f"Start Time : {test['startTime']}")
        print(f"End Time   : {test['endTime']}")
        print(f"Profit     : {test['profit']}")
        print(f"Expected   : {test['expected']}")
        print(f"Got        : {result}")
        print(f"Passed     : {result == test['expected']}")
        print("-" * 50)