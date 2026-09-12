## Dijkstra's Algorithm

**Dijkstra's algorithm finds the shortest distance from one source node to every other node in a weighted graph.**

The key conditions are:

* Edge weights must be **non-negative** (`>= 0`)
* Works for directed or undirected graphs
* Finds shortest paths from **one source** to all nodes

---

### 1. Example

Suppose we have:

```text
       4
   A ------ B
   |        |
  1|        |2
   |        |
   C ------ D
       3
```

Edges:

```text
A -> B = 4
A -> C = 1
C -> D = 3
B -> D = 2
```

Starting from `A`:

```text
A -> C = 1
A -> C -> D = 1 + 3 = 4
A -> B -> D = 4 + 2 = 6
```

So:

```text
A: 0
B: 4
C: 1
D: 4
```

The important thing is that Dijkstra **doesn't blindly explore every path**. It **repeatedly chooses the currently closest unprocessed node**.

---

# 2. Core idea

Let's maintain:

```python
dist[node]
```

which means:

> The shortest distance we currently know from the source to `node`.

Initially:

```text
dist[A] = 0
dist[B] = ∞
dist[C] = ∞
dist[D] = ∞
```

Why?

Because we know the distance from `A` to itself is `0`, but initially know nothing about the others.

Then repeatedly:

### Step 1: Pick the closest unprocessed node

From:

```text
A = 0
B = ∞
C = ∞
D = ∞
```

pick `A`.

### Step 2: Relax its edges

From `A`:

```text
A -> B = 4
A -> C = 1
```

So:

```text
B = 4
C = 1
```

Now:

```text
A = 0
B = 4
C = 1
D = ∞
```

### Step 3: Pick the closest unprocessed node

`C = 1`.

From `C`:

```text
C -> D = 3
```

Therefore:

```text
dist[D] = dist[C] + 3
        = 1 + 3
        = 4
```

Now:

```text
A = 0
B = 4
C = 1
D = 4
```

### Step 4: Pick the next closest

`B = 4` or `D = 4`.

Suppose we pick `B`.

From `B`:

```text
B -> D = 2
```

Potential distance to `D`:

```text
dist[B] + 2
= 4 + 2
= 6
```

But we already have:

```text
dist[D] = 4
```

So we don't change it.

Done.

---

# 3. What does "relax" mean?

This is the most important operation in Dijkstra.

Suppose we are currently processing:

```text
u
```

and there is an edge:

```text
u --weight--> v
```

We ask:

> Is going from source → `u` → `v` cheaper than the shortest route to `v` that I currently know?

Mathematically:

```python
dist[u] + weight < dist[v]
```

If yes:

```python
dist[v] = dist[u] + weight
```

For example:

```text
A -> C = 1
C -> D = 3
```

When processing `C`:

```python
dist[C] + 3 < dist[D]
```

becomes:

```python
1 + 3 < infinity
```

so:

```python
dist[D] = 4
```

This is called **relaxing the edge**.

---

# 4. Why do we need a priority queue?

We repeatedly need:

> Give me the unprocessed node with the smallest distance.

We could scan all nodes:

```python
min(dist)
```

but that's expensive.

Instead, we use a **min-heap / priority queue**.

Python provides:

```python
import heapq
```

We store:

```python
(distance, node)
```

For example:

```python
(0, "A")
(4, "B")
(1, "C")
```

The heap automatically gives us:

```text
(0, A)
(1, C)
(4, B)
```

in increasing distance order.

---

# 5. Python implementation

Here's the standard implementation:

```python
import heapq

def dijkstra(graph, source):
    dist = {node: float("inf") for node in graph}
    dist[source] = 0

    min_heap = [(0, source)]

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        # Ignore stale entry
        if curr_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = curr_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(min_heap, (new_dist, v))

    return dist
```

Graph:

```python
graph = {
    "A": [("B", 4), ("C", 1)],
    "B": [("D", 2)],
    "C": [("D", 3)],
    "D": []
}

print(dijkstra(graph, "A"))
```

Output:

```text
{'A': 0, 'B': 4, 'C': 1, 'D': 4}
```

---

# 6. Let's understand the code line-by-line

### Initialize distances

```python
dist = {node: float("inf") for node in graph}
```

Creates:

```python
{
    "A": inf,
    "B": inf,
    "C": inf,
    "D": inf
}
```

Then:

```python
dist[source] = 0
```

So:

```text
A = 0
B = ∞
C = ∞
D = ∞
```

---

### Initialize heap

```python
min_heap = [(0, source)]
```

If source is `A`:

```python
[(0, "A")]
```

The heap contains:

> "We need to process A, and the distance to A is 0."

---

### Get closest node

```python
curr_dist, u = heapq.heappop(min_heap)
```

Suppose we get:

```python
curr_dist = 1
u = "C"
```

That means:

> The currently closest node we want to process is C, whose known distance is 1.

---

### Check for stale entries

```python
if curr_dist > dist[u]:
    continue
```

This line initially looks weird, but it's **very important**.

Suppose we previously inserted:

```text
(10, D)
```

into the heap.

Later we discover a better route:

```text
(4, D)
```

So the heap can contain:

```text
(4, D)
(10, D)
```

We process `(4, D)` first and set:

```python
dist[D] = 4
```

Later `(10, D)` comes out.

But:

```python
curr_dist = 10
dist[D] = 4
```

Therefore:

```python
10 > 4
```

So:

```python
continue
```

We simply ignore the old/stale entry.

---

### Examine neighbors

```python
for v, weight in graph[u]:
```

Suppose:

```python
u = "C"
```

and:

```python
graph["C"] = [("D", 3)]
```

Then:

```text
v = D
weight = 3
```

---

### Calculate new distance

```python
new_dist = curr_dist + weight
```

If:

```text
C distance = 1
C -> D = 3
```

then:

```python
new_dist = 1 + 3
          = 4
```

---

### Relax

```python
if new_dist < dist[v]:
```

Currently:

```text
new_dist = 4
dist[D] = infinity
```

Therefore:

```python
dist[D] = 4
```

and put the new candidate into the heap:

```python
heapq.heappush(min_heap, (4, "D"))
```

---

# 7. The key intuition

The easiest way to remember Dijkstra is:

> **Always expand the node whose currently known distance from the source is smallest.**

And when expanding it:

> **Try to improve the distances of its neighbors.**

In pseudocode:

```text
distance[source] = 0

put source in priority queue

while priority queue isn't empty:

    take node with smallest distance

    for every neighbor:

        calculate:
            distance_to_current + edge_weight

        if this is better than our current answer:
            update neighbor's distance
            put neighbor in priority queue
```

---

# 8. Why is it actually correct?

This is the beautiful part of Dijkstra.

Suppose we select node `C` from the priority queue with:

```text
dist[C] = 5
```

and `C` is currently the closest unprocessed node.

Can there somehow be a hidden path to `C` with distance `3`?

For that path to exist, we would have to reach some earlier node `X` and then eventually reach `C`.

But if that path had total cost `3`, then `X` would have a distance **less than 5**.

Therefore `X` would have been selected before `C`.

When we processed `X`, we would have discovered the path toward `C`.

So by the time `C` is selected as the smallest-distance node, its distance cannot be improved.

**This reasoning only works because edge weights are non-negative.**

---

# 9. Why doesn't this work with negative weights?

Consider:

```text
A -> B = 5
A -> C = 10
C -> B = -10
```

Dijkstra might initially conclude:

```text
B = 5
C = 10
```

and process `B` because `5 < 10`.

But later:

```text
A -> C -> B
= 10 + (-10)
= 0
```

So the supposedly finalized `B = 5` should actually be:

```text
B = 0
```

That's why **Dijkstra requires non-negative edge weights**.

For graphs with negative edges, algorithms such as **Bellman-Ford** are used.

---

# 10. Complexity

With a binary heap:

```text
Time:  O((V + E) log V)
Space: O(V + E)
```

Usually you'll see the time complexity simplified to:

```text
O(E log V)
```

where:

* `V` = number of vertices/nodes
* `E` = number of edges

because for a connected graph `V^2 >= E >= V - 1`. So `E` is at least roughly as large as `V` or very dominating.

Think:

```text
Dijkstra
│
├── Visit/process vertices
│      V times
│      × log V heap operation for pop
│      = V log V
│
└── Examine edges
       E times
       │
       └── may cause heap push
              × log V
              = E log V
```

Therefore:

```text
V log V + E log V
        ↓
(V + E) log V
        ↓
E log V       # for connected graphs
```

---

## One important distinction

Dijkstra gives:

```text
source → every node
```

It is a **single-source shortest path** algorithm.

For example:

```text
       4
   A ------ B
   |
   1
   |
   C
```

If source is `A`:

```text
A → A = 0
A → B = 4
A → C = 1
```

If you want shortest paths **between every pair of nodes**, that's a different problem, for which algorithms like **Floyd-Warshall** or repeated Dijkstra can be used.

---

### The 3 things I'd memorize

If you're learning Dijkstra for LeetCode/interviews, focus on these:

```python
dist[source] = 0
```

**1. Start source at 0.**

```python
curr_dist, u = heappop(heap)
```

**2. Always process the currently closest node.**

```python
if curr_dist + weight < dist[v]:
    dist[v] = curr_dist + weight
    heappush(heap, (dist[v], v))
```

**3. Relax every outgoing edge.**

Once those three pieces make sense, the entire algorithm becomes much easier to recognize in coding problems.
