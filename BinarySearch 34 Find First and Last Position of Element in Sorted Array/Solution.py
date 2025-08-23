'''
####################################################################################################
############################### Binary Search with Linear Expansion ################################
####################################################################################################

Time Complexity:  O(logn + k)              	(for BinarySearch, k is the number of target occurrences )
Space Complexity: O(1)              	    (for Variables, indexes)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]

        L = 0
        R = len(nums) - 1
        any_value = float("inf")
        while L <= R:
            M = (R + L) // 2
            if nums[M] == target:
                any_value = M
                break
            elif nums[M] > target:
                R = M - 1
            else:
                L = M + 1

        if any_value == float("inf"): return [-1, -1]

        leftmost = rightmost = any_value

        while leftmost > 0 and nums[leftmost - 1] == target:
            leftmost -= 1

        while rightmost < len(nums) - 1 and nums[rightmost + 1] == target:
            rightmost += 1

        return [leftmost, rightmost]

####################################################################################################
####################################### Binary Search Twice ########################################
####################################################################################################

Time Complexity:  O(2 * logn)              	(BinarySearch for findLeft, findRight)
Space Complexity: O(1)              	    (for Variables, indexes)
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            L, R = 0, len(nums) - 1
            left_index = -1
            while L <= R:
                M = (L + R) // 2
                if nums[M] == target:
                    left_index = M
                    R = M - 1  # keep searching left
                elif nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            return left_index

        def findRight():
            L, R = 0, len(nums) - 1
            right_index = -1
            while L <= R:
                M = (L + R) // 2
                if nums[M] == target:
                    right_index = M
                    L = M + 1  # keep searching right
                elif nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            return right_index

        return [findLeft(), findRight()]

if __name__ == "__main__":
    solution = Solution()

    # Example cases
    print(solution.searchRange([5,7,7,8,8,10], 8))   # Expected: [3,4]
    print(solution.searchRange([5,7,7,8,8,10], 6))   # Expected: [-1,-1]
    print(solution.searchRange([], 0))               # Expected: [-1,-1]

    # Additional edge cases
    print(solution.searchRange([1], 1))              # Expected: [0,0]
    print(solution.searchRange([1], 2))              # Expected: [-1,-1]
    print(solution.searchRange([2,2,2,2], 2))        # Expected: [0,3]
    print(solution.searchRange([1,2,3,4,5], 1))      # Expected: [0,0]
    print(solution.searchRange([1,2,3,4,5], 5))      # Expected: [4,4]
    print(solution.searchRange([1,2,3,3,3,3,4,5], 3))# Expected: [2,5]
    print(solution.searchRange([1,3,3,3,5,6], 4))    # Expected: [-1,-1]
    print(solution.searchRange([1,1,2,2,3,3,4,4], 2))# Expected: [2,3]