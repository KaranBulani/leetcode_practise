'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(n)              (for deque)
'''

from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_q = deque() # decreasing deque
        min_q = deque() # increasing deque
        L = 0
        res = 0
        for R in range(len(nums)):
            # Maintain decreasing deque for max
            while max_q and max_q[-1] < nums[R]:
                max_q.pop()
            max_q.append(nums[R])

            # Maintain increasing deque for min
            while min_q and min_q[-1] > nums[R]:
                min_q.pop()
            min_q.append(nums[R])

            # If difference exceeds limit, shrink window by increasing L and popping from deque
            # no need to check if queue has value as it just got appended
            while max_q[0] - min_q[0] > limit:
                if nums[L] == max_q[0]:
                    max_q.popleft()
                if nums[L] == min_q[0]:
                    min_q.popleft()
                L += 1

            res = max(res, R - L + 1)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Examples from the question
    nums = [8, 2, 4, 7]
    limit = 4
    print(solution.longestSubarray(nums, limit))  # Expected: 2

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    print(solution.longestSubarray(nums, limit))  # Expected: 4

    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0
    print(solution.longestSubarray(nums, limit))  # Expected: 3

    # Additional edge cases
    # 1-element array (smallest possible length)
    nums = [5]
    limit = 0
    print(solution.longestSubarray(nums, limit))  # Expected: 1

    # All numbers the same, large limit (should take full array)
    nums = [7, 7, 7, 7, 7]
    limit = 10
    print(solution.longestSubarray(nums, limit))  # Expected: 5

    # Strict limit where differences exceed immediately
    nums = [1, 10]
    limit = 0
    print(solution.longestSubarray(nums, limit))  # Expected: 1

    # Large increasing sequence where limit just allows full range
    nums = [1, 2, 3, 4, 5]
    limit = 4
    print(solution.longestSubarray(nums, limit))  # Expected: 5

    # Large increasing sequence where limit is smaller
    nums = [1, 2, 3, 4, 5]
    limit = 2
    print(solution.longestSubarray(nums, limit))  # Expected: 3

    # Decreasing sequence
    nums = [10, 9, 8, 7, 6, 5]
    limit = 3
    print(solution.longestSubarray(nums, limit))  # Expected: 4