'''
Intuition

We need to create a deep copy of the graph.
For every original node:
* Create a new node with the same value.
* Connect cloned neighbors instead of original neighbors.

The challenge is:
* Graphs can contain cycles.
* Multiple nodes may point to the same node.
So if we blindly recurse, we'll keep revisiting nodes forever.

We need a hashmap: old_to_new = {}
which stores: original_node -> cloned_node

This lets us:
1. Avoid infinite loops.
2. Reuse already-created cloned nodes.

####################################################################################################

DFS Approach

Suppose we are cloning node 1.

* Step 1
Create clone: clone_node = Node(1)
Store: old_to_new[original_1] = clone_node

* Step 2
Visit each neighbor.
For neighbor 2: clone_neighbor = clone(original_2)
Append it: clone_node.neighbors.append(clone_neighbor)

* Step 3
If we later encounter node 1 again because of a cycle:

if node in old_to_new:
    return old_to_new[node]

We immediately return the existing clone.

####################################################################################################

Algorithm

For each node:

* Base Case
Already cloned:
if node in old_to_new:
    return old_to_new[node]

* Create Clone
copy = Node(node.val)
old_to_new[node] = copy

* Clone Neighbors
for neighbor in node.neighbors:
    copy.neighbors.append(clone(neighbor))

* Return Clone
return copy

####################################################################################################

Dry Run

Graph:
1 -- 2
|    |
4 -- 3

Start: clone(1)
Create: 1'
Store: {1: 1'}

Visit neighbor 2: clone(2)
Create: 2'
Store: {1:1', 2:2'}

Visit neighbor 3: clone(3)
Create: 3'
Store: {1:1', 2:2', 3:3'}

Visit neighbor 4: clone(4)
Create: 4'
Store: {1:1', 2:2', 3:3', 4:4'}

4 points back to 1.
Since: 1 in old_to_new
return: 1'
instead of creating another node.

Graph gets cloned correctly.

####################################################################################################

Complexity Analysis

Let:
* V = number of vertices
* E = number of edges

* Time
Each node visited once: O(V + E)

####################################################################################################

Every node is cloned exactly once:
	copy = Node(curr.val)
	old_to_new[curr] = copy

This happens:	V times
So already:		O(V)		work exists.

Then for every neighbor:	for neighbor in curr.neighbors:
we process an adjacency list entry.

Across the entire graph, the total number of adjacency-list entries is:	O(E) for directed graphs
								or
O(2E)	for undirected graphs
which simplifies to:		O(E)

Therefore total work:	work for vertices	+	work for edges	=	O(V) + O(E)	=	O(V + E)

Why not just say O(E)?

Because graphs can have very few edges.
Example:
	V = 1000
	E = 0

There are 1000 isolated nodes.
Suppose somehow you had to clone all nodes.

Then:
	O(E) = O(0)
which clearly doesn't account for cloning 1000 nodes.

You must include vertex work.
Hence:		O(V + E)

Another way to think about it
DFS graph traversal always follows this pattern:
	Visit every vertex once
	Visit every edge once

So almost every DFS/BFS graph algorithm ends up being:		Time = O(V + E)

####################################################################################################

* Space
HashMap: O(V)
Recursion stack: O(V)
	recursion stack is not counting total function calls made throughout execution.
	It counts: How many function calls can be alive simultaneously? So O(V)

Overall: O(V) extra space.

'''
from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        def clone(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)


def build_graph(adj_list):
    """
    Converts adjacency list into graph and returns node 1.
    [] => None
    """
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]

    return nodes[0]


def graph_to_adj_list(node):
    """
    Converts graph back into adjacency list for easy verification.
    """
    if not node:
        return []

    visited = set()
    queue = deque([node])

    nodes = {}

    while queue:
        curr = queue.popleft()

        if curr.val in visited:
            continue

        visited.add(curr.val)
        nodes[curr.val] = curr

        for neighbor in curr.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)

    max_val = max(nodes.keys())
    result = [[] for _ in range(max_val)]

    for val in sorted(nodes):
        result[val - 1] = sorted(
            neighbor.val for neighbor in nodes[val].neighbors
        )

    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 4], [1, 3], [2, 4], [1, 3]]
        ),

        # Example 2
        (
            [[]],
            [[]]
        ),

        # Example 3
        (
            [],
            []
        ),

        # Single node
        (
            [[]],
            [[]]
        ),

        # Two connected nodes
        (
            [[2], [1]],
            [[2], [1]]
        ),

        # Triangle cycle
        (
            [[2, 3], [1, 3], [1, 2]],
            [[2, 3], [1, 3], [1, 2]]
        ),

        # Square cycle
        (
            [[2, 4], [1, 3], [2, 4], [1, 3]],
            [[2, 4], [1, 3], [2, 4], [1, 3]]
        ),

        # Star graph
        (
            [[2, 3, 4, 5], [1], [1], [1], [1]],
            [[2, 3, 4, 5], [1], [1], [1], [1]]
        ),

        # Complex graph
        (
            [
                [2, 3],
                [1, 4, 5],
                [1, 5],
                [2, 5],
                [2, 3, 4]
            ],
            [
                [2, 3],
                [1, 4, 5],
                [1, 5],
                [2, 5],
                [2, 3, 4]
            ]
        ),
    ]

    for idx, (adj_list, expected) in enumerate(test_cases, start=1):
        root = build_graph(adj_list)

        cloned_root = solution.cloneGraph(root)

        result = graph_to_adj_list(cloned_root)

        print(f"Test Case {idx}")
        print("Input   :", adj_list)
        print("Expected:", expected)
        print("Actual  :", result)
        print("PASS" if result == expected else "FAIL")
        print("-" * 60)