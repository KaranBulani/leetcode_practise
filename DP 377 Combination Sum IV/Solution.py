'''
1. Observation

We are asked to count:
* all possible sequences
* where order matters
* and elements can be reused

This immediately suggests:
* At every step, we can choose any number
* After choosing a number, we reduce the remaining target
* Remaining problem has the same structure
So the problem naturally breaks into smaller subproblems.

Important insight
If:
    * current remaining target = t
then:
    * choosing number n
    * reduces problem into: ways(t - n)
Thus:
    ways(t) = ways(t - nums[0]) + ways(t - nums[1]) + ...

    depending on available numbers.

dfs(tgt) = sum(dfs(tgt - i) for i in nums)

Order matters
This is the MOST important observation.

Example: target = 3, nums = [1,2]
Starting with 1:    remaining = 2
Starting with 2:    remaining = 1
These create different sequences: (1,2), (2,1)
So we must explore every number as the NEXT choice.

####################################################################################################
                                            Top-Down DP
####################################################################################################

2. Simulation

Example: nums = [1,2,3], target = 4

Start from target = 4
We can choose:
1 → remaining = 3
2 → remaining = 2
3 → remaining = 1

So:
ways(4) =    ways(3) +    ways(2) +    ways(1)

Expand further
ways(3) =    ways(2) +    ways(1) +    ways(0)

Base case
If remaining target becomes: 0

that means:
* we formed one valid sequence

So:		ways(0) = 1
This is extremely important.

The 1 represents:	One complete valid way
It acts as the additive contribution that propagates upward through recursion.

Invalid state
If target becomes negative:		target < 0
No valid sequence possible.

So:		ways(negative) = 0
####################################################################################################

3. Recursion

Define:		dfs(remaining)
Meaning:	Number of sequences that can form remaining

Recurrence Relation

For every number:
	dfs(remaining) += dfs(remaining - num)
	Thus:	dfs(t) = Σ dfs(t - num)
for all valid numbers.

Base Cases
Valid completion
if remaining == 0:
    return 1
We successfully formed a sequence.

Invalid path
if remaining < 0:
    return 0

Impossible path.
####################################################################################################

4. Dynamic Programming

The recursion repeats many states.

Example:	dfs(3)
may be computed multiple times.
So we cache results.

This becomes Top-Down DP (Memoization).

Time Complexity
DP rule: (# Unique States) × (Work per state)

	# Unique states
	Remaining target can be:
	0 → target

	So:		O(target)	states.

Work per state
	For each state, we iterate through all numbers:
	O(len(nums))

Total Complexity
Time:  O(target * len(nums))
Space: O(target)

####################################################################################################
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 1

            if remaining < 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            ways = 0

            for num in nums:
                ways += dfs(remaining - num)

            memo[remaining] = ways
            return ways

        return dfs(target)

Dry Run

nums = [1,2,3], 	target = 4

dfs(4)    = dfs(3) + dfs(2) + dfs(1)
dfs(3)    = dfs(2) + dfs(1) + dfs(0)
dfs(0) 	  = 1

Eventually:
dfs(4) = 7

####################################################################################################
                                            BOTTOM-UP DP
####################################################################################################
2. Simulation

Example:
nums = [1,2,3], target = 4

Initialize
We need:	dp[0]

Why dp[0] = 1 ?
There is exactly one way to form target 0:
Choose nothing

So:
dp[0] = 1

This acts as the starting contribution for building larger targets.

Build target = 1
Using:
1:    dp[1] += dp[0]
2:    invalid
3:    invalid
So:	dp[1] = 1

Build target = 2
Using 1:    dp[2] += dp[1]
Using 2:    dp[2] += dp[0]
Using 3:    invalid
So:			dp[2] = 2
Sequences: (1,1), (2)

Build target = 3
Using 1:    dp[3] += dp[2]
Using 2:    dp[3] += dp[1]
Using 3:    dp[3] += dp[0]
So:			dp[3] = 4
Sequences:	(1,1,1), (1,2), (2,1), (3)

Build target = 4
dp[4]
    = dp[3] + dp[2] + dp[1]
    = 4 + 2 + 1
    = 7

####################################################################################################
3. Dynamic Programming

State Definition
dp[t] = Number of sequences that form target t

Transition

For every target:	dp[t] += dp[t - num]
Base Case		dp[0] = 1
One valid way to form zero.

Important Ordering Observation

We iterate:
target outer loop
numbers inner loop

Why?
Because:
We want different sequences counted separately

Example:
(1,2), (2,1)
Both must be counted.

This ordering ensures:
* every target considers all possible LAST choices
Thus order-sensitive counting works correctly.

####################################################################################################
4. Time Complexity

DP rule: 	(Unique States) × (Work per state)

Unique States
	Targets:
	0 → target
	So: O(target)

Work per State
	For each target:
	iterate through nums
	So:	O(len(nums))

Total Complexity
	Time:  O(target * len(nums))
	Space: O(target)

####################################################################################################
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)

        dp[0] = 1

        for curr_target in range(1, target + 1):

            for num in nums:

                if curr_target - num >= 0:
                    dp[curr_target] += dp[curr_target - num]

        return dp[target]

Dry Run
nums = [1,2,3], target = 4

Initial:
dp = [1,0,0,0,0]

After target = 1:
dp = [1,1,0,0,0]

After target = 2:
dp = [1,1,2,0,0]

After target = 3:
dp = [1,1,2,4,0]

After target = 4:
dp = [1,1,2,4,7]

Answer: 7

####################################################################################################
                                            BRUTE FORCE
####################################################################################################
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        combinations = 0
        def dfs(tgt: int) -> int:
            nonlocal combinations
            if tgt == 0:
                combinations += 1
                return
            if tgt < 0:
                return

            for n in nums:
                dfs(tgt - n)
            return

        dfs(target)
        return combinations

Time Complexity -
    Let:
    N = len(nums)
    T = target
    At every recursive call, you try all N numbers:

    Suppose nums has minimum value of 1, so recursive depth will go till T level deep. Never more than that

    Level 1 - all N nums are traversed
    Level 2 - all N nums are traversed
    ...
    Level T - all N nums are traversed

    All aggregate combinations would be N * N * N ... T times
    which is N^T


Space Complexity -
    You are not storing memo/cache.
    Only recursion stack is used.
    Maximum recursion depth:    O(T)
    (when repeatedly subtracting 1)
    Therefore:        O(T)

####################################################################################################
                                            FOLLOW UP
####################################################################################################
Follow Up: What if negative numbers are allowed?

Suppose:
nums = [1, -1]	target = 1

Then:
1
1 + (-1) + 1
1 + (-1) + 1 + (-1) + 1
...
Infinite sequences become possible.
So the answer becomes infinite.

Required Limitation
We must restrict sequence formation somehow.

Common restriction:
	Limit the maximum sequence length
	or
	Each number can only be used limited times

Without such restrictions:
Negative + Positive numbers
→ Can create cycles
→ Infinite combinations

Hence the problem becomes ill-defined.

'''

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([1, 2, 3], 4),
        ([9], 3),

        # Basic edge cases
        ([1], 1),
        ([1], 5),
        ([2], 1),
        ([2], 2),

        # Small diverse cases
        ([1, 2], 3),
        ([2, 3, 5], 8),
        ([4, 2, 1], 5),

        # Order matters checks
        ([1, 2], 4),
        ([3, 1, 2], 4),

        # No possible combinations
        ([5, 10], 1),
        ([7], 14),

        # Larger target
        ([1, 2, 3], 10),

        # Sparse numbers
        ([4, 5, 6], 15),

        # Mixed gaps
        ([1, 5, 10], 12),

        # Target exactly present
        ([3, 4, 5], 5),

        # Larger nums array
        ([1, 2, 3, 4, 5], 8),
    ]

    expected_answers = [
        7,   # ([1,2,3], 4)
        0,   # ([9], 3)

        1,   # ([1], 1)
        1,   # ([1], 5)
        0,   # ([2], 1)
        1,   # ([2], 2)

        3,   # ([1,2], 3)
        6,   # ([2,3,5], 8)
        15,  # ([4,2,1], 5)

        5,   # ([1,2], 4)
        7,   # ([3,1,2], 4)

        0,   # ([5,10], 1)
        1,   # ([7], 14)

        274, # ([1,2,3], 10)

        4,   # ([4,5,6], 15)

        3,   # ([1,5,10], 12)

        1,   # ([3,4,5], 5)

        120, # ([1,2,3,4,5], 8)
    ]

    for i, ((nums, target), expected) in enumerate(zip(test_cases, expected_answers), 1):
        result = solution.combinationSum4(nums, target)

        print(f"Test Case {i}")
        print(f"nums = {nums}")
        print(f"target = {target}")
        print(f"Expected = {expected}")
        print(f"Your Output = {result}")
        print(f"Pass = {result == expected}")
        print("-" * 50)