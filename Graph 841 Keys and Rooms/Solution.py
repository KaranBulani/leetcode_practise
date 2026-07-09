'''
1. Clarifying Questions (Interview)

Ask the interviewer:
1. Can a room contain duplicate keys?
   * No, keys are distinct.
2. Can a room contain its own key?
   * Doesn't matter; our solution still works.
3. Is room 0 always unlocked?
   * Yes.
4. Should I return true only if every room is reachable from room 0?
   * Yes.

####################################################################################################
3. Optimal Observation

This is actually a graph problem.
* Room = Node
* Key = Directed Edge

Example:
	0 -> 1
	0 -> 3
	1 -> 2
	2 -> 4

Starting from node 0,
Can we visit every node?
That's simply Graph Traversal.

Use either:
* DFS
* BFS
Both are optimal.

####################################################################################################
4. DFS Approach

Idea
	Start from room 0.
	Whenever you enter a room:
	* mark it visited
	* collect every key
	* recursively visit unlocked rooms

Finally,
visited rooms == total rooms ?

Dry Run

rooms = [
 [1],
 [2],
 [3],
 []
]

	Start
	visited = {}

	DFS(0), visited = {0}, key ->1
	DFS(1), visited={0,1}, key->2
	DFS(2), visited={0,1,2}, key->3
	DFS(3), visited={0,1,2,3}

	Visited = 4
	Total rooms = 4
	Return True

Another [
 [1,3],
 [3,0,1],
 [2],
 [0]
]

	Reachable:
		0
		↓
		1
		↓
		3
	Never reaches room 2.
	Return False.

####################################################################################################
# 6. Python Code (DFS)

python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            visited.add(room)

            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)

        return len(visited) == len(rooms)

####################################################################################################
Python Code (BFS)

python
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}
        queue = deque([0])

        while queue:
            room = queue.popleft()

            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == len(rooms)

####################################################################################################
8. Correctness Intuition

Every room that becomes reachable is visited exactly once.
When we visit a room, we immediately collect all its keys, which may unlock additional rooms. Since every reachable room is eventually explored and no room is processed more than once, at the end visited contains exactly the set of rooms reachable from room 0. Therefore, returning len(visited) == len(rooms) correctly determines whether all rooms can be visited.

####################################################################################################
9. Complexity Analysis

Let:
* n = number of rooms
* m = total number of keys across all rooms

Each room is visited once.
Each key is processed once.

Time O(n + m)

Space
* Visited set: O(n)
* DFS recursion stack or BFS queue: O(n)

Overall:
* Time: O(n + m)
* Space: O(n)

'''
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [[1], [2], [3], []],
            True
        ),

        # Example 2
        (
            [[1, 3], [3, 0, 1], [2], [0]],
            False
        ),

        # Smallest valid input - both rooms reachable
        (
            [[1], []],
            True
        ),

        # Smallest valid input - second room unreachable
        (
            [[], []],
            False
        ),

        # Room with multiple keys
        (
            [[1, 2, 3], [], [], []],
            True
        ),

        # Cycle involving all rooms
        (
            [[1], [2], [3], [0]],
            True
        ),

        # Separate disconnected room
        (
            [[1], [], [3], []],
            False
        ),

        # Duplicate paths to same room
        (
            [[1, 2], [2], [3], []],
            True
        ),

        # Self-loop only
        (
            [[0], []],
            False
        ),

        # Every room points back to room 0 only
        (
            [[1, 2, 3], [0], [0], [0]],
            True
        ),

        # Key exists but never obtainable
        (
            [[1], [], [3], [2]],
            False
        ),

        # Larger cycle
        (
            [[1], [2], [3], [4], [0]],
            True
        ),

        # Branching graph
        (
            [[1, 2], [3], [3], [4], []],
            True
        ),

        # Missing one critical key
        (
            [[1, 2], [3], [], [4], []],
            False
        ),

        # Empty rooms after first visit
        (
            [[1], [], [], []],
            False
        ),
    ]

    for i, (rooms, expected) in enumerate(test_cases, 1):
        result = solution.canVisitAllRooms(rooms)

        print(f"Test Case {i}")
        print(f"Rooms    : {rooms}")
        print(f"Expected : {expected}")
        print(f"Got      : {result}")
        print(f"Passed   : {result == expected}")
        print("-" * 50)