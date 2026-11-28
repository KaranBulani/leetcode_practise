"""
Problem

Given an integer n, return the number of trailing zeroes in n!.

######################################################################################################################################################################
1. Key Observation

A trailing zero is created by multiplying 10.

We know:
    10 = 2 × 5

Therefore, every trailing zero requires one pair of factors (2, 5).

For example:
    10! = 3628800

There are two trailing zeroes.
Now, in factorials, factors of 2 are much more frequent than factors of 5.
Therefore, the number of trailing zeroes depends on how many factors of 5 exist in n!.

######################################################################################################################################################################
3. Dry Run

Let's take:
    n = 100

We repeatedly divide n by 5 and add the result.
| Iteration | n after division | Count |
| --------- | ---------------- | ----- |
| 1         | 100 // 5 = 20    | 20    |
| 2         | 20 // 5 = 4      | 24    |
| 3         | 4 // 5 = 0       | 24    |

Answer = 24
So, 100! has 24 trailing zeroes.

######################################################################################################################################################################
4. Why do we divide repeatedly by 5?

This is the most important part.

Consider 25!.
Multiples of 5 contribute at least one factor of 5: 5, 10, 15, 20, 25

But notice:
    25 = 5 * 5

25 contributes TWO factors of 5, not one.

Therefore:
- 25 // 5 = 5 counts the first factor of 5.
- 25 // 25 = 1 counts the additional factor of 5.

Total:
     5 + 1 = 6

Let's look at the general formula:     n // 5  +  n // 25  +  n // 125  + ....
We stop when the division produces zero.

######################################################################################################################################################################
5. Complexity Analysis

Time Complexity:     O(log_5 n)
We divide n by 5 in every iteration.

Space Complexity: O(1)
We only use one variable to maintain the count.

######################################################################################################################################################################
6. Alternative: Mathematical One-liner

You could also write:

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum(n // (5 ** i) for i in range(1, 100))

However, the while loop is preferable because it avoids unnecessary iterations.
Interview takeaway: Whenever you encounter trailing zeroes in factorial problems, think about counting factors of 5 rather than calculating the factorial itself.
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0

        while n > 0:
            n //= 5
            count += n

        return count

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples
        (0, 0),
        (1, 0),
        (3, 0),
        (5, 1),
        (10, 2),

        # Powers of 5
        (25, 6),
        (125, 31),
        (625, 156),

        # Values around multiples of 5
        (4, 0),
        (6, 1),
        (9, 1),
        (24, 4),
        (26, 6),
        (99, 22),
        (100, 24),
        (101, 24),

        # Larger values
        (500, 124),
        (1000, 249),
        (5000, 1249),
        (10000, 2499),
    ]

    for n, expected in test_cases:
        result = solution.trailingZeroes(n)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Input: n = {n:<6} | "
            f"Output: {result:<6} | "
            f"Expected: {expected:<6} | "
            f"{status}"
        )