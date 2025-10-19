'''
In 523, we stopped when we found one pair.
But now, we want count of all such pairs (i, j) where remainders match.

If a remainder r appears freq[r] times so far,
then every new occurrence of remainder r can pair with all earlier ones to form valid subarrays.

So for each new remainder:		count += freq[r]
then increment freq[r] by 1.

Time complexity:  O(n)						Traversing nums
Space complexity: O(n)						prefixSumCounter
'''
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefixSumCounter = defaultdict(int)
        prefixSumCounter[0] = 1
        currSum = res = 0
        for num in nums:
            currSum += num
            remainder = currSum % k
            res += prefixSumCounter[remainder]
            prefixSumCounter[remainder] += 1
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    print(solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # Expected: 7
    print(solution.subarraysDivByK([5], 9))  # Expected: 0

    # Edge case: all zeros (every subarray sum = 0, divisible by any k)
    print(solution.subarraysDivByK([0, 0, 0], 5))  # Expected: ?

    # Edge case: negative numbers mix
    print(solution.subarraysDivByK([-1, 2, 9], 2))  # Expected: ?

    # Case: large k relative to nums
    print(solution.subarraysDivByK([2, -2, 2, -4], 6))  # Expected: ?

    # Case: single element divisible by k
    print(solution.subarraysDivByK([10], 5))  # Expected: ?

    # Case: single element not divisible by k
    print(solution.subarraysDivByK([7], 3))  # Expected: ?

    # Case: mix of positives and negatives summing to multiple of k
    print(solution.subarraysDivByK([3, 1, 4, 2, -3, 6], 5))  # Expected: ?

    # Case: longer array with repeated pattern
    print(solution.subarraysDivByK([1, 2, 3, 4, 5, 6], 3))  # Expected: ?