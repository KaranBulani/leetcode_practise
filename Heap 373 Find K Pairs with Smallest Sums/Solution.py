"""
1. Problem Understanding

We are given two integer arrays:
- nums1 sorted in non-decreasing order.
- nums2 sorted in non-decreasing order.
- An integer k.

We need to return k pairs (u, v) such that:
1. u comes from nums1.
2. v comes from nums2.
3. The sum u + v is as small as possible.

If fewer than k possible pairs exist, return all possible pairs.

Example
    nums1 = [1, 7, 11] nums2 = [2, 4, 6] k = 3

All possible pairs:
    (1, 2) = 3
    (1, 4) = 5
    (1, 6) = 7
    (7, 2) = 9
    (7, 4) = 11
    (7, 6) = 13
    (11, 2) = 13
    (11, 4) = 15
    (11, 6) = 17

The three smallest pairs are:
    [
        [1, 2],
        [1, 4],
        [1, 6]
    ]

#########################################################################################################################################################

2. Approach: Min Heap (Priority Queue)

The key observation is that BOTH arrays are sorted.
We can use this property to avoid generating every possible pair.
Think of the problem as a matrix.

For our example:

        nums2    2    4    6
    nums1
    1           3    5    7
    7           9   11   13
    11          13   15   17

Each cell represents:       nums1[i] + nums2[j]

Notice that:
- Every row is sorted from left to right.
- Every column is sorted from top to bottom.

Our goal is to extract the k smallest elements from this matrix.
We can accomplish this using a Min Heap.

#########################################################################################################################################################
3. Heap Initialization

Initially, insert the first element of each row into the heap.

In other words:    (nums1[0] + nums2[0], 0, 0)
                   (nums1[1] + nums2[0], 1, 0)
                   (nums1[2] + nums2[0], 2, 0)

For our example:
    Heap:
    (3, 0, 0)
    (9, 1, 0)
    (13, 2, 0)

Each heap entry contains:    (sum, i, j)

Where:
- sum = nums1[i] + nums2[j]
- i = index in nums1
- j = index in nums2

We insert at most min(k, len(nums1)) entries.
Why?
    Because we never need more than k pairs, and each row initially contributes only its smallest element.

#########################################################################################################################################################
4. Heap Processing

Now repeatedly extract the smallest element from the heap.

Whenever we extract (sum, i, j):

1. Add [nums1[i], nums2[j]] to our answer.
2. Move to the next column in the same row.
3. If another column exists, insert that pair into the heap.

In other words:
    (i, j)  ->  (i, j + 1)

Why only move right?
    Because each row is sorted.
    Once we have extracted the smallest available element from a row, the next smallest candidate from that row must be the element immediately to its right.
    We don't need to insert every element of every row in advance.

#########################################################################################################################################################
5. Dry Run

Input:
    nums1 = [1, 7, 11] nums2 = [2, 4, 6] k = 3

Initial heap:
    (3, 0, 0)
    (9, 1, 0)
    (13, 2, 0)

Iteration 1
    Pop the smallest:    (3, 0, 0)
    Pair:                [1, 2]
    Move right in the same row:        (1, 1) -> sum = 1 + 4 = 5
    Heap becomes:
        (5, 0, 1)
        (9, 1, 0)
        (13, 2, 0)
    Answer:            [[1, 2]]

Iteration 2
    Pop:        (5, 0, 1)
    Pair:        [1, 4]
    Move right:        (1, 2) -> sum = 1 + 6 = 7
    Heap becomes:
        (7, 0, 2)
        (9, 1, 0)
        (13, 2, 0)
    Answer:        [[1, 2], [1, 4]]

Iteration 3
    Pop:        (7, 0, 2)
    Pair:        [1, 6]
    There is no more element to the right in this row.
    Heap becomes:
        (9, 1, 0)
        (13, 2, 0)
    Answer:        [[1, 2], [1, 4], [1, 6]]

We have collected k = 3 pairs, so we stop.

#########################################################################################################################################################
7. Time Complexity Analysis

Let:
    m = len(nums1)
    n = len(nums2)

Heap Initialization
    We insert at most:    min(k, m) elements.
    Each insertion takes:    O(log(min(k, m)))
    Total initialization complexity:    O(min(k, m) * log(min(k, m)))

Heap Processing
    We extract at most k elements.
    Each extraction takes:        O(log(min(k, m)))
    We may also insert one new element after each extraction, which takes the same complexity.
    Therefore:        O(k * log(min(k, m)))

Overall Time Complexity
    Combining both:        O(min(k, m) * log(min(k, m)) + k * log(min(k, m)))
    Simplifying:        O(k * log(min(k, m)))

#########################################################################################################################################################
Space Complexity

The heap can contain at most:    min(k, m) elements.

Therefore:
- Auxiliary heap space: O(min(k, m))
- Output space: O(k)

Overall space including the returned result:    O(k + min(k, m)) = O(k)
Auxiliary space excluding the output:    O(min(k, m))

#########################################################################################################################################################
8. Important Observations

1. We don't generate all m * n possible pairs.
2. We maintain only one candidate from each row in the heap.
3. Once a pair is extracted, we insert the next element from that same row.
4. The sorted property of both arrays guarantees that moving right generates the next candidate in that row.
5. We initialize only min(k, m) rows because we cannot need more than k pairs.

Core pattern to remember:

This is a classic K-smallest-elements problem where we have multiple sorted lists.
We use a Min Heap to perform a K-way merge, similar to merging K sorted linked lists (LeetCode 23).

The important idea is that instead of inserting all elements into the heap, we maintain only the next available candidate from each sorted list.
"""
import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        if not nums1 or not nums2 or k == 0:
            return []

        heap = []

        # Initialize heap with the first element of each row
        for i in range(min(k, len(nums1))):
            heapq.heappush( heap, (nums1[i] + nums2[0], i, 0) )

        result = []

        while heap and len(result) < k:

            total, i, j = heapq.heappop(heap)

            # Add current pair to result
            result.append([nums1[i], nums2[j]])

            # Move to the next column in the same row
            if j + 1 < len(nums2):
                heapq.heappush( heap, (nums1[i] + nums2[j + 1], i, j + 1) )

        return result

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Example 0
    nums1 = [1,2,4,5,6]
    nums2 = [3,5,7,9]
    k = 3
    expected = [[1, 2], [1, 4], [1, 6]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 1:", result, "| Expected:", expected)

    # Test Case 1: Example 1
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    expected = [[1, 2], [1, 4], [1, 6]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 1:", result, "| Expected:", expected)


    # Test Case 2: Example 2 - Duplicate elements
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    k = 2
    expected = [[1, 1], [1, 1]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 2:", result, "| Expected:", expected)


    # Test Case 3: Single element in both arrays
    nums1 = [1]
    nums2 = [2]
    k = 1
    expected = [[1, 2]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 3:", result, "| Expected:", expected)


    # Test Case 4: Negative numbers
    nums1 = [-5, -2, 0]
    nums2 = [-4, -1, 3]
    k = 4
    expected = [[-5, -4], [-5, -1], [-2, -4], [-2, -1]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 4:", result, "| Expected:", expected)


    # Test Case 5: k equals total possible pairs
    nums1 = [1, 2]
    nums2 = [3, 4]
    k = 4
    expected = [[1, 3], [1, 4], [2, 3], [2, 4]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 5:", result, "| Expected:", expected)


    # Test Case 6: k greater than the length of nums1
    nums1 = [1, 2]
    nums2 = [3, 5, 7, 9]
    k = 5
    expected = [[1, 3], [1, 5], [2, 3], [1, 7], [2, 5]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 6:", result, "| Expected:", expected)


    # Test Case 7: All elements identical
    nums1 = [1, 1, 1]
    nums2 = [2, 2, 2]
    k = 5
    expected = [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 7:", result, "| Expected:", expected)


    # Test Case 8: Large negative and positive values
    nums1 = [-1000000000, 1000000000]
    nums2 = [-1000000000, 1000000000]
    k = 3
    expected = [
        [-1000000000, -1000000000],
        [-1000000000, 1000000000],
        [1000000000, -1000000000]
    ]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 8:", result, "| Expected:", expected)


    # Test Case 9: k = 1
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    k = 1
    expected = [[1, 2]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 9:", result, "| Expected:", expected)


    # Test Case 10: Unequal array sizes
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [10]
    k = 3
    expected = [[1, 10], [2, 10], [3, 10]]
    result = solution.kSmallestPairs(nums1, nums2, k)
    print("Test Case 10:", result, "| Expected:", expected)