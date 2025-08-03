'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3

Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9
'''
import collections
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        cur_sum, q = 0, collections.deque() #(prefix_sum, end_idx)

        for R in range(len(nums)):
            cur_sum += nums[R]
            if cur_sum >= k:
                res = min(res, R + 1) #Sum from start to Rth index

            # Try to compress left if current is greater than k and recalculate min
            while q and cur_sum - q[0][0] >= k:
                prefix_sum, end_idx = q.popleft()
                res = min(res, R - end_idx)

            # Validate the monotonic queue
            while q and q[-1][0] > cur_sum:
                q.pop()
            q.append((cur_sum, R))

        return -1 if res == float("inf") else res

if __name__ == "__main__":
    solution = Solution()

    # Basic Examples
    print(solution.shortestSubarray([1], 1))            # Expected: 1
    print(solution.shortestSubarray([1, 2], 4))         # Expected: -1
    print(solution.shortestSubarray([2, -1, 2], 3))     # Expected: 3

    # Edge Case: No subarray meets requirement
    print(solution.shortestSubarray([-1, -1, -1], 1))   # Expected: -1

    # Edge Case: Multiple negatives and positives
    print(solution.shortestSubarray([84, -37, 32, 40, 95], 167))  # Expected: 3

    # Minimum subarray is in the middle
    print(solution.shortestSubarray([1, 2, 3, 4, 5], 9)) # Expected: 2

    # Large k, must take whole array
    print(solution.shortestSubarray([1]*100000, 100000))  # Expected: 100000

    # Negative numbers in the beginning
    print(solution.shortestSubarray([-100, 1, 2, 3, 4, 5, 100], 105))  # Expected: 2

    # Large negative followed by large positive
    print(solution.shortestSubarray([-10000, 10000], 1))  # Expected: 2

    # Subarray at the end
    print(solution.shortestSubarray([0, 0, 0, 5, 6], 10))  # Expected: 2