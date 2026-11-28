"""
Problem: Given an integer x, return True if x is a palindrome, and False otherwise.
A palindrome reads the same forward and backward.

Examples:
    Input: x = 121
    Output: True

    Input: x = -121
    Output: False

    Input: x = 10
    Output: False

######################################################################################################################################################################
Approach 1: Convert to String (Simplest)

    class Solution:
        def isPalindrome(self, x: int) -> bool:
            s = str(x)
            return s == s[::-1]

Explanation:
- str(x) converts the integer into a string.
- s[::-1] reverses the string.
- Compare the original string with its reversed version.

Complexity:
- Time: O(log₁₀ x)
- Space: O(log₁₀ x)

######################################################################################################################################################################
Approach 2: Without Converting to String (Mathematical)

We can reverse the number mathematically using % and //.

    class Solution:
        def isPalindrome(self, x: int) -> bool:

            if x < 0:
                return False

            original = x
            reversed_num = 0

            while x > 0:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x //= 10

            return original == reversed_num

How it works:

Let's take x = 121.
| Iteration | x   | digit (x % 10) | reversed_num |
| --------- | --- | ---------------- | ------------ |
| 1         | 121 | 1                | 1            |
| 2         | 12  | 2                | 12           |
| 3         | 1   | 1                | 121          |

At the end:
    original = 121
    reversed_num = 121

    return original == reversed_num  # True

######################################################################################################################################################################
Approach 3: Optimized (Reverse Only Half)

Recommended
We don't need to reverse the entire number. We only need to reverse half of it.

Key idea:
For a palindrome, the first half and second half should match.

For example:
    x = 1221

    First half:  12
    Second half: 21

    Reverse second half: 12

    12 == 12 -> True


Implementation:

    class Solution:
        def isPalindrome(self, x: int) -> bool:

            if x < 0 or (x % 10 == 0 and x != 0):
                return False

            reversed_num = 0

            while x > reversed_num:
                digit = x % 10
                reversed_num = reversed_num * 10 + digit
                x //= 10

            return x == reversed_num or x == reversed_num // 10


Why do we need two conditions?

There are two cases:

1. Even number of digits: 1221

    x = 12
    reversed_num = 12
    x == reversed_num  -> True

2. Odd number of digits: 12321

    x = 12
    reversed_num = 123
    reversed_num // 10 = 12
    x == reversed_num // 10 -> True

We remove the middle digit because it doesn't affect palindrome symmetry.

######################################################################################################################################################################
Complexity Comparison

| Approach                   | Time     | Space    |
| -------------------------- | -------- | -------- |
| String conversion          | O(log x) | O(log x) |
| Full mathematical reversal | O(log x) | O(1)     |
| Half mathematical reversal | O(log x) | O(1)     |

For an integer x, the number of digits is: len(str(x))
So you can express the time complexity as:  O( len(str(x)) )

More precisely: O( log₁₀ |x|)

Because the number of decimal digits in a positive integer x is approximately O( log₁₀ (x)).
Both are equivalent ways of expressing the complexity.

For LeetCode explanations, O(log x) is the conventional notation, while O(len(str(x))) is more intuitive when reasoning about digit-based algorithms.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from LeetCode
        (121, True),
        (-121, False),
        (10, False),

        # Single-digit numbers
        (0, True),
        (1, True),
        (9, True),

        # Even and odd length palindromes
        (11, True),
        (1221, True),
        (12321, True),
        (123321, True),
        (123454321, True),

        # Non-palindromes
        (123, False),
        (1234, False),
        (12345, False),
        (123421, False),
        (1001, True),
        (100, False),

        # Negative numbers
        (-1, False),
        (-121, False),
        (-1221, False),

        # Numbers ending in zero
        (10, False),
        (100, False),
        (1000, False),
        (1010, False),

        # Large numbers / integer boundaries
        (2147447412, True),
        (2147483647, False),
        (-2147483648, False),
    ]

    for x, expected in test_cases:
        result = solution.isPalindrome(x)
        status = "PASS" if result == expected else "FAIL"

        print(
            f"Input: {x:12} | "
            f"Expected: {str(expected):5} | "
            f"Got: {str(result):5} | "
            f"{status}"
        )