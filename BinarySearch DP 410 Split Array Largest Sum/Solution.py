'''
####################################################################################################
########################################### DP SOLUTION ############################################
####################################################################################################

Time Complexity:

1. States in DP
   * Our DP/memoization table is keyed by (i, m) where:
     * i ranges from 0 to n-1 → n possible values
     * m ranges from 1 to given m → m possible values
   * So, there are O(n × m) unique states.
2. Work per State
   * For each state (i, m), we loop j from i to len(nums) - m + 1.
     In the worst case, this is O(n) work.
   * Therefore, total work = O(n × m × n) = O(n² × m).
🔹 Final Time Complexity: O(n² × m) Where n = len(nums).

Space Complexity:

1. DP Memo Table: Stores at most n × m entries → O(n × m) space.
2. Recursion Call Stack: The depth of recursion is at most m (since m decreases with each split).
🔹 Final Space Complexity: O(n × m) (DP dominates over recursion stack).

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Memoization dictionary to store results for (i, k) states
        dp = {}

        def dfs(i, m):
            """
            Recursive function to determine the minimal largest sum
            by splitting nums[i:] into m subarrays.
            """
            # Base case: If only one subarray left, take the sum of remaining elements
            if m == 1:
                return sum(nums[i:])

            # If we have already computed this state, return cached result
            if (i, m) in dp:
                return dp[(i, m)]

            # Initialize result to infinity (we want the minimum)
            res = float("inf")
            # Current running sum for the first subarray
            curSum = 0

            # Iterate over possible split points
            # We stop at len(nums) - m + 1 because we must leave enough numbers for remaining subarrays
            for j in range(i, len(nums) - m + 1):
                curSum += nums[j]  # Add current number to the running sum

                # Max sum in the current split: the max of current subarray sum and the best possible sum of remaining splits
                maxSum = max(curSum, dfs(j + 1, m - 1))

                # Update result to be the minimum of previous result and current split's max sum
                res = min(res, maxSum)

                # Optimization: If current sum already exceeds best result found, stop exploring further splits
                if curSum > res:
                    break

            # Store computed result in dp for memoization
            dp[(i, m)] = res
            return res

        # Start recursion from index 0 with m subarrays
        return dfs(0, k)

####################################################################################################
########################################### BS SOLUTION ############################################
####################################################################################################

Time Complexity:

* Binary Search Range: max(nums) → sum(nums)
  That’s at most O(log(sum(nums) - max(nums))) iterations.

* Each def can_split check: O(n) (looping through nums once).

* Total Time Complexity:
  O(n * log(sum(nums)))

Space Complexity: O(1)                  (for Variables, indexes)

'''

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Function to split array into k parts so that the largest sum is minimized.
        Uses binary search over possible max subarray sums.
        """

        # Helper function: Can we split into <= k subarrays with each sum <= max_sum?
        def can_split(max_sum):
            curr_sum = 0
            subarrays_needed = 1  # At least one subarray to start
            for num in nums:
                if curr_sum + num > max_sum:
                    # Start a new subarray if in previous iteration adding num exceeded max_sum, reset curr_sum to current num
                    subarrays_needed += 1
                    curr_sum = num
                    if subarrays_needed > k:  # Too many subarrays, fail
                        return False
                else:
                    curr_sum += num
            return True

        # Binary search boundaries:
        # Minimum possible largest sum = max(nums) (can't be smaller than the biggest element "As we are trying to minimize max" )
        # Maximum possible largest sum = sum(nums) (whole array as one subarray, minus any one k values, but let's consider whole)
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                # If possible, try smaller maximum sum
                res = mid
                right = mid - 1
            else:
                # If not possible, increase allowed maximum sum
                left = mid + 1

        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1 from question
    nums = [7, 2, 5, 10, 8]
    k = 2
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 18

    # Example 2 from question
    nums = [1, 2, 3, 4, 5]
    k = 2
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 9

    # Edge case: Single element array, k = 1
    nums = [10]
    k = 1
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 10

    # Edge case: All elements are 0
    nums = [0, 0, 0, 0]
    k = 2
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 0

    # Edge case: k equals length of array (each element is its own subarray)
    nums = [3, 1, 4, 2]
    k = 4
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 4

    # Larger numbers to test upper limits
    nums = [10**6, 10**6, 10**6]
    k = 2
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 2000000

    # Complex case: mixed small and large numbers
    nums = [1, 4, 4, 7, 2, 9, 5]
    k = 3
    result = solution.splitArray(nums, k)
    print(result)  # Expected: 11
