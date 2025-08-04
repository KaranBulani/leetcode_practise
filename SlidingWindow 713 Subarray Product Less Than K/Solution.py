'''
####################################################################################################
########################################### BRUTE FORCE ############################################
####################################################################################################

Time Complexity:  O(n^2)              (for & while loop)
Space Complexity: O(1)                (for Variables, indexes)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        for L in range(len(nums)):
            R = L
            cur_product = 1
            while R < len(nums) and cur_product * nums[R] < k:
                cur_product = cur_product * nums[R]
                res += 1
                R += 1
        return res

####################################################################################################
############################################ Optimized #############################################
####################################################################################################

Time Complexity:  O(2n)              (for sliding window)
Space Complexity: O(1)               (for Variables, indexes)

'''
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0                    # No subarray can have product < k if k <= 1

        L = 0                           # Left pointer for sliding window
        product = 1                     # Current product of the window
        count = 0                       # Result to store number of valid sub arrays

        for R in range(len(nums)):
            product *= nums[R]          # Expand the window to the right

            # Shrink the window from the left until product < k
            # Then again start introduction new R
            while product >= k:
                product //= nums[L]
                L += 1

            # At each new introduction of R, count expands by windowLen, Check it
            count += R - L + 1

        return count

if __name__ == "__main__":
    solution = Solution()

    # Example case 1
    nums1 = [10, 5, 2, 6]
    k1 = 100
    print(solution.numSubarrayProductLessThanK(nums1, k1))  # Expected: 8

    # Example case 2
    nums2 = [1, 2, 3]
    k2 = 0
    print(solution.numSubarrayProductLessThanK(nums2, k2))  # Expected: 0

    # Edge case: Single element less than k
    nums3 = [1]
    k3 = 2
    print(solution.numSubarrayProductLessThanK(nums3, k3))  # Expected: 1

    # Edge case: Single element equal to k
    nums4 = [10]
    k4 = 10
    print(solution.numSubarrayProductLessThanK(nums4, k4))  # Expected: 0

    # Edge case: All elements are 1, k is small
    nums5 = [1, 1, 1]
    k5 = 2
    print(solution.numSubarrayProductLessThanK(nums5, k5))  # Expected: 6

    # Edge case: All elements are large, all products exceed k
    nums6 = [1000, 1000, 1000]
    k6 = 1
    print(solution.numSubarrayProductLessThanK(nums6, k6))  # Expected: 0

    # Edge case: Increasing sequence
    nums7 = [1, 2, 3, 4]
    k7 = 10
    print(solution.numSubarrayProductLessThanK(nums7, k7))  # Expected: 7

    # Edge case: Long input with all 1s, to test performance
    nums8 = [1] * 10000
    k8 = 2
    print(solution.numSubarrayProductLessThanK(nums8, k8))  # Expected: 10000 * (10000 + 1) // 2 = 50005000