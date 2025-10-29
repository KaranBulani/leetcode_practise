'''
Time complexity:  O(n)		 			Single traversal
Space complexity: O(n)		 			due to first_seen
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        currSum = 0
        first_seen = {0: -1}

        for R in range(len(nums)):
            curr = 1 if nums[R] == 1 else -1
            currSum += curr

            if currSum not in first_seen:
                first_seen[currSum] = R
                continue
            res = max(res, R - first_seen[currSum])

        return res


if __name__ == "__main__":
    solution = Solution()

    # ✅ Example 1
    nums = [0, 1]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 2

    # ✅ Example 2
    nums = [0, 1, 0]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 2

    # ✅ Example 3
    nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 6

    # ⚙️ Edge Case 1: Single element (no valid subarray)
    nums = [0]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 0

    # ⚙️ Edge Case 2: All zeros (no valid subarray)
    nums = [0, 0, 0, 0]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 0

    # ⚙️ Edge Case 3: All ones (no valid subarray)
    nums = [1, 1, 1, 1]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 0

    # ⚙️ Edge Case 4: Alternating pattern (entire array valid)
    nums = [0, 1, 0, 1, 0, 1, 0, 1]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 8

    # ⚙️ Edge Case 5: Large balanced section in middle
    nums = [1, 1, 1, 0, 0, 0, 1]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 6

    # ⚙️ Edge Case 6: Complex pattern
    nums = [0, 1, 1, 0, 1, 0, 0]
    result = solution.findMaxLength(nums)
    print(result)  # Expected: 6