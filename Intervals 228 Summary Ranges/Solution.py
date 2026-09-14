'''
The key observation is that we only need to find consecutive runs.

For example:
	nums = [0,1,2,4,5,7]
	0,1,2  →  "0->2"
	4,5    →  "4->5"
	7      →  "7"

####################################################################################################

Approach

Use two pointers:

* start = beginning of the current range
* Move i while the next number is consecutive.
* When the consecutive sequence ends, create the range and start a new one.

####################################################################################################

Example

	nums = [0,1,2,4,5,7]

	start = 0
	0 → 1 → 2
	next is 4, so range = "0->2"

	start = 3
	4 → 5
	next is 7, so range = "4->5"

	start = 5
	7 is the last element
	range = "7"

	Answer:
	["0->2", "4->5", "7"]

####################################################################################################

Complexity

* Time: O(n) — each element is visited once.
* Space: O(1) auxiliary space, excluding the output.

LeetCode pattern to remember: whenever a sorted array asks you to group consecutive values, think "find the start and end of each consecutive run."
'''

class Solution:
    def summaryRanges(self, nums):
        ans = []
        start = 0

        for i in range(len(nums)):
            # Current range ends if:
            # 1. We're at the last element, or
            # 2. Next element is not consecutive
            if i == len(nums) - 1 or nums[i + 1] != nums[i] + 1:
                if start == i:
                    ans.append(str(nums[start]))
                else:
                    ans.append(f"{nums[start]}->{nums[i]}")

                start = i + 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9],

        # Edge cases
        [],
        [1],
        [0],
        [-1],
        [-5, -4, -3, -2, -1],

        # All isolated
        [1, 3, 5, 7, 9],

        # One continuous range
        [1, 2, 3, 4, 5],

        # Multiple ranges
        [1, 2, 4, 5, 7, 8, 9, 12],

        # Negative + positive
        [-5, -4, -3, 0, 1, 2, 5],

        # Range crossing zero
        [-2, -1, 0, 1, 2],

        # Large values
        [2147483645, 2147483646, 2147483647],

        # Minimum integer values
        [-2147483648, -2147483647, -2147483646],

        # Large gaps
        [-100, -50, 0, 50, 100],

        # Two separate ranges
        [1, 2, 3, 10, 11, 12],

        # Alternating singletons and ranges
        [1, 2, 5, 6, 7, 10, 12, 13],

        # Larger mixed case
        [-10, -9, -8, -5, -4, 0, 1, 2, 3, 10, 12, 13, 14],
    ]

    for nums in test_cases:
        result = solution.summaryRanges(nums)

        print(f"Input:    {nums}")
        print(f"Output:   {result}")
        print("-" * 60)