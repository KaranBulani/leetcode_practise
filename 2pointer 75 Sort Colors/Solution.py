'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from question
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(nums1)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 2: Another example from question
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    print(nums2)  # Expected: [0, 1, 2]

    # Test case 3: Already sorted
    nums3 = [0, 0, 1, 1, 2, 2]
    solution.sortColors(nums3)
    print(nums3)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 4: Reverse sorted
    nums4 = [2, 2, 1, 1, 0, 0]
    solution.sortColors(nums4)
    print(nums4)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 5: Only 0s
    nums5 = [0, 0, 0]
    solution.sortColors(nums5)
    print(nums5)  # Expected: [0, 0, 0]

    # Test case 6: Only 1s
    nums6 = [1, 1, 1]
    solution.sortColors(nums6)
    print(nums6)  # Expected: [1, 1, 1]

    # Test case 7: Only 2s
    nums7 = [2, 2, 2]
    solution.sortColors(nums7)
    print(nums7)  # Expected: [2, 2, 2]

    # Test case 8: Alternating values
    nums8 = [0, 1, 2, 0, 1, 2]
    solution.sortColors(nums8)
    print(nums8)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 9: Single element
    nums9 = [1]
    solution.sortColors(nums9)
    print(nums9)  # Expected: [1]

    # Test case 10: Two elements
    nums10 = [2, 0]
    solution.sortColors(nums10)
    print(nums10)  # Expected: [0, 2]
