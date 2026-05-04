'''
1. Observation
Problem in my own words
We need to split the array into two subsets with equal sum.

Key observations
* Let total sum = S
* We need two subsets with equal sum ⇒ each subset must sum to S/2
* ❗ If S is odd → impossible
* Problem reduces to:
  > Can we find a subset with sum = S/2 ?

Constraints insight
* n ≤ 200, nums[i] ≤ 100
* Max sum = 200 × 100 = 20000 → feasible for DP

Core idea
👉 This becomes a Subset Sum problem

####################################################################################################
2. Simulation
Example:
nums = [1,5,11,5]
S = 22 → target = 11
We try building sum = 11:
* Start with {} → sum = 0
* Add 1 → 1
* Add 5 → 6
* Add another 5 → 11 ✅
So subset exists ⇒ return True

####################################################################################################
3. Recursion
Define:
canMake(i, target)

Meaning:
> Can we make target using elements from index i → end

Choices:
* Take nums[i]
* Skip nums[i]

Recurrence:
canMake(i, target) =
    canMake(i+1, target - nums[i]) OR
    canMake(i+1, target)

Base cases:
* target == 0 → True
* i == n or target < 0 → False

####################################################################################################
                                        BOTTOM UP - DP
####################################################################################################
4. Dynamic Programming

State
dp[s] = True → subset exists with sum s

Initialization
dp[0] = True

Transition
For each num:
for s from target → num:
    dp[s] = dp[s] OR dp[s - num]

⚠️ Iterate backwards to avoid reuse in same iteration
👉 If we iterate forward, we might reuse the same number multiple times in the same iteration (like Coin Change).
👉 By going backward, we ensure each number is used only once → proper 0/1 choice.

✅ Final Code (Optimized 1D DP)
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If sum is odd → impossible
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # when num - 1 > target below for loop automatically doesnt run because of step,
            # So no index out of bound exception
            for curr_sum in range(target, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[target]

⏱ Complexity
* Time: O(n * target)
* Space: O(target)

🔑 Key Takeaways
* Always check sum parity first
* Convert partition → subset sum
* Backward iteration is critical
* This is a classic 0/1 Knapsack pattern

####################################################################################################
                                            TOP DOWN - DP
####################################################################################################
4. Dynamic Programming (Top-Down / Memoization)

State
(i, remaining)

Memoization
* Cache results to avoid recomputation

Complexity
* States = n * target
* Each state computed once

✅ Final Code (Top-Down DP)
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def canMake(i, remaining):
            # Base cases
            if remaining == 0:
                return True
            if i == len(nums) or remaining < 0:
                return False

            # Check memo
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Choices
            take = canMake(i + 1, remaining - nums[i])
            skip = canMake(i + 1, remaining)

            memo[(i, remaining)] = take or skip
            return memo[(i, remaining)]

        return canMake(0, target)

⏱ Complexity
* Time: O(n * target)
* Space:
  * Recursion stack: O(n)
  * Memo: O(n * target)

🔑 Key Insights
* This is classic subset sum via recursion + memo
* State = (index, remaining)
* Memo avoids exponential explosion
* Equivalent to bottom-up DP but easier to reason initially

'''
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If sum is odd → impossible
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # when num - 1 > target below for loop automatically doesnt run because of step,
            # So no index out of bound exception
            for curr_sum in range(target, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[target]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([7, 1, 2], "Example 0"),
        ([1, 5, 11, 5], "Example 1"),
        ([1, 2, 3, 5], "Example 2"),

        # Edge cases
        ([1], "Single element"),
        ([2, 2], "Two equal elements"),
        ([1, 1], "Two ones"),
        ([100, 100], "Max equal values"),

        # Odd total sum (should fail)
        ([1, 2, 3], "Odd sum small"),
        ([2, 3, 5], "Odd sum medium"),

        # Larger cases
        ([1, 2, 5, 6, 7, 10], "Medium size"),
        ([3, 3, 3, 4, 5], "Tricky subset"),

        # All same elements
        ([4, 4, 4, 4], "All equal"),
        ([7, 7, 7], "All equal odd count"),

        # Large input edge
        ([1]*200, "Max size all ones"),

        # Mixed tricky
        ([2, 2, 3, 5], "Subset not obvious"),
        ([1, 2, 3, 4, 5, 6, 7], "Increasing sequence"),
    ]

    for nums, label in test_cases:
        result = solution.canPartition(nums)
        print(f"{label} | Input: {nums}")
        print(f"Output: {result}")
        print("-" * 50)