'''
##################################################################################################################

Time Complexity:            O(2n)         (bucket creation + num reassignment)
Space Complexity:           O(1)          for counts

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        index = 0
        for color, cnt in enumerate(counts):
            for _ in range(cnt):
                nums[index] = color
                index += 1

##################################################################################################################

Time Complexity:            O(n)         (bucket creation + num reassignment)
Space Complexity:           O(1)          for L, M, R

'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Sorts nums in-place so that all 0’s come first, then 1’s, then 2’s.
        Dutch National Flag algorithm: O(n) time, O(1) extra space.
        """

        # Pointers:
        # L_red: next position to place 0
        # M_white: current index to evaluate
        # R_blue: next position to place 2
        L_red, M_white, R_blue = 0, 0, len(nums) - 1

        # Loop until the current pointer crosses the right boundary
        while M_white <= R_blue:
            if nums[M_white] == 0:
                # If the current element is 0, swap it with the element at L_red
                # and move both L_red and M_white one step forward
                nums[L_red], nums[M_white] = nums[M_white], nums[L_red]
                L_red += 1
                M_white += 1
            elif nums[M_white] == 1:
                # If the current element is 1, it’s already in the correct region
                # Just move the current pointer forward
                M_white += 1
            else:
                # If the current element is 2, swap it with the element at R_blue
                # Decrease R_blue to shrink the blue region
                nums[M_white], nums[R_blue] = nums[R_blue], nums[M_white]
                R_blue -= 1
                # Do NOT increment M_white here because the new element at M_white
                # might be a 0, 1, or 2 and still needs processing


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example from question
    nums1 = [2, 0, 2, 1, 1, 0]
    print(nums1)
    solution.sortColors(nums1)
    print(nums1)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 2: Another example from question
    nums2 = [2, 0, 1]
    print(nums2)
    solution.sortColors(nums2)
    print(nums2)  # Expected: [0, 1, 2]

    # Test case 3: Already sorted
    nums3 = [0, 0, 1, 1, 2, 2]
    print(nums3)
    solution.sortColors(nums3)
    print(nums3)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 4: Reverse sorted
    nums4 = [2, 2, 1, 1, 0, 0]
    print(nums4)
    solution.sortColors(nums4)
    print(nums4)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 5: Only 0s
    nums5 = [0, 0, 0]
    print(nums5)
    solution.sortColors(nums5)
    print(nums5)  # Expected: [0, 0, 0]

    # Test case 6: Only 1s
    nums6 = [1, 1, 1]
    print(nums6)
    solution.sortColors(nums6)
    print(nums6)  # Expected: [1, 1, 1]

    # Test case 7: Only 2s
    nums7 = [2, 2, 2]
    print(nums7)
    solution.sortColors(nums7)
    print(nums7)  # Expected: [2, 2, 2]

    # Test case 8: Alternating values
    nums8 = [0, 1, 2, 0, 1, 2]
    print(nums8)
    solution.sortColors(nums8)
    print(nums8)  # Expected: [0, 0, 1, 1, 2, 2]

    # Test case 9: Single element
    nums9 = [1]
    print(nums9)
    solution.sortColors(nums9)
    print(nums9)  # Expected: [1]

    # Test case 10: Two elements
    nums10 = [2, 0]
    print(nums10)
    solution.sortColors(nums10)
    print(nums10)  # Expected: [0, 2]
