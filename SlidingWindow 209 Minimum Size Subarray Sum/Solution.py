'''
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

def minSubArrayLen(target, nums):
    n = len(nums)
    prefix = [0] * (n + 1)

    # Step 1: Build prefix sum array
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    min_len = float('inf')

    # Step 2: For each prefix[i], binary search for smallest j > i
    for i in range(n):
        required = target + prefix[i]
        # Find leftmost index where prefix[j] >= required
        bound = bisect.bisect_left(prefix, required, i + 1)
        if bound <= n:
            min_len = min(min_len, bound - i)

    return 0 if min_len == float('inf') else min_len

Time: O(n log n) – O(n) for prefix sum + O(log n) per binary search (done n times)
Space: O(n) for prefix array

############################################################################################################################


Time Complexity:  O(2n)              (for L, R)
Space Complexity: O(1)              (for Variables)
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minLen = float("inf")
        L, curSum = 0, 0
        for R in range(len(nums)):
            curSum += nums[R]

            # While the current window sum meets or exceeds the target,
            # try to shrink the window from the left to find the minimal length or new minimal length
            while curSum >= target:
                minLen = min(minLen, R - L + 1 )
                curSum -= nums[L]
                L += 1

        # If minLen was never updated, no valid subarray was found; return 0
        return 0 if minLen == float("inf") else minLen

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from the problem statement
        (7,   [2, 3, 1, 2, 4, 3]),   # expected 2  ([4,3])
        (4,   [1, 4, 4]),            # expected 1  ([4])
        (11,  [1, 1, 1, 1, 1, 1, 1, 1]),  # expected 0  (no valid subarray)

        # Additional edge cases
        (1,   []),                   # expected 0  (empty array)
        (5,   [5]),                  # expected 1  (single element equals target)
        (5,   [3]),                  # expected 0  (single element below target)
        (100, [1]*100),              # expected 100 (sum exactly reaches target only with full array)
        (10,  [2, 3, 1, 2, 4, 3]),   # expected 2  (same as first but target rolled forward)
        (15,  [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]),  # expected 1 ([10,7,...] actually [10] or [15] whichever minimal)
        (15,  [1, 2, 3, 4, 5]),      # expected 3  ([4,5, and maybe a smaller one])
    ]

    for idx, (target, nums) in enumerate(test_cases, 1):
        result = solution.minSubArrayLen(target, nums)
        print(f"Case {idx}: target={target}, nums={nums} -> {result}")