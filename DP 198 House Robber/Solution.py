'''
####################################################################################################
####################################################################################################
1. Observation
✅ In your own words
    At every house, you have two choices:
    * Rob it → cannot rob next house
    * Skip it → move to next house
    Goal: maximize total money

✅ Key constraints
    * Cannot pick adjacent elements
    * Need maximum sum
    * n ≤ 100 → DP is perfect

✅ Core Insight     👉 This is a decision problem at each index
####################################################################################################
                                            returning dp[0]
####################################################################################################
2. Simulation

        Take: nums = [2,7,9,3,1]

        At index i, you decide:
        | Index | Choice                   | Result |
        | ----- | ------------------------ | ------ |
        | 0     | rob → 2 + solve(index 2) |        |
        |       | skip → solve(index 1)    |        |

        🔁 Pattern emerges:
        At every index:                 max(    rob current + skip next,    skip current )

3. Recursion

        ✅ Define function
        f(i) = max money we can rob starting from index i

        ✅ Recurrence relation
        f(i) = max(
            nums[i] + f(i+2),   # rob
            f(i+1)              # skip
        )

        ✅ Base case
        f(i) = 0  if i >= n

                                            Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(
                nums[i] + dfs(i+2),
                dfs(i+1)
            )
            return memo[i]

        return dfs(0)

                                            Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])

        return dp[0]

                                            Optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 # dp[i+2]
        prev1 = 0 # dp[i+1]

        for num in reversed(nums):
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1

####################################################################################################
                                            returning dp[n]
####################################################################################################
Let’s redefine:     dp[i] = max money we can rob from first i houses

👉 So:
    dp[0] = 0 → no house
    dp[1] = nums[0]
👉 Final answer = dp[n]

🔁 Transition
At house i (1-based):
dp[i] = max(
    dp[i-1],                # skip current
    nums[i-1] + dp[i-2]     # rob current
)

                                            Memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if i <= 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(
                nums[i-1] + dfs(i-2),
                dfs(i-1)
            )
            return memo[i]

        return dfs(len(nums))

                                            Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2] )

        return dp[n]

                                            Optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 # dp[i - 2]
        prev1 = 0 # dp[i - 1]
        n = len(nums)

        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1
####################################################################################################
✅ Why recursion works
* Same problem repeats → overlapping subproblems
* Optimal substructure present

| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Recursion   | O(2ⁿ) | O(n)  |
| Memoization | O(n)  | O(n)  |
| Tabulation  | O(n)  | O(n)  |
| Optimized   | O(n)  | O(1)  |
'''
class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0  # dp[i - 2]
        prev1 = 0  # dp[i - 1]

        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr

        return prev1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from problem
        [1, 2, 3, 1],
        [2, 7, 9, 3, 1],

        # Edge cases
        [0],  # Single house, zero money
        [5],  # Single house, positive money
        [0, 0, 0, 0],  # All zeros
        [1, 1, 1, 1],  # All same values

        # Small variations
        [2, 1],  # Two houses, pick max
        [1, 2],  # Increasing order
        [2, 1, 1, 2],  # Classic tricky case

        # Larger patterns
        [10, 1, 1, 10],  # Pick non-adjacent high values
        [5, 5, 10, 100, 10, 5],  # Greedy trap case
        [4, 1, 2, 7, 5, 3, 1],  # Mixed values

        # Alternating high-low
        [100, 1, 100, 1, 100],

        # Increasing sequence
        [1, 2, 3, 4, 5, 6, 7],

        # Decreasing sequence
        [7, 6, 5, 4, 3, 2, 1],

        # Larger input
        [2, 3, 2, 3, 5, 1, 1, 3, 10, 2]
    ]

    for i, nums in enumerate(test_cases):
        result = solution.rob(nums)
        print(f"Test Case {i + 1}: nums = {nums}")
        print(f"Output: {result}")
        print("-" * 40)