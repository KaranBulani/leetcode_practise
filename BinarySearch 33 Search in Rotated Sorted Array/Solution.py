'''
Time Complexity:  O(logn)              (for Binary Search)
Space Complexity: O(1)                 (for Variables, indexes)
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (R + L)//2

            # Found the target
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            elif nums[L] <= nums[mid]:
                if nums[L] <= target < nums[mid]:
                    R = mid - 1 # target lies in left half
                else:
                    L = mid + 1 # target lies in right half
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[R]:
                    L = mid + 1  # target lies in right half
                else:
                    R = mid - 1  # target lies in left half
        return -1 # not found


if __name__ == "__main__":
    solution = Solution()

    # Example cases from the question
    print(solution.search([3,1], 1))  # Expected: 1
    print(solution.search([5,1,3], 5))  # Expected: 0
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1
    print(solution.search([1], 0))  # Expected: -1

    # Additional edge cases
    # Target is the first element
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 4))  # Expected: 0

    # Target is the last element
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 2))  # Expected: 6

    # Array not rotated, target present
    print(solution.search([1, 2, 3, 4, 5, 6, 7], 5))  # Expected: 4

    # Array not rotated, target absent
    print(solution.search([1, 2, 3, 4, 5, 6, 7], 9))  # Expected: -1

    # Minimum size array, target present
    print(solution.search([1], 1))  # Expected: 0

    # Two elements, rotated, target present
    print(solution.search([3, 1], 1))  # Expected: 1

    # Two elements, rotated, target absent
    print(solution.search([3, 1], 2))  # Expected: -1

    # Target in left sorted portion
    print(solution.search([6, 7, 8, 1, 2, 3, 4, 5], 7))  # Expected: 1

    # Target in right sorted portion
    print(solution.search([6, 7, 8, 1, 2, 3, 4, 5], 4))  # Expected: 6