'''
####################################################################################################
############################################ DP Approach ###########################################
####################################################################################################

Time Complexity:  O(n^2)              	(for DP)
Space Complexity: O(n)              	(for DP array)

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i] will store the length of the longest increasing subsequence
        # that ends with nums[i]
        dp = [1] * n

        for i in range(n):
            # Check all elements before nums[i]
            for j in range(i):
                # If nums[j] < nums[i], then nums[i] can extend the subsequence ending at nums[j]
                if nums[j] < nums[i]:
                    # Update dp[i] to the max length possible by appending nums[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        # The answer is the longest subsequence found among all positions
        return max(dp)

####################################################################################################
############################################ DP Approach ###########################################
####################################################################################################

Time Complexity:  O(nlogn)              (BinarySearch for each number)
Space Complexity: O(n)              	(for sub array)

TUF Explanation - https://youtu.be/on2hvxBXJH4?si=od2bVJYKO8fZopZJ
'''


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 'sub' will store the increasing subsequence (not necessarily the LIS itself,
        # but its length will match the LIS length).
        sub = []

        for num in nums:
            # We want to find the position in 'sub' where 'num' should go.
            # Use binary search to find the smallest index 'pos'
            # such that sub[pos] >= num.
            left, right = 0, len(sub) - 1
            pos = len(sub)  # default is append at the end (if num is largest so far)

            while left <= right:
                mid = (left + right) // 2
                if sub[mid] >= num:
                    # Found a candidate position — try to go left for a smaller index
                    pos = mid
                    right = mid - 1
                else:
                    # num is greater, so LIS can extend — move right
                    left = mid + 1

            # After binary search, 'pos' tells us where num should be:
            if pos == len(sub):
                # Case 1: num is bigger than all elements in sub → append
                sub.append(num)
            else:
                # Case 2: replace the element at 'pos' with num
                # (this keeps sub as small as possible and maximizes future LIS extensions)
                sub[pos] = num

        # Length of 'sub' = length of LIS
        return len(sub)

if __name__ == "__main__":
    solution = Solution()

    # Examples from the problem statement
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print(solution.lengthOfLIS(nums1))  # Expected: 4  (LIS = [2,3,7,101])

    nums2 = [0, 1, 0, 3, 2, 3]
    print(solution.lengthOfLIS(nums2))  # Expected: 4  (LIS = [0,1,2,3])

    nums3 = [7, 7, 7, 7, 7, 7, 7]
    print(solution.lengthOfLIS(nums3))  # Expected: 1  (all same numbers)

    # Additional edge cases
    nums4 = [1]
    print(solution.lengthOfLIS(nums4))  # Expected: 1  (single element)

    nums5 = [4, 10, 4, 3, 8, 9]
    print(solution.lengthOfLIS(nums5))  # Expected: 3  (LIS = [4,8,9])

    nums6 = [2, 2, 2, 2, 2]
    print(solution.lengthOfLIS(nums6))  # Expected: 1  (duplicates only)

    nums7 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(solution.lengthOfLIS(nums7))  # Expected: 6  (LIS = [1,3,6,7,9,10])

    nums8 = list(range(1, 11))
    print(solution.lengthOfLIS(nums8))  # Expected: 10 (already increasing)

    nums9 = list(range(10, 0, -1))
    print(solution.lengthOfLIS(nums9))  # Expected: 1  (strictly decreasing)

    nums10 = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    print(solution.lengthOfLIS(nums10))  # Expected: 6  (LIS = [3,5,6,19] is not correct; correct LIS is [2,4,5,6,7,12])