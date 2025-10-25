'''
####################################################################################################
########################################## SLIDING WINDOW ##########################################
####################################################################################################
Time complexity:  O(N)									 for one pass
Space complexity: O(1)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostOdd(curr: int) -> int:
            res = 0
            left = 0
            freq = defaultdict(int)
            for right, value in enumerate(nums):
                isEven = value % 2
                freq[isEven] += 1

                while freq[1] > curr:
                    leftIsEven = nums[left] % 2
                    freq[leftIsEven] -= 1
                    left += 1

                res += right - left + 1
            return res
        return atMostOdd(k) - atMostOdd(k - 1)

####################################################################################################
############################################ PREFIX SUM ############################################
####################################################################################################

Time complexity:  O(N)									 for two pass
Space complexity: O(N)									 for prefix sum
'''
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] % 2

        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0
        currSum = 0
        for num in nums:
            currSum += num
            ans += prefix[currSum - k]
            prefix[currSum] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(solution.numberOfSubarrays(nums, k))  # Expected: 2

    # Example 2
    nums = [2, 4, 6]
    k = 1
    print(solution.numberOfSubarrays(nums, k))  # Expected: 0

    # Example 3
    nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected: 16

    # Edge Case 1: Single element odd
    nums = [1]
    k = 1
    print(solution.numberOfSubarrays(nums, k))  # Expected: 1

    # Edge Case 2: Single element even
    nums = [2]
    k = 1
    print(solution.numberOfSubarrays(nums, k))  # Expected: 0

    # Edge Case 3: All odd numbers
    nums = [1, 3, 5, 7]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected: 3

    # Edge Case 4: Alternating odd/even
    nums = [1, 2, 1, 2, 1]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected: 4

    # Edge Case 5: Large sequence of evens before odds
    nums = [2, 2, 2, 1, 1, 2]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected: 3