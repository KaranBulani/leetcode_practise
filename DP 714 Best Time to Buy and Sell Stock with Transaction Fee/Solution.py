'''
1. Observation

Read the problem statement

We have:
* prices[i] = stock price on day i
* We can perform multiple transactions
* At most one stock can be held at a time
* We must sell before buying again
* Every completed buy + sell transaction costs fee
* We want to maximize profit

For example:
	prices = [1, 3, 2, 8, 4, 9]
	fee = 2

Best strategy:
	Buy  at 1
	Sell at 8 → profit = 8 - 1 - 2 = 5

	Buy  at 4
	Sell at 9 → profit = 9 - 4 - 2 = 3

	Total = 8

Identify key words and phrases
The important constraint is:
> You may not engage in multiple transactions simultaneously.

This means that on any day, we are in one of only two states:
1. Holding a stock
2. Not holding a stock

That immediately suggests a 2-state DP.

####################################################################################################
2. Simulation

Let's simulate:
	prices = [1, 3, 2, 8, 4, 9]
	fee = 2

At any point, we ask:

State 1: not_holding
We don't currently own a stock.

We have two choices:
* Skip → remain not_holding
* Buy → move to holding

State 2: holding
We currently own a stock.

We have two choices:
* Skip → remain holding
* Sell → move to not_holding

So our state transitions are:
                  buy
        ┌─────────────────────┐
        │                     ↓
not_holding              holding
        ↑                     │
        └─────────────────────┘
                  sell

The fee is paid when we sell: sell → +price - fee

####################################################################################################
3. Dynamic Programming

We don't need recursion here because the days naturally progress from left to right.

We can define:
	not_holding = maximum profit if we finish today without owning stock
	holding = maximum profit if we finish today while owning stock

Transition for not_holding

There are two possibilities.

1. Skip
We were already not holding yesterday:
	not_holding

2. Sell
We were holding yesterday and sell today:
	holding + price - fee

Therefore:
	new_not_holding = max(
		not_holding,
		holding + price - fee
	)

####################################################################################################

Transition for holding

Again, two possibilities.

1. Skip
We were already holding:
	holding

2. Buy
We were not holding and buy today:
	not_holding - price

Therefore:
new_holding = max(
    holding,
    not_holding - price
)

####################################################################################################

Initial state

Before processing any stock price:
	not_holding = 0

We have no stock and no profit.

But:
	holding = -∞

because we cannot be holding a stock before making a purchase.

####################################################################################################

Important: update both states simultaneously

Suppose we have:
	new_not_holding = max(not_holding, holding + price - fee)
	new_holding = max(holding, not_holding - price)

Then:
	not_holding = new_not_holding
	holding = new_holding

We must conceptually calculate both from yesterday's states.
This is the same idea as the stock DP you were working through earlier:
	not_holding
		├── skip
		└── sell

	holding
		├── skip
		└── buy

####################################################################################################
4. Work Through the Example
	prices = [1, 3, 2, 8, 4, 9]
	fee = 2

Initial:
	not_holding = 0
	holding = -∞

Price = 1

Buy:
	holding = 0 - 1 = -1

So:
	not_holding = 0
	holding = -1

####################################################################################################

Price = 3

Sell:
	holding + price - fee
	= -1 + 3 - 2
	= 0

No profit is gained by selling yet.

So:
	not_holding = 0
	holding = -1

####################################################################################################

Price = 2

Buying at 2 isn't better than our existing purchase at 1.
	holding = max(-1, 0 - 2)
			= -1

####################################################################################################

Price = 8

Now selling is profitable:
	holding + 8 - 2
	= -1 + 8 - 2
	= 5

So:
	not_holding = 5

We have effectively:
	buy at 1
	sell at 8
	profit = 5

####################################################################################################

Price = 4

Now we can buy again:
	holding = max(-1, 5 - 4)
			= 1

Notice something important:
	holding = 1

This doesn't mean we have physically earned 1 while holding a stock.

It means:
	profit from previous transaction - cost of current stock
	= 5 - 4
	= 1

####################################################################################################

Price = 9

Sell:
	holding + 9 - 2
	= 1 + 9 - 2
	= 8

Therefore:
	answer = 8

####################################################################################################
5. Technique Selection

Following the template:
	Observation
		↓
	Only two possible states:
	holding / not_holding
		↓
	Each state has two possible actions
		↓
	Recurrence relation
		↓
	Dynamic Programming

The key insight isn't simply:
> "This is a stock DP problem."

Instead, we observe that the problem's constraints create two states.
Once we identify those states, the transitions become natural.

####################################################################################################
6. Optimize the DP

Our DP technically has:
	dp[day][state]

But today's values depend only on yesterday's values.
Therefore, we don't need an entire n × 2 table.
We only need:
	not_holding
	holding

So:
Time Complexity		O(n)

We process every price once.
Space Complexitya		O(1)

Only two variables are maintained.
####################################################################################################
Why do we return not_holding?
At the end, we want the maximum realized profit.
If we return holding, we would still own a stock, meaning some of the value is tied up in an unsold stock.

Therefore:		return not_holding
is the correct final state.
'''
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        not_holding = 0
        holding = float("-inf")

        for price in prices:
            new_not_holding = max(
                not_holding,
                holding + price - fee
            )

            new_holding = max(
                holding,
                not_holding - price
            )

            not_holding = new_not_holding
            holding = new_holding

        return not_holding

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "prices": [1, 3, 2, 8, 4, 9],
            "fee": 2,
            "expected": 8
        },

        # Example 2
        {
            "prices": [1, 3, 7, 5, 10, 3],
            "fee": 3,
            "expected": 6
        },

        # Edge Case 1: Only one day
        {
            "prices": [5],
            "fee": 2,
            "expected": 0
        },

        # Edge Case 2: Prices always decrease
        {
            "prices": [9, 7, 5, 3, 1],
            "fee": 2,
            "expected": 0
        },

        # Edge Case 3: Prices always increase
        {
            "prices": [1, 2, 3, 4, 5],
            "fee": 1,
            "expected": 3
        },

        # Edge Case 4: No profit after transaction fee
        {
            "prices": [1, 2, 3, 4],
            "fee": 5,
            "expected": 0
        },

        # Edge Case 5: Fee = 0
        {
            "prices": [1, 3, 2, 8, 4, 9],
            "fee": 0,
            "expected": 12
        },

        # Edge Case 6: All prices equal
        {
            "prices": [5, 5, 5, 5, 5],
            "fee": 2,
            "expected": 0
        },

        # Edge Case 7: Multiple profitable transactions
        {
            "prices": [1, 5, 2, 7, 3, 9],
            "fee": 1,
            "expected": 13
        },

        # Edge Case 8: Selling and buying around a dip
        {
            "prices": [1, 10, 2, 3, 12],
            "fee": 2,
            "expected": 17
        },

        # Edge Case 9: Profit exists, but fee eliminates it
        {
            "prices": [1, 2],
            "fee": 1,
            "expected": 0
        },

        # Edge Case 10: Large values
        {
            "prices": [49999, 1, 49998],
            "fee": 100,
            "expected": 49897
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.maxProfit(test["prices"], test["fee"])

        print(
            f"Test Case {i}: "
            f"Result = {result}, "
            f"Expected = {test['expected']}, "
            f"{'PASS' if result == test['expected'] else 'FAIL'}"
        )