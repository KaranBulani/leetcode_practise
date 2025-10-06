'''
####################################################################################################
🧠 Intuition
There are two possible cases for the maximum sum subarray:

Case 1: The subarray does not wrap around.
* This is just the normal Kadane’s algorithm.
* Example: [5, -3, 5] → the subarray [5, -3, 5] (non-wrapping).

Case 2: The subarray wraps around.
* Think of it as taking the entire array sum minus the minimum subarray.
* Because if the *middle (minimum)* part is removed, the *outside* forms the wrapping subarray.
* Example: [5, -3, 5] → total sum = 7, min subarray = -3, so 7 - (-3) = 10.

So final answer = max(normal_kadane, total_sum - min_subarray_sum)

⚠️ Edge Case
If all numbers are negative,
then total_sum - min_subarray_sum = 0, which is invalid (empty subarray).
So we must return the result from normal Kadane in that case.

####################################################################################################
Time complexity:  O(n)				single pass
Space complexity: O(1)				constant space
####################################################################################################
'''
class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        cur_max = cur_min = 0
        max_sum = -float('inf')
        min_sum = float('inf')

        for num in nums:
            # Case 1: Kadane’s for max subarray
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)

            # Case 2: Kadane’s for min subarray
            cur_min = min(num, cur_min + num)
            min_sum = min(min_sum, cur_min)

            total_sum += num

        # If all numbers are negative, return the maximum single element
        if max_sum < 0:
            return max_sum

        # Otherwise, consider both cases
        return max(max_sum, total_sum - min_sum)

if __name__ == "__main__":
    solution = Solution()

    # Example cases
    print(solution.maxSubarraySumCircular([1, -2, 3, -2]))  # Example 1
    print(solution.maxSubarraySumCircular([5, -3, 5]))  # Example 2
    print(solution.maxSubarraySumCircular([-3, -2, -3]))  # Example 3

    # Additional diverse cases
    print(solution.maxSubarraySumCircular([3, -1, 2, -1]))  # mix of positives and negatives
    print(solution.maxSubarraySumCircular([3, -2, 2, -3]))  # balanced positives and negatives
    print(solution.maxSubarraySumCircular([10, -12, 11, -5, 6]))  # alternating highs/lows
    print(solution.maxSubarraySumCircular([8, -1, -3, 8, -6, 7]))  # multiple wraps possible
    print(solution.maxSubarraySumCircular([-5, -1, -2]))  # all negatives, different from example
    print(solution.maxSubarraySumCircular([5]))  # single-element array (positive)
    print(solution.maxSubarraySumCircular([-5]))  # single-element array (negative)
    print(solution.maxSubarraySumCircular([10000, -30000, 10000, 10000]))  # large magnitudes