'''
1. Observation

We need to find:
* The length of the Longest Increasing Subsequence (LIS)
* The number of subsequences having that maximum length

Key observation:

For every index i:
* length[i] → length of LIS ending at index i
* count[i] → number of LIS ending at index i
If nums[j] < nums[i], then we can extend subsequence ending at j.

Two important cases arise:

Case 1: Better LIS found

	If:	length[j] + 1 > length[i]
	then we found a strictly longer subsequence.

	So:
	* update length[i]
	* inherit count from j

Case 2: Another LIS of same length found

	If: length[j] + 1 = length[i]
	then another way exists to build same-length LIS.

	So:
	* add counts
####################################################################################################

2. Simulation

Example:
nums = [1,3,5,4,7]

Initialize:
length = [1,1,1,1,1]
count  = [1,1,1,1,1]
Every element alone forms LIS of length 1.

i = 1 (3)

	Compare with 1
	1 < 3
	Possible LIS: 1 -> 3
	Update:
		length[1] = 2
		count[1] = 1

i = 2 (5)

	Can extend from:
	* 1
	* 3

	Best comes from 3
	1 -> 3 -> 5

	Update:
	length[2] = 3
	count[2] = 1

i = 3 (4)

	Can extend from:
	* 1
	* 3
	Cannot extend from 5
	Best:
	1 -> 3 -> 4
	Update:
	length[3] = 3
	count[3] = 1

i = 4 (7)

	Can extend from:
	* 5
	* 4
	Both produce LIS length 4.
	From 5:
	1 -> 3 -> 5 -> 7
	From 4:
	1 -> 3 -> 4 -> 7
	So:
	length[4] = 4
	count[4] = 2

Final:
length = [1,2,3,3,4]
count  = [1,1,1,1,2]

Maximum LIS length: 4
Number of LIS: 2
####################################################################################################
3. Dynamic Programming

State:
* length[i] = LIS length ending at i
* count[i] = number of LIS ending at i

Transition:

If: nums[j] < nums[i]
then:
	Better subsequence found

	if length[j] + 1 > length[i]:
		length[i] = length[j] + 1
		count[i] = count[j]

	Same best length found again

	elif length[j] + 1 == length[i]:
		count[i] += count[j]

############################################## BOTTOM UP ##############################################
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):

                if nums[j] < nums[i]:
                    # Better LIS found
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    # Another LIS of same length
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        ans = 0
        for i in range(n):
            if length[i] == max_len:
                ans += count[i]
        return ans
####################################################################################################
Time Complexity

We check every pair (j, i) where: 0 <= j < i < n
So total transitions: O(n^2)

Work done per transition is constant.

Total Complexity O(n^2)

Space Complexity

We use two arrays:
* length
* count
each of size n.

So: O(n)
'''
class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples
        {
            "nums": [1, 3, 5, 4, 7],
            "expected": 2
        },
        {
            "nums": [2, 2, 2, 2, 2],
            "expected": 5
        },

        # Single element
        {
            "nums": [10],
            "expected": 1
        },

        # Strictly increasing
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 1
        },

        # Strictly decreasing
        {
            "nums": [5, 4, 3, 2, 1],
            "expected": 5
        },

        # Multiple LIS of same length
        {
            "nums": [1, 2, 4, 3, 5, 4, 7, 2],
            "expected": 3
        },

        # Duplicates with increasing pattern
        {
            "nums": [1, 2, 2, 2, 3],
            "expected": 3
        },

        # Negative numbers
        {
            "nums": [-1, -2, -3, -4],
            "expected": 4
        },

        # Mixed negative and positive
        {
            "nums": [-1, 3, 4, 5, 2, 2, 2, 2],
            "expected": 1
        },

        # All same except one larger
        {
            "nums": [1, 1, 1, 1, 2],
            "expected": 4
        },

        # Larger branching possibilities
        {
            "nums": [1, 3, 2, 4, 3, 5],
            "expected": 3
        },

        # Repeated increasing opportunities
        {
            "nums": [1, 2, 1, 2, 1, 2],
            "expected": 6
        },

        # Longest subsequence length = 2
        {
            "nums": [4, 6, 1, 3, 5],
            "expected": 2
        },

        # Edge case with many equal choices
        {
            "nums": [1, 1, 1, 2, 2, 2, 3, 3, 3],
            "expected": 27
        },
    ]

    for idx, test in enumerate(test_cases, 1):
        nums = test["nums"]
        expected = test["expected"]

        result = solution.findNumberOfLIS(nums)

        print(f"Test Case {idx}")
        print(f"nums     = {nums}")
        print(f"Expected = {expected}")
        print(f"Your Ans = {result}")
        print(f"Passed   = {result == expected}")
        print("-" * 50)