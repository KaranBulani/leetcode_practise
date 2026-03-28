'''
class Solution:
    def __init__(self):
        self.count = 0

    def climbStairs(self, n: int) -> int:
        if n == 0:
            self.count += 1
			return
        if n < 0:
            return

        values = [1, 2]
        for v in values:
            self.climbStairs(n - v)

        return self.count

Time Complexity = O(2^n)
Space Complexity =
	Max depth = n (if you keep subtracting 1) 👉 O(n)

####################################################################################################
####################################################################################################

DP Explanation:
🧠 1. Observation
Problem in your own words
* You are at step 0
* You need to reach step n
* At each move, you can jump:
  * +1 step
  * +2 steps
* Count total distinct ways

Key Observations
* Order matters:
  * (1,2) ≠ (2,1)
* Each step depends on previous steps
* Constraints: n <= 45 → exponential will TLE

Core Insight
To reach step n, you must come from:
* step n-1 (1 jump)
* step n-2 (2 jumps)
👉 This naturally forms a recurrence.



🧪 2. Simulation
Let’s simulate small values:

n = 1
[1]
→ ways = 1

n = 2
[1,1]
[2]
→ ways = 2

n = 3
[1,1,1]
[1,2]
[2,1]
→ ways = 3

n = 4
[1,1,1,1]
[1,1,2]
[1,2,1]
[2,1,1]
[2,2]
→ ways = 5

Pattern Detected
f(1) = 1
f(2) = 2
f(3) = 3
f(4) = 5
👉 Each value = sum of previous two

🔁 3. Recursion
Recurrence Relation
f(n) = f(n-1) + f(n-2)

Base Cases
python
f(0) = 1   # one valid way (do nothing)
f(1) = 1

Recursive Solution (Brute Force)
def f(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return f(n-1) + f(n-2)


Problem with this approach
* Same subproblems recomputed
* Example:
  * f(3) called multiple times
👉 Leads to:
Time Complexity = O(2^n) ❌

####################################################################################################
Top Down DP
####################################################################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n: int) -> int:
            if n == 0:
                return 1
            if n < 0:
                return 0

            if n in memo:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]

        return dfs(n)

| Approach     | Time   | Space  |
| ------------ | ------ | ------ |
| Memoization  | O(n)   | O(n)   |

####################################################################################################
Bottom Up Dp
####################################################################################################

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

| Approach     | Time   | Space  |
| ------------ | ------ | ------ |
| Tabulation   | O(n)   | O(n)   |
####################################################################################################
| Approach     | Time   | Space  |
| ------------ | ------ | ------ |
| Optimized DP | O(n)   | O(1) ✅ |

'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2, prev1 = 1, 2

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples
        (1, 1),  # Only one way
        (2, 2),  # 1+1, 2
        (3, 3),  # 1+1+1, 1+2, 2+1

        # Small values
        (4, 5),
        (5, 8),

        # Medium values
        (6, 13),
        (7, 21),
        (10, 89),

        # Edge cases
        (0, 1),  # Optional edge case (not in constraints, but useful)
        (45, 1836311903),  # Max constraint
    ]

    for n, expected in test_cases:
        result = solution.climbStairs(n)
        print(f"n = {n} | Output = {result} | Expected = {expected} | {'PASS' if result == expected else 'FAIL'}")