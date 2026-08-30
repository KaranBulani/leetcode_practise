'''
####################################################################################################
Time complexity

Let:
* N = len(nums)
* Q = len(queries)
* B = √N

1. Sorting queries
We sort Q queries: queries.sort(...)
Therefore:
							O(Q . log Q)

2. add() and remove()
Each operation performs only dictionary operations:
	freq.get(...)
	freq[val] = ...
	del freq[val]
These are O(1) average case.

So:
			add = O(1)
			remove = O(1)

3. Movement of L

Queries are grouped by:			ql // B
Within a block, L moves at most B positions per query.

Therefore: O(QB)
Since:				B = √N

we get:				O(Q √N)

4. Movement of R

There are approximately:	N / B		blocks.
For each block, R can move across at most N positions.

Therefore, total R movement		O((N / B) . N)
								O(N^2 / B)

With:
						B = √N

we get:
						O(N^3/2)


5. Validity check

distinct == k and odd_count == 0

which is:
	O(1)


Total time complexity

Combining everything:
		O(Q . log Q) + O(Q . √N) + O(N^3/2)

Therefore:
				O(Q . log Q + Q . √N + N^3/2)

Since the constraints have:
				Q <= 10^5, N <= 10^5

and effectively Q = O(N), this becomes:
				O(N . log N + N^3/2 + N^3/2)

Hence:
			O(N^3/2)
for the given constraint relationship.

Space complexity

We have:

freq
	At most N different values:						O(N)

queries
	We create:	(ql, qr, original_index)
	for every query:		O(Q)

ans
	One boolean per query: O(Q)

Therefore:
				O(N+Q)

Since Q = O(N) under these constraints:				O(N)

## Final complexity

| Component         |                 Complexity |
| ----------------- | -------------------------  |
| Sort queries      |               O(Q log Q)   |
| Move L            |                   O(Q√N)   |
| Move R            |                   O(N√N)   |
| Validity check    |                     O(Q)   |
| Total             | O(Q log Q + Q√N + N√N)     |
| With Q = O(N)     |                 O(N√N)     |
| Space             |    O(N + Q) → O(N)         |
'''
import math

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:

        n = len(nums)
        BLOCK_SIZE = int(math.sqrt(n))

        # Keep original query index because we sort the queries
        queries = [
            (ql, qr, i)
            for i, (ql, qr) in enumerate(queries)
        ]

        # Mo's ordering
        queries.sort(
            key=lambda x: (
                x[0] // BLOCK_SIZE,
                x[1]
            )
        )

        # Current window = [L, R]
        L = 0
        R = -1

        freq = {}
        distinct = 0
        odd_count = 0

        def add(idx: int):
            nonlocal distinct, odd_count

            val = nums[idx]
            old_freq = freq.get(val, 0)

            # 0 -> 1: new distinct value
            if old_freq == 0:
                distinct += 1

            # Even -> Odd
            # Odd -> Even
            if old_freq % 2 == 0:
                odd_count += 1
            else:
                odd_count -= 1

            freq[val] = old_freq + 1

        def remove(idx: int):
            nonlocal distinct, odd_count

            val = nums[idx]
            old_freq = freq[val]

            # Odd -> Even
            # Even -> Odd
            if old_freq % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

            new_freq = old_freq - 1

            if new_freq == 0:
                distinct -= 1
                del freq[val]
            else:
                freq[val] = new_freq

        ans = [False] * len(queries)

        for ql, qr, query_idx in queries:

            # Expand right
            while R < qr:
                R += 1
                add(R)

            # Shrink left
            while L < ql:
                remove(L)
                L += 1

            # Shrink right
            while R > qr:
                remove(R)
                R -= 1

            # Expand left
            while L > ql:
                L -= 1
                add(L)

            # O(1) validity check
            ans[query_idx] = (
                distinct == k and
                odd_count == 0
            )

        return ans

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 2, 1]
    k = 2
    queries = [[0, 1], [0, 3], [1, 2]]
    expected = [False, True, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 1:", result)
    print("Expected:", expected)
    print()

    # Example 2
    nums = [3, 3, 3]
    k = 1
    queries = [[1, 2], [0, 2]]
    expected = [True, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 2:", result)
    print("Expected:", expected)
    print()

    # All elements are unique
    nums = [1, 2, 3, 4]
    k = 2
    queries = [
        [0, 1],
        [0, 2],
        [1, 3],
        [0, 3]
    ]
    expected = [False, False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 3:", result)
    print("Expected:", expected)
    print()

    # Same element repeated
    nums = [5, 5, 5, 5]
    k = 1
    queries = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
        [1, 3],
        [2, 3]
    ]
    expected = [True, False, True, True, False, True]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 4:", result)
    print("Expected:", expected)
    print()

    # Exactly k distinct, all frequencies even
    nums = [1, 1, 2, 2, 3, 3]
    k = 3
    queries = [
        [0, 5],
        [0, 3],
        [2, 5],
        [0, 1],
        [1, 4]
    ]
    expected = [True, False, False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 5:", result)
    print("Expected:", expected)
    print()

    # More than k distinct
    nums = [1, 1, 2, 2, 3, 3]
    k = 2
    queries = [
        [0, 3],
        [0, 5],
        [1, 4],
        [2, 5]
    ]
    expected = [True, False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 6:", result)
    print("Expected:", expected)
    print()

    # Frequencies are even, but number of distinct elements is wrong
    nums = [1, 1, 2, 2]
    k = 1
    queries = [
        [0, 1],
        [2, 3],
        [0, 3]
    ]
    expected = [True, True, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 7:", result)
    print("Expected:", expected)
    print()

    # Overlapping queries
    nums = [1, 2, 1, 2, 3, 3]
    k = 2
    queries = [
        [0, 3],
        [1, 4],
        [2, 5],
        [0, 5],
        [0, 2]
    ]
    expected = [True, False, False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 8:", result)
    print()

    # Same query repeated
    nums = [1, 1, 2, 2]
    k = 2
    queries = [
        [0, 3],
        [0, 3],
        [0, 3],
        [1, 2]
    ]
    expected = [True, True, True, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 9:", result)
    print("Expected:", expected)
    print()

    # k = n
    nums = [1, 2, 3, 4]
    k = 4
    queries = [
        [0, 3],
        [0, 2],
        [1, 3]
    ]
    expected = [False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 10:", result)
    print("Expected:", expected)
    print()

    # Large frequency combinations
    nums = [1, 1, 1, 1, 2, 2, 2, 2]
    k = 2
    queries = [
        [0, 7],
        [0, 3],
        [4, 7],
        [0, 5],
        [2, 7]
    ]
    expected = [True, False, False, False, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 11:", result)
    print("Expected:", expected)
    print()

    # Alternating elements
    nums = [1, 2, 1, 2, 1, 2]
    k = 2
    queries = [
        [0, 1],
        [0, 3],
        [0, 5],
        [1, 4],
        [2, 5]
    ]
    expected = [False, True, False, True, True]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 12:", result)
    print("Expected:", expected)
    print()

    # Different values but identical frequency patterns
    nums = [10, 20, 10, 20, 30, 30]
    k = 3
    queries = [
        [0, 5],
        [0, 3],
        [2, 5],
        [1, 4]
    ]
    expected = [True, True, True, False]

    result = solution.validSubarrays(nums, k, queries)
    print("Test 13:", result)
    print("Expected:", expected)
    print()