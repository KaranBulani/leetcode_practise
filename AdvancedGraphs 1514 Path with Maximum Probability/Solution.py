'''
This is essentially Dijkstra's algorithm, except instead of minimizing distance, we're maximizing probability.

For each node, maintain:
	prob[node] = maximum probability with which we can reach node

When we're at node u and take an edge with probability p to v:
	new_prob = prob[u] * p

If new_prob is better than the current prob[v], update it.
####################################################################################################

How to think about it

Suppose we have:

0 --0.5-- 1 --0.5-- 2
 \                 /
  ------0.2--------

Starting from 0:
	prob[0] = 1

	0 -> 1:
	1 * 0.5 = 0.5

	1 -> 2:
	0.5 * 0.5 = 0.25

	0 -> 2:
	1 * 0.2 = 0.2


So:
	prob[2] = 0.25

The key difference from normal Dijkstra is:

| Normal Dijkstra                    | Maximum Probability                          |
| ---------------------------------- | -------------------------------------------- |
| new_dist = dist[u] + edge_weight   | new_prob = prob[u] * edge_prob               |
| Pick smallest distance             | Pick largest probability                     |
| Min-heap                           | Max-heap (implemented using negative values) |

####################################################################################################
Why Dijkstra works here

Every edge probability is between 0 and 1.

Therefore, extending a path can only decrease or maintain its probability:
	probability * edge_probability <= probability

So when we pop the node with the highest probability from the heap, we can safely finalize it, exactly like Dijkstra finalizes the smallest-distance node.

####################################################################################################
Complexity

Building the graph: O(E)

Each node/edge can cause heap operations, giving:

Time:  O((V + E) log V)
Space: O(V + E)

The most important thing to remember is:
	> Dijkstra = optimize a path where extending a path combines the current value with the edge value.

Here the combination operation is multiplication instead of addition.
'''
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i, (u, v) in enumerate(edges):
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))

        # prob[node] = best probability found so far
        prob = [0.0] * n
        prob[start_node] = 1.0

        # Python heap is a min-heap, so use negative probability
        heap = [(-1.0, start_node)]

        while heap:
            curr_prob, u = heapq.heappop(heap)
            curr_prob = -curr_prob

            # We already have a better path to u
            if curr_prob < prob[u]:
                continue

            if u == end_node:
                return curr_prob

            for v, edge_prob in graph[u]:
                new_prob = curr_prob * edge_prob

                if new_prob > prob[v]:
                    prob[v] = new_prob
                    heapq.heappush(heap, (-new_prob, v))

        return 0.0


if __name__ == "__main__":
    solution = Solution()

    # ---------------------------------------------------------
    # Example 1: Best path uses multiple edges
    # 0 -> 1 -> 2 = 0.5 * 0.5 = 0.25
    # Direct path 0 -> 2 = 0.2
    # Expected: 0.25
    # ---------------------------------------------------------
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 1:", result)  # Expected: 0.25

    # ---------------------------------------------------------
    # Example 2: Direct path is better
    # Direct: 0 -> 2 = 0.3
    # Via 1: 0.5 * 0.5 = 0.25
    # Expected: 0.3
    # ---------------------------------------------------------
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.3]
    start = 0
    end = 2

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 2:", result)  # Expected: 0.3

    # ---------------------------------------------------------
    # Example 3: No path
    # 0 and 2 are disconnected
    # Expected: 0.0
    # ---------------------------------------------------------
    n = 3
    edges = [[0, 1]]
    succProb = [0.5]
    start = 0
    end = 2

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 3:", result)  # Expected: 0.0

    # ---------------------------------------------------------
    # Test 4: Simple single edge
    # Expected: 0.8
    # ---------------------------------------------------------
    n = 2
    edges = [[0, 1]]
    succProb = [0.8]
    start = 0
    end = 1

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 4:", result)  # Expected: 0.8

    # ---------------------------------------------------------
    # Test 5: Longer path is the best
    #
    # 0 -> 1 -> 2 -> 3
    # = 0.9 * 0.9 * 0.9 = 0.729
    #
    # Direct: 0 -> 3 = 0.5
    #
    # Expected: 0.729
    # ---------------------------------------------------------
    n = 4
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [0, 3]
    ]
    succProb = [0.9, 0.9, 0.9, 0.5]
    start = 0
    end = 3

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 5:", result)  # Expected: 0.729

    # ---------------------------------------------------------
    # Test 6: Zero probability edge
    #
    # 0 -> 1 has probability 0
    # 0 -> 2 -> 1 = 0.5 * 0.5 = 0.25
    #
    # Expected: 0.25
    # ---------------------------------------------------------
    n = 3
    edges = [
        [0, 1],
        [0, 2],
        [2, 1]
    ]
    succProb = [0.0, 0.5, 0.5]
    start = 0
    end = 1

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 6:", result)  # Expected: 0.25

    # ---------------------------------------------------------
    # Test 7: Probability 1 edges
    #
    # 0 -> 1 -> 2 -> 3
    # = 1 * 1 * 1 = 1
    #
    # Expected: 1.0
    # ---------------------------------------------------------
    n = 4
    edges = [
        [0, 1],
        [1, 2],
        [2, 3]
    ]
    succProb = [1.0, 1.0, 1.0]
    start = 0
    end = 3

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 7:", result)  # Expected: 1.0

    # ---------------------------------------------------------
    # Test 8: Need to choose between several paths
    #
    # Path A: 0 -> 1 -> 4
    # = 0.9 * 0.5 = 0.45
    #
    # Path B: 0 -> 2 -> 4
    # = 0.8 * 0.8 = 0.64
    #
    # Path C: 0 -> 3 -> 4
    # = 0.7 * 0.9 = 0.63
    #
    # Expected: 0.64
    # ---------------------------------------------------------
    n = 5
    edges = [
        [0, 1],
        [1, 4],
        [0, 2],
        [2, 4],
        [0, 3],
        [3, 4]
    ]
    succProb = [
        0.9,
        0.5,
        0.8,
        0.8,
        0.7,
        0.9
    ]
    start = 0
    end = 4

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 8:", result)  # Expected: 0.64

    # ---------------------------------------------------------
    # Test 9: Start has several choices, but only one leads
    # to the optimal probability
    #
    # 0 -> 1 -> 3 = 0.5 * 0.9 = 0.45
    # 0 -> 2 -> 3 = 0.8 * 0.8 = 0.64
    #
    # Expected: 0.64
    # ---------------------------------------------------------
    n = 4
    edges = [
        [0, 1],
        [1, 3],
        [0, 2],
        [2, 3]
    ]
    succProb = [0.5, 0.9, 0.8, 0.8]
    start = 0
    end = 3

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 9:", result)  # Expected: 0.64

    # ---------------------------------------------------------
    # Test 10: Disconnected graph with multiple components
    #
    # Component 1: 0 -- 1 -- 2
    # Component 2: 3 -- 4
    #
    # No path from 0 to 4
    #
    # Expected: 0.0
    # ---------------------------------------------------------
    n = 5
    edges = [
        [0, 1],
        [1, 2],
        [3, 4]
    ]
    succProb = [0.5, 0.8, 0.9]
    start = 0
    end = 4

    result = solution.maxProbability(n, edges, succProb, start, end)
    print("Test 10:", result)  # Expected: 0.0