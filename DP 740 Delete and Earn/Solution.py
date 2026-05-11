'''
1. Observation

Read the problem statement
We can pick any number x and earn x points.
But after picking x, all values:
* x - 1
* x + 1
become unavailable.
We can pick the same value multiple times if multiple copies exist.

Key Observation

If a value appears multiple times, we should either:
* take all occurrences
* or take none
Because taking one x already removes x-1 and x+1, so there is no reason to partially take x.

So instead of thinking about individual elements:
We compress the array into:
points[x] = x * frequency(x)

Example:
nums = [2,2,3,3,3,4]
points[2] = 4
points[3] = 9
points[4] = 4

Now the problem becomes:
> Choose numbers such that no adjacent values are chosen.

This is exactly the same structure as:
House Robber

Because:
* taking value x
* prevents taking x-1 and x+1

Processing Direction
We process values from:
1 → max(nums)
because adjacency matters between values.

Core Idea
The problem is NOT about array positions.
It is about adjacent values.
So we transform:
nums → points per value
and solve using DP on values.
####################################################################################################

2. Simulation

Example:
nums = [2,2,3,3,3,4]

Build points array:
points[2] = 4
points[3] = 9
points[4] = 4

Now simulate:

At value 2
Options:
* Skip → 0
* Take → 4
Best: 	4

At value 3
If we take 3:
* cannot take 2
Options:
* Skip 3 → keep previous = 4
* Take 3 → 9
Best:	9

At value 4
If we take 4:
* cannot take 3
Options:
* Skip 4 → 9
* Take 4 → 4 + dp[2] = 8
Best:	9

Answer:		9
####################################################################################################

3. Recursion

Define:		dfs(value)

Meaning:
> Maximum points obtainable considering values from 1...value

Recurrence Relation

For each value:
	Option 1: Skip current value
	dfs(value - 1)

	Option 2: Take current value
	If we take current value:
	* cannot take value - 1

So:		points[value] + dfs(value - 2)

Therefore:
dfs(value) = max(
    dfs(value - 1),
    points[value] + dfs(value - 2)
)
this rule works post i = 2 before i = 2 we have base cases

Base Cases
dfs(0) = 0              # sum of all nums which are 0 is 0
dfs(1) = points[1]      # sum of 1 is points[1]
after 1 above formula kicks in

Why this works

At every value we make exactly one decision:
* take it
* skip it

If we take it:
* adjacent value becomes invalid

This creates smaller subproblems with identical structure.
Hence recursion + DP works naturally.
####################################################################################################

4. Dynamic Programming

Requirements

We have:
* recurrence relation
* overlapping subproblems
So DP applies.
####################################################################################################
                                            Top-Down DP
####################################################################################################

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        memo = {}
        def dfs(value):
            # Base cases
            if value == 0:
                return 0

            if value == 1:
                return points[1]

            # Check cache
            if value in memo:
                return memo[value]

            # Skip current value
            skip = dfs(value - 1)

            # Take current value
            take = points[value] + dfs(value - 2)

            memo[value] = max(skip, take)

            return memo[value]

        return dfs(max_num)


####################################################################################################
                                            BOTTOM-UP DP
####################################################################################################
DP Definition

dp[value] means:
> Maximum points obtainable considering values from 1...value

Transition
dp[value] = max(
    dp[value - 1],
    points[value] + dp[value - 2]
)

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        dp = [0] * (max_num + 1)
        dp[1] = points[1]

        for value in range(2, max_num + 1):
            skip = dp[value - 1]
            take = points[value] + dp[value - 2]
            dp[value] = max(skip, take)

        return dp[max_num]


####################################################################################################
Time Complexity

We compute each state once.
Number of states: 	max(nums)
Work per state:		O(1)

So:		Time: O(max(nums))

Space Complexity

Memo stores one entry per state.
Space: O(max(nums))

####################################################################################################
                                        Space Optimized DP
####################################################################################################
Since each state only depends on:
* previous state
* two previous state
we can optimize space.

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        prev2 = 0
        prev1 = points[1]
        for value in range(2, max_num + 1):
            current = max(prev1, points[value] + prev2)
            prev2 = prev1
            prev1 = current

        return prev1
####################################################################################################
Time Complexity		O(max(nums))

Space Complexity	O(1)
'''
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        prev2 = 0
        prev1 = points[1]
        for value in range(2, max_num + 1):
            current = max(prev1, points[value] + prev2)
            prev2 = prev1
            prev1 = current

        return prev1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example cases
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),

        # Single element
        ([1], 1),
        ([10000], 10000),

        # All same numbers
        ([5, 5, 5, 5], 20),
        ([10, 10], 20),

        # No adjacent conflicts
        ([1, 3, 5, 7], 16),
        ([2, 4, 6, 8], 20),

        # Simple adjacent conflicts
        ([1, 2], 2),
        ([2, 3], 3),
        ([3, 4], 4),

        # Choosing many smaller vs one bigger
        ([2, 2, 2, 3, 3, 4], 6),
        ([1, 1, 1, 2, 4, 5, 5, 5, 6], 18),

        # Multiple grouped ranges
        ([1, 1, 2, 2, 3, 3], 8),
        ([8, 10, 4, 9, 1, 3, 5, 9, 4, 10], 37),

        # Large gaps between numbers
        ([1, 100, 200], 301),
        ([2, 2, 50, 51, 52], 56),

        # Repeated high frequency
        ([3, 3, 3, 4, 2], 9),
        ([4, 4, 4, 5, 5, 6], 18),

        # Edge ordering cases
        ([6, 5, 4, 3, 2, 1], 12),
        ([1, 2, 3, 15, 16, 17], 35),

        # Stress-style medium case
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6], 22),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.deleteAndEarn(nums)

        print(f"Test Case {i}")
        print(f"nums      = {nums}")
        print(f"Expected  = {expected}")
        print(f"Got       = {result}")
        print(f"PASS      = {result == expected}")
        print("-" * 50)