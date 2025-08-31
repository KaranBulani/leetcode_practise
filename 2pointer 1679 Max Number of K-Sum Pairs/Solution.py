'''
####################################################################################################
######################################### HashMap Solution #########################################
####################################################################################################

Time Complexity:  O(n)                     (for count)
Space Complexity: O(keys)                  (for keys)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        count = 0

        for num in list(freq.keys()):  # iterate over unique numbers
            complement = k - num

            if complement not in freq:
                continue

            if num == complement:
                # Special case: use pairs from same number
                count += freq[num] // 2
            else:
                # Match min available between num and complement
                count += min(freq[num], freq[complement])
                freq[complement] = 0  # avoid recounting

            #for all scenario as that num is considered
            freq[num] = 0
        return count

####################################################################################################
############################################ 2 pointer #############################################
####################################################################################################

Time Complexity:  O(nlogn)              (for sort)
Space Complexity: O(1)                  (for 2 pointer)
'''
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        L, R = 0, len(nums) - 1
        res = 0
        while L < R:
            total = nums[L] + nums[R]
            if total == k:
                L += 1
                R -= 1
                res += 1
            elif total < k:
                L += 1
            else:
                R -= 1
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1 from question
    nums = [1, 2, 3, 4]
    k = 5
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 2

    # Example 2 from question
    nums = [3, 1, 3, 4, 3]
    k = 6
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 1

    # Edge Case 1: No valid pairs
    nums = [1, 2, 3]
    k = 10
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 0

    # Edge Case 2: All numbers are the same and form multiple pairs
    nums = [2, 2, 2, 2]
    k = 4
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 2

    # Edge Case 3: Odd length array with leftover element
    nums = [1, 4, 2, 3, 5]
    k = 5
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 2

    # Edge Case 4: Large numbers with only one valid pair
    nums = [10**9, 1, 2, 10**9 - 1]
    k = 10**9
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 1

    # Edge Case 5: Array of length 1 (cannot form a pair)
    nums = [5]
    k = 5
    result = solution.maxOperations(nums, k)
    print(result)  # Expected: 0