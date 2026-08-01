'''
Intuition

The score is (sum of chosen nums1) * min(chosen nums2)

Notice that the minimum nums2 determines the multiplier.
Instead of trying to maximize both simultaneously, suppose we fix the minimum nums2.

Then the problem becomes:
> Among all elements whose nums2 is at least this minimum, choose the k largest nums1.
That is much easier.

####################################################################################################

Key Observation

Suppose
	nums1 = [1,3,3,2]
	nums2 = [2,1,3,4]
	k = 3

Create pairs.
	(2,1)
	(1,3)
	(3,3)
	(4,2)

where,
	(nums2, nums1)

Now sort by nums2 descending.
	(4,2)
	(3,3)
	(2,1)
	(1,3)

Look carefully.

When we're standing at (2,1)
every element above it has nums2 >= 2

Therefore,
if we choose this element as part of our answer,
the minimum nums2 must be exactly 2.

This is why each element acts as an anchor for the minimum.

####################################################################################################

What should we maximize?

Since the multiplier is fixed
	minimum = 2

we only need largest possible sum(nums1) from the current prefix.
That means:
	keep the k largest nums1 values.

A min-heap does exactly that.

####################################################################################################

Example Walkthrough

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]

pairs after sorting

(4,2)
(3,3)
(2,1)
(1,3)

Heap stores nums1.

Step 1
	pair = (4,2)
	heap = [2]
	sum = 2
	Need size 3.

Step 2
	pair = (3,3)
	heap = [2,3]
	sum = 5
	Need size 3.

Step 3
	pair = (2,1)
	heap = [1,3,2]
	sum = 6
	Heap size = k.

	Current minimum nums2 = 2.

	Score - 6 * 2 = 12
	Answer = 12.

Step 4
	pair = (1,3)
	push 3

	heap becomes [1,2,3,3]
	remove smallest
	remove 1

	heap [2,3,3]
	sum = 8
	Current minimum nums2 1
	Score 8 * 1 = 8
	Best remains 12

####################################################################################################

Why do we remove the smallest nums1?

Suppose heap currently has
	2
	5
	8
and new nums1 is 10

Keeping
	5
	8
	10
always gives a larger sum than
	2
	5
	8
Since multiplier is already fixed, larger sum is always better.
Therefore remove the smallest nums1.

####################################################################################################\

Correctness Proof

Let the current pair have nums2 = x

Corresponding nums1 value can either be added in heap due to being bigger or not added.

Not added:
* if not being added then current num1 smaller than smalles value of heap
* Also even though current pair's num1 isnt considered, we know num2 will be smaller
* so even if we consider num2 result will be smaller as num2 is smaller.

Added:
* As current pair has bigger num1 we make changes on heap and calculate.

####################################################################################################

Complexity

Sorting - O(n log n)
Each heap operation - O(log k)
Total - O(n log n)

Space - O(k)
'''
from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)

        heap = []
        curr_sum = 0
        answer = 0

        for num2, num1 in pairs:
            heapq.heappush(heap, num1)
            curr_sum += num1

            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)

            if len(heap) == k:
                answer = max(answer, curr_sum * num2)

        return answer

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ==========================
        # Examples from Question
        # ==========================
        {
            "nums1": [1, 3, 3, 2],
            "nums2": [2, 1, 3, 4],
            "k": 3,
            "expected": 12
        },
        {
            "nums1": [4, 2, 3, 1, 1],
            "nums2": [7, 5, 10, 9, 6],
            "k": 1,
            "expected": 30
        },

        # ==========================
        # Edge Cases
        # ==========================

        # Minimum input size
        {
            "nums1": [5],
            "nums2": [10],
            "k": 1,
            "expected": 50
        },

        # k == n
        {
            "nums1": [5, 2, 8],
            "nums2": [4, 7, 3],
            "k": 3,
            "expected": 45
        },

        # All nums1 are zero
        {
            "nums1": [0, 0, 0, 0],
            "nums2": [5, 4, 3, 2],
            "k": 2,
            "expected": 0
        },

        # All nums2 are zero
        {
            "nums1": [10, 20, 30],
            "nums2": [0, 0, 0],
            "k": 2,
            "expected": 0
        },

        # All values equal
        {
            "nums1": [5, 5, 5, 5],
            "nums2": [3, 3, 3, 3],
            "k": 2,
            "expected": 30
        },

        # Strictly increasing
        {
            "nums1": [1, 2, 3, 4, 5],
            "nums2": [1, 2, 3, 4, 5],
            "k": 2,
            "expected": 36
        },

        # Strictly decreasing
        {
            "nums1": [5, 4, 3, 2, 1],
            "nums2": [5, 4, 3, 2, 1],
            "k": 2,
            "expected": 36
        },

        # Large nums1 with small minimum nums2
        {
            "nums1": [100, 90, 80],
            "nums2": [1, 2, 3],
            "k": 2,
            "expected": 340
        },

        # Large minimum nums2 but smaller nums1
        {
            "nums1": [5, 4, 3],
            "nums2": [100, 90, 80],
            "k": 2,
            "expected": 810
        },

        # Duplicate nums2 values
        {
            "nums1": [2, 8, 6, 4],
            "nums2": [5, 5, 5, 5],
            "k": 3,
            "expected": 90
        },

        # Duplicate nums1 values
        {
            "nums1": [7, 7, 7, 7],
            "nums2": [1, 2, 3, 4],
            "k": 2,
            "expected": 42
        },

        # Choosing larger sum is not always optimal
        {
            "nums1": [10, 1, 1],
            "nums2": [1, 100, 100],
            "k": 2,
            "expected": 200
        },

        # Zeros mixed with positives
        {
            "nums1": [0, 10, 20],
            "nums2": [100, 2, 3],
            "k": 2,
            "expected": 60
        },

        # Larger k
        {
            "nums1": [8, 5, 9, 6, 2],
            "nums2": [4, 7, 5, 3, 9],
            "k": 4,
            "expected": 84
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        result = solution.maxScore(
            test["nums1"],
            test["nums2"],
            test["k"]
        )

        print(f"Test Case {idx}")
        print(f"nums1    = {test['nums1']}")
        print(f"nums2    = {test['nums2']}")
        print(f"k        = {test['k']}")
        print(f"Expected = {test['expected']}")
        print(f"Your Ans = {result}")
        print(f"Passed   = {result == test['expected']}")
        print("-" * 60)