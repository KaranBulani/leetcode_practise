'''
####################################################################################################
####################################################################################################

🧩 1. What max1st and curr2nd represent
Inside the loop:
	max1st = max(max1st, prefix[i - S] - prefix[i - S - F])
	res = max(res, max1st + curr2nd)
* max1st: the best (maximum) sum of an F-length subarray before the current S-length subarray
  → We use max() because we need to remember the maximum F-sum seen so far.
* curr2nd: the sum of the current S-length subarray (ending at index i-1).

🧩 2. Why we don’t take max() for curr2nd
Because at each iteration, we are already scanning all possible S-subarrays (one per loop iteration).
We only need the sum of the current S-subarray at this point.

The overall maximum combination is being tracked by res:
res = max(res, max1st + curr2nd)
So the max() logic for S-subarray is *implicit* — it’s handled by the running max res.

🧩 3. If we used max() there too…
If you did something like:
	max2nd = max(max2nd, curr2nd)
	res = max(res, max1st + max2nd)

That would break correctness — because you might combine:
* an F-subarray before one S-subarray,
* with the best S-subarray that overlaps or appears earlier (not allowed).
So we only take the current S window sum to maintain non-overlapping order.

✅ Summary

| Variable  | Purpose                                       | Uses max()? | Why                                              |
| --------- | --------------------------------------------- | ----------- | ------------------------------------------------ |
| max1st    | Best F-length subarray before current window  | ✅          | Need max of all previous                         |
| curr2nd   | Sum of current S-length subarray              | ❌          | Only one per loop — overall max tracked by res   |
| res       | Best total combination                        | ✅          | Tracks global max                                |

####################################################################################################
####################################################################################################

Time complexity:  O(n)		 			Single traversal
Space complexity: O(n)		 			prefix
'''

class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)
        #print(prefix)
        #print(nums, firstLen, secondLen)
        def helper(F: int, S: int) -> int:
            max1st = 0
            res = 0
            for i in range(F + S, len(nums) + 1):
                #print("i: ",i," 1st: ", prefix[i - S] - prefix[i - S - F]," 2nd: ", prefix[i] - prefix[i - S])
                max1st = max(max1st, prefix[i - S] - prefix[i - S - F])
                curr2nd = prefix[i] - prefix[i - S]
                res = max(res, max1st + curr2nd)
            return res

        return max(helper(firstLen, secondLen), helper(secondLen, firstLen))


if __name__ == "__main__":
    solution = Solution()

    # Example 1 (from question)
    nums = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    firstLen = 1
    secondLen = 2
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: 20

    # Example 2 (from question)
    nums = [3, 8, 1, 3, 2, 1, 8, 9, 0]
    firstLen = 3
    secondLen = 2
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: 29

    # Example 3 (from question)
    nums = [2, 1, 5, 6, 0, 9, 5, 0, 3, 8]
    firstLen = 4
    secondLen = 3
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: 31

    # Edge Case 1: minimal lengths and size
    nums = [1, 2]
    firstLen = 1
    secondLen = 1
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: 3

    # Edge Case 2: all zeros
    nums = [0, 0, 0, 0, 0]
    firstLen = 2
    secondLen = 2
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: 0

    # Edge Case 3: strictly increasing sequence
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    firstLen = 2
    secondLen = 3
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: ?

    # Edge Case 4: both subarrays could be anywhere (check both orders)
    nums = [5, 1, 5, 1, 5, 1, 5]
    firstLen = 2
    secondLen = 3
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: ?

    # Edge Case 5: large numbers and alternating pattern
    nums = [1000, 1, 1000, 1, 1000, 1, 1000]
    firstLen = 2
    secondLen = 2
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: ?

    # Edge Case 6: overlapping test scenario (verify non-overlap logic)
    nums = [5, 5, 5, 5, 5, 5]
    firstLen = 3
    secondLen = 2
    result = solution.maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print(result)  # Expected: ?
