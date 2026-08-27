# Bit Manipulation Cheatsheet — LeetCode

A practical Python cheatsheet for common **bit-manipulation patterns**, especially the kinds of operations that frequently appear in LeetCode problems.

---

## 1. Binary Representation in Python

### Using `bin()` — Includes `0b` Prefix

The built-in `bin()` function converts an integer into a binary string prefixed with `0b`.

```python
number = 10
print(bin(number))  # Output: '0b1010'
```

---

### Using Slicing — Removes `0b` Prefix

If you only want the raw `0` and `1` digits, use string slicing `[2:]` to strip the first two characters.

```python
number = 10
print(bin(number)[2:])  # Output: '1010'
```

---

### Using F-Strings or `format()` — Clean Formatting

You can use the `b` format specifier inside an f-string or the `format()` function to get the raw binary string directly.

```python
number = 10

# Using f-string
print(f"{number:b}")  # Output: '1010'

# Using format()
print(format(number, "b"))  # Output: '1010'
```

---

### Pad with Leading Zeros — Fixed Width

To make your binary representation a fixed length (e.g., 8 bits for a byte), add a number before the `b` in your format string.

```python
number = 10

# Zero-pad to 8 characters
print(f"{number:08b}")  # Output: '00001010'
```

---

# 2. Core Bitwise Operators

| Operator | Name | Meaning |
|---|---|---|
| `&` | AND | Bit is `1` only if both bits are `1` |
| `\|` | OR | Bit is `1` if either bit is `1` |
| `^` | XOR | Bit is `1` if the bits are different |
| `~` | NOT | Flips all bits |
| `<<` | Left shift | Shift bits left |
| `>>` | Right shift | Shift bits right |

Example:

```python
a = 10        # 1010
b = 6         # 0110

print(a & b)  # 0010 = 2
print(a | b)  # 1110 = 14
print(a ^ b)  # 1100 = 12
print(~a)     # -11
print(a << 1) # 10100 = 20
print(a >> 1) # 0101 = 5
```

### Quick Rule

```text
&  → keep common 1-bits
|  → combine 1-bits
^  → keep different bits
~  → flip bits
<< → multiply by 2^k (for non-negative integers)
>> → divide by 2^k (floor for non-negative integers)
```

---

# 3. Powers of 2

A power of 2 has exactly **one set bit**.

```text
1  = 0001
2  = 0010
4  = 0100
8  = 1000
16 = 10000
```

### Check if `n` is a power of 2

```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
```

Why?

```text
n     = 1000
n - 1 = 0111
      = 0000 after AND
```

So:

```python
n & (n - 1) == 0
```

means only one bit was set.

---

# 4. Get the Lowest Set Bit

```python
n & -n
```

This isolates the **rightmost `1` bit**.

Example:

```text
n    = 1011000
-n   = 0101000   # two's-complement concept
----------------
n & -n = 0001000

============================================================
2's Complement (negative numbers)
============================================================

To get -n:
    1. Flip all bits: ~n
    2. Add 1:         ~n + 1

Therefore:
    -n = ~n + 1

Example:
    n  = 0010  (2)
    ~n = 1101
    +1 = 1110  (-2)

Key trick:
    n & -n
    → isolates the lowest set bit
    
```

Useful for:

- Fenwick Tree / BIT
- finding a set bit
- bitmask problems
- extracting powers of 2

---

# 5. Remove the Lowest Set Bit

```python
n &= n - 1
```

This removes the rightmost `1`.

Example:

```text
n     = 1011000
n - 1 = 1010111

n & (n - 1)
      = 1010000
```

### Count set bits

This gives an efficient way to count `1`s:

```python
def count_bits(n: int) -> int:
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count
```

Python also provides:

```python
n.bit_count()
```

---

# 6. Test Whether a Bit Is Set

To check bit position `k`:

```python
(n >> k) & 1
```

Example:

```python
n = 10  # 1010

print((n >> 0) & 1)  # 0
print((n >> 1) & 1)  # 1
print((n >> 2) & 1)  # 0
print((n >> 3) & 1)  # 1
```

Equivalent mask form:

```python
(n & (1 << k)) != 0
```

---

# 7. Set a Bit

Set bit `k` to `1`:

```python
n |= 1 << k
```

Example:

```python
n = 8       # 1000
n |= 1 << 1 # 1010

print(n)    # 10
```

---

# 8. Clear a Bit

Clear bit `k` to `0`:

```python
n &= ~(1 << k)
```

Example:

```python
n = 10        # 1010
n &= ~(1 << 1)

print(n)      # 8
```

---

# 9. Toggle a Bit

Toggle bit `k`:

```python
n ^= 1 << k
```

If the bit is:

```text
0 → 1
1 → 0
```

Example:

```python
n = 10       # 1010
n ^= 1 << 1  # 1000

print(n)     # 8
```

---

# 10. Create a Mask for Bit `k`

```python
1 << k
```

Examples:

```python
1 << 0  # 0001 = 1
1 << 1  # 0010 = 2
1 << 2  # 0100 = 4
1 << 3  # 1000 = 8
```

This is one of the most important expressions in bitmask-based LeetCode problems.

---

# 11. XOR Properties

XOR has several extremely useful properties:

```text
a ^ a = 0
a ^ 0 = a
a ^ b = b ^ a
(a ^ b) ^ c = a ^ (b ^ c)
```

### Find the single number

If every number appears twice except one:

```python
result = 0

for n in nums:
    result ^= n

return result
```

Why?

```text
a ^ b ^ a
= (a ^ a) ^ b
= 0 ^ b
= b
```

This pattern appears frequently in LeetCode.

---

# 12. XOR as "Difference"

Remember:

```text
same bit → 0
different bit → 1
```

Truth table:

| A | B | A ^ B |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

A useful mental model:

```text
XOR tells you where two bit patterns differ.
```

---

# 13. Swap Two Numbers Using XOR

Classic bit trick:

```python
a ^= b
b ^= a
a ^= b
```

However, in Python, simply use:

```python
a, b = b, a
```

The XOR version is mainly useful for understanding XOR properties.

---

# 14. Extract a Range of Bits

Suppose you want bits `[l, r]`.

Create a mask:

```python
length = r - l + 1
mask = (1 << length) - 1
```

Then shift it into position:

```python
mask <<= l
```

Example for bits `[2, 4]`:

```text
length = 3

(1 << 3) - 1
= 0111

0111 << 2
= 11100
```

Then:

```python
bits = n & mask
```

---

# 15. Lowest `k` Bits

Mask:

```python
(1 << k) - 1
```

Example:

```python
n = 0b10110110

mask = (1 << 4) - 1
# mask = 0b1111

n & mask
# 0b0110
```

So:

```python
n & ((1 << k) - 1)
```

extracts the lowest `k` bits.

---

# 16. Set the Lowest `k` Bits

Mask:

```python
(1 << k) - 1
```

Example:

```python
n |= (1 << k) - 1
```

For `k = 4`:

```text
mask = 1111
```

---

# 17. Bitmask for a Set

A very common LeetCode pattern is representing a set using an integer.

For example, suppose we have:

```text
{0, 2, 4}
```

Represent it as:

```text
bit 4 = 1
bit 2 = 1
bit 0 = 1

mask = 10101
```

### Add element `x`

```python
mask |= 1 << x
```

### Remove element `x`

```python
mask &= ~(1 << x)
```

### Check whether `x` exists

```python
if mask & (1 << x):
    ...
```

### Toggle element `x`

```python
mask ^= 1 << x
```

---

# 18. Enumerate All Subsets Using Bitmasks

For `n` elements, there are:

```text
2^n
```

subsets.

Each integer from `0` to `2^n - 1` can represent one subset.

```python
for mask in range(1 << n):
    subset = []

    for i in range(n):
        if mask & (1 << i):
            subset.append(nums[i])
```

Example:

```text
nums = [a, b, c]

000 → {}
001 → {a}
010 → {b}
011 → {a, b}
100 → {c}
101 → {a, c}
110 → {b, c}
111 → {a, b, c}
```

---

# 19. Enumerate Set Bits

Instead of checking every bit:

```python
while mask:
    bit = mask & -mask

    # Process bit

    mask &= mask - 1
```

To get the bit index:

```python
index = bit.bit_length() - 1
```

Full pattern:

```python
while mask:
    bit = mask & -mask
    index = bit.bit_length() - 1

    # use index

    mask &= mask - 1
```

---

# 20. Enumerate All Submasks

This is a very important advanced bitmask pattern.

Given:

```python
mask
```

iterate through all submasks:

```python
sub = mask

while sub:
    # process sub

    sub = (sub - 1) & mask
```

Include zero if required:

```python
sub = mask

while True:
    # process sub

    if sub == 0:
        break

    sub = (sub - 1) & mask
```

---

# 21. Count Set Bits

### Python built-in

```python
n.bit_count()
```

### Manual

```python
count = 0

while n:
    n &= n - 1
    count += 1
```

### Common LeetCode use

If a mask represents selected items:

```python
selected_count = mask.bit_count()
```

---

# 22. Number of Bits Needed

```python
n.bit_length()
```

Examples:

```python
(1).bit_length()   # 1
(2).bit_length()   # 2
(7).bit_length()   # 3
(8).bit_length()   # 4
(10).bit_length()  # 4
```

Useful for:

- determining the highest set bit
- constructing masks
- binary search over bits
- finding the number of bits needed to represent a number

Highest set-bit index:

```python
highest_bit = n.bit_length() - 1
```

---

# 23. Find the Highest Set Bit

For positive `n`:

```python
highest = 1 << (n.bit_length() - 1)
```

Example:

```text
n = 10 = 1010

n.bit_length() - 1 = 3

1 << 3 = 1000
```

---

# 24. Clear All Bits Above Position `k`

Keep only bits `0 ... k`:

```python
n &= (1 << (k + 1)) - 1
```

Example:

```text
n       = 11010110
k       = 4
mask    = 00011111
result  = 00010110
```

---

# 25. Left Shift

```python
n << k
```

For non-negative integers:

```text
n << k = n * 2^k
```

Example:

```python
5 << 1  # 10
5 << 2  # 20
5 << 3  # 40
```

---

# 26. Right Shift

```python
n >> k
```

For non-negative integers:

```text
n >> k = floor(n / 2^k)
```

Example:

```python
20 >> 1  # 10
20 >> 2  # 5
20 >> 3  # 2
```

---

# 27. Multiply / Divide by Powers of 2

```python
n << k  # multiply by 2^k
n >> k  # divide by 2^k for non-negative n
```

Examples:

```python
n = 7

n << 2  # 28
n >> 1  # 3
```

---

# 28. Check Odd / Even

### Even

```python
(n & 1) == 0
```

### Odd

```python
(n & 1) == 1
```

Equivalent:

```python
n % 2 == 0
n % 2 == 1
```

The bit version is useful when working with bit operations.

---

# 29. Two's Complement Intuition

For signed integers, negative numbers are commonly represented using two's complement.

The important identity for bit tricks is:

```python
-n
```

Conceptually:

```text
-n = ~n + 1
```

This is why:

```python
n & -n
```

isolates the lowest set bit.

---

# 30. XOR Prefix / Prefix XOR

If you repeatedly need XOR over ranges, build a prefix XOR array.

```python
prefix = [0]

for n in nums:
    prefix.append(prefix[-1] ^ n)
```

XOR from index `l` through `r`:

```python
prefix[r + 1] ^ prefix[l]
```

Because:

```text
a ^ b ^ c ^ b ^ c = a
```

---

# 31. XOR Instead of Addition

XOR is **not normal addition**.

For example:

```text
5 + 3 = 8

0101
0011
----
1000
```

But:

```text
5 ^ 3 = 6

0101
0011
----
0110
```

However, XOR represents addition **without carry**.

This leads to the classic identity:

```text
a + b
= (a ^ b) + ((a & b) << 1)
```

The first term contains the sum without carries.

The second term contains the carries.

---

# 32. Add Two Integers Using Bits

Conceptual approach:

```python
while b:
    carry = (a & b) << 1
    a = a ^ b
    b = carry
```

Interpretation:

```text
a ^ b          → sum without carry
(a & b) << 1   → carry
```

### Important Python Note

Python integers have arbitrary precision, so the above needs a fixed-width mask if you are implementing a signed 32-bit LeetCode problem exactly.

Typical 32-bit setup:

```python
MASK = 0xFFFFFFFF
MAX_INT = 0x7FFFFFFF

while b:
    carry = ((a & b) << 1) & MASK
    a = (a ^ b) & MASK
    b = carry

return a if a <= MAX_INT else ~(a ^ MASK)
```

---

# 33. Reverse Bits

For a fixed-width integer, repeatedly extract the lowest bit:

```python
result = 0

for _ in range(32):
    result = (result << 1) | (n & 1)
    n >>= 1
```

Pattern:

```text
extract lowest bit
        ↓
append it to result
        ↓
shift original right
```

---

# 34. Build a Number Bit by Bit

A common pattern:

```python
result = 0

for bit in bits:
    result = (result << 1) | bit
```

Example:

```text
bits = [1, 0, 1, 1]

result:

0
1
10
101
1011
```

---

# 35. Get the `k`-th Bit from the Right

Zero-indexed:

```python
(n >> k) & 1
```

One-indexed:

```python
(n >> (k - 1)) & 1
```

Be careful about whether the problem uses:

```text
bit 0 = rightmost bit
```

or one-based indexing.

---

# 36. Common Mask Patterns

| Goal | Expression |
|---|---|
| Bit `k` mask | `1 << k` |
| Check bit `k` | `(n >> k) & 1` |
| Set bit `k` | `n \|= 1 << k` |
| Clear bit `k` | `n &= ~(1 << k)` |
| Toggle bit `k` | `n ^= 1 << k` |
| Lowest set bit | `n & -n` |
| Remove lowest set bit | `n & (n - 1)` |
| Lowest `k` bits | `(1 << k) - 1` |
| Keep bits `0..k` | `(1 << (k + 1)) - 1` |
| Power of 2 | `n > 0 and n & (n - 1) == 0` |
| Count set bits | `n.bit_count()` |
| Number of bits | `n.bit_length()` |

---

# 37. Common LeetCode Patterns

## Pattern A — Single Number

**Problem shape:**

> Every element appears twice except one.

Use:

```python
ans = 0

for n in nums:
    ans ^= n

return ans
```

---

## Pattern B — Power of Two

**Problem shape:**

> Determine whether `n` is a power of two.

Use:

```python
return n > 0 and (n & (n - 1)) == 0
```

---

## Pattern C — Count Set Bits

**Problem shape:**

> Count the number of `1`s in binary.

Use:

```python
return n.bit_count()
```

Or:

```python
count = 0

while n:
    n &= n - 1
    count += 1

return count
```

---

## Pattern D — Bitmask DP

**Problem shape:**

> Track which elements/items have been selected.

Use:

```python
mask = 0

# Add i
mask |= 1 << i

# Check i
if mask & (1 << i):
    ...

# Remove i
mask &= ~(1 << i)
```

---

## Pattern E — Enumerate All Subsets

```python
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            # nums[i] is selected
            ...
```

Time:

```text
O(n * 2^n)
```

---

## Pattern F — Enumerate Submasks

```python
sub = mask

while sub:
    # process sub
    sub = (sub - 1) & mask
```

Number of submasks:

```text
2^(number of set bits in mask)
```

---

## Pattern G — Greedy Bit-by-Bit Construction

Some problems ask you to maximize/minimize a number.

A common strategy is to decide bits from:

```text
highest → lowest
```

Template:

```python
ans = 0

for bit in range(max_bit, -1, -1):
    candidate = ans | (1 << bit)

    if valid(candidate):
        ans = candidate
```

This appears in:

- maximum XOR
- bitwise optimization
- constructing maximum numbers
- greedy mask problems

---

# 38. Maximum XOR Pattern

A common approach is to build the answer from the highest bit down.

Conceptually:

```python
ans = 0

for bit in range(max_bit, -1, -1):
    candidate = ans | (1 << bit)

    # Check whether this bit can be achieved.
    if possible(candidate):
        ans = candidate
```

For maximum XOR specifically, another common pattern is a **prefix set**:

```python
mask = 0
ans = 0

for bit in range(max_bit, -1, -1):
    mask |= 1 << bit

    prefixes = {n & mask for n in nums}

    candidate = ans | (1 << bit)

    if any((candidate ^ p) in prefixes for p in prefixes):
        ans = candidate
```

Mental model:

```text
Try to make the highest bit of XOR = 1.
If possible, keep it.
Then move to the next bit.
```

---

# 39. Bitwise AND of a Range

For a range:

```text
[left, right]
```

the common trick is to remove differing lower bits.

```python
shift = 0

while left < right:
    left >>= 1
    right >>= 1
    shift += 1

return left << shift
```

Mental model:

```text
Keep only the common binary prefix.
```

Example:

```text
10 = 1010
11 = 1011
12 = 1100
```

Common prefix across the entire range:

```text
1
```

So:

```text
1010
1011
1100
----
0000
```

---

# 40. Gray Code

Gray code changes only one bit between consecutive values.

Formula:

```python
gray = n ^ (n >> 1)
```

Example:

```text
n = 5

101
010
---
111
```

So:

```python
5 ^ (5 >> 1) == 7
```

---

# 41. Check if Two Numbers Have Opposite Signs

For fixed-width signed integers, sign is represented by the highest bit.

A common conceptual test:

```python
(a < 0) != (b < 0)
```

For pure bit-manipulation problems, you may also encounter:

```python
(a ^ b) < 0
```

This relies on signed two's-complement behavior.

---

# 42. Useful Python Bit Functions

Python already provides several excellent helpers:

```python
n.bit_count()
```

Number of set bits.

```python
n.bit_length()
```

Number of bits needed to represent `n` in binary.

```python
bin(n)
```

Binary string with `0b`.

```python
format(n, "b")
```

Binary string without `0b`.

```python
f"{n:b}"
```

Binary string without `0b`.

```python
f"{n:08b}"
```

8-bit zero-padded binary string.

---

# 43. Fast Mental Conversions

Memorize powers of 2:

```text
2^0  = 1
2^1  = 2
2^2  = 4
2^3  = 8
2^4  = 16
2^5  = 32
2^6  = 64
2^7  = 128
2^8  = 256
2^9  = 512
2^10 = 1024
```

Common hexadecimal masks:

```text
0x0F = 0000 1111
0xFF = 1111 1111
0xFFFF = 16 ones
0xFFFFFFFF = 32 ones
```

---

# 44. Common Bit Tricks — Quick Reference

```python
# Binary
bin(n)
bin(n)[2:]
f"{n:b}"
f"{n:08b}"

# Check bit k
(n >> k) & 1

# Set bit k
n |= 1 << k

# Clear bit k
n &= ~(1 << k)

# Toggle bit k
n ^= 1 << k

# Lowest set bit
n & -n

# Remove lowest set bit
n &= n - 1

# Power of 2
n > 0 and (n & (n - 1)) == 0

# Count set bits
n.bit_count()

# Number of bits
n.bit_length()

# Lowest k bits
n & ((1 << k) - 1)

# Keep bits 0 through k
n & ((1 << (k + 1)) - 1)

# Multiply by 2^k
n << k

# Divide by 2^k for non-negative n
n >> k

# Add two integers using bit operations
carry = (a & b) << 1
a = a ^ b

# Enumerate subsets
for mask in range(1 << n):
    ...

# Enumerate submasks
sub = mask
while sub:
    ...
    sub = (sub - 1) & mask
```

---

# 45. How to Recognize a Bit Manipulation Problem

Look for these clues:

### 1. The problem explicitly mentions binary

Examples:

```text
binary representation
bits
bit positions
set bits
```

### 2. Constraints involve small `n`

Especially:

```text
n <= 20
n <= 25
n <= 30
n <= 32
```

This can indicate subset/bitmask techniques.

### 3. The problem asks about subsets

Think:

```python
mask
1 << n
```

### 4. Every number appears twice

Think:

```python
XOR
```

### 5. Power of two

Think:

```python
n & (n - 1)
```

### 6. Need to repeatedly choose/remove one set bit

Think:

```python
n & -n
n &= n - 1
```

### 7. Need maximum/minimum under XOR/AND/OR

Think:

```text
highest bit → lowest bit
```

and potentially:

```text
greedy bit construction
Trie
bitmask
```

---

# 46. The Most Important 10 to Memorize

If you only memorize ten expressions, memorize these:

```python
# 1. Binary
bin(n)

# 2. Check bit k
(n >> k) & 1

# 3. Set bit k
n | (1 << k)

# 4. Clear bit k
n & ~(1 << k)

# 5. Toggle bit k
n ^ (1 << k)

# 6. Lowest set bit
n & -n

# 7. Remove lowest set bit
n & (n - 1)

# 8. Power of 2
n > 0 and (n & (n - 1)) == 0

# 9. Count set bits
n.bit_count()

# 10. Enumerate subsets
for mask in range(1 << n):
    ...
```

---

# 47. Bit Manipulation Decision Tree

```text
Need binary representation?
        ↓
bin(n) / f"{n:b}"

Need to check one bit?
        ↓
(n >> k) & 1

Need to modify one bit?
        ↓
Set    → n |= 1 << k
Clear  → n &= ~(1 << k)
Toggle → n ^= 1 << k

Need the lowest 1-bit?
        ↓
n & -n

Need to remove the lowest 1-bit?
        ↓
n &= n - 1

Need to count 1-bits?
        ↓
n.bit_count()

Need to check power of 2?
        ↓
n > 0 and n & (n - 1) == 0

Need to represent a subset?
        ↓
Use an integer mask

Need all subsets?
        ↓
range(1 << n)

Need all submasks of mask?
        ↓
sub = (sub - 1) & mask

Need maximum/minimum bitwise result?
        ↓
Try bits from highest → lowest
```

---

# 48. Final Mental Model

Think of an integer as a row of switches:

```text
bit position:  7 6 5 4 3 2 1 0
               ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
number:        0 1 0 1 1 0 1 0
```

Then:

```text
1 << k
```

creates a switch at position `k`.

```text
&
```

asks:

> Are both switches ON?

```text
|
```

asks:

> Is either switch ON?

```text
^
```

asks:

> Are the switches different?

```text
~
```

asks:

> Flip every switch.

```text
<<
```

moves switches left.

```text
>>
```

moves switches right.

Most LeetCode bit-manipulation problems are combinations of these basic operations.

**Core expressions to remember:**

```python
1 << k
(n >> k) & 1
n & -n
n & (n - 1)
n.bit_count()
n.bit_length()
mask |= 1 << k
mask &= ~(1 << k)
mask ^= 1 << k
sub = (sub - 1) & mask
```
