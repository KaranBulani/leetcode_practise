"""
1. Problem Statement

Reverse the bits of a given 32-bit unsigned integer.
Given an integer n, reverse its 32 bits and return the resulting integer.

Example 1:
    Input: n = 43261596
    Output: 964176192

Binary representation:
Original:  00000010100101000001111010011100
Reversed:  00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822

######################################################################################################################################################################
2. Approach 1: Bit Manipulation (Optimal)

The idea is to extract bits from the original number one by one and construct the reversed number.

We use two operations:
1. n & 1: Extract the last bit of n.
2. n >> 1: Remove the last bit from n.

To construct the reversed number:
1. Shift the result left by 1 position.
2. Extract the last bit of n.
3. Add that bit to the result.
4. Repeat 32 times.

######################################################################################################################################################################
3. Dry Run

Consider:
n = 13

Binary representation (using 4 bits for illustration): 1101
Reversed: 1011

Let's understand the operations:
| Iteration | Extracted bit | Result (binary) |
| --------- | ------------- | --------------- |
| 1         | 1             | 1               |
| 2         | 0             | 10              |
| 3         | 1             | 101             |
| 4         | 1             | 1011            |

Final result:
    Binary: 1011
    Decimal: 11

For the actual LeetCode problem, we perform exactly 32 iterations, not 4.

######################################################################################################################################################################
4. Understanding the Bitwise Operations

A. Left shift (<<)

    result = 5       # 0101
    result <<= 1

    Result:
    1010 = 10

    Shifting left by one position effectively multiplies the number by 2.

B. Bitwise AND (&)

    n = 13           # 1101
    n & 1

    1101
    & 0001
    ------
    0001

    Result: 1
    This extracts the least significant bit.

C. Right shift (>>)

    n = 13           # 1101
    n >>= 1

    Result:
    110

    This removes the last bit.

D. Bitwise OR (|)

    result = 4       # 100
    bit = 1          # 001
    result |= bit

    100 | 001
    -----
    101

    Result: 5

######################################################################################################################################################################
5. Complexity Analysis

Let B = 32 (fixed number of bits).

| Complexity | Value | Explanation                         |
| ---------- | ----- | ----------------------------------- |
| Time       | O(1)  | Exactly 32 iterations               |
| Space      | O(1)  | Only a constant number of variables |

Technically, the time complexity is O(B), but since B is always 32, it is O(1).

######################################################################################################################################################################
6. Alternative Approach: Binary String

Python provides convenient string formatting and conversion functions.

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = f"{n:032b}"
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)

Explanation:
- f"{n:032b}": Converts the number into a 32-bit binary string, padding with leading zeros.
- [::-1]: Reverses the string.
- int(reversed_binary, 2): Converts the reversed binary string back into a decimal integer.

Complexity:
- Time: O(32) = O(1)
- Space: O(32) = O(1)

This is Pythonic, but the bit manipulation approach is more useful for understanding how bits work.

######################################################################################################################################################################
7. Key Takeaways

Remember these operations for future bit manipulation problems:
| Operation        | Purpose                          |
| ---------------- | -------------------------------- |
|  n & 1           | Extract last bit                 |
|  n >> 1          | Remove last bit                  |
|  result << 1     | Shift result left                |
|  result | bit   | Append a bit                      |

    result = 5       # Binary: 0101
    bit = 1          # Binary: 0001
    result = result | bit
    print(result)    # 5

|  f"{n:032b}"     | Convert to 32-bit binary string  |
|  int(binary, 2)  | Convert binary string to integer |

My recommendation: Use Approach 1 for LeetCode. It builds a strong foundation for bit manipulation problems such as Single Number, Counting Bits, Number of 1 Bits, and Reverse Integer.
"""
class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0
        for _ in range(32):
            # Shift result left to make room for next bit
            result <<= 1

            # Extract last bit of n and add it to result
            result |= (n & 1)

            # Remove last bit from n
            n >>= 1
        return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from LeetCode
        (43261596, 964176192),
        (2147483644, 1073741822),

        # Edge cases
        (0, 0),
        (1, 2147483648),
        (2, 1073741824),
        (2147483646, 2147483646),

        # Additional test cases
        (3, 3221225472),
        (4, 536870912),
        (8, 268435456),
        (16, 134217728),
        (255, 4278190080),
        (256, 8388608),
        (65535, 4294901760),
        (65536, 65536),
        (1073741824, 2),
    ]

    for n, expected in test_cases:
        result = solution.reverseBits(n)

        print(f"Input:    {n}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print(f"Correct:  {result == expected}")
        print("-" * 40)