'''
Explanation: https://leetcode.com/problems/longest-subarray-with-at-most-k-distinct-prime-factors/solutions/8477233/master-3-techniques-in-one-problem-begin-33j0/
####################################################################################################

Complexity Analysis

Let:
	n = nums.size()
	M = max(nums)
	L = sqrt(M)          -- the sieve bound
	d = maximum number of distinct prime factors of any single element

Stage									| Time												| Space
============================================================================================================
Sieve of Eratosthenes					| O(LloglogL)										| O(L)
Prime factorization (all elements)		| trial division up to √(each element) per element	| —
Sliding window							| O(n⋅d)												| O(n⋅d) for freq + factors

Overall:

O(LloglogL)+O(factorization)+O(n⋅d)
Here L = √M, so even for M = 10^9, L is only around 31,623 — sieving to that bound is essentially instant.

Space is dominated by the sieve (O(√M)) plus the per-element factor lists and the frequency map (O(n·d)):
O(√M)+O(n⋅d)
No integer can have an enormous number of distinct prime factors — d stays small, even numbers up to 10^9 have at most ~10 distinct primes — so this stays efficient in practice regardless of how large the individual values in nums get.
'''

class Solution:
    def getPrimes(self, n: int) -> list[int]:
        primes = []
        isPrime = [True] * (n + 1)
        if n >= 0:
            isPrime[0] = False
        if n >= 1:
            isPrime[1] = False

        for i in range(2, n + 1):
            if isPrime[i]:
                primes.append(i)
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False

        return primes

    def getFact(self, nums: list[int], primes: list[int]) -> dict[int: list[int]]:
        factors = dict()
        for n in nums:
            temp = n
            curr_factor = []
            for p in primes:
                if n % p == 0:
                    curr_factor.append(p)
                    while n % p == 0:
                        n = n // p
            if n > 1:
                curr_factor.append(n)
            factors[temp] = curr_factor
        return factors

    def longestSubarray(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        primes = self.getPrimes(int(max_num ** 0.5) + 1)
        factors = self.getFact(nums, primes)
        freq = {}
        left = 0

        window = 0
        for right in range(len(nums)):
            for facts in factors[nums[right]]:
                freq[facts] = freq.get(facts, 0) + 1

            if len(freq) <= k:
                window = max(window, right - left + 1)
            else:
                for facts in factors[nums[left]]:
                    freq[facts] -= 1
                    if freq[facts] == 0:
                        del freq[facts]
                left += 1

        return window

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [7, 6, 10, 12, 11]
    k = 3
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 3

    # Example 2
    nums = [4, 6, 9, 18]
    k = 4
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 4

    # Example 3
    nums = [6, 10, 15]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 1

    # Edge Case 1: Single element
    nums = [2]
    k = 1
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 1

    # Edge Case 2: All elements have the same prime factor
    nums = [2, 4, 8, 16, 32]
    k = 1
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 5

    # Edge Case 3: All elements share the same two prime factors
    nums = [6, 12, 18, 24, 30]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 5

    # Edge Case 4: Every element introduces a new prime factor
    nums = [2, 3, 5, 7, 11]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 2

    # Edge Case 5: k = 1, multiple different prime factors
    nums = [2, 4, 3, 8, 16]
    k = 1
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 2

    # Edge Case 6: Valid window is in the middle
    nums = [2, 3, 6, 10, 15, 7]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 2

    # Edge Case 7: One element contains multiple prime factors
    nums = [2 * 3 * 5, 2 * 3, 2]
    k = 3
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 3

    # Edge Case 8: k is larger than all possible distinct factors
    nums = [6, 10, 15, 21]
    k = 100
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 4

    # Edge Case 9: Alternating prime factors
    nums = [2, 3, 2, 3, 2, 3]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 6

    # Edge Case 10: Longest valid window requires shrinking from left
    nums = [2, 3, 5, 2, 3]
    k = 2
    result = solution.longestSubarray(nums, k)
    print(result)  # Expected: 3