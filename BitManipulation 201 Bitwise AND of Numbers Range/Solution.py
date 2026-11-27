"""
######################################################################################################################################################################
Approach 1: Common Prefix (Optimal)
######################################################################################################################################################################
Intuition

We are given two integers left and right.
We need to calculate the bitwise AND of every integer in the range [left, right].

Key observation:
When we perform bitwise AND on all numbers in a range, the bits that differ between left and right will eventually become 0.

Only the common binary prefix of left and right survives.

######################################################################################################################################################################
Example 1

left = 5 right = 7

Binary representations:
    5 = 101
    6 = 110
    7 = 111

Perform bitwise AND:
  101
& 110
-----
  100

Now:
  100
& 111
-----
  100

Output:     4

Notice that the common prefix of 101 and 111 is 1.
The remaining bits are different, so they become zero.

######################################################################################################################################################################
Understanding the code

1. Initialize shift
    shift = 0
We keep track of how many positions we shift the numbers to the right.

2. Find the common binary prefix

while left != right:
    left >>= 1
    right >>= 1
    shift += 1

We repeatedly remove the rightmost bit from both numbers until they become equal.

Let's dry run:
left = 5
right = 7

| Iteration | left (binary) | right (binary) | shift |
| --------- | ------------- | -------------- | ----- |
| Initial   | 101           | 111            | 0     |
| 1         | 10            | 11             | 1     |
| 2         | 1             | 1              | 2     |
Now left == right, so the loop stops.

3. Restore the common prefix

return left << shift

We shifted both numbers right twice, so we shift the common prefix back to the left twice.

left = 1
1 << 2

Binary: 100
Decimal: 4

Answer: 4

######################################################################################################################################################################
Approach 2: Brian Kernighan's Algorithm

Another interesting approach uses this bit manipulation trick: n = n & (n - 1)
This removes the rightmost set bit (rightmost 1) from a number.

######################################################################################################################################################################
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        while left < right:
            right = right & (right - 1)

        return right

######################################################################################################################################################################
Intuition

We repeatedly remove the rightmost set bit from right until right becomes less than or equal to left.
Every removed bit corresponds to a bit position that cannot remain set in the AND of the entire range.

######################################################################################################################################################################
Example


left = 5
right = 7


Initially:
left  = 101
right = 111


Iteration 1:  right = 7 & 6

  111
& 110
-----
  110

Now right = 6.

Iteration 2:

right = 6 & 5

  110
& 101
-----
  100

Now right = 4.
Since left = 5 and right = 4, the condition left < right becomes false.

Return 4.

######################################################################################################################################################################
Complexity Analysis

Let N be the larger of left and right.

| Complexity | Approach 1 | Approach 2 |
| ---------- | ---------- | ---------- |
| Time       | O(log N)   | O(log N)   |
| Space      | O(1)       | O(1)       |

Both approaches are optimal in terms of asymptotic time complexity.
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Original examples
        (5, 7, 4),
        (0, 0, 0),
        (1, 2147483647, 0),

        # Single-element ranges
        (5, 5, 5),
        (10, 10, 10),
        (0, 1, 0),

        # Small ranges
        (0, 5, 0),
        (1, 3, 0),
        (4, 7, 4),
        (8, 15, 8),

        # Powers of 2 and their boundaries
        (7, 8, 0),
        (8, 9, 8),
        (15, 16, 0),
        (16, 31, 16),
        (31, 32, 0),
        (32, 63, 32),

        # Ranges with common binary prefixes
        (26, 30, 24),
        (12, 15, 12),
        (17, 19, 16),
        (20, 25, 16),

        # Larger ranges
        (100, 200, 0),
        (100, 127, 96),
        (120, 127, 120),
        (200, 255, 192),
        (255, 256, 0),

        # Near maximum constraint
        (2147483646, 2147483647, 2147483646),
        (1073741824, 2147483647, 1073741824),
    ]

    for left, right, expected in test_cases:
        result = solution.rangeBitwiseAnd(left, right)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Input: left={left}, right={right} | "
            f"Output: {result} | "
            f"Expected: {expected} | "
            f"{status}"
        )