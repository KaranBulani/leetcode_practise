## Floyd–Warshall Algorithm

**Floyd–Warshall** finds the **shortest distance between every pair of vertices** in a weighted graph.

So unlike **Dijkstra**, which is usually used for one source:

```text
source → all vertices
```

Floyd–Warshall gives:

```text
every vertex → every other vertex
```

It works with **negative edge weights**, as long as there is **no negative cycle**.

---

### 1. Core idea

Suppose we want the shortest path from `i` to `j`.

Initially, we know the direct edge:

```text
dist[i][j]
```

Now consider whether going through some intermediate vertex `k` is better:

```text
i → k → j
```

Its cost is:

```text
dist[i][k] + dist[k][j]
```

Therefore:

```python
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

That's essentially the entire algorithm.

---

### 2. Why the three loops?

The implementation is:

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )
```

The important part is that **`k` is the outer loop**.

Think of `k` as:

> "I'm now allowing vertex `k` to be used as an intermediate vertex."

For example:

```text
k = 0
```

Allow vertex `0` as an intermediate.

Then:

```text
k = 1
```

Allow vertices `0, 1` as intermediates.

Then:

```text
k = 2
```

Allow vertices `0, 1, 2` as intermediates.

And so on.

So after finishing iteration `k`, `dist[i][j]` represents the shortest path from `i` to `j` using only vertices `0...k` as intermediate vertices.

That's the key DP idea behind Floyd–Warshall.

---

## 3. Python implementation

Let's say we have:

```text
0 --5--> 1
|        |
10       3
|        |
v        v
2 <------ 
```

More concretely:

```python
n = 3

INF = float("inf")

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

edges = [
    (0, 1, 5),
    (1, 2, 3),
    (0, 2, 10)
]

for u, v, weight in edges:
    dist[u][v] = weight
```

Initially:

```text
      0    1    2
0     0    5   10
1    INF   0    3
2    INF  INF   0
```

Now run Floyd–Warshall:

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )
```

When `k = 1`, we discover:

```text
0 → 1 → 2
```

which costs:

```text
5 + 3 = 8
```

This is better than the existing direct path:

```text
0 → 2 = 10
```

So:

```text
dist[0][2] = 8
```

Final matrix:

```text
      0    1    2
0     0    5    8
1    INF   0    3
2    INF  INF   0
```

---

## 4. Complete function

```python
def floyd_warshall(n, edges):
    INF = float("inf")

    # dist[i][j] = shortest distance from i to j
    dist = [[INF] * n for _ in range(n)]

    # Distance from a vertex to itself
    for i in range(n):
        dist[i][i] = 0

    # Direct edges
    for u, v, weight in edges:
        dist[u][v] = weight

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist
```

Example:

```python
edges = [
    (0, 1, 5),
    (1, 2, 3),
    (0, 2, 10)
]

print(floyd_warshall(3, edges))
```

Output:

```text
[
    [0, 5, 8],
    [inf, 0, 3],
    [inf, inf, 0]
]
```

---

## 5. The DP perspective

This is where Floyd–Warshall becomes easier to remember.

Define:

```text
dp[k][i][j]
```

as:

> shortest distance from `i` to `j` when vertices `0...k` are allowed as intermediate vertices.

For vertex `k`, there are only **two possibilities**:

### Don't use `k`

```text
dp[k-1][i][j]
```

### Use `k`

```text
dp[k-1][i][k] + dp[k-1][k][j]
```

Therefore:

```text
dp[k][i][j] =
    min(
        dp[k-1][i][j],
        dp[k-1][i][k] + dp[k-1][k][j]
    )
```

The clever part is that we don't actually need the `k` dimension.

We can update the same `dist` matrix in-place:

```python
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

That's why the implementation only needs **O(V²) space**.

---

## 6. Negative edges

Floyd–Warshall can handle negative edges.

For example:

```text
0 → 1 = 4
1 → 2 = -5
0 → 2 = 3
```

Then:

```text
0 → 1 → 2
= 4 + (-5)
= -1
```

So the algorithm correctly changes:

```text
dist[0][2] = 3
```

to:

```text
dist[0][2] = -1
```

### Negative cycle detection

After running the algorithm:

```python
for i in range(n):
    if dist[i][i] < 0:
        print("Negative cycle exists")
```

Why?

Normally:

```text
dist[i][i] = 0
```

But if we can start at `i`, follow a cycle, and return to `i` with negative total cost, then:

```text
dist[i][i] < 0
```

indicates a negative cycle.

---

## 7. Complexity

There are three nested loops:

```python
for k in range(V):
    for i in range(V):
        for j in range(V):
```

So:

**Time:**

```text
O(V³)
```

**Space:**

```text
O(V²)
```

because we maintain the `V × V` distance matrix.

---

### Floyd–Warshall vs Dijkstra

|                     | Floyd–Warshall | Dijkstra                   |
| ------------------- | -------------- | -------------------------- |
| Finds               | All pairs      | Single source              |
| Negative edges      | ✅              | ❌                          |
| Negative cycles     | Can detect     | ❌                          |
| Typical complexity  | `O(V³)`        | `O((V+E) log V)` with heap |
| Main data structure | Matrix         | Heap + adjacency list      |

**The one thing I'd remember for Floyd–Warshall is:**

> **For every possible intermediate vertex `k`, ask whether `i → k → j` is shorter than the current `i → j`.**

```python
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
```

That's Floyd–Warshall.
