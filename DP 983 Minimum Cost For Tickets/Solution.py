'''
1. Observation

Read the problem statement

We are given:
* days[i] → days on which we must travel
* 3 ticket types:
  * 1-day
  * 7-day
  * 30-day
We need the minimum total cost to cover all travel days.

Identify key observations

Observation 1
    We only care about the travel days present in days.
    Non-travel days do not require decisions.

Observation 2
    At every travel day, we have exactly 3 choices:
    * Buy 1-day pass
    * Buy 7-day pass
    * Buy 30-day pass
    Each choice covers a range of future days.

Observation 3
    After buying a pass, we skip all days already covered.
    Example:
    * Buy 7-day pass on day 4
    * Covers days [4...10]
    * Next uncovered travel day becomes our next decision point

Observation 4
    The problem asks for:
    * minimum cost
    * overlapping subproblems
    * optimal decisions
    This strongly suggests Dynamic Programming.

Identify processing direction

We process travel days from left → right.
At index i:
* Decide which ticket to buy
* Jump to the next uncovered travel day
####################################################################################################

2. Simulation

Take: days = [1,4,6,7,8,20], costs = [2,7,15]

Start at day 1.

Choice 1 → Buy 1-day pass
	Cost:
	2 + solve(next day after 1)
	Next index → day 4

Choice 2 → Buy 7-day pass
	Covers:	1 → 7
	Covered travel days:	1,4,6,7
	Next uncovered day:	8
	Cost:	7 + solve(index of day 8)

Choice 3 → Buy 30-day pass
	Covers all travel days.
	Cost:	15
We choose minimum among all choices.

Generalization

Define:	dp(i) = minimum cost to cover travel days starting from index i

At every index:
* Try all 3 passes
* Move to next uncovered index
* Take minimum cost
This forms the recurrence.

####################################################################################################
                                        returning dp[0]
####################################################################################################

3. Recurrence Relation

Let:	        dfs(i)
represent:  	> minimum cost needed to cover all travel days starting from days[i]

Base Case
	If all days are covered:
	if i >= len(days):
		return 0
	No more cost needed.

Transitions

From days[i], we can buy:
1-Day Pass
	Covers: days[i]
	Next index: first day >= days[i] + 1
	Cost:	costs[0] + dfs(next_index)

7-Day Pass
	Covers: days[i] → days[i] + 6
	Next index: first day >= days[i] + 7
	Cost: costs[1] + dfs(next_index)

30-Day Pass
	Covers: days[i] → days[i] + 29
	Next index: first day >= days[i] + 30
	Cost: costs[2] + dfs(next_index)

Final Recurrence
	dfs(i) = min(cost_1 + dfs(next_1), cost_7 + dfs(next_7), cost_30 + dfs(next_30))

############################################## TOP DOWN ##############################################

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            # 1-day pass
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            one_day = costs[0] + dfs(j)

            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            seven_day = costs[1] + dfs(j)

            # 30-day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            thirty_day = costs[2] + dfs(j)

            memo[i] = min(one_day, seven_day, thirty_day)
            return memo[i]

        return dfs(0)

Time Complexity
	Number of states: O(n)
	For every state:
	* we scan ahead for 3 ticket types
	* worst-case scan: O(n), if scanning entire n len days with 1 day movement, work done for this state would be O(n)
	Total:	O(n^2)

Space Complexity
	Memo table:	O(n)
	Recursion stack: O(n)
	Total: O(n)

############################################## BOTTOM UP ##############################################

DP Definition
dp[i] = minimum cost to cover travel days starting from index i

Base Case
	dp[n] = 0

Transition
	Same recurrence as top-down.
	We fill from back to front.

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):

            # 1-day pass
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            one_day = costs[0] + dp[j]

            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            seven_day = costs[1] + dp[j]

            # 30-day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            thirty_day = costs[2] + dp[j]

            dp[i] = min(one_day, seven_day, thirty_day)

        return dp[0]

Time Complexity
	States:		O(n)
	Work per state: O(n)
	Total: O(n^2)

Space Complexity
	DP array: O(n)
	No recursion stack.
	Total: O(n)
####################################################################################################
                                        returning dp[n]
####################################################################################################

Previously, we defined:
dp(i) = minimum cost starting from index i

So naturally:
answer = dp[0]
because we start from the first travel day.

Now we will redefine the DP meaning.

New DP Definition

Let: dp(i) represent:
> minimum cost to cover first i travel days
Now:
* i = 0 → no travel days covered
* i = n → all travel days covered
So final answer becomes: dp[n]

############################################## TOP DOWN ##############################################

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = {}
        def dfs(i):
            # minimum cost to cover first i travel days
            if i == 0:
                return 0
            if i in memo:
                return memo[i]

            current_day = days[i - 1]

            # 1-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day:
                j -= 1
            one_day = dfs(j) + costs[0]

            # 7-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day - 6:
                j -= 1
            seven_day = dfs(j) + costs[1]

            # 30-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day - 29:
                j -= 1
            thirty_day = dfs(j) + costs[2]

            memo[i] = min(one_day, seven_day, thirty_day)
            return memo[i]

        return dfs(n)

Time Complexity
    States: O(n)
    Work per state: O(n)
    Total: O(n^2)

Space Complexity
    Memo: O(n)
    Recursion stack: O(n)
    Total: O(n)
############################################## BOTTOM UP ##############################################
Base Case
dp[0] = 0

Filling Order
We build:	dp[1], dp[2], ..., dp[n]

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            current_day = days[i - 1]

            # 1-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day:
                j -= 1
            one_day = dp[j] + costs[0]

            # 7-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day - 6:
                j -= 1
            seven_day = dp[j] + costs[1]

            # 30-day pass
            j = i - 1
            while j > 0 and days[j - 1] >= current_day - 29:
                j -= 1
            thirty_day = dp[j] + costs[2]

            dp[i] = min(one_day, seven_day, thirty_day)
        return dp[n]

Time Complexity
	States: O(n)
	Work per state: O(n)
	Total: O(n^2)

Space Complexity
	DP array:	O(n)
	Total:	O(n)
####################################################################################################
                                            My Approach
####################################################################################################

This solution uses a calendar-day DP instead of a travel-index DP.

Earlier approaches used:
	dp[i] = minimum cost starting from travel day index i.

This approach instead defines:
	dp[day] = minimum cost to cover all travel up to calendar day day.

So:
* DP size becomes 365
* We process every day sequentially

This is possible because:
* days range is small (1 → 365)

####################################################################################################
3. Recurrence Relation

Define DP State:
dp[i] = minimum cost to cover all required travel days from day 1 to day i.

Base Case
	dp[0] = 0
	No days → no cost.

Transition

For every calendar day i:

	Case 1: Non-travel Day
	If day i is NOT a travel day:
	dp[i] = dp[i - 1]
	Reason:
	* no new ticket needed
	* previous cost carries forward

	Case 2: Travel Day
	We must cover day i. We have 3 choices.

	1-Day Pass
		Covers only current day.
		Transition: dp[i - 1] + costs[0]

	7-Day Pass
		Covers: i-6 → i
		Transition: dp[i - 7] + costs[1]
		If i < 7:
			* pass covers all previous days
		So: costs[1]

	30-Day Pass
		Covers: i-29 → i
		Transition: dp[i - 30] + costs[2]
		If i < 30:
			* pass covers everything
		So: costs[2]

Final Recurrence

For travel day i:
	dp[i] = min( dp[i-1] + cost_1, dp[i-7] + cost_7, dp[i-30] + cost_30)

For non-travel day:
	dp[i] = dp[i-1]
####################################################################################################

4. Dynamic Programming

Why DP? Overlapping Subproblems
To compute: dp[i]
we repeatedly need:
* dp[i-1]
* dp[i-7]
* dp[i-30]
These states are reused many times.

Depends on:
* whether current day is travel day
* previous computed states

Processing Order
We compute: 0 → last_day
because current state depends on smaller days.

############################################## BOTTOM UP ##############################################

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1] + 1)
        dp[0] = 0
        travel_days = set(days)

        for i in range(1, len(dp)):

            # non-travel day
            if i not in travel_days:
                dp[i] = dp[i - 1]
                continue

            # 1-day pass
            day_1_pass = dp[i - 1] + costs[0] if i >= 1 else costs[0]

            # 7-day pass
            day_7_pass = dp[i - 7] + costs[1] if i >= 7 else costs[1]

            # 30-day pass
            day_30_pass = dp[i - 30] + costs[2] if i >= 30 else costs[2]

            dp[i] = min(
                day_1_pass,
                day_7_pass,
                day_30_pass
            )

        return dp[-1]

############################################## TOP DOWN ##############################################

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        travel_days = set(days)
        memo = {}
        def dfs(day):

            # base case
            if day <= 0:
                return 0

            # already computed
            if day in memo:
                return memo[day]

            # non-travel day
            if day not in travel_days:
                memo[day] = dfs(day - 1)
                return memo[day]

            # travel day
            # 1-day pass
            day_1_pass = dfs(day - 1) + costs[0]
            # 7-day pass
            day_7_pass = dfs(day - 7) + costs[1]
            # 30-day pass
            day_30_pass = dfs(day - 30) + costs[2]

            memo[day] = min(
                day_1_pass,
                day_7_pass,
                day_30_pass
            )
            return memo[day]
        return dfs(days[-1])
####################################################################################################

Time Complexity

    Let: D = days[-1]
    Maximum possible: 365
    We iterate through all calendar days once: O(D)
    For every day: constant work is done
    Set lookup: i in travel_days -> is: O(1)

    So total: O(D)
    Since: D <= 365
    overall complexity is effectively constant.

Space Complexity

    DP Array stores: O(D)
    Travel Days Set stores: O(n)

    Total Space Complexity -     O(D + n)

    Since: D <= 365
    this is effectively constant space relative to input limits.
####################################################################################################

Important Note

In bottom-up DP:
	dp[i - 7] could become negative.
	So you handled it using:
	if i >= 7 else costs[1]
In top-down recursion:
	dfs(day - 7) may become: dfs(-3)
	So we simply use:
	if day <= 0:
		return 0
This automatically handles all negative days cleanly.

'''

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        {
            "days": [1, 4, 6, 7, 8, 20],
            "costs": [2, 7, 15],
            "expected": 11
        },

        # Example 2
        {
            "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
            "costs": [2, 7, 15],
            "expected": 17
        },

        # Single travel day
        {
            "days": [100],
            "costs": [5, 20, 50],
            "expected": 5
        },

        # All consecutive days within 7 days
        {
            "days": [1, 2, 3, 4, 5, 6, 7],
            "costs": [3, 8, 20],
            "expected": 8
        },

        # All consecutive days within 30 days
        {
            "days": list(range(1, 31)),
            "costs": [2, 10, 25],
            "expected": 25
        },

        # Sparse travel days
        {
            "days": [1, 50, 120, 200, 365],
            "costs": [4, 10, 25],
            "expected": 20
        },

        # 30-day pass better than many 1-day passes
        {
            "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "costs": [3, 14, 15],
            "expected": 15
        },

        # Multiple optimal combinations possible
        {
            "days": [1, 3, 5, 7, 12, 20, 30],
            "costs": [2, 7, 15],
            "expected": 13
        },

        # Travel across year end
        {
            "days": [330, 331, 332, 333, 334, 335, 365],
            "costs": [2, 7, 25],
            "expected": 9
        },

        # Every day of the year
        {
            "days": list(range(1, 366)),
            "costs": [2, 7, 25],
            "expected": 307
        },

        # Cheap 7-day pass dominates
        {
            "days": [1, 2, 4, 5, 6, 7, 29, 30],
            "costs": [5, 6, 100],
            "expected": 12
        },

        # Cheap 30-day pass dominates
        {
            "days": [1, 5, 10, 15, 20, 25, 30],
            "costs": [5, 20, 21],
            "expected": 21
        },
    ]

    for idx, test in enumerate(test_cases, 1):
        result = solution.mincostTickets(test["days"], test["costs"])

        print(f"Test Case {idx}")
        print(f"Days     : {test['days']}")
        print(f"Costs    : {test['costs']}")
        print(f"Expected : {test['expected']}")
        print(f"Your Ans : {result}")
        print(f"Passed   : {result == test['expected']}")
        print("-" * 50)