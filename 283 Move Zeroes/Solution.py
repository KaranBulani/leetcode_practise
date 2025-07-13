'''
Good explanation - https://youtu.be/PNJoyRaIW7U?si=wj72WL1oza6CN6KN

Time Complexity: O(n) (go through)
Space Complexity: O(1) for L, R
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        L, R = 0, 0
        while R < len(nums):
            # whenever we see a non-zero at R, swap it to the next L position
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            # always advance R
            R += 1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # From prompt
        [0, 1, 0, 3, 12],
        [0],
        # Extra edge cases
        [1, 2, 3],             # no zeroes
        [0, 0, 0],             # all zeroes
        [4, 0, 5, 0, 0, 6, 7], # multiple zero clusters
        [0, 1],                # zero at front
        [1, 0],                # zero at end
        [0, -1, 0, -2, 0],     # negatives and zeroes
        [1] * 100 + [0] * 100  # large tail of zeroes
    ]

    expected_outputs = [
        [1, 3, 12, 0, 0],
        [0],
        [1, 2, 3],
        [0, 0, 0],
        [4, 5, 6, 7, 0, 0, 0],
        [1, 0],
        [1, 0],
        [-1, -2, 0, 0, 0],
        [1] * 100 + [0] * 100
    ]

    for i, (nums, expected) in enumerate(zip(test_cases, expected_outputs), 1):
        nums_copy = nums.copy()
        solution.moveZeroes(nums_copy)
        print(f"Test #{i}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {nums_copy}")
        print(f"  Expected: {expected}")
