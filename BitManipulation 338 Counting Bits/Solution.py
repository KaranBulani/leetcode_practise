'''
Given n, return:
ans[i] = number of 1-bits in binary representation of i

Example:
n = 5

0 → 0  → 0
1 → 1  → 1
2 → 10 → 1
3 → 11 → 2
4 → 100 → 1
5 → 101 → 2

[0, 1, 1, 2, 1, 2]

####################################################################################################
1. Brute Force — Count bits for every number

The most straightforward solution is:
For every i from 0 to n, count its set bits independently.

We can do that using the classic:	x &= x - 1
which removes the lowest set bit.

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            x = i
            while x:
                x &= x - 1
                count += 1
            ans.append(count)
        return ans

### Why does x & (x - 1) remove a bit?

Take:
x 	= 101100
x-1 = 101011

		How is x - 1 = 101011?
		x 	= 101100
				- 1
		------------

		You can't subtract 1 from 0 without borrowing, so borrow from the nearest 1 on the left:
		101100
		   ↑
		   0

		That 1 becomes 0, and all the zeros we passed over become 1:
		101100
		 ↓
		101011

		So,
		  101100
		-      1
		--------
		  101011

     101100
&    101011
------------
     101000

The lowest 1 disappears.
Therefore, the loop executes exactly as many times as there are 1s.

### Complexity

For each number: O(number of set bits)

In the worst case: O(log n)

So overall:
Time:  O(n log n)
Space: O(n)

This is good, but we can do better.

####################################################################################################
2. Using i >> 1

This is one of the most important solutions.
Observe:
i       binary      popcount
0       0           0
1       1           1
2       10          1
3       11          2
4       100         1
5       101         2
6       110         2
7       111         3

Consider:
	6 = 110

Right shift by one:
	6 >> 1 = 11 = 3

We removed the last bit.

Therefore:
	bits[i] = bits[i >> 1] + (i & 1)

Why?
	i >> 1 contains all bits except the last bit.
	i & 1 tells us whether the last bit is 0 or 1.

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans

### Example

For i = 13:
13 = 1101

13 >> 1 = 110 = 6
13 & 1  = 1

Therefore:
bits[13] = bits[6] + 1
         = 2 + 1
         = 3

### Complexity
Every i takes constant time:

Time:  O(n)
Space: O(n)
This is probably the cleanest solution to remember.

####################################################################################################
3. Using i & (i - 1)

Another beautiful DP relationship is:
bits[i] = bits[i & (i - 1)] + 1

Why?
i & (i - 1) removes the lowest set bit.

Example:

i = 12
12     		  = 1100
11	(i - 1)   = 1011

12 & 11
       = 1000
       = 8

So:
bits[12] = bits[8] + 1
         = 1 + 1
         = 2

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1

        return ans

### Complexity
Time:  O(n)
Space: O(n)

####################################################################################################
4. Using the lowest set bit

Another way to express the same idea is to identify the lowest set bit.
For example:
	10 = 1010
	lowest set bit = 0010

We can get it using: i & -i
	where -i is 2's compliment (Flip all bits and add 1)

But for this problem, we can formulate:
	ans[i] = ans[i - (i & -i)] + 1

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            lowest_bit = i & -i
            ans[i] = ans[i - lowest_bit] + 1

        return ans

Example:
i = 10 = 1010
i & -i = 0010

i - lowest_bit
= 1010 - 0010
= 1000
= 8

Therefore:
bits[10] = bits[8] + 1
         = 1 + 1
         = 2

Again:
Time:  O(n)
Space: O(n)

####################################################################################################
5. Using powers of 2

Every time we reach a power of 2, the binary representation starts a new "block".
0        → 0
1        → 1

2        → 10
3        → 11

4        → 100
5        → 101
6        → 110
7        → 111

8        → 1000
9        → 1001
10       → 1010
...


Notice:
4  → 100   → 1
5  → 101   → 1 + bits[1]
6  → 110   → 1 + bits[2]
7  → 111   → 1 + bits[3]

So if power is the largest power of 2 ≤ i:
bits[i] = 1 + bits[i - power]

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        power = 1
        for i in range(1, n + 1):
            if i == power * 2:
                power *= 2

            ans[i] = 1 + ans[i - power]

        return ans

For example:

power = 4

i = 4
bits[4] = 1 + bits[0] = 1

i = 5
bits[5] = 1 + bits[1] = 2

i = 6
bits[6] = 1 + bits[2] = 2

i = 7
bits[7] = 1 + bits[3] = 3

This is essentially the approach you were working on earlier.

####################################################################################################
6. Using the highest power of 2 with bit_length

We can make the previous approach slightly more Pythonic.
For every i, find the highest power of 2 ≤ i.
	power = 1 << (i.bit_length() - 1)

			Let's use:
				i = 6

			i.bit_length() gives: 3

			So, i.bit_length() - 1 is 2
			Then, 1 << 2 means 0001 << 2
			which gives 0100
			or
			4

			Therefore, power = 4
			And indeed, 4 ≤ 6
			and 4 is the largest power of 2 ≤ 6.

Then:
	ans[i] = 1 + ans[i - power]

bit_length explanation

	i       binary      bit_length()
	--------------------------------
	1       1              1
	2       10             2
	3       11             2
	4       100            3
	5       101            3
	6       110            3
	7       111            3
	8       1000           4

### Code
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            power = 1 << (i.bit_length() - 1)
            ans[i] = 1 + ans[i - power]

        return ans

This is:
	Time: O(n)
	Space: O(n)

Although for an interview/LeetCode solution, I'd prefer the simpler i >> 1 version.

####################################################################################################
Comparison

| Approach           |         Time |  Space | Main idea                |
| ------------------ | -----------: | -----: | ------------------------ |
| Count each bit     | O(n log n) | O(n) | Count bits independently |
| i >> 1           |   O(n) | O(n) | Remove last bit          |
| i & (i-1)        |   O(n) | O(n) | Remove lowest 1        |
| i & -i           |   O(n) | O(n) | Remove lowest set bit    |
| Highest power of 2 |       O(n) | O(n) | 1 + previous block     |

'''

class Solution:
    def countBits(self, n: int) -> list[int]:
        # Paste your solution here
        pass


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Given examples
        (0, [0]),
        (1, [0, 1]),
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),

        # Small edge cases
        (3, [0, 1, 1, 2]),
        (4, [0, 1, 1, 2, 1]),
        (6, [0, 1, 1, 2, 1, 2, 2]),
        (7, [0, 1, 1, 2, 1, 2, 2, 3]),
        (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),

        # Powers of 2
        (16, [
            0, 1, 1, 2, 1, 2, 2, 3,
            1, 2, 2, 3, 2, 3, 3, 4,
            1
        ]),

        # Larger example
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),

        # Boundary constraint
        (100000, None),
    ]

    for n, expected in test_cases:
        result = solution.countBits(n)

        if expected is not None:
            print(f"n = {n}")
            print(f"Expected: {expected}")
            print(f"Got:      {result}")
            print(f"PASS:     {result == expected}")
            print("-" * 50)
        else:
            # For n = 100000, don't manually write the expected 100001 values.
            # Check important properties instead.
            print(f"n = {n}")
            print(f"Length correct: {len(result) == n + 1}")
            print(f"First value correct: {result[0] == 0}")
            print(f"Last value correct: {result[-1] == 6}")  # 100000 = 11000011010100000
            print("-" * 50)