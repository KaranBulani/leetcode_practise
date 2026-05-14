'''
1. Observation

Read the problem statement

We need to place either + or - before every number such that the final expression evaluates to target.
We must return the number of possible expressions.

Example:
nums = [1,1,1], target = 1
Possible:
+1 +1 -1 = 1
+1 -1 +1 = 1
-1 +1 +1 = 1
Answer = 3

Identify key observations

At every index:
* We have exactly 2 choices
  * Add current number
  * Subtract current number
So each decision changes the remaining target.

Important Observation
Instead of building the expression forward, we can think:
> "How many ways can we reach the remaining target from index i onward?"

This naturally forms recursion.

Constraints
nums.length <= 20
sum(nums) <= 1000

Brute force: 2^n
is possible but inefficient due to repeated states.

Repeated states suggest: Dynamic Programming
####################################################################################################

2. Simulation

Take:	nums = [1,1,1],	target = 1

Start at index 0.

Choice 1 → Use +1
	Remaining target:	1 - 1 = 0
	Now solve:			dfs(1, 0)

Choice 2 → Use -1
	Remaining target:	1 + 1 = 2
	Now solve:			dfs(1, 2)

So:
dfs(i, target)	=
	ways after adding nums[i]
			+
	ways after subtracting nums[i]

Repeated states
	Different paths can reach same state:	(index, remaining_target)
So we cache them.
####################################################################################################

3. Recursion

Define:	dfs(i, remaining_target)

Meaning:
> Number of ways to form remaining_target
> using elements from index i onward.

Base Case

	If all numbers are used:

	if i == len(nums):

	Then:
	* If remaining target became 0
	  → found valid expression
	* Else invalid

	So:
	if remaining_target == 0:
		return 1
	return 0

Recurrence Relation

	At every index:

	Option 1 → Put +
	dfs(i + 1, remaining_target - nums[i])

	Option 2 → Put -
	dfs(i + 1, remaining_target + nums[i])

	Total ways:
	dfs(i, target) =
		dfs(i + 1, target - nums[i])
		+
		dfs(i + 1, target + nums[i])
####################################################################################################

4. Dynamic Programming

Why DP works
State is fully determined by: (index, remaining_target)
Same state always gives same answer. So memoization avoids recomputation.

####################################################################################################
                                            Top-Down DP
####################################################################################################

Time Complexity - O(n * totalSum)
Space Complexity - O(n * totalSum)

n - number of elements in nums
totalSum - number we are trying to reach

For each n elements in nums, we can have any value till totalSum
So for nums[1] we can have nums[1] * totalSum
   for nums[2] we can have nums[2] * totalSum
   ...
   for n nums we can have total states as O(n * totalSum)

So total states become space complexity, and total state with per state work done becomes time complexity.


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i: int, remaining_target: int) -> int:
            if i == len(nums):
                if remaining_target == 0:
                    return 1
                return 0

            if (i, remaining_target) in memo:
                return memo[(i, remaining_target)]

            add = dfs(i + 1, remaining_target - nums[i])
            subtract = dfs(i + 1, remaining_target + nums[i])

            memo[(i, remaining_target)] = add + subtract

            return memo[(i, remaining_target)]

        return dfs(0, target)

####################################################################################################
                                            BOTTOM-UP DP
####################################################################################################
DP Meaning
dp[s] = Number of ways to create sum s
Since sums can be negative, we use hashmap.

Transition
    For every number:
        From every existing sum:
        * Add current number
        * Subtract current number

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)

            for curr_sum, ways in dp.items():
                next_dp[curr_sum + num] += ways
                next_dp[curr_sum - num] += ways

            dp = next_dp

        return dp[target]

####################################################################################################
                                            BRUTE FORCE
####################################################################################################

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        def dfs(i: int, curr_target: int) -> None:
            nonlocal res
            if i == len(nums) and curr_target == 0:
                res += 1
                return

            if i >= len(nums):
                return

            dfs(i+1, curr_target - nums[i])
            dfs(i+1, curr_target + nums[i])
            return

        dfs(0, target)
        return res

####################################################################################################
For every index, you make 2 recursive calls:
* one with curr_target - nums[i]
* one with curr_target + nums[i]

########################################## Time Complexity ##########################################

At each element, there are 2 choices:
* +nums[i]
* -nums[i]

So the recursion tree becomes:
* Level 0 → 1 node
* Level 1 → 2 nodes
* Level 2 → 4 nodes
* Level 3 → 8 nodes
* ...
* Level n → 2^n nodes
Total recursive calls:	1 + 2 + 4 + 8 + ... + 2^n

This is a geometric series:	 2^(n+1) - 1
So:		O(2^n)

                    target
                 /          \
            target-1      target+1
             /    \         /    \
          ...    ...     ...    ...
Each level doubles.

######################################### Space Complexity #########################################

The maximum recursion depth is:		n

because:
dfs(i+1, ...)
moves one step forward each call.

So recursion stack stores at most n calls simultaneously.

Thus:	O(n)
'''

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)

            for curr_sum, ways in dp.items():
                next_dp[curr_sum + num] += ways
                next_dp[curr_sum - num] += ways

            dp = next_dp

        return dp[target]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # =========================
        # Examples from question
        # =========================
        {
            "nums": [1, 1, 1, 1, 1],
            "target": 3,
            "expected": 5
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 1
        },

        # =========================
        # Basic small cases
        # =========================
        {
            "nums": [1],
            "target": -1,
            "expected": 1
        },
        {
            "nums": [1],
            "target": 0,
            "expected": 0
        },
        {
            "nums": [1, 2],
            "target": 1,
            "expected": 1
        },
        {
            "nums": [1, 2, 3],
            "target": 0,
            "expected": 2
        },

        # =========================
        # Zero handling
        # =========================
        {
            "nums": [0],
            "target": 0,
            "expected": 2
        },
        {
            "nums": [0, 0],
            "target": 0,
            "expected": 4
        },
        {
            "nums": [0, 0, 0, 0, 0],
            "target": 0,
            "expected": 32
        },
        {
            "nums": [0, 0, 1],
            "target": 1,
            "expected": 4
        },

        # =========================
        # Impossible targets
        # =========================
        {
            "nums": [1, 2, 3],
            "target": 10,
            "expected": 0
        },
        {
            "nums": [2, 4, 6],
            "target": 5,
            "expected": 0
        },

        # =========================
        # Duplicate values
        # =========================
        {
            "nums": [1, 1, 1, 1],
            "target": 2,
            "expected": 4
        },
        {
            "nums": [2, 2, 2, 2],
            "target": 0,
            "expected": 6
        },

        # =========================
        # Negative target cases
        # =========================
        {
            "nums": [1, 2, 1],
            "target": -2,
            "expected": 2
        },
        {
            "nums": [3, 1, 2],
            "target": -6,
            "expected": 1
        },

        # =========================
        # Larger values
        # =========================
        {
            "nums": [100],
            "target": 100,
            "expected": 1
        },
        {
            "nums": [100, 100],
            "target": 0,
            "expected": 2
        },
        {
            "nums": [10, 20, 30, 40],
            "target": 0,
            "expected": 2
        },
    ]

    for i, test in enumerate(test_cases, 1):
        nums = test["nums"]
        target = test["target"]
        expected = test["expected"]

        result = solution.findTargetSumWays(nums, target)

        print(f"Test Case {i}")
        print(f"nums     = {nums}")
        print(f"target   = {target}")
        print(f"Expected = {expected}")
        print(f"Your Output = {result}")
        print(f"Passed = {result == expected}")
        print("-" * 50)