'''
1. Observation

✅ Reduce problem

We are given:
* coins[] → denominations (infinite supply)
* amount → target

We need:
👉 Minimum number of coins to make amount
👉 Return -1 if impossible

✅ Key observations
* This is an optimization problem (min coins)
* We are allowed:
  * reuse coins unlimited times
* Order does NOT matter (combination, not permutation)

✅ Constraints thinking
* amount <= 10^4 → manageable DP (if the final solution doesn't go beyond 10^6)
* Coins can be big number → greedy may fail
Coins = [1, 3, 4], amount = 6
Greedy picks: 4 + 1 + 1 = 3 coins
Optimal: 3 + 3 = 2 coins
So coin change is not greedy

✅ Core Insight
* Try all possible coin choices
* Minimize number of coins

👉 This screams:
> "Try all choices + take minimum" → DP
####################################################################################################
                                            TOP DOWN - DP
####################################################################################################
3. Recursion (Top-Down View)

✅ Define function
f(rem_amount) = minimum coins needed to make rem_amount

✅ Recurrence
For every coin:
f(rem) = min(f(rem - coin) + 1)

✅ Base cases
f(0) = 0
f(rem < 0) = ∞ (invalid)

⚠️ Overlapping subproblems
Same rem_amount will be recomputed multiple times → use memoization
####################################################################################################
4. Dynamic Programming (Memoization)

✅ Memo definition
memo[rem] = minimum coins needed for rem

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = {}

        def dfs(rem):
            # Base cases
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            # Check cache
            if rem in memo:
                return memo[rem]

            # Try all coins
            min_coins = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)

            # Store result
            memo[rem] = min_coins
            return memo[rem]

        ans = dfs(amount)
        return ans if ans != float('inf') else -1

####################################################################################################
                                        BOTTOM UP - DP
####################################################################################################
2. Simulation
Example:	coins = [1,2,5], amount = 11
Let’s build from small → big:
| Amount | Best |
| ------ | ---- |
| 0      | 0    |
| 1      | 1    |
| 2      | 1    |
| 3      | 2    |
| 4      | 2    |
| 5      | 1    |
| 6      | 2    |
| ...    | ...  |
| 11     | 3    |

Transition idea:
To make amt, try every coin:
dp[amt] = min(dp[amt - coin] + 1)

Generalization
For any amount:
* Pick a coin
* Solve smaller problem
* Add 1 coin
####################################################################################################
3. Recursion
Define function
f(amount) = minimum coins needed

Recurrence
f(amount) = min(f(amount - coin) + 1) for all coins

Base cases
f(0) = 0
f(negative) = ∞ (invalid)
####################################################################################################
4. Dynamic Programming

✅ State
dp[x] = minimum coins needed to make amount x

✅ Transition
dp[x] = min(dp[x - coin] + 1)

✅ Initialization
dp[0] = 0
dp[x] = ∞ (for all x > 0)

✅ Answer
if dp[amount] == ∞ → return -1
else → return dp[amount]
####################################################################################################
✅ Time Complexity -
    states = amount
    work per state = len(coins)
    TC = O(amount * coins)

✅ Space Complexity -
    O(amount)

'''
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Step 1: DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # Step 2: Build solution
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0: # dp[amt - coin] != ∞ can also add this condition

                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        # Step 3: Result
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic cases (from problem)
        {"coins": [1, 2, 5], "amount": 11, "expected": 3},
        {"coins": [2], "amount": 3, "expected": -1},
        {"coins": [1], "amount": 0, "expected": 0},

        # Edge cases
        {"coins": [1], "amount": 1, "expected": 1},            # smallest valid
        {"coins": [1], "amount": 2, "expected": 2},            # only one coin type
        {"coins": [2, 5, 10], "amount": 0, "expected": 0},     # zero amount
        {"coins": [2], "amount": 4, "expected": 2},            # exact division
        {"coins": [2], "amount": 1, "expected": -1},           # impossible

        # Greedy failure cases (important!)
        {"coins": [1, 3, 4], "amount": 6, "expected": 2},      # 3+3, not 4+1+1
        {"coins": [2, 3, 5], "amount": 7, "expected": 2},      # 5+2

        # Larger combinations
        {"coins": [1, 2, 5], "amount": 100, "expected": 20},
        {"coins": [2, 5, 10, 1], "amount": 27, "expected": 4}, # 10+10+5+2

        # Unreachable due to GCD constraint
        {"coins": [4, 6], "amount": 7, "expected": -1},

        # Large coin values
        {"coins": [186, 419, 83, 408], "amount": 6249, "expected": 20},

        # Single coin large amount
        {"coins": [7], "amount": 49, "expected": 7},

        # Another tricky combination
        {"coins": [9, 6, 5, 1], "amount": 11, "expected": 2},  # 6+5
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.coinChange(test["coins"], test["amount"])
        print(f"Test Case {i}:")
        print(f"Coins = {test['coins']}, Amount = {test['amount']}")
        print(f"Expected = {test['expected']}, Got = {result}")
        print("PASS" if result == test["expected"] else "FAIL")
        print("-" * 40)