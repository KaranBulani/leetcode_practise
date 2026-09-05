**Binary exponentiation**, also called **exponentiation by squaring**, is a way to calculate

$$
a^n
$$

much faster than multiplying `a` by itself `n` times.

The key idea is:

> **Use the binary representation of the exponent to reduce the number of multiplications from O(n) to O(log n).**

---

# 1. The normal approach

Suppose we want:

$$
2^{10}
$$

The naive approach is:

```text
2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 × 2
```
That's **9 multiplications**.

For a huge exponent like, $$2^{1000000000}$$ that's obviously impossible to do one multiplication at a time.

---

# 2. The mathematical trick: squaring

Notice:

$$
a^2 = a \times a
$$

$$
a^4 = a^2 \times a^2
$$

$$
a^8 = a^4 \times a^4
$$

$$
a^{16} = a^8 \times a^8
$$

So instead of calculating every power:

```text
a
a²
a³
a⁴
a⁵
...
```

we can jump:

```text
a → a² → a⁴ → a⁸ → a¹⁶ → ...
```

Each step **squares** the previous result.

That's where "exponentiation by squaring" comes from.

---

# 3. What if the exponent isn't a power of 2?

Suppose:

$$
a^{13}
$$

We can write:

$$
13 = 8 + 4 + 1
$$

Therefore:

$$
a^{13} = a^8 \times a^4 \times a^1
$$

And we can obtain those powers by repeated squaring:

```text
a¹
 ↓ square
a²
 ↓ square
a⁴
 ↓ square
a⁸
```

Then:

```text
a⁸ × a⁴ × a¹ = a¹³
```

And this is directly related to the **binary representation** of 13:

$$
13 = 1101_2
$$

The `1`s occur at:

```text
8  4  2  1
1  1  0  1
```

So:

$$
13 = 8 + 4 + 1
$$

---

# 4. The recursive idea

There are two cases.

### If n is even

Suppose:

$$
a^{10}
$$

We can split the exponent:

$$
a^{10} = a^5 \times a^5
$$

Therefore:

$$
\boxed{a^{10} = (a^5)^2}
$$

More generally:

$$
\boxed{a^n = (a^{n/2})^2}
$$

when `n` is even.

---

### If n is odd

Suppose:

$$
a^{11}
$$

We can write:

$$
a^{11} = a \times a^{10}
$$

And then:

$$
a^{10} = (a^5)^2
$$

So:

$$
\boxed{a^{11} = a \times (a^5)^2}
$$

More generally:

$$
\boxed{a^n = a \times (a^{\lfloor n/2\rfloor})^2}
$$

when `n` is odd.

---

# 5. Recursive implementation

```python
def power(a, n):
    if n == 0:
        return 1

    half = power(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return a * half * half
```

Let's trace:

```python
power(2, 13)
```

We get:

```text
power(2, 13)
    ↓
power(2, 6)
    ↓
power(2, 3)
    ↓
power(2, 1)
    ↓
power(2, 0)
```

Notice how the exponent keeps getting **halved**:

```text
13 → 6 → 3 → 1 → 0
```

That's why the complexity is:

$$
\boxed{O(\log n)}
$$

rather than O(n).

---

# 6. The iterative version — more important for DSA

Usually, you'll see binary exponentiation written iteratively.

```python
def power(a, n):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result *= a

        a *= a
        n //= 2

    return result
```

This version is particularly useful when you need **modular exponentiation**.

For example:

```python
def power(a, n, mod):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod

        a = (a * a) % mod
        n //= 2

    return result
```

This is extremely common in competitive programming.

---

# 7. Understand the iterative version deeply

Let's calculate:

$$
2^{13}
$$

Initially:

```text
result = 1
a = 2
n = 13
```

### Iteration 1

`n = 13` is odd.

So:

```text
result = result × a
       = 1 × 2
       = 2
```

Then square `a`:

```text
a = 2 × 2 = 4
```

and halve `n`:

```text
n = 13 // 2 = 6
```

State:

```text
result = 2
a      = 4
n      = 6
```

---

### Iteration 2

`n = 6` is even.

Don't multiply into `result`.

Square:

```text
a = 4 × 4 = 16
```

Halve:

```text
n = 6 // 2 = 3
```

State:

```text
result = 2
a      = 16
n      = 3
```

---

### Iteration 3

`n = 3` is odd.

Therefore:

```text
result = 2 × 16
       = 32
```

Square:

```text
a = 16 × 16
  = 256
```

Halve:

```text
n = 3 // 2
  = 1
```

State:

```text
result = 32
a      = 256
n      = 1
```

---

### Iteration 4

`n = 1` is odd.

```text
result = 32 × 256
       = 8192
```

Square:

```text
a = 256²
```

Halve:

```text
n = 1 // 2 = 0
```

Stop.

Therefore:

$$
\boxed{2^{13}=8192}
$$

---

# 8. Why do we check `n % 2`?

This is the most important part to understand.

We're essentially reading the exponent's **binary representation** from right to left.

For:

$$
13 = 1101_2
$$

the bits are:

```text
1 1 0 1
```

From right to left:

```text
1 → use a¹
0 → don't use a²
1 → use a⁴
1 → use a⁸
```

Therefore:

$$
2^{13}
=
2^8 \times 2^4 \times 2^1
$$

The code:

```python
if n % 2 == 1:
    result *= a
```

is essentially saying:

> "Is the current binary bit 1? If yes, include this power."

And:

```python
a *= a
```

moves us from:

```text
a¹ → a² → a⁴ → a⁸ → a¹⁶ → ...
```

while:

```python
n //= 2
```

moves through the bits:

```text
1101 → 110 → 11 → 1 → 0
```

So the algorithm is really **binary decomposition of the exponent + repeated squaring**.

---

# 9. Why does it become O(log n)?

Every iteration does:

```python
n //= 2
```

So:

$$
n,\frac n2,\frac n4,\frac n8,\ldots
$$

until it reaches zero.

The number of halvings needed is approximately:

$$
\log_2 n
$$

Therefore:

### Time

$$
\boxed{O(\log n)}
$$

### Space

For the iterative version:

$$
\boxed{O(1)}
$$

For the recursive version:

$$
\boxed{O(\log n)}
$$

because of the recursion stack.

---

# 10. Why this matters for modular exponentiation

This is especially important for problems like:

$$
a^n \mod M
$$

where `n` can be enormous.

You can combine exponentiation by squaring with the property:

$$
(xy)\bmod M
=
((x\bmod M)(y\bmod M))\bmod M
$$

So you can safely do:

```python
def power(a, n, mod):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod

        a = (a * a) % mod
        n //= 2

    return result
```

The crucial line is:

```python
a = (a * a) % mod
```

rather than allowing `a` to become astronomically large.

This is the same technique behind Python's:

```python
pow(a, n, mod)
```

which you may have seen in LeetCode.

---

## The mental model I'd recommend remembering

Don't memorize the code first. Remember these **three transformations**:

```text
Exponent is odd?
        ↓
Take current power

Current power
        ↓ square
Next power

Exponent
        ↓ divide by 2
Next binary bit
```

So:

$$
\boxed{
a^n
\quad\longrightarrow\quad
\text{read bits of }n
\quad+\quad
\text{keep squaring }a
}
$$

Once this clicks, binary exponentiation becomes a very straightforward pattern rather than something you have to memorize.

---

## Why iterative & recursive essentially same?

---

### 1. Start with the recursive solution

```python
def power(a, n):
    if n == 0:
        return 1

    half = power(a, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return a * half * half
```

For:

```python
power(2, 13)
```

the recursive calls are:

```text
power(2, 13)
    ↓
power(2, 6)
    ↓
power(2, 3)
    ↓
power(2, 1)
    ↓
power(2, 0)
```

The important thing is:

> **The recursive function goes DOWN first, and only calculates answers while coming BACK UP.**

Let's explicitly write what happens.

---

### 2. Going down

We call:

```text
power(2, 13)
```

It needs:

```text
power(2, 6)
```

which needs:

```text
power(2, 3)
```

which needs:

```text
power(2, 1)
```

which needs:

```text
power(2, 0)
```

At this point:

```text
power(2, 0) = 1
```

Now we start returning.

---

### 3. Coming back up

For `n = 1`:

$$
2^1 = 2 \times 1 \times 1 = 2
$$

So:

```text
power(2, 1) = 2
```

Then `n = 3`:

$$
2^3 = 2 \times 2^1 \times 2^1
$$

```text
power(2, 3) = 2 × 2 × 2 = 8
```

Then `n = 6`:

$$
2^6 = (2^3)^2
$$

```text
power(2, 6) = 8 × 8 = 64
```

Then `n = 13`:

$$
2^{13} = 2 \times (2^6)^2
$$

```text
power(2, 13) = 2 × 64 × 64 = 8192
```

So recursion is essentially:

```text
GO DOWN
13 → 6 → 3 → 1 → 0

COME BACK UP
0 → 1 → 3 → 6 → 13
```

---

## 4. Now look at the iterative solution

```python
def power(a, n):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result *= a

        a *= a
        n //= 2

    return result
```

At first glance this seems completely different.

But look at the values:

```text
n:
13 → 6 → 3 → 1 → 0
```

**That's exactly the same sequence of exponents that recursion creates!**

The difference is what we're doing with them.

---

## 5. The key difference

Recursive:

```text
13 → 6 → 3 → 1 → 0
                 ↓
             calculate
                 ↓
13 ← 6 ← 3 ← 1 ← 0
```

It goes down first.

Iterative:

```text
13 → 6 → 3 → 1 → 0
↓    ↓    ↓    ↓
use  skip use  use
```

It calculates the answer **while going down**.

That's the fundamental difference.

---

## 6. But how can iterative calculate while going down?

This is where `result` becomes important.

Let's trace the iterative algorithm carefully.

Start:

```text
result = 1
a = 2
n = 13
```

#### n = 13

13 is odd:

```python
result *= a
```

so:

```text
result = 1 × 2 = 2
```

Then:

```python
a *= a
n //= 2
```

giving:

```text
a = 4
n = 6
```

---

#### n = 6

6 is even.

Don't add `a` to result.

Square `a`:

```text
a = 4² = 16
n = 3
```

State:

```text
result = 2
a = 16
n = 3
```

---

#### n = 3

3 is odd:

```text
result = 2 × 16
       = 32
```

Then:

```text
a = 16² = 256
n = 1
```

---

#### n = 1

1 is odd:

```text
result = 32 × 256
       = 8192
```

Then:

```text
n = 0
```

Done.

---

## 7. Here's the BIG connection

Look at what `a` represents during the loop:

```text
a = 2
a = 4
a = 16
a = 256
```

These are:

$$
2^1,\;2^2,\;2^4,\;2^8
$$

And `result` picks the powers corresponding to the `1` bits of 13.

Remember:

$$
13 = 1101_2
$$

Therefore:

$$
13 = 8 + 4 + 1
$$

So we need:

$$
2^{13}
=
2^8 \times 2^4 \times 2^1
$$

The iterative algorithm does exactly that:

```text
n       a        result
--------------------------------
13      2        2        ← take 2¹
 6      4        2        ← skip 2²
 3     16       32        ← take 2⁴
 1    256     8192        ← take 2⁸
 0
```

So:

```text
result = 2¹ × 2⁴ × 2⁸
       = 2¹³
```

---

## 8. Why does recursion look different then?

Because recursion is using this mathematical identity:

#### Even n

$$
a^n = (a^{n/2})^2
$$

#### Odd n

$$
a^n = a \times (a^{\lfloor n/2\rfloor})^2
$$

For `13`:

$$
2^{13}
=
2 \times (2^6)^2
$$

For `6`:

$$
2^6 = (2^3)^2
$$

For `3`:

$$
2^3 = 2 \times (2^1)^2
$$

For `1`:

$$
2^1 = 2 \times (2^0)^2
$$

The recursive function is literally building this expression.

---

## 9. Iteration is doing the same mathematics in a different order

Recursive version:

```text
Calculate 2⁰
       ↓
Calculate 2¹
       ↓
Calculate 2³
       ↓
Calculate 2⁶
       ↓
Calculate 2¹³
```

Iterative version:

```text
Start with 1

Take 2¹ if needed
Square → 2²

Take 2² if needed
Square → 2⁴

Take 2⁴ if needed
Square → 2⁸

Take 2⁸ if needed
```

So:

#### Recursive

> "Tell me the answer for half the exponent, then I'll use it to calculate my answer."

#### Iterative

> "I'll progressively build the answer from the powers of 2."

---

## 10. A very useful way to think about it

There's actually a hidden **stack** in the recursive version.

For:

```python
power(2, 13)
```

the stack looks like:

```text
power(2, 13)
power(2, 6)
power(2, 3)
power(2, 1)
power(2, 0)
```

Then the stack unwinds:

```text
power(2, 0) → 1
power(2, 1) → 2
power(2, 3) → 8
power(2, 6) → 64
power(2, 13) → 8192
```

The iterative solution says:

> "I don't want the call stack. I'll maintain the necessary state myself."

That state is primarily:

```python
result
a
n
```

So you can think of the iterative solution as **removing the recursion stack and finding a different state representation that allows the work to be done while descending**.

---

## 11. One subtle but important point

The iterative algorithm isn't simply a mechanical translation of the recursive code.

For example, you **cannot** just take:

```python
half = power(a, n // 2)
```

and somehow replace it with:

```python
while n:
    ...
```

Instead, we recognize a deeper structure:

Recursive solution says:

$$
a^n
$$

can be constructed from powers:

$$
a^1,\;a^2,\;a^4,\;a^8,\ldots
$$

and the binary representation tells us which ones to multiply.

That insight gives us the iterative algorithm.

---

### The one sentence I'd remember

**Recursive exponentiation-by-squaring halves the exponent and lets the call stack remember the work; iterative exponentiation-by-squaring halves the exponent while using `result` to remember the work.**

Both exploit exactly the same fact:

$$
\boxed{a^{2k}=(a^k)^2}
$$

and

$$
\boxed{a^{2k+1}=a(a^k)^2}
$$

The **mathematics is identical**; only **where we store the intermediate state** is different.
