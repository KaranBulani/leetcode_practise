'''
Key idea

We have a directed weighted graph:

* n = number of nodes
* times[i] = [u, v, w] means u → v takes w time
* Signal starts at node k
* We need the minimum time required to reach every node
* The answer is the maximum of those minimum times
* If even one node is unreachable → -1

Why maximum?

Suppose the shortest times from k are:
	node 1 → 0
	node 2 → 2
	node 3 → 5
	node 4 → 3

The signal reaches:
* node 2 at time 2
* node 4 at time 3
* node 3 at time 5

So the entire network has received the signal at time 5.

####################################################################################################

Walk through an example

	times = [
		[2, 1, 1],
		[2, 3, 1],
		[3, 4, 1]
	]
	n = 4
	k = 2


Graph:
		   1
	   2 ────→ 1
	   │
	   │1
	   ↓
	   3 ────→ 4
		   1

Starting from 2:
	dist[2] = 0
	dist[1] = 1
	dist[3] = 1
	dist[4] = 2

Therefore:
	max(dist.values())
	= max(0, 1, 1, 2)
	= 2

Answer:		2

####################################################################################################

Why Dijkstra works here

At any point, the heap gives us the node with the smallest currently known arrival time.

When we pop:
	time, node = heappop(heap)

we try to improve all of its outgoing edges:
	new_time = time + weight

If this gives a shorter route:
	if neighbor not in dist or new_time < dist[neighbor]:

we update it and push it into the heap.

Because all edge weights are non-negative, once the smallest-time node is popped, we can safely use it to build shortest paths.

####################################################################################################

Complexity

There are:
* V = n vertices
* E = len(times) edges

With a binary heap:
	Time:  O((V + E) log V)
	Space: O(V + E)

In practice, you'll often see the time complexity written as:
	O(E log V)
for this implementation.

The important pattern to remember for LeetCode:

> "Shortest path from one source → positive edge weights → Dijkstra → after finding all shortest distances, take the maximum."

'''
from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        # Build adjacency list
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # Shortest known distance from k to every node
        dist = {k: 0}

        # (time, node)
        heap = [(0, k)]

        while heap:
            time, node = heappop(heap)

            # Ignore stale heap entries
            if time > dist[node]:
                continue

            for neighbor, weight in graph[node]:

                new_time = time + weight

                if neighbor not in dist or new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heappush(heap, (new_time, neighbor))

        # Not all nodes were reachable
        if len(dist) != n:
            return -1

        # Last node to receive the signal
        return max(dist.values())



if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ---------------------------------------------------------
        # DiverseExamplesFromQuestion
        # ---------------------------------------------------------

        # Example 1
        {
            "times": [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
            "n": 4,
            "k": 2,
            "expected": 2
        },

        # Example 2
        {
            "times": [[1, 2, 1]],
            "n": 2,
            "k": 1,
            "expected": 1
        },

        # Example 3
        {
            "times": [[1, 2, 1]],
            "n": 2,
            "k": 2,
            "expected": -1
        },

        # ---------------------------------------------------------
        # Edge Cases
        # ---------------------------------------------------------

        # Single node
        {
            "times": [],
            "n": 1,
            "k": 1,
            "expected": 0
        },

        # Two nodes, direct connection
        {
            "times": [[1, 2, 5]],
            "n": 2,
            "k": 1,
            "expected": 5
        },

        # Source has no outgoing edges and there are other nodes
        {
            "times": [],
            "n": 3,
            "k": 1,
            "expected": -1
        },

        # Zero-weight edge
        {
            "times": [[1, 2, 0], [2, 3, 0]],
            "n": 3,
            "k": 1,
            "expected": 0
        },

        # ---------------------------------------------------------
        # Multiple paths - choose the shorter one
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 10],
                [1, 3, 2],
                [3, 2, 3]
            ],
            "n": 3,
            "k": 1,
            "expected": 5
        },

        # Shortest path to 4 is 1 -> 2 -> 4
        {
            "times": [
                [1, 2, 1],
                [1, 3, 10],
                [2, 3, 2],
                [2, 4, 3],
                [3, 4, 1]
            ],
            "n": 4,
            "k": 1,
            "expected": 4
        },

        # ---------------------------------------------------------
        # Directed graph
        # ---------------------------------------------------------

        # Reverse direction does NOT work
        {
            "times": [
                [2, 1, 5]
            ],
            "n": 2,
            "k": 1,
            "expected": -1
        },

        # Directed chain
        {
            "times": [
                [1, 2, 1],
                [2, 3, 2],
                [3, 4, 3],
                [4, 5, 4]
            ],
            "n": 5,
            "k": 1,
            "expected": 10
        },

        # ---------------------------------------------------------
        # Source is in the middle of the graph
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 1],
                [2, 3, 2],
                [3, 4, 3],
                [4, 5, 4]
            ],
            "n": 5,
            "k": 3,
            "expected": -1
        },

        {
            "times": [
                [1, 2, 1],
                [2, 3, 2],
                [3, 4, 3],
                [4, 5, 4],
                [3, 1, 10]
            ],
            "n": 5,
            "k": 3,
            "expected": 10
        },

        # ---------------------------------------------------------
        # Cycles
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 1],
                [2, 3, 1],
                [3, 1, 1],
                [3, 4, 2]
            ],
            "n": 4,
            "k": 1,
            "expected": 4
        },

        # Cycle with zero weights
        {
            "times": [
                [1, 2, 0],
                [2, 3, 0],
                [3, 1, 0],
                [3, 4, 5]
            ],
            "n": 4,
            "k": 1,
            "expected": 5
        },

        # ---------------------------------------------------------
        # One node is disconnected
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 1],
                [2, 3, 1],
                [3, 4, 1]
            ],
            "n": 5,
            "k": 1,
            "expected": -1
        },

        # ---------------------------------------------------------
        # Star graph
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 5],
                [1, 3, 2],
                [1, 4, 8],
                [1, 5, 3]
            ],
            "n": 5,
            "k": 1,
            "expected": 8
        },

        # ---------------------------------------------------------
        # Need to find shortest paths before determining max
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 100],
                [1, 3, 1],
                [3, 2, 1],
                [2, 4, 1],
                [3, 4, 100]
            ],
            "n": 4,
            "k": 1,
            "expected": 3
        },

        # ---------------------------------------------------------
        # Larger graph
        # ---------------------------------------------------------

        {
            "times": [
                [1, 2, 4],
                [1, 3, 2],
                [2, 3, 5],
                [2, 4, 10],
                [3, 2, 1],
                [3, 4, 3],
                [4, 5, 2],
                [2, 5, 20],
                [5, 6, 1],
                [4, 6, 10]
            ],
            "n": 6,
            "k": 1,
            "expected": 8
        },
    ]

    # -------------------------------------------------------------
    # Run all tests
    # -------------------------------------------------------------

    for i, test in enumerate(test_cases, 1):

        result = solution.networkDelayTime(
            test["times"],
            test["n"],
            test["k"]
        )

        if result == test["expected"]:
            print(f"Test {i}: PASS")
        else:
            print(f"Test {i}: FAIL")
            print(f"  Input:    times={test['times']}, n={test['n']}, k={test['k']}")
            print(f"  Expected: {test['expected']}")
            print(f"  Got:      {result}")