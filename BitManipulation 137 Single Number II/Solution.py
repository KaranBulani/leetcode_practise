"""
1. Problem Statement

Given an integer array nums where every element appears three times except for one element, which appears exactly once, find the single element and return it.
You must implement a solution with:
- Linear runtime complexity: O(n)
- Constant extra space: O(1)

Example 1:
    Input: nums = [2, 2, 3, 2]
    Output: 3

Example 2:
    Input: nums = [0, 1, 0, 1, 0, 1, 99]
    Output: 99

######################################################################################################################################################################
2. Approach: Bit Manipulation (Bit Counting)

The key observation is:
    Every number appears exactly 3 times, except one number that appears once.
    If we examine each bit position independently, the bits contributed by numbers appearing three times will have a count divisible by 3.

Therefore:

1. Iterate through all 32 bit positions.
2. Count how many numbers have a 1 at each bit position.
3. Take the count modulo 3.
4. If the remainder is 1, that bit belongs to the unique number.
5. Reconstruct the answer using those bits.

Example walkthrough

Consider:
nums = [2, 2, 3, 2]

Binary representation (4 bits for simplicity):
    2 = 0010
    2 = 0010
    3 = 0011
    2 = 0010
    --------------
        0033

Count the number of set bits at each position:
    | Bit position | Number of 1s | Modulo 3 |
    | ------------ | ------------ | -------- |
    | 3            | 0            | 0        |
    | 2            | 0            | 0        |
    | 1            | 4            | 1        |
    | 0            | 1            | 1        |

The resulting bits are:    0011 = 3
Hence, the answer is 3.

######################################################################################################################################################################
4. Understanding the important operations

A. Right shift (>>)

    num >> i                        - Shifts the binary representation of num to the right by i positions.

    Example:
        num = 10         # Binary: 1010
        print(num >> 1)  # 5  -> 0101
        print(num >> 2)  # 2  -> 0010

B. Bitwise AND (&)

    (num >> i) & 1                  - Extracts the bit at position i.

    Example:
        num = 10               # 1010
        print((num >> 0) & 1)  # 0
        print((num >> 1) & 1)  # 1
        print((num >> 2) & 1)  # 0
        print((num >> 3) & 1)  # 1

C. Left shift (<<)

    1 << i                          - Creates a number with only the bit at position i set to 1.

    1 << 0  # 0001
    1 << 1  # 0010
    1 << 2  # 0100
    1 << 3  # 1000

D. Bitwise OR (|=)

    result |= (1 << i)              - Sets the bit at position i in result to 1 without changing its other bits.

    Example:
        result = 0  # 0000
        result |= (1 << 1)              # result = 0010
        result |= (1 << 0)              # result = 0011

######################################################################################################################################################################
5. Complexity Analysis

Let n be the number of elements.

| Operation               | Complexity  |
| ----------------------- | ----------- |
| Outer loop (32 bits)    |  O(32)      |
| Inner loop (n elements) |  O(n)       |
| Reconstruct result      |  O(32)      |

Total time complexity:           O(32 × n) = O(n)
Space complexity:                O(1)

We only use a fixed number of variables, regardless of input size.

######################################################################################################################################################################
6. Alternative: State Machine (Advanced Bit Manipulation)

There is another elegant solution using two variables: ones and twos.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones

How does it work?

    For every bit position, we maintain a counter with three possible states:
    | Number of occurrences |  twos  |  ones  |
    | --------------------- | ------ | ------ |
    | 0                     | 0      | 0      |
    | 1                     | 0      | 1      |
    | 2                     | 1      | 0      |
    | 3                     | 0      | 0      |

    The two variables represent a counter modulo 3.
    - ones stores bits that have appeared once.
    - twos stores bits that have appeared twice.
    - When a bit appears for the third time, both states reset to zero.

At the end, ones contains the unique number.

    Complexity:
    - Time: (O(n))
    - Space: (O(1))

######################################################################################################################################################################
7. Which approach should you remember?

| Criteria              | Bit Counting | State Machine     |
| --------------------- | ------------ | ----------------- |
| Time                  |   O(n)       |   O(n)            |
| Space                 |   O(1)       |   O(1)            |
| Easy to understand    | Yes          | Requires practice |
| Interview explanation | Easier       | More advanced     |
| Number of passes      | 32 passes    | 1 pass            |

My recommendation: Understand and remember the bit-counting approach first. Then learn the state-machine approach because it is a beautiful application of bit manipulation and finite-state logic.
One important distinction: Python supports arbitrary-precision integers, whereas this problem's bit-counting implementation explicitly reconstructs a 32-bit signed integer. The negative-number conversion is therefore important.

######################################################################################################################################################################
######################################################################################################################################################################
1. How are negative integers represented in 32 bits?

A signed 32-bit integer has the following range:        -2^{31}  to  2^{31} - 1

In binary, the most significant bit (bit 31) determines whether the number is negative or positive.
- MSB = 0 → Positive number
- MSB = 1 → Negative number

For example:

| Integer | 32-bit binary                      |
| ------- | ---------------------------------- |
| 3       |  00000000000000000000000000000011  |
| -3      |  11111111111111111111111111111101  |

Negative numbers use Two's Complement representation.

######################################################################################################################################################################
2. What is the problem with Python?

Python integers have arbitrary precision. Unlike C++ or Java's int, Python integers are not restricted to 32 bits.

Let's consider this example:
    result = 4294967293
    print(result)

Output:                     4294967293

But suppose these 32 bits represent a signed integer:               11111111111111111111111111111101

In 32-bit Two's Complement, this represents -3, not 4294967293.
Python doesn't automatically interpret that bit pattern as a signed 32-bit integer.
We need to convert it ourselves.

######################################################################################################################################################################
how does python know if 11111111111111111111111111111101 is -3 or 4294967293

Python does not know that 11111111111111111111111111111101 represents -3. It depends on how you interpret those bits. The same 32 bits can represent two different numbers.

1. Same binary, two interpretations
Consider:       11111111111111111111111111111101

If interpreted as an unsigned 32-bit integer :   2^{32}-3 = 4294967293
If interpreted as a signed 32-bit integer (Two's Complement) :   -3
Both are correct interpretations of the same bit pattern.

2. How does Python interpret it?
Python doesn't have unsigned or signed 32-bit integer types by default.
For example:
    x = 4294967293
    print(x)
    print(bin(x))

Output:
    4294967293
    0b11111111111111111111111111111101

Python considers this a positive integer because you assigned it a positive integer value.
It does not look at the MSB and automatically decide that the number is negative.

3. What about negative numbers in Python?
If you explicitly assign:
    x = -3
    print(x)
    print(bin(x))

Output:
    -3
    -0b11

Notice something interesting!
Python doesn't display the 32-bit Two's Complement representation here.
That's because Python integers conceptually behave as though they have an unlimited number of sign bits.
For negative numbers, bitwise operations behave as though the number has infinitely many leading 1s.

For example:
    print(-3 >> 1)

Output: -2

4. How do we convert between interpretations?
Python provides a simple way to understand this:

    result = 4294967293
    # Convert unsigned 32-bit to signed 32-bit
    if result >= (1 << 31):
        result -= (1 << 32)
    print(result)

Output:   -3
We explicitly tell Python how to interpret the bit pattern.

 5. Compare Python with C++
| Feature                                  | Python  int     | C++  int32_t  |
| ---------------------------------------- | --------------- | ------------- |
| Fixed 32-bit width                       | No              | Yes           |
| Arbitrary precision                      | Yes             | No            |
| Automatically interprets MSB as sign bit | No              | Yes           |
| Two's Complement representation          | Not fixed-width | Yes           |

The most important takeaway for LeetCode 137:
When reconstructing a number using 32 bits, you are initially constructing an unsigned value between: 0  and  2^{32}-1
But the problem expects a signed 32-bit integer.
Therefore, you manually convert values whose MSB is 1 by subtracting  2^{32} .
That's why we need those two lines of code.

######################################################################################################################################################################
3. Understanding the conversion

Our code:
    if result >= (1 << 31):
        result -= (1 << 32)

Let's break it down.

First condition:
    result >= (1 << 31)

Since:     1 << 31 = 2^{31} = 2147483648

If result is greater than or equal to 2147483648, its 32nd bit (MSB) is set.
That means the number represents a negative integer in signed 32-bit representation.

Second operation:
    result -= (1 << 32)

Since:      1 << 32 = 2^{32} = 4294967296

We subtract 2^{32} to convert the unsigned representation into its signed equivalent.

######################################################################################################################################################################
4. Let's take an actual example

Suppose:
    result = 4294967293


Its binary representation:      11111111111111111111111111111101

Step 1:
    result >= 2147483648
    True.

Step 2:
    result = 4294967293 - 4294967296

Result: -3

Correct

######################################################################################################################################################################
5. What happens if we don't do this?

Consider
    nums = [0, 0, 0, -3]
The expected answer is: -3

But during bit reconstruction, the 32-bit representation of -3 is reconstructed as the positive Python integer:         4294967293
Without the conversion, your solution would return the wrong answer.

######################################################################################################################################################################
6. Remember this formula

For converting an unsigned 32-bit integer into a signed 32-bit integer:
    if result >= (1 << 31):
        result -= (1 << 32)

Mathematically:

Signed value = result,                  result <  2^{31}
               result - 2^{32},         result >= 2^{31}

Key takeaway: Python doesn't have a native fixed-width signed int type. When implementing fixed-width bit manipulation algorithms in Python, you sometimes need to handle signed integer conversion manually.
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                if (num >> i) & 1:
                    count += 1

            if count % 3:
                result |= (1 << i) # result = result or 1 << i

        # Handle negative numbers (32-bit signed integer) additional explanation provided above
        if result >= (1 << 31):
            result -= (1 << 32)

        return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from LeetCode
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),

        # Single element
        ([5], 5),
        ([0], 0),
        ([-1], -1),

        # Negative numbers
        ([-2, -2, -2, -5], -5),
        ([4, 4, 4, -7], -7),

        # Large positive and negative integers
        ([1000000000, 1000000000, 1000000000, 2147483647], 2147483647),
        ([-2147483648, -2147483648, -2147483648, 123], 123),

        # Different arrangements
        ([7, 7, 7, 3, 3, 3, 9], 9),
        ([9, 3, 9, 3, 9, 3, 5], 5),
        ([10, 20, 10, 30, 20, 10, 20], 30),

        # Multiple triplets
        ([1, 1, 1, 2, 2, 2, 3, 3, 3, 99], 99),
        ([-5, -5, -5, -10, -10, -10, -100], -100),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.singleNumber(nums)

        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {i}: {status}")
        print(f"Input:    {nums}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print("-" * 40)