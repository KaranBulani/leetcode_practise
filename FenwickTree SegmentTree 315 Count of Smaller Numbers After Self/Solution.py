'''
####################################################################################################
                                            Binary Search
####################################################################################################
Core Idea
* Traverse from right → left.
* Maintain a sorted structure of numbers already seen.
* For current number:
    * find insertion index using binary search
    * insertion index = count of smaller numbers

nums = [5,2,6,1]
| num | sorted list | insertion idx | answer |
| --- | ----------- | ------------- | ------ |
| 1   | []          | 0             | 0      |
| 6   | [1]         | 1             | 1      |
| 2   | [1,6]       | 1             | 1      |
| 5   | [1,2,6]     | 2             | 2      |
Result: [2,1,1,0]

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_arr = []
        ans = []

        def lower_bound(target):
            low = 0
            high = len(sorted_arr)
            while low < high:
                mid = (low + high) // 2
                if sorted_arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        for num in reversed(nums):
            idx = lower_bound(num)
            ans.append(idx)
            sorted_arr.insert(idx, num)

        return ans[::-1]

Binary search is fast, but insertion in list is costly.
Time:
    search = O(logn)
    insertion = O(n)
    total = O(n^2)
Space: O(n)

####################################################################################################
                                            Segment Tree
####################################################################################################
Core Idea

Process from: right -> left
For every number:
1. Find how many smaller numbers already appeared
2. Insert current number into Segment Tree

Why Coordinate Compression?
    Values can be: -10^4 to 10^4

Segment Tree works best on compact indices.
So: nums = [5,2,6,1]
Unique sorted values: [1,2,5,6]

Ranks:
	1 -> 0
	2 -> 1
	5 -> 2
	6 -> 3

Segment Tree Operations

We need:
	1. Update
	Insert current number. update(index, +1)

	2. Query
	Count numbers smaller than current. query(0, rank - 1)

Code
from typing import List

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, node, left, right, index):
        # leaf node
        if left == right:
            self.tree[node] += 1
            return

        mid = (left + right) // 2
        if index <= mid:
            self.update(2 * node, left, mid, index)
        else:
            self.update(2 * node + 1, mid + 1, right, index)

        self.tree[node] = (
            self.tree[2 * node] +
            self.tree[2 * node + 1]
        )

    def query(self, node, left, right, ql, qr):
        # completely outside
        if qr < left or right < ql:
            return 0

        # completely inside
        if ql <= left and right <= qr:
            return self.tree[node]

        mid = (left + right) // 2

        return (
            self.query(2 * node, left, mid, ql, qr) +
            self.query(2 * node + 1, mid + 1, right, ql, qr)
        )

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = {
            num: i
            for i, num in enumerate(sorted(set(nums)))
        }
        size = len(ranks)
        seg_tree = SegmentTree(size)
        ans = []

        for num in reversed(nums):

            rank = ranks[num]

            # count smaller elements
            if rank == 0:
                ans.append(0)
            else:
                ans.append(
                    seg_tree.query(
                        1,              # node, curr_node, parent
                        0,              # left, left_end_range
                        size - 1,       # right, right_end_range
                        0,              # query left
                        rank - 1        # query right
                    )
                )

            # insert current number
            seg_tree.update(
                1,                      # node, curr_node, parent
                0,                      # left, left_end_range
                size - 1,               # right, right_end_range
                rank                    # at what rank should addition take place
            )

        return ans[::-1]

Dry Run
nums = [5,2,6,1]
Compressed:
	1->0
	2->1
	5->2
	6->3

Process right → left:
| num | query smaller | update   |
| --- | ------------- | -------- |
| 1   | 0             | insert 1 |
| 6   | 1             | insert 6 |
| 2   | 1             | insert 2 |
| 5   | 2             | insert 5 |

Answer: [2,1,1,0]

Complexity

Each:
* update = O(log n)
* query = O(log n)

Total:
* Time = O(n * log n)
* Space = O(n)

BIT vs Segment Tree
| Feature              | BIT         | Segment Tree |
| -------------------- | ----------- | ------------ |
| Easier               | ✅          | ❌           |
| Memory               | Less        | More         |
| Flexible             | Less        | More         |
| Range Queries        | Prefix only | Any range    |
| Interview Popularity | Very High   | High         |

####################################################################################################
                                            Fenwick Tree
####################################################################################################
Core Idea

We process from right → left.
For each number:
* ask: how many numbers smaller than current already seen?

BIT efficiently supports:
* prefix sum
* updates

Problem - Numbers can be negative: -10^4 <= nums[i] <= 10^4

BIT indices must be positive.
So we use: Coordinate Compression

Example:
nums = [5,2,6,1]
Sorted unique: [1,2,5,6]

Mapping:
1 -> 1
2 -> 2
5 -> 3
6 -> 4

BIT Operations
    Query - Count numbers smaller than current: query(rank - 1)
    Update - Insert current number: update(rank, 1)

Complexity
* Time: O(n * log n)
* Space: O(n)

####################################################################################################

Why set(nums)?
We only care about distinct values when assigning ranks.

Example:
nums = [5, 2, 6, 1, 2, 5]

If we do: sorted(nums)
we get: [1, 2, 2, 5, 5, 6]
Now what rank should 2 get?
* position 1?
* position 2?

Duplicates create ambiguity.

Instead: sorted(set(nums))
gives: [1, 2, 5, 6]

Now ranks are unique:
1 -> 1
2 -> 2
5 -> 3
6 -> 4

What goes wrong without set?

Suppose: nums = [2, 2, 2]
If you build ranks using: sorted(nums) # [2, 2, 2]
and then:
ranks = {
    num: i + 1
    for i, num in enumerate(sorted(nums))
}

you get: {2: 3} because dictionary keys overwrite previous entries.
You wasted space and the rank assignment becomes unintuitive.

Using set:
sorted(set(nums))
# [2]
gives: {2: 1}
which is exactly what we want.

'''
from typing import List

class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index # like get next

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index # like get parent
        return total

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = {
            num: i + 1
            for i, num in enumerate(sorted(set(nums))) # reason for using set mentioned above in notes
        }

        bit = BIT(len(ranks))
        ans = []

        for num in reversed(nums):
            rank = ranks[num]
            ans.append(bit.query(rank - 1))
            bit.update(rank, 1)
        return ans[::-1]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example cases
        {
            "nums": [5, 2, 6, 1],
            "expected": [2, 1, 1, 0]
        },
        {
            "nums": [-1],
            "expected": [0]
        },
        {
            "nums": [-1, -1],
            "expected": [0, 0]
        },

        # Edge cases
        {
            "nums": [1, 2, 3, 4, 5],  # strictly increasing
            "expected": [0, 0, 0, 0, 0]
        },
        {
            "nums": [5, 4, 3, 2, 1],  # strictly decreasing
            "expected": [4, 3, 2, 1, 0]
        },
        {
            "nums": [2, 2, 2, 2],  # all duplicates
            "expected": [0, 0, 0, 0]
        },
        {
            "nums": [1, 0, 2],  # small mixed
            "expected": [1, 0, 0]
        },
        {
            "nums": [3, 2, 2, 6, 1],
            "expected": [3, 1, 1, 1, 0]
        },
        {
            "nums": [10, 9, 8, 7],
            "expected": [3, 2, 1, 0]
        },
        {
            "nums": [1, 9, 7, 8, 5],
            "expected": [0, 3, 1, 1, 0]
        },
        {
            "nums": [-1, -2, -3, -4],
            "expected": [3, 2, 1, 0]
        },
        {
            "nums": [-4, -3, -2, -1],
            "expected": [0, 0, 0, 0]
        },
        {
            "nums": [0, 0, -1, 0],
            "expected": [1, 1, 0, 0]
        },
        {
            "nums": [10000, -10000],
            "expected": [1, 0]
        },
        {
            "nums": [4, 1, 2, 3],
            "expected": [3, 0, 0, 0]
        },
        {
            "nums": [7],
            "expected": [0]
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        nums = test["nums"]
        expected = test["expected"]

        result = solution.countSmaller(nums)

        print(f"Test Case {idx}")
        print(f"Input     : {nums}")
        print(f"Expected  : {expected}")
        print(f"Your Output: {result}")
        print(f"Passed    : {result == expected}")
        print("-" * 50)