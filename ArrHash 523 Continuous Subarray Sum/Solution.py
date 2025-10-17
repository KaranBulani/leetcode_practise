'''
if for any
    sum(i,j) % k == 0
then return True

-> sum(i,j) % k = 0
-> [prefix(j) - prefix(i-1)] % k = 0
-> prefix(j) % k - prefix(i-1) % k = 0
-> prefix(j) % k = prefix(i-1) % k
-> basically we want to find same remainder and find difference when same remainder is repeated

Note: over here differences between index which is J - I + 1
      but I is over here + I - 1

      -> J - ( +I - 1) - 1
      -> J - I +1 -1
      -> J - I

Time complexity:  O(n)						Traversing nums
Space complexity: O(n)						remainder_index
'''
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_index = {0 : -1}

        currSum = 0
        for i, num in enumerate(nums):
            currSum += num
            remainder = currSum % k if k != 0 else currSum
            if remainder in remainder_index and (i - remainder_index[remainder]) > 1:
                return True
            elif remainder not in remainder_index:
                remainder_index[remainder] = i
        return False


if __name__ == "__main__":
    solution = Solution()

    # Example 1 (From question)
    nums = [23, 2, 4, 6, 7]
    k = 6
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Example 2 (From question)
    nums = [23, 2, 6, 4, 7]
    k = 6
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Example 3 (From question)
    nums = [23, 2, 6, 4, 7]
    k = 13
    print(solution.checkSubarraySum(nums, k))  # Expected: False

    # Edge Case 1: Small array with no valid subarray
    nums = [1, 2]
    k = 4
    print(solution.checkSubarraySum(nums, k))  # Expected: False

    # Edge Case 2: Consecutive zeros (sum = 0, multiple of any k)
    nums = [0, 0]
    k = 1
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Edge Case 3: Zero in between other numbers forming valid subarray
    nums = [5, 0, 0, 0]
    k = 5
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Edge Case 4: Large k, but subarray sum is 0 (multiple of k)
    nums = [0, 0, 0, 0, 0]
    k = 10000
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Edge Case 5: Large numbers where prefix sums repeat mod k
    nums = [5, 10, 15, 20]
    k = 5
    print(solution.checkSubarraySum(nums, k))  # Expected: True

    # Edge Case 6: Single element array (invalid because subarray must have length ≥ 2)
    nums = [5]
    k = 3
    print(solution.checkSubarraySum(nums, k))  # Expected: False

    # Edge Case 7: Long array but no valid multiple
    nums = [1, 2, 3]
    k = 7
    print(solution.checkSubarraySum(nums, k))  # Expected: False