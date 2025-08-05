'''
Time Complexity:  O(logn)              (for binary search)
Space Complexity: O(1)              (for Variables, indexes)
'''


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high  = 0, len(nums) - 1
        while low <= high:
            mid = (high + low)//2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    solution = Solution()

    # Each entry is (nums, target, expected_index)
    test_cases = [
        # Examples from the prompt
        ([-1, 0, 3, 5, 9, 12], 13, -1),
        ([-1, 0, 3, 5, 9, 12], 9, 4),  # target in middle
        ([-1, 0, 3, 5, 9, 12], 2, -1),  # target not present

        # Additional edge cases
        ([1], 1, 0),  # single element, match
        ([1], 0, -1),  # single element, no match
        ([1, 2], 1, 0),  # two elements, target at start
        ([1, 2], 2, 1),  # two elements, target at end
        ([1, 2], 3, -1),  # two elements, target greater
        ([1, 2], -5, -1),  # two elements, target smaller

        (list(range(0, 10000, 2)), 998, 499),  # larger even-only array, even target
        (list(range(0, 10000, 2)), 999, -1),  # larger even-only array, odd target

        ([-10000, -5000, 0, 5000, 10000], -10000, 0),  # negatives and positives, first
        ([-10000, -5000, 0, 5000, 10000], 10000, 4),  # negatives and positives, last
    ]

    for nums, target, expected in test_cases:
        result = solution.search(nums, target)
        print(f"nums={nums[:5]}{'...' if len(nums) > 5 else ''}, "
              f"target={target} → got {result}, expected {expected}")