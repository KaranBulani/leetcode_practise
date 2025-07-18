'''
Time Complexity:  O(n^3)       (2 for loop and 1 for L,R)
                  O(nlogn)      for sort

                  O(n^k-1)      Where k is kSum

Space Complexity: O(k)          for quad as it has at max k lenth
                + O(k)          for recursive calls
                + O(1)          for L, K
                : O(k)
                We don't count result
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        #No need to add this in kSum fn parameter as it's anyway available to it.
        res, quad = [], []
        nums.sort()

        def kSum(k: int, start: int, target: int):
            # If need to pick more than two numbers, reduce the problem
            if k != 2:
                # Stop at len(nums) - k + 1 to leave enough room for the remaining k−1 picks
                # Don't touch last 3 values if k is 4
                for i in range(start, len(nums) - k + 1):
                    # Skip duplicates at the same position: if this value is same as the previous at this level, ignore it
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    # Choose nums[i] as part of the current combination
                    quad.append(nums[i])

                    # Recurse to pick the remaining k−1 numbers, adjusting start and target
                    # in 2nd parameter we do i+1 not start+1
                    kSum(k - 1, i + 1, target - nums[i])
                    # Backtrack: remove the last choice before the next iteration
                    quad.pop()
                # Once we've handled k > 2, we don't want to run the two-pointer logic below
                return

            # Base case: when k == 2, below section exactly like LC -> 15. Sum
            L, R = start, len(nums) - 1
            while L < R:
                twoSum = nums[L] + nums[R]
                if twoSum > target:
                    R -= 1
                elif twoSum < target:
                    L += 1
                else:
                    res.append(quad + [nums[L], nums[R]])

                    # Move left pointer past duplicates
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

                    # Move right pointer past duplicates
                    R -= 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1

        kSum(4, 0, target)
        return res

if __name__ == "__main__":
    sol = Solution()

    # Example test cases from the prompt
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    # Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print("Input:", nums1, "Target:", target1)
    print("Output:", sol.fourSum(nums1, target1))  # Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print()

    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    # Expected: [[2, 2, 2, 2]]
    print("Input:", nums2, "Target:", target2)
    print("Output:", sol.fourSum(nums2, target2))  # Expected: [[2, 2, 2, 2]]
    print()

    # Additional edge cases

    # 1. Empty array
    nums3 = []
    target3 = 0
    # Expected: []
    print("Input:", nums3, "Target:", target3)
    print("Output:", sol.fourSum(nums3, target3))  # Expected: []
    print()

    # 2. Less than four elements
    nums4 = [1, 2, 3]
    target4 = 6
    # Expected: []
    print("Input:", nums4, "Target:", target4)
    print("Output:", sol.fourSum(nums4, target4))  # Expected: []
    print()

    # 3. All zeros
    nums5 = [0, 0, 0, 0, 0]
    target5 = 0
    # Expected: [[0, 0, 0, 0]]
    print("Input:", nums5, "Target:", target5)
    print("Output:", sol.fourSum(nums5, target5))  # Expected: [[0, 0, 0, 0]]
    print()

    # 4. No valid quadruplets
    nums6 = [1, 2, 3, 4, 5]
    target6 = 100
    # Expected: []
    print("Input:", nums6, "Target:", target6)
    print("Output:", sol.fourSum(nums6, target6))  # Expected: []
    print()

    # 5. Negative and positive mix
    nums7 = [-3, -1, 0, 2, 4, 5]
    target7 = 2
    # Expected: [[-3, -1, 0, 6]?] (depending on nums; adjust expected accordingly)
    # Note: no 6 present; real expected: [[-3, -1, 0, 6]] is invalid here, so expected: []
    print("Input:", nums7, "Target:", target7)
    print("Output:", sol.fourSum(nums7, target7))  # Expected: []
    print()

    # 6. Large numbers
    nums8 = [10**9, 10**9, -10**9, -10**9, 0]
    target8 = 0
    # Expected: [[-10**9, -10**9, 10**9, 10**9], [-10**9, 0, 0, 10**9]?]
    # Actually: [[-1000000000, -1000000000, 1000000000, 1000000000]]
    print("Input:", nums8, "Target:", target8)
    print("Output:", sol.fourSum(nums8, target8))  # Expected: [[-1000000000, -1000000000, 1000000000, 1000000000]]
