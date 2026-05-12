'''
1. Observation

We can:
    * Buy a stock
    * Sell a stock
    * Skip a day

Restrictions:
    * Cannot hold multiple stocks
    * After selling, next day becomes cooldown (cannot buy)

We want:
    * Maximum total profit

Identify key observations

At any day, our situation is determined by:
    1. Current day i
    2. Whether we are free to buy or currently holding a stock

If we are:
    * Free to buy
      * Buy today
      * Skip today
    * Holding a stock
      * Sell today
      * Keep holding

Important cooldown observation

If we sell on day i, then day i+1 becomes cooldown.

So after selling:
    * We directly move to i+2
This is the key transition of the problem.

Core Idea
This is a decision problem:
    * Every day we choose an action
    * Future profit depends on current decision

Same states repeat again and again:
    * (day, free_to_buy)

So this naturally leads to:
    * Recursion
    * Memoization (DP)
####################################################################################################

2. Simulation

Example:	prices = [1,2,3,0,2]

Day 0:
	* Buy at 1
Day 1:
	* Sell at 2
	  Profit = 1
Day 2:
	* Cooldown (cannot buy)
Day 3:
	* Buy at 0
Day 4:
	* Sell at 2
	  Profit = 2

Total profit = 3

Now observe the structure:
At every day:
* choose action
* move to next valid state
This becomes a recursive decision tree.
####################################################################################################

3. Recursion

Define:		dfs(i, free_to_buy)

Meaning:
* Maximum profit possible starting from day i
    where:
    * free_to_buy = True
      → we do NOT currently own stock
    * free_to_buy = False
      → we ARE holding stock

Base Case
If:
	i >= len(prices)
	No days left.
So:		return 0

Recurrence Relation

Case 1: Free to Buy
We have 2 choices:
1. Buy stock
    If we buy:
    * spend prices[i]
    * move to next day holding stock
    -prices[i] + dfs(i+1, False)

2. Skip day
    dfs(i+1, True)

Take maximum:
    dfs(i, True) =
    max(
        -prices[i] + dfs(i+1, False),
        dfs(i+1, True)
    )

Case 2: Holding Stock
We have 2 choices:
1. Sell stock
    If we sell:
    * gain prices[i]
    * next day becomes cooldown
    * so move to i+2
    prices[i] + dfs(i+2, True)

2. Keep holding
    dfs(i+1, False)

Take maximum:
    dfs(i, False) =
        max(
            prices[i] + dfs(i+2, True),
            dfs(i+1, False)
        )
####################################################################################################

4. Dynamic Programming

Why DP? Many states repeat.

Example:
* dfs(3, True) may be reached from multiple paths.
So we cache results.

####################################################################################################
                                            Top-Down DP
####################################################################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i: int, free_to_buy: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, free_to_buy) in memo:
                return memo[(i, free_to_buy)]

            # We do not currently own stock
            if free_to_buy:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, True)
                profit = max(buy, skip)

            # We currently own stock
            else:
                sell = prices[i] + dfs(i + 2, True) # cooldown
                hold = dfs(i + 1, False)
                profit = max(sell, hold)

            memo[(i, free_to_buy)] = profit
            return profit

        return dfs(0, True)

####################################################################################################
                                            BOTTOM-UP DP
####################################################################################################

Define:
    dp[i][1] -> max profit at day i when free to buy
    dp[i][0] -> max profit at day i when holding stock

Transition:
dp[i][1] =
	max(
		-prices[i] + dp[i+1][0],
		dp[i+1][1]
	)

dp[i][0] =
	max(
		prices[i] + dp[i+2][1],
		dp[i+1][0]
	)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):

            # Free to buy
            dp[i][1] = max(
                -prices[i] + dp[i + 1][0],
                dp[i + 1][1]
            )

            # Holding stock
            dp[i][0] = max(
                prices[i] + dp[i + 2][1],
                dp[i + 1][0]
            )

        return dp[0][1]

####################################################################################################

Number of States

State:  (i, free_to_buy)

Possible values:
    * i → n
    * free_to_buy → 2 values

Total states:
O(2n) = O(n)

Work per State

Each state does:
* constant number of transitions
So: O(1)

Time Complexity
    (#states) × (work per state)
    = O(2n) × O(1)
    = O(n)

Space Complexity
    Memo table:	O(2n)
    Recursion stack: O(2n)
    Total: O(n)
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([1, 2, 3, 0, 2], 3),
        ([1], 0),

        # Edge cases
        ([2, 1], 0),  # decreasing prices
        ([1, 2], 1),  # single profitable transaction
        ([1, 2, 4], 3),  # hold longer instead of multiple sells
        ([4, 3, 2, 1], 0),  # always decreasing
        ([1, 2, 3, 4, 5], 4),  # continuous increase
        ([5, 4, 3, 2, 10], 8),  # late profitable sell
        ([6, 1, 3, 2, 4, 7], 6),  # multiple opportunities
        ([1, 2, 3, 0, 2, 3], 4),  # cooldown impacts decisions
        ([2, 1, 4], 3),  # buy after drop
        ([1, 2, 3, 0, 2, 1, 4], 5),  # multiple cooldown transitions
        ([3, 2, 6, 5, 0, 3], 7),  # classic stock variation
        ([1, 4, 2], 3),  # early sell best
        ([2, 1, 2, 0, 1], 1),  # cooldown prevents chaining
        ([1, 2, 1, 2, 1, 2], 2),  # alternating prices
        ([0, 0, 0, 0], 0),  # all same prices
        ([10, 1, 10, 1, 10], 18),  # large profits with cooldown
    ]

    for i, (prices, expected) in enumerate(test_cases, 1):
        result = solution.maxProfit(prices)

        print(f"Test Case {i}")
        print(f"Prices   : {prices}")
        print(f"Expected : {expected}")
        print(f"Got      : {result}")
        print(f"Passed   : {result == expected}")
        print("-" * 40)