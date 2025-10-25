'''
####################################################################################################
############################################ 3 pointer #############################################
####################################################################################################

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

####################################################################################################
####################################################################################################

Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(n)              (for HashMap)

'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(n) -> int:
            freq = {}
            left = 0
            res = 0
            for right, num in enumerate(nums):
                freq[num] = 1 + freq.get(num, 0)

                # distinct character if greater than n then start shifting left
                while len(freq) > n:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                # all subarrays ending at right and starting between left…right are valid
                # Example => [1] || L,R = 0 || res = 1
                # Example => [1,2] || L = 0, R = 1 || res += 1-0+1 => 1(prev) + 2(curr)
                res += right - left + 1
            return res

        # exactly  K  distinct = at  most  K  distinct − at  most  (K-1)  distinct
        return atMost(k) - atMost(k - 1)
    
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