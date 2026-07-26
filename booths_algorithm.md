There are **two completely different algorithms** named after Booth:

1. **Booth's Multiplication Algorithm** (used in computer architecture for multiplying signed binary numbers)
2. **Booth's String Algorithm** (used to find the lexicographically smallest rotation of a string)

Since you asked for **Booth's String Algorithm**, let's focus on that.

---

# Problem

Given a string, imagine rotating it in every possible way.

Example:

```
s = "baca"

Rotations:

baca
acab
caba
abac
```

The lexicographically smallest one is

```
abac
```

We want its starting index.

Brute force:

* Generate all N rotations
* Compare them

Time:

```
O(N²)
```

Booth's algorithm solves it in

```
O(N)
```

---

# Core Idea

Instead of comparing **every rotation with every other rotation**, Booth eliminates rotations that **can never be the smallest**.

Think of it as a tournament.

If rotation A loses to rotation B,

then **many rotations near A also lose immediately**.

Those can be skipped.

This skipping is why it becomes linear.

---

# Step 1 — Duplicate the string

```
s = "baca"

s2 = "bacabaca"
```

Why?

Because every rotation becomes a substring of length N.

For example

```
rotation 2:

caba

=

s2[2 : 2+4]
```

No modular arithmetic is needed anymore.

---

# Step 2 — Two Candidates

Maintain

```
i = first candidate
j = second candidate
```

Initially

```
i = 0
j = 1
```

Meaning we're comparing

```
rotation starting at 0

vs

rotation starting at 1
```

---

# Step 3 — Compare Character by Character

Variable

```
k
```

means

```
How many characters matched so far?
```

Initially

```
k = 0
```

Compare

```
s2[i+k]

vs

s2[j+k]
```

---

Suppose

```
s = "baca"

i = 0
j = 1
```

Compare

```
rotation 0

b a c a

rotation 1

a c a b
```

First character

```
b

vs

a
```

Mismatch immediately.

---

# Which Rotation Loses?

Since

```
b > a
```

rotation 0 is larger.

Therefore

```
rotation 0
```

can never be the answer.

Move

```
i
```

forward.

---

# Here's the Clever Part

Suppose instead we had matched several characters first.

Imagine

```
abcdef...

abcxef...
```

They match for

```
k = 3
```

Then differ.

We already know

```
first 3 characters identical
```

Only the fourth differs.

That tells us something powerful.

---

Suppose

```
rotation i loses
```

after matching

```
k
```

characters.

Then **every rotation starting between**

```
i

and

i+k
```

also loses.

They all share the same matched prefix.

So instead of

```
i += 1
```

we do

```
i += k + 1
```

This is the magic.

Many candidates disappear at once.

---

# Why is that Safe?

Imagine

```
banana
```

Comparing two rotations

```
banana

ananab
```

Suppose they matched

```
3
```

characters.

If

```
banana
```

loses,

then

```
rotation starting one character later
rotation starting two characters later
rotation starting three characters later
```

all inherit the same losing prefix.

None can suddenly become smallest.

Hence skip them.

This is the entire optimization.

---

# Why Reset k?

After moving

```
i
```

or

```
j
```

we're comparing completely different rotations.

Previous comparisons no longer matter.

So

```
k = 0
```

---

# Example

Take

```
s = "caba"
```

Rotations

```
0 caba
1 abac
2 baca
3 acab
```

Answer should be

```
1
```

---

Initially

```
i = 0
j = 1
k = 0
```

Compare

```
c

a
```

Since

```
c > a
```

rotation

```
0
```

loses.

Move

```
i = 1
```

Now

```
i == j
```

so

```
j++
```

Now

```
i = 1
j = 2
```

Compare

```
abac

baca
```

```
a < b
```

Rotation

```
2
```

loses.

Move

```
j = 3
```

Compare

```
abac

acab
```

First character

```
a == a
```

Second

```
b > c ?

No

b < c
```

Rotation

```
3
```

loses.

Done.

Winner

```
1
```

---

# The Algorithm

```python
def booth(s):
    if not s:
        return 0

    s2 = s + s
    n = len(s)

    i = 0
    j = 1
    k = 0

    while i < n and j < n and k < n:

        if s2[i + k] == s2[j + k]:
            k += 1

        elif s2[i + k] > s2[j + k]:
            # rotation i loses
            i += k + 1

            if i <= j:
                i = j + 1

            k = 0

        else:
            # rotation j loses
            j += k + 1

            if j <= i:
                j = i + 1

            k = 0

    return min(i, j)
```

---

# Why Is It O(N)?

At first glance, there are nested operations (`i`, `j`, and `k`), so it might look quadratic.

The key observation is:

* `i` only moves forward and never backward.
* `j` only moves forward and never backward.
* Every mismatch advances either `i` or `j` by at least `k + 1`, skipping over candidates permanently.
* `k` increases only while characters match, and whenever a mismatch occurs it resets to `0`. The matched characters are never reprocessed in the same way because one side of the comparison is advanced past the matched prefix.

Since `i` and `j` can each advance at most `n` positions, the total amount of work is proportional to `n`.

Therefore:

* **Time:** `O(n)`
* **Space:** `O(n)` for the duplicated string (`s + s`). (If modular indexing is used instead of creating `s2`, the extra space can be reduced to `O(1)`.)

---

# Intuition to Remember

Think of Booth's algorithm as a **competition between rotations**:

* Two rotations race character by character.
* The first differing character decides the loser.
* If they matched for `k` characters before losing, then **all rotations starting within that matched prefix are guaranteed losers too**.
* Eliminate them all at once by jumping `k + 1` positions.

That single observation—eliminating many candidates after one comparison—is what turns the naive `O(n²)` approach into an `O(n)` algorithm.
