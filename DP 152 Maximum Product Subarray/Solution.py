'''
1. Observation

🔹 Reduce problem
We need to find a contiguous subarray whose product is maximum.

🔹 Key observations
1. Product behaves differently than sum:
   * Negative × Negative = Positive
   * So a small (negative) value can become large positive later
2. At every index, the answer depends on:
   * Previous maximum product
   * Previous minimum product (important due to negatives)
3. Zero acts as a reset point
   * Any subarray crossing 0 becomes 0

🔹 Core Insight
At each index i, we must track:
* maxProd[i] → maximum product ending at i
* minProd[i] → minimum product ending at i

Because:
> minimum can become maximum when multiplied by negative


####################################################################################################
                                            TOP DOWN - DP
####################################################################################################
2. Simulation Insight → Structure

At index i, result depends on:
* previous max product
* previous min product
👉 So state must return both values
👉 This problem is sequential dependency DP, Each state depends only on i-1
####################################################################################################
3. Recursion
🔹 Define function
f(i) → returns (maxProd ending at i, minProd ending at i)

🔹 Base Case
f(0) = (nums[0], nums[0])

🔹 Recurrence
From previous state:
prevMax, prevMin = f(i-1)

currMax = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
currMin = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)

🔹 Important
* Function returns a pair
* We track global answer separately
####################################################################################################
4. Dynamic Programming (Top-Down / Memoization)

🔹 Memo
memo[i] = (maxProd, minProd)

🔹 Code
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        memo = {}
        res = nums[0]

        def dfs(i):
            nonlocal res

            if i in memo:
                return memo[i]

            if i == 0:
                memo[i] = (nums[0], nums[0])
                return memo[i]

            prevMax, prevMin = dfs(i - 1)

            curr = nums[i]

            currMax = max(curr, curr * prevMax, curr * prevMin)
            currMin = min(curr, curr * prevMax, curr * prevMin)
            res = max(res, currMax)

            memo[i] = (currMax, currMin)
            return memo[i]

        dfs(len(nums) - 1)
        return res
####################################################################################################
5. Complexity
* Time: O(n) (each state computed once)
* Space: O(n) (recursion + memo)

####################################################################################################
                                        BOTTOM UP - DP
####################################################################################################
2. Simulation

Take:
nums = [2, 3, -2, 4]

| i | num | maxProd | minProd | explanation          |
| - | --- | ------- | ------- | -------------------- |
| 0 | 2   | 2       | 2       | start                |
| 1 | 3   | 6       | 3       | extend               |
| 2 | -2  | -2      | -12     | flip due to negative |
| 3 | 4   | 4       | -48     | restart from 4       |

👉 Answer = 6

🔹 Generalization

At index i:
We have 3 choices:
1. Start fresh → nums[i]
2. Extend previous max → nums[i] * prevMax
3. Extend previous min → nums[i] * prevMin
####################################################################################################
3. Dynamic Programming

🔹 State Definition
maxProd[i] = maximum product subarray ending at i
minProd[i] = minimum product subarray ending at i

🔹 Transition
maxProd[i] = max( nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1] )
minProd[i] = min( nums[i], nums[i] * maxProd[i-1], nums[i] * minProd[i-1] )

🔹 Base Case
maxProd[0] = nums[0]
minProd[0] = nums[0]

🔹 Answer - max over all maxProd[i]

🔹 Optimization
We don’t need full arrays → just track previous values.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        res = nums[0]
        for num in nums[1:]:
            currMax = max(num, num * prevMax, num * prevMin)
            currMin = min(num, num * prevMax, num * prevMin)

            res = max(res, currMax)
            prevMax = currMax
            prevMin = currMin

        return res
####################################################################################################
🔹 Time & Space Complexity
* Time: O(n)
* Space: O(1)
'''

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        prevMax = nums[0]
        prevMin = nums[0]
        res = nums[0]
        for num in nums[1:]:
            currMax = max(num, num * prevMax, num * prevMin)
            currMin = min(num, num * prevMax, num * prevMin)

            res = max(res, currMax)
            prevMax = currMax
            prevMin = currMin

        return res

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples
        [2, 3, -2, 4],
        [-2, 0, -1],

        # Single element
        [5],
        [-5],
        [0],

        # All positives
        [1, 2, 3, 4],

        # All negatives (even count)
        [-1, -2, -3, -4],

        # All negatives (odd count)
        [-1, -2, -3],

        # Contains zeros splitting subarrays
        [0, 2],
        [2, 0, 3, -2, 4],
        [-2, 0, -1, 0, 3, -4],

        # Mixed tricky cases
        [2, -5, -2, -4, 3],
        [-2, 3, -4],
        [3, -1, 4],
        [-2, -3, 7],

        # Edge: multiple zeros
        [0, 0, 0],

        # Edge: alternating signs
        [1, -2, 3, -4, 5, -6],

        # Edge: large length pattern
        [1, -2, -3, 4, -1, 2, 1, -5, 4],

        # Edge: product resets frequently
        [-1, 0, -2, 0, -3, 0, -4],

        # Edge: max product at end
        [-2, -3, 0, -2, -40],

        # Edge: max product at start
        [6, -3, -10, 0, 2],

        # Edge: contains 1 and -1 heavily
        [1, -1, 1, -1, 1, -1, 1],
    ]

    for i, nums in enumerate(test_cases):
        result = solution.maxProduct(nums)
        print(f"Test Case {i+1}: nums = {nums}")
        print(f"Output: {result}")
        print("-" * 50)