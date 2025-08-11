'''
Time Complexity:  O(logn)              (for Binar Search)
Space Complexity: O(1)                 (for Variables, indexes)
'''

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        cur_min = float("inf")
        while L <= R:

            # If the current range is already sorted (no rotation in between L and R)
            # then nums[L] is the smallest in this range
            if nums[L] <= nums[R]:
                cur_min = min(cur_min, nums[L])
                break  # No need to search further

            # Update the current minimum with the middle element
            mid = (R + L) // 2
            cur_min = min(cur_min, nums[mid])

            # If the left half is sorted, then the minimum must be in the right half
            if nums[L] <= nums[mid]:
                L = mid + 1
            # Otherwise, the right half is sorted, so the minimum is in the left half
            else:
                R = mid - 1
        return cur_min

if __name__ == "__main__":
    solution = Solution()

    # Test cases from the question
    test_cases = [
        # (input, expected_output)
        ([3, 4, 5, 1, 2], 1),            # Rotated mid-way
        ([4, 5, 6, 7, 0, 1, 2], 0),      # Rotated near end
        ([11, 13, 15, 17], 11),          # No rotation

        # Additional edge cases
        ([1], 1),                        # Single element
        ([2, 1], 1),                      # Two elements, rotated once
        ([1, 2], 1),                      # Two elements, no rotation
        ([5, 6, 7, 8, 9, 1, 2, 3, 4], 1),# Large rotation break in middle
        ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1),# Rotation at last element
        ([1000, -5000, -4000, -3000], -5000), # Includes negative numbers
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findMin(nums)
        print(f"Test case {i}: Input={nums} | Expected={expected} | Got={result}")