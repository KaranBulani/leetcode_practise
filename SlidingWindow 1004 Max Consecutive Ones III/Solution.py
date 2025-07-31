'''
Time Complexity:  O(2n)              (for L, R)
Space Complexity: O(1)              (for Variables, indexes)
'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L = 0
        countOf0 = 0
        maxLen = 0
        for R in range(len(nums)):
            # countOf0 increment/decrement
            if nums[R] == 0: countOf0 += 1
            while countOf0 > k:
                if nums[L] == 0:
                    countOf0 -= 1
                L += 1
            # recalculate max
            maxLen = max(maxLen, R-L+1)
        return maxLen

if __name__ == "__main__":
    solution = Solution()

    # (nums, k, expected)
    test_cases = [
        # From prompt examples
        ([1,1,1,0,0,0,1,1,1,1,0], 2, 6),  # flip two zeros in the middle
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10),

        # Edge cases
        ([], 0, 0),                        # empty array
        ([0, 0, 0, 0], 0, 0),             # no flips allowed, all zeros
        ([0, 0, 0, 0], 2, 2),             # flip two zeros
        ([1, 1, 1, 1], 2, 4),             # all ones, flips don’t matter
        ([1, 0, 1, 0, 1], 0, 1),          # no flips, alternating
        ([1, 0, 1, 0, 1], 1, 3),          # one flip
        ([1, 0, 1, 0, 1], 2, 4),          # two flips
        ([0], 0, 0),                      # single zero, no flip
        ([0], 1, 1),                      # single zero, one flip
        ([1], 0, 1),                      # single one
        ([1, 1, 0, 1, 1, 0, 1], 1, 5),    # flip the best zero
        ([1, 0, 0, 1, 1, 0, 1, 0, 1], 3, 6),
    ]

    for nums, k, expected in test_cases:
        result = solution.longestOnes(nums, k)
        print(f"nums={nums}, k={k} -> {result}  (expected: {expected})")