'''
####################################################################################################
######################################## Kadane's Algorithm ########################################
####################################################################################################
Time complexity:  O(n)				Traversing through arr
Space complexity: O(1)				As only variables.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

####################################################################################################
######################################## Divide And Conquer ########################################
####################################################################################################

⚙️ Algorithm
1. Base case:
   If `left == right`, return `nums[left]`.
2. Divide:
   Compute `mid = (left + right) // 2`.
3. Conquer:
   * Recursively find the max subarray in the left half.
   * Recursively find the max subarray in the right half.
4. Combine:
   * Compute max crossing sum — subarray that crosses the midpoint:
     * max sum from `mid` to left
     * max sum from `mid + 1` to right
     * total = left_sum + right_sum
5. Return the maximum of:
   * left subarray sum
   * right subarray sum
   * crossing subarray sum

Time complexity:  O(nlogn)				Each level splits array in half (log n levels) and combines in O(n).
Space complexity: O(logn)				recursion stack.
'''


class Solution:
    def maxSubArray(self, nums):
        def helper(nums, left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2

            # Maximum subarray sum on left and right halves
            left_max = helper(nums, left, mid)
            right_max = helper(nums, mid + 1, right)

            # Find max sum crossing the midpoint
            left_sum = float('-inf')
            curr = 0
            for i in range(mid, left - 1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)

            right_sum = float('-inf')
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                right_sum = max(right_sum, curr)

            cross_sum = left_sum + right_sum

            return max(left_max, right_max, cross_sum)

        return helper(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    solution = Solution()

    # Example 1: Standard mixed case
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 6

    # Example 2: Single element
    nums = [1]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 1

    # Example 3: All positive numbers
    nums = [5, 4, -1, 7, 8]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 23

    # Edge Case 1: All negative numbers
    nums = [-3, -5, -2, -11, -4]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: -2

    # Edge Case 2: Large number of small values
    nums = [0, 0, 0, 0, 0]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 0

    # Edge Case 3: Single negative element
    nums = [-1]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: -1

    # Edge Case 4: Increasing sequence
    nums = [1, 2, 3, 4, 5]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 15

    # Edge Case 5: Decreasing sequence
    nums = [5, 4, 3, 2, 1, -10]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 15

    # Edge Case 6: Zeros and negatives mixed
    nums = [0, -1, 0, -2, 0]
    result = solution.maxSubArray(nums)
    print(result)  # Expected output: 0