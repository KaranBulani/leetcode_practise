# 1. What is GCD?

**GCD (Greatest Common Divisor)** of two numbers is the largest number that divides both.

```text
gcd(12, 18) = 6
```

Because common divisors are:

```text
12 → 1, 2, 3, 4, 6, 12
18 → 1, 2, 3, 6, 9, 18

common → 1, 2, 3, 6
maximum → 6
```

---

# 2. Euclid's Algorithm ⭐⭐⭐


```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

The key mathematical property is:

```text
gcd(a, b) = gcd(b, a % b)
```

For example:

```text
gcd(48, 18)

48 % 18 = 12
18 % 12 = 6
12 % 6  = 0

answer = 6
```

---

# 3. GCD of MORE than 2 numbers ⭐⭐⭐

GCD is **associative**:

```text
gcd(a, b, c) = gcd(gcd(a, b), c)
```

And therefore:

```text
gcd(a, b, c, d) = gcd(gcd(gcd(a, b), c), d)
```
* Grouping doesn't matter
* This is why we can calculate GCD over an entire array by repeatedly applying GCD. 
* It's also why concepts like prefix GCD and segment trees work so naturally with GCD.
* 
* 
For example:
```text
gcd(24, 36, 60)
```

becomes:

```text
gcd(gcd(24, 36), 60)
= gcd(12, 60)
= 12
```

---

# 4. `gcd(0, x) = x` ⭐⭐

This is a very useful implementation trick.

```text
gcd(0, 7)  = 7
gcd(0, 15) = 15
gcd(0, 100) = 100
```

That's why you can initialize:

```python
g = 0

for x in nums:
    g = gcd(g, x)
```

instead of treating the first element specially.

---

# 5. GCD is commutative ⭐⭐

```text
gcd(a, b) = gcd(b, a)
```

So:

```python
gcd(a, b)
```

and:

```python
gcd(b, a)
```

are identical.

That's why this:

```python
gcd(val, prev_gcd)
```

can simply become:

```python
self.gcd(prev_gcd, val)
```

No need to check which number is larger.

---

# 6. GCD and divisibility

If:

```text
gcd(a, b) = g
```

then:

```text
g divides a
g divides b
```

---

# 7. A very useful GCD property ⭐⭐⭐

If `g = gcd(a, b)`, then:

```text
gcd(a/g, b/g) = 1
```

Example:

```text
a = 18
b = 24

gcd = 6

18/6 = 3
24/6 = 4

gcd(3, 4) = 1
```

So after removing their common factor, the numbers become **coprime**.

---

# 10. What does "coprime" mean?

Two numbers are **coprime** if their GCD is `1`.

```text
gcd(8, 15) = 1
```

Therefore `8` and `15` are coprime.

Important: **coprime does NOT mean both numbers are prime.**

For example:

```text
gcd(8, 9) = 1
```

Neither is prime, but they're coprime.

---

# 11. LCM

**LCM = Least Common Multiple**

For:

```text
a = 4
b = 6
```

Multiples:

```text
4 → 4, 8, 12, 16, 20...
6 → 6, 12, 18, 24...
```

First common positive multiple:

```text
12
```

So:

```text
lcm(4, 6) = 12
```

---

# 12. GCD × LCM relationship ⭐⭐⭐

This is probably the **most important LCM formula**:

```text
gcd(a, b) × lcm(a, b) = a × b
```

Therefore:

```text
lcm(a, b) = (a // gcd(a, b)) * b
```

Notice the division **before multiplication**.

Use:

```python
def lcm(a, b):
    return (a // gcd(a, b)) * b
```

rather than:

```python
return a * b // gcd(a, b)
```

The first version can avoid unnecessary overflow in languages with fixed-width integers.

Python itself doesn't have integer overflow for normal integers, but it's still the standard pattern.

---

# 13. LCM of multiple numbers

Just like GCD:

```text
lcm(a, b, c) = lcm(lcm(a, b), c)
```

Example:

```text
lcm(4, 6, 8)
= lcm(lcm(4, 6), 8)
= lcm(12, 8)
= 24
```

So you can maintain a running LCM too:

```python
l = 1
for x in nums:
    l = lcm(l, x)
```

---

# 14. GCD vs LCM identity

This is a nice mental model:

### GCD

Think:

> **What is the largest thing that fits inside all of them?**

```text
12, 18
 ↓
 6
```

### LCM

Think:

> **What is the smallest thing that contains all of them as factors?**

```text
12, 18
 ↓
36
```

---

# 15. `gcd(a, a) = a`

Obvious but useful:

```text
gcd(7, 7) = 7
```

---

# 16. `gcd(a, 1) = 1`

```text
gcd(100, 1) = 1
```

And consequently, if an array contains `1`:

```text
gcd(entire array) = 1
```

because:

```text
gcd(anything, 1) = 1
```

This can give useful shortcuts in problems.

---

# 17. `lcm(a, 1) = a`

Similarly:

```text
lcm(15, 1) = 15
```

---

# 18. GCD of a number and its multiple

If:

```text
b = k * a
```

then:

```text
gcd(a, b) = a
```

Example:

```text
gcd(7, 35) = 7
```

because `35 = 5 × 7`.

---

# 19. GCD can only stay the same or decrease ⭐⭐⭐

This is **very useful for algorithmic problems**.

Suppose you're processing:

```text
[12, 18, 24, 30]
```

Running GCD:

```text
12
gcd(12,18) = 6
gcd(6,24)  = 6
gcd(6,30)  = 6
```

Notice:

```text
12 → 6 → 6 → 6
```

It can never increase.

Why?

Because:

```text
gcd(previous_gcd, x)
```

must be a divisor of `previous_gcd`.

So:

```text
new_gcd <= previous_gcd
```

This property is surprisingly useful in advanced GCD problems.

---

# 20. GCD is NOT invertible ❗

For sums:

```text
prefix_sum[r] - prefix_sum[l-1]
```

gives a range sum.

But you **cannot** do something analogous for GCD.

For example:

```text
gcd(12, 18, 24) = 6
```

Knowing:

```text
gcd(12, 18, 24) = 6
```

and:

```text
gcd(12, 18) = 6
```

doesn't let you "remove" `18` and recover:

```text
gcd(12, 24)
```

So unlike sum:

```text
range_sum = prefix[r] - prefix[l-1]
```

there is no:

```text
range_gcd = prefix_gcd[r] ??? prefix_gcd[l-1]
```