'''
####################################################################################################
####################################################################################################
1. Observation

Problem in simple words
* You have a staircase with costs on each step.
* You can start from index 0 or 1.
* From any step, you can go +1 or +2 steps.
* You must reach top (beyond last index) with minimum cost.

Key observations
* You pay cost when you land on a step, not when leaving.
* Final goal is just beyond last index (n).
* From last step, you can jump directly to top.

Important pattern
At any step i, your cost depends on:
* Coming from i-1
* Coming from i-2
👉 This screams optimal substructure → DP

####################################################################################################
2. Simulation

Let’s take: cost = [10, 15, 20]
Think backward:
* To reach step 2 → min(cost to reach 1, cost to reach 0) + cost[2]
* To reach top → min(cost to reach last two steps)

Generalization
Let:		dp[i] = minimum cost to reach step i
Then:		dp[i] = cost[i] + min(dp[i-1], dp[i-2])

Final answer:	min(dp[n-1], dp[n-2])

####################################################################################################
Top-Down + Memoization

Base cases
f(-1) = 0
f(0) = cost[0]
f(1) = cost[1] + min(f(-1), f(0))
f(n) = cost[n] + min(f(n-2), f(n-1)
Add cost[n] as that might not exist in list with this problem becomes "Min cost to reach index n + 1"

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost = cost + [0]
        def dfs(i: int) -> int:
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i-1), dfs(i-2))
            return memo[i]

        return dfs(len(cost) - 1)

####################################################################################################
Bottom-Up + Tabulation

Transition 				dp[i] = cost[i] + min(dp[i-1], dp[i-2])

class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])

####################################################################################################
Space Optimization 🔥

class Solution:
    def minCostClimbingStairs(self, cost):
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
####################################################################################################
| Approach                    | Time Complexity | Space Complexity | Notes                            |
| --------------------------- | --------------- | ---------------- | -------------------------------- |
|   Recursion (Brute Force)   | O(2^n)          | O(n)             | Exponential due to recomputation |
|   Top-Down (Memoization)    | O(n)            | O(n)             | `n` states + recursion stack     |
|   Bottom-Up (DP Array)      | O(n)            | O(n)             | Iterative, no recursion stack    |
|   Space Optimized DP        | O(n)            | O(1)             | Only last 2 states stored        |
'''
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Given examples
        ([10, 15, 20], 15),
        ([1,100,1,1,1,100,1,1,100,1], 6),

        # Edge cases
        ([0, 0], 0),                          # minimum size, zero cost
        ([5, 5], 5),                          # choose cheaper start (either same)
        ([0, 1, 2, 2], 2),                    # best path avoids expensive steps
        ([1, 2], 1),                          # smallest valid input

        # Increasing costs
        ([1,2,3,4,5,6], 9),

        # Decreasing costs
        ([6,5,4,3,2,1], 9),

        # Alternating high/low
        ([1,100,1,100,1,100], 3),

        # All same values
        ([7,7,7,7,7,7], 21),

        # Larger input
        ([1]*1000, 500),

        # Random tricky cases
        ([3,2,1,0], 2),
        ([1,100,1,1,100,1], 3),
    ]

    for i, (cost, expected) in enumerate(test_cases):
        result = solution.minCostClimbingStairs(cost)
        print(f"Test Case {i+1}:")
        print(f"Input: {cost}")
        print(f"Expected: {expected}, Got: {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)