'''
Time Complexity:  O(n)              (for finding if cycle exists,)
Space Complexity: O(1)              (for slow, fast pointer)
##############################################################
EXAMPLE 1:
        0,1,2,3,4
nums = [1,3,4,2,2]

0 -> [1] → [3] → [2] → [4]
                  ↑     |
                  |_____|
##############################################################
EXAMPLE 2:
        0,1,2,3,4
nums = [3,1,3,4,2]

0 → [3] → [4] → [2]
      ↑          |
      |__________|
##############################################################
EXAMPLE 3:
        0,1,2,3,4
nums = [3,3,3,3,3]

0 → [3] ↺
1 ───┘
2 ───┘
4 ───┘
##############################################################
EXAMPLE 4:
        0,1,2,3,4,5,6,7,8,9
nums = [2,5,9,6,9,3,8,9,7,1]

0 → 2 → 9 → 1 → 5 → 3 → 6 → 8 → 7
        ↑                       |
        |_______________________|
##############################################################
With above examples we can conclude that, Repeated node will be the one more number of inward arrows
Hence it's LinkedList problem
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find if there exist cycle
        tortoise = nums[0]
        hare = nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break

        # Find entrance of cycle
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1

if __name__ == "__main__":
    solution = Solution()

    # Examples from the question
    test_cases = [
        [1, 3, 4, 2, 2],       # Example 1
        [3, 1, 3, 4, 2],       # Example 2
        [3, 3, 3, 3, 3],       # Example 3

        # Additional edge cases
        [1, 1],                # Smallest n, duplicate is 1
        [2, 2, 2, 2, 2],       # All numbers same
        [1, 4, 6, 2, 3, 5, 6], # Duplicate at the end
        [9, 7, 5, 4, 3, 2, 1, 8, 6, 9], # Duplicate at start & end
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 5], # Duplicate in middle
        [1, 2, 2, 3, 4, 5],    # Consecutive duplicate
        [5, 4, 3, 2, 1, 5],    # Duplicate is first and last element
    ]

    for nums in test_cases:
        result = solution.findDuplicate(nums)
        print(f"Input: {nums} -> Output: {result}")
