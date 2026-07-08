'''
Intuition
Think of the permutation as a number.

Example:
	1 2 3  -> 123
	1 3 2  -> 132
	2 1 3  -> 213

We need the smallest permutation that is larger than the current one.

To increase the number as little as possible:
1. Find the first place (from the right) where the sequence stops decreasing.
2. Increase that digit by swapping it with the next larger digit on its right.
3. Make the remaining suffix as small as possible (reverse it).
####################################################################################################

Observation
Starting from the end:
		1 2 5 4 3
			  ↑

Notice the suffix is always non-increasing.
		5 4 3
This is already the largest arrangement of these numbers.

So to get the next permutation, we must modify something before this suffix.
####################################################################################################
Algorithm

Step 1. Find the Pivot

    Traverse from right to left.
    Find the first index where		nums[i] < nums[i+1]

    Example:
            1 2 5 4 3
                ↑
            Pivot = 2

Step 2. If no pivot exists

    Example
            5 4 3 2 1

    Entire array is decreasing.
    This is already the largest permutation.
    Answer:
    1 2 3 4 5

    Simply reverse the whole array.

Step 3. Find the next greater element

    Again search from the right.
    Find the first element greater than pivot.

    Example

            1 2 5 4 3
                    ↑

    3 is the first element greater than 2. 3 would also be the smallest one out of 5,4,3

    Swap.
            1 3 5 4 2

Step 4. Reverse the suffix

    Current suffix
            5 4 2
    It's decreasing.

    Reverse it.
            2 4 5

    Final answer
            1 3 2 4 5

####################################################################################################
## Why does reversing work?

After swapping, the suffix is still in decreasing order.

Example
	5 4 2

The smallest arrangement of these numbers is simply
	2 4 5

Since the suffix is already decreasing, reversing it sorts it into increasing order in O(n).

####################################################################################################
* Time Complexity: O(n)
  * Find pivot: O(n)
  * Find next greater: O(n)
  * Reverse suffix: O(n)
  * Overall: O(n)

* Space Complexity: O(1)
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Step 1: Find pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # Step 2: If no pivot, reverse everything
        if pivot == -1:
            nums.reverse()
            return

        # Step 3: Find next greater element
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # Step 4: Reverse suffix
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),

        # Edge Cases
        ([1], [1]),  # Single element
        ([1, 2], [2, 1]),  # Two elements increasing
        ([2, 1], [1, 2]),  # Two elements decreasing
        ([1, 1], [1, 1]),  # All same
        ([2, 2, 2], [2, 2, 2]),  # All duplicates
        ([1, 3, 2], [2, 1, 3]),  # Pivot in middle
        ([2, 1, 3], [2, 3, 1]),  # Pivot near end
        ([1, 5, 1], [5, 1, 1]),  # Duplicate with pivot
        ([1, 4, 3, 2], [2, 1, 3, 4]),  # Long decreasing suffix
        ([2, 3, 1], [3, 1, 2]),  # Example from description
        ([1, 2, 5, 4, 3], [1, 3, 2, 4, 5]),  # Larger suffix
        ([5, 4, 7, 5, 3, 2], [5, 5, 2, 3, 4, 7]),
        ([1, 3, 5, 4, 2], [1, 4, 2, 3, 5]),
        ([0, 1, 0], [1, 0, 0]),  # Contains zero
        ([100, 99, 98], [98, 99, 100]),  # Large values
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        arr = nums[:]  # Copy to preserve original
        solution.nextPermutation(arr)

        print(f"Test Case {i}")
        print(f"Input    : {nums}")
        print(f"Output   : {arr}")
        print(f"Expected : {expected}")
        print(f"Pass     : {arr == expected}")
        print("-" * 50)