'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort() # nums = sorted(nums) both same
        res = []
        for A in range(len(nums)):

            # skip if current is same as prev, A > 0  then only prev applicable
            if A > 0 and nums[A] == nums[A - 1]:
                continue

            L, R = A + 1, len(nums) - 1
            while L < R:
                threeSum = nums[A] + nums[L] + nums[R]
                if threeSum == 0:
                    res.append([nums[A], nums[L], nums[R]])
                    # Could use 'break' to get out but same 'A' can have another soln like '-1',-1,2 OR '-1',0,1

                    # what if its '-2',0,0,2,2  then same soln will be repeated even when L,R is changed.
                    # So keep changing till value is same and stop once it isn't
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                    R -= 1
                    while nums[R] == nums[R + 1] and L < R:
                        R -= 1

                elif threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1

        return res

if __name__ == "__main__":
    solution = Solution()

    # test cases from prompt
    test_cases = [
        [-1, 0, 1, 2, -1, -4],  # example 1
        [0, 1, 1],  # example 2
        [0, 0, 0],  # example 3

        # additional edge cases
        [0, 0, 0, 0],  # all zeros, multiple duplicates
        [3, -2, -1, 0, 1, 2],  # positives and negatives summing multiple ways
        [1, -1, -1, 0],  # duplicates with only one valid triplet
        [100000, -100000, 0],  # large values at bounds
        [-2, 0, 1, 1, 2]  # duplicates with two distinct triplets
    ]

    expected = [
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        [[0, 0, 0]],

        [[0, 0, 0]],
        [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
        [[-1, 0, 1]],
        [[-100000, 0, 100000]],
        [[-2, 0, 2], [-2, 1, 1]]
    ]

    for i, (nums, exp) in enumerate(zip(test_cases, expected), 1):
        result = solution.threeSum(nums)
        print(f"Test case {i}:")
        print(f"  Input:    {nums}")
        print(f"  Output:   {result}")
        print(f"  Expected: {exp}")
        print(f"  Pass:     {sorted(result) == sorted(exp)}\n")