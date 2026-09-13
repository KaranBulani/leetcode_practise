## Bellman-Ford Algorithm

**Bellman-Ford** is a shortest-path algorithm used to find the shortest distance from **one source vertex to every other vertex** in a weighted graph.

Its biggest advantage over Dijkstra is:

> **Bellman-Ford can handle negative edge weights.**

It can also detect **negative-weight cycles** reachable from the source.

---

### 1. Example

Suppose we have this directed graph:

```text
       4
   A ------> B
   |         |
  5|        -2
   ↓         ↓
   C <------ D
       -3
```

Edges:

```python
edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "D", -2),
    ("D", "C", -3),
]
```

Starting from `A`:

```text
A → B = 4

A → B → D = 4 + (-2) = 2

A → B → D → C = 2 + (-3) = -1
```

So:

```text
distance[A] = 0
distance[B] = 4
distance[D] = 2
distance[C] = -1
```

---

# 2. The core idea: Relax every edge

The most important concept in Bellman-Ford is **relaxation**.

Suppose we know:

```text
distance[u] = 5
```

and there is an edge:

```text
u ----(-3)----> v
```

Then going through `u` gives:

```text
distance[v] = distance[u] + weight
            = 5 + (-3)
            = 2
```

So if:

```python
distance[v] > distance[u] + weight:
```

we update it:

```python
distance[v] = distance[u] + weight
```

This is called **relaxing the edge**.

---

# 3. Why do we repeat this?

Suppose:

```text
A → B → C → D
```

and:

```text
A → B = 5
B → C = 2
C → D = 3
```

Initially:

```text
dist[A] = 0
dist[B] = ∞
dist[C] = ∞
dist[D] = ∞
```

We process the edges.

### First pass

```text
A → B
```

gives:

```text
dist[B] = 5
```

Then:

```text
B → C
```

can use the newly discovered `B`:

```text
dist[C] = 5 + 2 = 7
```

Then:

```text
C → D
```

gives:

```text
dist[D] = 7 + 3 = 10
```

So one pass can sometimes propagate the distance through the entire graph.

But we **cannot rely on the ordering of edges**.

For example, if the edges were processed in this order:

```text
C → D
B → C
A → B
```

then the first pass would only discover `B`.

The next pass discovers `C`.

The next pass discovers `D`.

Therefore, Bellman-Ford simply says:

> **Relax every edge `V - 1` times.**

---

# 4. Why exactly `V - 1` times?

This is the key insight.

If there is **no negative cycle**, the shortest path to a vertex can contain at most:

```text
V - 1 edges
```

because a path containing `V` or more edges must repeat some vertex.

For example, with 4 vertices:

```text
A → B → C → D
```

has at most:

```text
3 = V - 1
```

edges.

Each iteration of Bellman-Ford can effectively propagate the shortest path by another edge.

Therefore:

```text
V - 1 iterations
```

are sufficient.

---

# 5. Python implementation

Let's implement it using an edge list.

```python
def bellman_ford(vertices, edges, source):
    INF = float("inf")

    # Initially, every vertex is unreachable
    dist = {v: INF for v in vertices}

    # Distance from source to itself is 0
    dist[source] = 0

    # Relax every edge V - 1 times
    for _ in range(len(vertices) - 1):

        for u, v, weight in edges:

            if dist[u] != INF:
                dist[v] = min(
                    dist[v],
                    dist[u] + weight
                )

    return dist
```

Example:

```python
vertices = ["A", "B", "C", "D"]

edges = [
    ("A", "B", 4),
    ("A", "C", 5),
    ("B", "D", -2),
    ("D", "C", -3),
]

print(bellman_ford(vertices, edges, "A"))
```

Output:

```text
{'A': 0, 'B': 4, 'C': -1, 'D': 2}
```

---

# 6. Why do we check `dist[u] != INF`?

This line:

```python
if dist[u] != INF:
```

is important.

Suppose:

```text
A → B
C → D
```

and source is `A`.

Initially:

```text
dist[A] = 0
dist[B] = ∞
dist[C] = ∞
dist[D] = ∞
```

There is no way to reach `C` from `A`.

So when processing:

```text
C → D
```

we shouldn't do:

```python
dist[D] = dist[C] + weight
```

because:

```text
∞ + weight
```

doesn't represent an actual path.

Hence:

```python
if dist[u] != INF:
```

means:

> Only use an edge if we can actually reach its starting vertex.

---

# 7. Negative cycle detection

This is another major feature of Bellman-Ford.

Consider:

```text
A → B = 1
B → C = 2
C → A = -5
```

Going around the cycle:

```text
A → B → C → A
```

costs:

```text
1 + 2 - 5 = -2
```

Every time we go around the cycle, the distance becomes smaller:

```text
A = 0
A = -2
A = -4
A = -6
...
```

So there is no finite shortest distance.

We can detect this by doing **one extra iteration** after the normal `V - 1` iterations.

```python
for u, v, weight in edges:
    if dist[u] != INF and dist[u] + weight < dist[v]:
        print("Negative cycle detected")
```

If an edge can **still be relaxed**, then there is a reachable negative cycle.

---

# 8. Complete implementation

```python
def bellman_ford(vertices, edges, source):
    INF = float("inf")

    dist = {v: INF for v in vertices}
    dist[source] = 0

    # V - 1 iterations
    for _ in range(len(vertices) - 1):

        changed = False

        for u, v, weight in edges:

            if dist[u] != INF and dist[u] + weight < dist[v]:

                dist[v] = dist[u] + weight
                changed = True

        # Optimization:
        # If nothing changed, we're already done.
        if not changed:
            break

    # Check for negative cycle
    for u, v, weight in edges:

        if dist[u] != INF and dist[u] + weight < dist[v]:
            return None  # Negative cycle exists

    return dist
```

---

# 9. Bellman-Ford vs Dijkstra

This is probably the most important comparison to remember:

|                          | Bellman-Ford               | Dijkstra                     |
| ------------------------ | -------------------------- | ---------------------------- |
| Negative edges           | ✅ Yes                      | ❌ No                         |
| Negative cycle detection | ✅ Yes                      | ❌ No                         |
| Time                     | `O(VE)`                    | `O((V + E) log V)` with heap |
| Usually faster           | ❌                          | ✅                            |
| Main technique           | Relax all edges repeatedly | Greedy + priority queue      |

So the rule of thumb is:

```text
No negative weights
        ↓
   Dijkstra
```

```text
Negative weights possible
        ↓
   Bellman-Ford
```

---

## 10. The mental model

If you want to remember Bellman-Ford intuitively, think:

> **"Keep giving every edge a chance to improve the answer."**

For every edge:

```python
u ----weight----> v
```

ask:

```python
Can I reach v cheaper by going through u?
```

which is:

```python
if dist[u] + weight < dist[v]:
    dist[v] = dist[u] + weight
```

Repeat this `V - 1` times.

Then do it **once more**:

```text
Still improving?
     ↓
   Yes
     ↓
Negative cycle
```

That's essentially the entire Bellman-Ford algorithm.
