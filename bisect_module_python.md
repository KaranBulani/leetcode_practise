## `bisect` in Python 

Python's `bisect` module is mainly useful for **binary search on a sorted array**.

```python
import bisect
```

### 1. `bisect_left(arr, x)`

Returns the **first position where `x` can be inserted** while keeping `arr` sorted.

```python
arr = [1, 2, 2, 2, 5]

bisect.bisect_left(arr, 2)   # 1
bisect.bisect_left(arr, 3)   # 4
```

Think:

> **first index `>= x`**

Equivalent concept:

```text
[1, 2, 2, 2, 5]
    ↑
    first position >= 2
```

---

### 2. `bisect_right(arr, x)`

Returns the **position after all existing `x`s**.

```python
arr = [1, 2, 2, 2, 5]

bisect.bisect_right(arr, 2)  # 4
bisect.bisect_right(arr, 3)  # 4
```

Think:

> **first index `> x`**

---

### The most important difference

```python
arr = [1, 2, 2, 2, 5]

bisect_left(arr, 2)   # 1
bisect_right(arr, 2)  # 4
```

So:

```text
bisect_left   → first >= x
bisect_right  → first >  x
```

---

### 3. `insort`

Inserts an element while maintaining sorted order.

```python
arr = [1, 3, 5]

bisect.insort(arr, 4)

print(arr)
# [1, 3, 4, 5]
```

Usually **less important for LeetCode**, because insertion itself is `O(n)`.

---

## Common LeetCode patterns

### Check if `x` exists

```python
i = bisect.bisect_left(arr, x)

if i < len(arr) and arr[i] == x:
    # x exists
```

### Count occurrences of `x`

```python
count = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)
```

### Find first element `>= x`

```python
i = bisect.bisect_left(arr, x)
```

### Find first element `> x`

```python
i = bisect.bisect_right(arr, x)
```

### Find last element `<= x`

```python
i = bisect.bisect_right(arr, x) - 1
```

---

### One thing to remember

`bisect` **assumes the array is already sorted**.

```text
bisect_left  → >=
bisect_right → >
```

If you remember just that, you can solve a large number of LeetCode binary-search problems.
