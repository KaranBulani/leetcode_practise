'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
'''
from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int) # Frequency map for current window
        res = 0
        l_far = 0 # Left Boundary for "farthest valid window"
        l_near = 0 # Left Boundary for "nearest Valid window"

        # Expand
        for r in range(len(nums)):
            count[nums[r]] += 1 # Add current number

            # If we have more than k distinct, shrink from the left
            while len(count) > k:
                count[nums[l_near]] -= 1
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])  # Remove key if frequency is zero
                l_near += 1
                l_far = l_near  # Both pointers reset when count > k

            # Shrink from left (l_near) until the first element's freq > 1
            # This finds the smallest window that still has exactly k distinct numbers
            while count[nums[l_near]] > 1:
                count[nums[l_near]] -= 1
                l_near += 1

            # If we have exactly k distinct numbers, count valid subarrays
            if len(count) == k:
                # All subarrays starting from l_far (max valid len) to l_near(min valid len) are valid
                res += l_near - l_far + 1

        return res

if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    test_cases = [
        # Format: (nums, k, expected_output)
        ([1, 2, 1, 2, 3], 2, 7),  # Example 1 from prompt
        ([1, 2, 1, 3, 4], 3, 3),  # Example 2 from prompt

        # Edge cases
        ([1], 1, 1),  # Single element array, k=1
        ([1], 2, 0),  # Single element array, k>len(array)
        ([1, 1, 1, 1], 1, 10),  # All identical numbers, k=1 (all subarrays valid)
        ([1, 1, 1, 1], 2, 0),  # All identical numbers, k>1 (no valid subarray)

        # Diverse patterns
        ([1, 2, 3, 4], 4, 1),  # k = length of array → only the whole array
        ([1, 2, 3, 4], 3, 2),  # Only subarrays with exactly 3 distinct integers
        ([1, 2, 1, 3, 2], 2, 7),  # Multiple repeating values with k=2
        ([1, 2, 1, 3, 2], 3, 3),  # Multiple repeating values with k=3

        # Larger repeated pattern
        ([1, 2, 3, 1, 2, 3, 4], 3, 10),
    ]

    for nums, k, expected in test_cases:
        result = solution.subarraysWithKDistinct(nums, k)
        print(f"nums={nums}, k={k} => got {result}, expected {expected}")