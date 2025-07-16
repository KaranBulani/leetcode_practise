'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        pass

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
