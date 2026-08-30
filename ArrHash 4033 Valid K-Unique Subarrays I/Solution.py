'''
####################################################################################################
'''
import math

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        BLOCK_SIZE = int(math.sqrt(n))

        queries = [
            (ql, qr, i)
            for i, (ql, qr) in enumerate(queries)
        ]

        queries.sort(
            key=lambda x: (
                x[0] // BLOCK_SIZE,
                x[1]
            )
        )

        L = 0
        R = -1

        freq = {}
        distinct = 0
        def add(idx: int):
            nonlocal distinct
            val = nums[idx]

            if freq.get(val, 0) == 0:
                distinct += 1
            freq[val] = freq.get(val, 0) + 1

        def remove(idx: int):
            nonlocal distinct
            val = nums[idx]

            freq[val] -= 1
            if freq[val] == 0:
                distinct -= 1
                del freq[val]

        ans = [False] * len(queries)

        for ql, qr, query_idx in queries:

            while R < qr:
                R += 1
                add(R)

            while L < ql:
                remove(L)
                L += 1

            while R > qr:
                remove(R)
                R -= 1

            while L > ql:
                L -= 1
                add(L)

            dist_bool = distinct == k
            even_bool = all(v % 2 == 0 for v in freq.values())
            ans[query_idx] = dist_bool and even_bool

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