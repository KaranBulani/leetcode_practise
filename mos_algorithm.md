**Mo's Algorithm** is a technique for answering a large number of **range queries on a static array** efficiently.

The key idea is:

> Instead of answering every `[L, R]` query from scratch, **reorder the queries** so that the current range changes only a little between consecutive queries.

---

# 1. The problem Mo's Algorithm solves

Suppose:

```text
nums = [1, 2, 1, 3, 2, 4, 1]
```

and we have queries:

```text
[0, 3]
[2, 5]
[1, 6]
[0, 6]
```

Maybe we want to calculate:

> How many distinct numbers are in `nums[L:R+1]`?

Doing each query independently could cost `O(N)`:

```text
query 1 → scan [0..3]
query 2 → scan [2..5]
query 3 → scan [1..6]
...
```

With `Q` queries:

```text
O(N * Q)
```

Mo's algorithm tries to get this closer to:

```text
O((N + Q) * sqrt(N))
```

for many common range-query problems.

---

# 2. The central idea

Imagine we maintain a **current window**:

```text
          L         R
          ↓         ↓
nums = [1, 2, 1, 3, 2, 4, 1]
          └─────────┘
```

We maintain some information about this window.

For example:

```python
freq[x] = frequency of x inside [L, R]
distinct = number of values whose frequency > 0
```

Now suppose the next query is:

```text
[2, 5]
```

Instead of recalculating everything:

```text
old: [0, 3]
new:    [2, 5]
```

we simply:

```text
remove 0
remove 1
add 4
add 5
```

Only **4 elements changed**.

That's the entire philosophy behind Mo's Algorithm.

---

# 3. But queries come in arbitrary order

Suppose queries are:

```text
[0, 100]
[500, 600]
[10, 20]
[300, 400]
```

If we process them in that order, the window jumps around enormously.

For example:

```text
[0, 100]
      ↓
[500, 600]
```

requires ~1000 pointer movements.

So we **sort the queries intelligently**.

---

# 4. Divide the array into blocks

Choose:

```python
BLOCK_SIZE = int(sqrt(N))
```

Suppose:

```text
N = 16
BLOCK_SIZE = 4
```

Then divide indices into:

```text
Block 0:  0 1 2 3
Block 1:  4 5 6 7
Block 2:  8 9 10 11
Block 3: 12 13 14 15
```

For a query `[L, R]`, its block is:

```python
L // BLOCK_SIZE
```

---

# 5. Sort queries

The basic sorting rule is:

```python
queries.sort(key=lambda q: (q.L // BLOCK_SIZE, q.R))
```

Meaning:

1. Sort by the block containing `L`
2. Within the same block, sort by `R`

For example:

```text
queries:

[1, 10]
[3, 5]
[7, 8]
[4, 12]
[2, 6]
[9, 15]
```

might become:

```text
Block 0:
[3, 5]
[2, 6]
[1, 10]

Block 1:
[7, 8]
[4, 12]

Block 2:
[9, 15]
```

This causes `L` and `R` to move relatively little.

---

# 6. The four operations

This is the part you really need to understand.

Suppose current range is:

```text
[L, R]
```

and next query is:

```text
[l, r]
```

We transform the current range into the new range.

### Expand right

```python
while R < r:
    R += 1
    add(R)
```

### Shrink right

```python
while R > r:
    remove(R)
    R -= 1
```

### Expand left

```python
while L > l:
    L -= 1
    add(L)
```

### Shrink left

```python
while L < l:
    remove(L)
    L += 1
```

That's basically the entire implementation mechanism.

---

# 7. Complete example: Number of distinct elements

Let's solve:

> Given `nums` and many `[L, R]` queries, return the number of distinct elements in every range.

```python
from math import isqrt


def mos_algorithm(nums, queries):
    n = len(nums)
    q = len(queries)

    BLOCK_SIZE = isqrt(n)

    # (L, R, query_index)
    ordered_queries = [
        (l, r, i)
        for i, (l, r) in enumerate(queries)
    ]

    # Sort queries
    ordered_queries.sort(
        key=lambda x: (
            x[0] // BLOCK_SIZE,
            x[1]
        )
    )

    freq = {}
    distinct = 0

    ans = [0] * q

    L = 0
    R = -1

    def add(index):
        nonlocal distinct

        x = nums[index]

        freq[x] = freq.get(x, 0) + 1

        if freq[x] == 1:
            distinct += 1

    def remove(index):
        nonlocal distinct

        x = nums[index]

        freq[x] -= 1

        if freq[x] == 0:
            distinct -= 1

    for l, r, query_index in ordered_queries:

        while R < r:
            R += 1
            add(R)

        while R > r:
            remove(R)
            R -= 1

        while L < l:
            remove(L)
            L += 1

        while L > l:
            L -= 1
            add(L)

        ans[query_index] = distinct

    return ans
```

Example:

```python
nums = [1, 2, 1, 3, 2, 4, 1]

queries = [
    [0, 3],
    [2, 5],
    [1, 6],
    [0, 6]
]

print(mos_algorithm(nums, queries))
```

Output:

```text
[3, 4, 4, 4]
```

---

# 8. Why does `R = -1` initially?

This is a small but important detail.

We start with an **empty range**:

```text
L = 0
R = -1
```

because:

```text
[L, R] = [0, -1]
```

contains nothing.

For the first query:

```text
[0, 3]
```

we do:

```python
while R < 3:
    R += 1
    add(R)
```

giving:

```text
R = 0 → add(0)
R = 1 → add(1)
R = 2 → add(2)
R = 3 → add(3)
```

Now our maintained range is exactly:

```text
[0, 3]
```

---

# 9. Why does sorting help?

This is the most important conceptual part.

Suppose:

```text
BLOCK_SIZE = 3
```

and queries are:

```text
[0, 8]
[1, 2]
[2, 7]
[3, 5]
[4, 9]
[6, 8]
```

We sort approximately as:

```text
L block 0:
[1, 2]
[0, 8]
[2, 7]

L block 1:
[3, 5]
[4, 9]

L block 2:
[6, 8]
```

Notice:

### `L`

Within a block, `L` doesn't move much.

When we move to another block, it moves approximately `BLOCK_SIZE`.

### `R`

Within a block, `R` moves in sorted order:

```text
2 → 8 → 7
```

Then in the next block:

```text
5 → 9
```

So the total amount of movement is much smaller than processing arbitrary queries.

---

# 10. Why is the complexity approximately `O((N + Q)√N)`?

Let:

```text
B = √N
```

There are approximately:

```text
N / B = √N
```

blocks.

### Movement of L

Within each block, `L` moves at most `B`.

Across `Q` queries:

```text
O(QB)
```

### Movement of R

For each block, `R` can travel across roughly `N`.

There are `N/B` blocks:

```text
O(N * N/B)
```

With `B = √N`:

```text
O(N√N)
```

Therefore:

```text
O(Q√N + N√N)
```

or:

```text
O((N + Q)√N)
```

assuming `add()` and `remove()` are `O(1)`.

---

# 11. The `add()` / `remove()` abstraction is the secret

This is what makes Mo's Algorithm useful for many different problems.

The Mo framework stays almost identical.

Only these functions change:

```python
def add(index):
    ...

def remove(index):
    ...
```

For example, if the query asks:

### Number of distinct values

```python
freq[x]
distinct
```

### Frequency of the most common value

```python
freq[x]
max_frequency
```

### Sum of elements

```python
current_sum += nums[index]
```

```python
current_sum -= nums[index]
```

### Sum of squares

```python
current += nums[index] ** 2
```

### Number of values occurring exactly twice

You can maintain:

```python
freq[x]
count_freq_2
```

and update it in `add()` / `remove()`.

---

# 12. A useful mental model

Think of Mo's Algorithm as having **three layers**:

```text
                 MO'S ALGORITHM
                       │
          ┌────────────┴────────────┐
          │                         │
     Query ordering            Window state
          │                         │
    sort by blocks             [L, R]
                                    │
                         ┌──────────┴──────────┐
                         │                     │
                       add()                remove()
```

The algorithm doesn't really "solve" the query itself.

Instead:

> **Mo's Algorithm efficiently maintains the answer while `[L, R]` changes.**

That's the key insight.

---

# 13. When should you think of Mo's Algorithm?

A good pattern to recognize is:

```text
Static array
+
Many range queries
+
Each query can be maintained using add/remove
+
No updates to the array
```

Then Mo's Algorithm is a candidate.

For example:

```text
"How many distinct numbers are in nums[L:R]?"
"How many numbers occur exactly twice?"
"What is the sum of some property over nums[L:R]?"
"How many pairs satisfy some condition inside [L,R]?"
```

---

# 14. When NOT to use it

If you have:

```text
range sum
```

then prefix sums are much simpler:

```text
prefix[R + 1] - prefix[L]
```

If you have:

```text
range sum + point updates
```

then Fenwick Tree / Segment Tree is usually better.

Mo's Algorithm is particularly interesting when the query's answer is **hard to compute directly**, but easy to maintain when adding/removing one element.

---

## The pattern to memorize

For LeetCode-style problems, I would memorize this skeleton:

```python
B = isqrt(n)

queries.sort(key=lambda q: (q.l // B, q.r))

L = 0
R = -1

for l, r, idx in queries:

    while R < r:
        R += 1
        add(R)

    while R > r:
        remove(R)
        R -= 1

    while L < l:
        remove(L)
        L += 1

    while L > l:
        L -= 1
        add(L)

    ans[idx] = current_answer
```

The **hard part isn't this code**.

The hard part is recognizing:

> **"Can I maintain my answer in O(1) when one element enters/leaves the range?"**

If yes, Mo's Algorithm is often worth considering.
