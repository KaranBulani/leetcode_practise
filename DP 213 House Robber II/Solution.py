'''
🔹 1. Observation
    Problem in simple words
    * Houses are in a circle (first and last are adjacent).
    * Cannot rob adjacent houses.
    * Maximize total money.

    Key difference from House Robber I
    * In House Robber I → linear
    * Here → circular constraint

    👉 This creates a conflict:
    * If you rob house 0, you cannot rob last house
    * If you rob last house, you cannot rob house 0

    Core Insight ⭐
    Convert circular → two linear problems:
    1. Rob houses [0 → n-2] (exclude last)
    2. Rob houses [1 → n-1] (exclude first)
    👉 Answer = max(case1, case2)

🔹 2. Simulation
    Example: [2,3,2]
        Case 1: [2,3]
        * max = 3

        Case 2: [3,2]
        * max = 3
        👉 Answer = 3

    Example: [1,2,3,1]
        Case 1: [1,2,3]
        * max = 4

        Case 2: [2,3,1]
        * max = 3
        👉 Answer = 4

    Pattern emerging:
    * Each case becomes classic House Robber I

🔹 3. Recursion (Recurrence)
    For linear robber:
    f(i) = maximum money we can rob from houses [0 … i]
    f(i) = max(
        nums[i] + f(i-2),   rob
        f(i-1)              skip
    )

    Base cases:
    f(0) = nums[0]
    f(1) = max(nums[0], nums[1])
####################################################################################################
🔸 Top-Down (Memoization)

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            memo = {}

            def dfs(i):
                if i < 0:
                    return 0
                if i in memo:
                    return memo[i]

                memo[i] = max(
                    arr[i] + dfs(i-2),
                    dfs(i-1)
                )
                return memo[i]

            return dfs(len(arr) - 1)

        return max(
            rob_linear(nums[:-1]),  # exclude last
            rob_linear(nums[1:])    # exclude first
        )
####################################################################################################
🔸 Bottom-Up

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(
                    arr[i] + dp[i-2],
                    dp[i-1]
                )
            return dp[-1]

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )
####################################################################################################
🔸 Space Optimized ⭐

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev2 = 0   # dp[i-2]
            prev1 = 0   # dp[i-1]

            for num in arr:
                curr = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return prev1

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )
####################################################################################################
| Approach        | Time | Space |
| --------------- | ---- | ----- |
| Top-Down (Memo) | O(n) | O(n)  |
| Bottom-Up (DP)  | O(n) | O(n)  |
| Space Optimized | O(n) | O(1)  |
'''
class Solution:
    def rob(self, nums: list[int]) -> int:


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples (given)
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),

        # Edge cases
        ([1], 1),  # single house
        ([0], 0),  # single house with 0
        ([1, 2], 2),  # two houses

        # Small variations
        ([2, 1, 1, 2], 3),  # circular constraint matters
        ([1, 3, 1, 3, 100], 103),  # skip adjacency smartly

        # All same values
        ([5, 5, 5, 5], 10),

        # Increasing sequence
        ([1, 2, 3, 4, 5, 6], 12),

        # Decreasing sequence
        ([6, 5, 4, 3, 2, 1], 12),

        # Larger random
        ([200, 3, 140, 20, 10], 340),

        # Zero-heavy
        ([0, 0, 0, 0], 0),

        # Alternating high-low
        ([10, 1, 10, 1, 10], 20),

        # Tricky circular conflict
        ([100, 1, 1, 100], 101),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = solution.rob(nums)
        print(f"Test Case {i + 1}: nums = {nums}")
        print(f"Expected = {expected}, Got = {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 50)