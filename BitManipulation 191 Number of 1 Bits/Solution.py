"""
1. Problem Understanding

Given a positive integer n, return the number of  1  bits in its binary representation.
This is also called the  Hamming Weight .

Example:
    Input: n = 11
    Binary representation: 1011
    Output: 3
There are three  1  bits in  1011 .

######################################################################################################################################################################
2. Approach 1: Using Bitwise AND and Right Shift

We can solve this using two bitwise operators:
-  &  (Bitwise AND)
-  >>  (Right Shift)
Key observation: When we perform  n & 1 , we extract the rightmost bit of the binary representation.

Why?
        1011  (11)
    AND 0001  (1)
    ---------
        0001  (1)

If the rightmost bit is  1 , increment the count.
Then right-shift  n  by one position to process the next bit.

######################################################################################################################################################################
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            if n & 1:
                count += 1

            n >>= 1

        return count

######################################################################################################################################################################
Dry Run

Input:  n = 11
Binary representation:  1011

| Iteration | n (binary) | n & 1 | count |
| --------- | ---------- | ----- | ----- |
| 1         | 1011       | 1     | 1     |
| 2         | 101        | 1     | 2     |
| 3         | 10         | 0     | 2     |
| 4         | 1          | 1     | 3     |
After the fourth iteration,  n  becomes  0 , so the loop terminates.
Output:                 3

######################################################################################################################################################################
3. Approach 2: Brian Kernighan's Algorithm (Optimized)

There is a clever bit manipulation technique that removes the rightmost set bit (rightmost 1) in every iteration.

The operation is:  n = n & (n - 1)

Why does this work?

Consider:
    n     = 101100
    n - 1 = 101011

           101100
    AND    101011
    --------------
           101000

Notice that the rightmost  1  has been removed!
Therefore, instead of iterating through every bit, we iterate only as many times as there are set bits.

######################################################################################################################################################################
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count

######################################################################################################################################################################
Dry Run

Input:
    n = 11

Binary representation:  1011
| Iteration | n before operation | n & (n-1) | count |
| --------- | ------------------ | --------- | ----- |
| 1         | 1011               | 1010      | 1     |
| 2         | 1010               | 1000      | 2     |
| 3         | 1000               | 0000      | 3     |

Loop terminates because  n = 0 .
Output:  3

######################################################################################################################################################################
4. Complexity Analysis

Let:
-  B  = number of bits in the integer.
-  K  = number of set bits (1s).

| Approach        | Time Complexity | Space Complexity |
| --------------- | --------------- | ---------------- |
| Right Shift     | O(B)            | O(1)             |
| Brian Kernighan | O(K)            | O(1)             |
For LeetCode 191, the input is a 32-bit integer, so both approaches are effectively O(1).

######################################################################################################################################################################
6. Important Takeaways

Remember these three bit manipulation operations:
| Operation     | Purpose                      |
| ------------- | ---------------------------- |
|  n & 1        | Extract rightmost bit        |
|  n >> 1       | Remove rightmost bit         |
|  n & (n - 1)  | Remove rightmost set bit (1) |

My recommendation:  Understand both approaches, but remember Brian Kernighan's algorithm: n = n & (n - 1)

It is a very useful technique for bit manipulation problems and appears in several other algorithmic problems.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n = n & (n - 1)
            count += 1

        return count


def main():
    solution = Solution()

    test_cases = [
        (11, 3),
        (128, 1),
        (2147483645, 30),
        (1, 1),
        (0, 0),
        (7, 3),
        (15, 4),
        (255, 8),
        (256, 1),
        (4294967295, 32)
    ]

    for i, (n, expected) in enumerate(test_cases, 1):
        result = solution.hammingWeight(n)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Test {i}: {status} | "
            f"Input: {n} | "
            f"Expected: {expected} | "
            f"Actual: {result}"
        )

if __name__ == "__main__":
    main()