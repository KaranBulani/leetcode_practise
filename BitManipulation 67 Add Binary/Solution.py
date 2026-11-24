"""
1. Problem Understanding

Given two binary strings a and b, return their sum as a binary string.
We need to perform binary addition just like normal decimal addition, but with base 2.

Binary addition rules:
| Addition  | Result | Carry |
| --------- | ------ | ----- |
| 0 + 0     | 0      | 0     |
| 0 + 1     | 1      | 0     |
| 1 + 0     | 1      | 0     |
| 1 + 1     | 0      | 1     |
| 1 + 1 + 1 | 1      | 1     |
The important part is handling the carry.

#########################################################################################################################################################
2. Approach

We can simulate addition from right to left.

Steps:

1. Initialize two pointers i and j at the last indices of strings a and b.
2. Initialize carry = 0.
3. While either string has remaining digits or carry is non-zero:
   - Extract the current digit from a, if available.
   - Extract the current digit from b, if available.
   - Calculate their sum along with carry.
   - The current binary digit is total % 2.
   - The new carry is total // 2.
   - Append the current digit to the result.
4. Reverse the result because we constructed it from right to left.

#########################################################################################################################################################
4. Dry Run

Input:
a = "1010"b = "1011"

We start adding from the rightmost digit.
| Step | a[i] | b[j] | Carry In | Total | Result Digit | Carry Out |
| ---- | ---- | ---- | -------- | ----- | ------------ | --------- |
| 1    | 0    | 1    | 0        | 1     | 1            | 0         |
| 2    | 1    | 1    | 0        | 2     | 0            | 1         |
| 3    | 0    | 0    | 1        | 1     | 1            | 0         |
| 4    | 1    | 1    | 0        | 2     | 0            | 1         |
| 5    | -    | -    | 1        | 1     | 1            | 0         |

We constructed the result from right to left:
1 -> 10 -> 101 -> 0101 -> 10101

Output: "10101"

#########################################################################################################################################################
5. Complexity Analysis

Let:

- n = length of string a
- m = length of string b

Time Complexity: O(max(n, m))

- We traverse both strings once.
- Each iteration performs constant-time operations.
- Reversing the result also takes O(max(n, m)).

Space Complexity: O(max(n, m))

- The result list stores at most max(n, m) + 1 digits.
- The additional result string also requires linear space.

#########################################################################################################################################################
6. Important Observations

1. We don't need to convert binary strings into decimal integers.
2. total % 2 gives the current binary digit.
3. total // 2 gives the carry.
4. We must include carry in the while-loop condition because the final addition can produce an extra digit.

Alternative Python shortcut:

Python supports arbitrary-precision integers and binary conversion:

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

However, the simulation approach is preferable for understanding binary addition and implementing it without integer conversion.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2
        return ''.join(result[::-1])

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from LeetCode
        ("11", "1", "100"),
        ("1010", "1011", "10101"),

        # Basic edge cases
        ("0", "0", "0"),
        ("0", "1", "1"),
        ("1", "0", "1"),
        ("1", "1", "10"),

        # Different string lengths
        ("1", "1111", "10000"),
        ("1111", "1", "10000"),
        ("101", "10", "111"),
        ("10", "101", "111"),

        # Carry propagation
        ("111", "1", "1000"),
        ("1111", "1111", "11110"),
        ("11111", "11111", "111110"),
        ("10111", "11001", "110000"),

        # No carry cases
        ("1000", "1", "1001"),
        ("10000", "10", "10010"),

        # Larger inputs
        ("11111111", "1", "100000000"),
        ("1111111111", "1111111111", "11111111110"),
        ("1010101010101010", "1010101010101010", "10101010101010100"),
    ]

    for a, b, expected in test_cases:
        result = solution.addBinary(a, b)

        status = "PASS" if result == expected else "FAIL"

        print(f"Input: a={a}, b={b}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print(f"Status:   {status}")
        print("-" * 50)