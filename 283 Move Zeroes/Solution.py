'''
Good explanation - https://youtu.be/PNJoyRaIW7U?si=wj72WL1oza6CN6KN

Dry run on `[4, 0, 5, 0, 0, 6, 7]`:

1. Start: `L=0, R=0`, array = `[4, 0, 5, 0, 0, 6, 7]`
   * `nums[R]=4` is non-zero → swap with itself → `L=1, R=1`.

2. Step: `L=1, R=1`, array = `[4, 0, 5, 0, 0, 6, 7]`
   * `nums[R]=0` → do nothing → `L=1, R=2`.

3. Step: `L=1, R=2`, array = `[4, 0, 5, 0, 0, 6, 7]`
   * `nums[R]=5` → swap with `nums[L]` → `[4, 5, 0, 0, 0, 6, 7]` → `L=2, R=3`.

4. Steps: `R=3,4` both zeros → just advance R.

5. Step: `L=2, R=5`, array = `[4, 5, 0, 0, 0, 6, 7]`
   * `nums[R]=6` → swap with `nums[L]` → `[4, 5, 6, 0, 0, 0, 7]` → `L=3, R=6`.

6. Step: `L=3, R=6`, array = `[4, 5, 6, 0, 0, 0, 7]`
   * `nums[R]=7` → swap with `nums[L]` → `[4, 5, 6, 7, 0, 0, 0]` → `L=4, R=7`.

7. End: `R` reaches `len(nums)`, loop stops, final array is `[4, 5, 6, 7, 0, 0, 0]`.

All zeros have moved to the end, and non-zero elements retained their original relative order.

Time Complexity: O(n) (go through)
Space Complexity: O(1) for L, R
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        if len(nums) <= 1:
            return

        L, R = 0, 0
        while R < len(nums):
            # If the current element at R is non-zero, we need to move it to index L.
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                # After placing a non-zero at L, move L forward so the next non-zero goes to the next slot.
                L += 1
            # Always advance R to continue scanning.
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
