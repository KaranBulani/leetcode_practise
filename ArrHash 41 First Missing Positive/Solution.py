'''
Time Complexity:  O(3n)             * n for converting -ve values to inf --> Now all nums[i] are : 0, ... len(nums), len(nums) + 1 (Invalid), ........ inf
                                    * n for going through all valid ones "0 ... len(nums)" and marking their index as -ve and handling duplicates
                                            --> Now all nums[i] are : -0, -1, -2 ... -inf
                                    * n for going through nums and return whichever is still +ve that index is our answer

Space Complexity: O(1)               (as it's inplace)
'''

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        # Step 1: Replace non-positive numbers with +infinity
        # Any non-positive value (zero or negative) cannot be the answer, so mark them as unused
        for i, n in enumerate(nums):
            if n <= 0:
                nums[i] = float('inf')

        # Step 2: Use index marking to record presence
        # For each number x in the array, if 1 <= x <= len(nums),
        # mark the value at index x-1 as negative to indicate 'x' exists
        for n in nums:
            abs_n = abs(n)  # take absolute value in case it's already been marked
            if 1 <= abs_n <= len(nums):
               # Multiply by -1 to mark presence; abs() prevents double-negation issues, which happen when there are duplicates
               nums[abs_n - 1] = -1 * abs( nums[abs_n - 1])

        # Step 3: The first index i (starting from 0) where nums[i] is still positive
        # indicates that (i+1) was never seen in the array
        for i in range(len(nums)):
            if nums[i] > 0:
                # Missing positive is index+1
                return i + 1

        # If all positions 1..len(nums) are marked, then the array contains 1..n
        # So the first missing positive is n+1
        return len(nums) + 1

if __name__ == "__main__":
    solution = Solution()

    # Test cases from the problem statement
    test_cases = [
        ([1, 2, 0], 3),              # consecutive positives starting at 1
        ([3, 4, -1, 1], 2),          # missing 2 between present 1 and 3
        ([7, 8, 9, 11, 12], 1),      # no 1 present at all
    ]

    # Additional edge cases
    test_cases += [
        ([1], 2),                    # single element present
        ([2], 1),                    # single element missing 1
        ([1, 1, 2, 2], 3),           # duplicates of small positives
        ([-5, -3, -1], 1),           # all negatives
        ([1, 2, 3, 4, 5], 6),        # all first k positives present
        ([2, 3, 4, 5, 6], 1),        # 1 missing despite many positives
        ([100000, 99999], 1),        # large values, small missing
        (list(range(1, 1000)), 1000) # long consecutive run
    ]

    for nums, expected in test_cases:
        num_copy = nums.copy()
        result = solution.firstMissingPositive(nums)
        print(f"Input: {num_copy}\nExpected: {expected}, Got: {result}\n")