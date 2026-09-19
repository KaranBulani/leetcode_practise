'''

Approach: Level-order traversal with next pointers

We can process one level at a time and build the next chain for the next level.

For each level:
* cur traverses the current level using already-established next pointers.
* dummy is a temporary node representing the beginning of the next level.
* tail points to the last node we've added to the next level.
* For every cur, append its left and right children to the next-level chain.
* After finishing the current level:
  * cur = dummy.next

####################################################################################################

Dry run

For:
        1
       / \
      2   3
     /     \
    4       5
     \
      7

After processing level 1:	1 -> None

Next level:		2 -> 3 -> None

Next level:		4 -> 5 -> None

Next level:		7 -> None

The important part is that when processing:		2 -> 3

we don't care whether 2 or 3 has a missing child. We simply append whatever children exist.

####################################################################################################

Why the dummy node works

Suppose the current level is:		2 -> 3 -> 4 -> None

and their children are:
	2:       5
	3:      / \
		   6   7
	4:        8

While traversing:		cur = 2

we create:
	dummy -> 5
			  ^
			tail

Then:		cur = 3

append 6, 7:
	dummy -> 5 -> 6 -> 7
						^
					  tail

Then 4:
	dummy -> 5 -> 6 -> 7 -> 8
							 ^
						   tail

Therefore:			dummy.next

is always the first node of the next level.

####################################################################################################
Follow-up: O(1) extra space

This solution already satisfies the follow-up.

Complexity

Let N be the number of nodes.
Time:		O(N)
Every node is processed once.

Extra space:		O(1)

We only use:
	cur
	dummy
	tail

We don't use a queue, recursion, or any data structure proportional to the tree height/width.

Important distinction

A normal BFS solution would use:		queue = deque([root])

which requires O(W) space, where W is the maximum width of the tree.

The dummy-node approach avoids that by reusing the next pointers as our level traversal mechanism.

####################################################################################################
The pattern to remember

This is a very useful binary-tree pattern:

	cur = root
	while cur:
		dummy = Node(0)
		tail = dummy
		while cur:
			if cur.left:
				tail.next = cur.left
				tail = tail.next
			if cur.right:
				tail.next = cur.right
				tail = tail.next
			cur = cur.next
		cur = dummy.next

Think of it as:
> Current level → use next pointers → construct next-level next pointers.

This is the cleanest way to solve 117 with O(1) extra space.
'''
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: "Node | None") -> "Node | None":
        cur = root
        while cur:
            # Dummy node for the next level
            dummy = Node(0)
            tail = dummy

            # Traverse current level using next pointers
            # Repoint next level's next pointer using tail and curr
            while cur:

                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next

            # Move to the first node of the next level
            cur = dummy.next

        return root

# ---------------------------------------------------------
# Helper: Build binary tree from level-order representation
# ---------------------------------------------------------
def build_tree(values):
    if not values:
        return None

    nodes = [
        Node(value) if value is not None else None
        for value in values
    ]

    j = 1

    for node in nodes:
        if node is not None:
            if j < len(nodes):
                node.left = nodes[j]
                j += 1

            if j < len(nodes):
                node.right = nodes[j]
                j += 1

    return nodes[0]

# ---------------------------------------------------------
# Helper: Convert next pointers to LeetCode-style output
# ---------------------------------------------------------
def get_next_output(root):
    if root is None:
        return []

    result = []

    # Start with first node of each level
    level_start = root

    while level_start:

        curr = level_start
        next_level_start = None

        # Traverse current level using next pointers
        while curr:
            result.append(curr.val)

            if curr.next is None:
                result.append("#")

            # Find first child of the next level
            if next_level_start is None:
                if curr.left:
                    next_level_start = curr.left
                elif curr.right:
                    next_level_start = curr.right

            curr = curr.next

        level_start = next_level_start

    return result

# ---------------------------------------------------------
# Test cases
# ---------------------------------------------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # 1. Example from question
        {
            "input": [1, 2, 3, 4, 5, None, 7],
            "expected": [1, "#", 2, 3, "#", 4, 5, 7, "#"]
        },

        # 2. Empty tree
        {
            "input": [],
            "expected": []
        },

        # 3. Single node
        {
            "input": [1],
            "expected": [1, "#"]
        },

        # 4. Only left child
        {
            "input": [1, 2],
            "expected": [1, "#", 2, "#"]
        },

        # 5. Only right child
        {
            "input": [1, None, 2],
            "expected": [1, "#", 2, "#"]
        },

        # 6. Two children
        {
            "input": [1, 2, 3],
            "expected": [1, "#", 2, 3, "#"]
        },

        # 7. Completely skewed left
        {
            "input": [1, 2, None, 3, None, 4],
            "expected": [1, "#", 2, "#", 3, "#", 4, "#"]
        },

        # 8. Completely skewed right
        {
            "input": [1, None, 2, None, 3, None, 4],
            "expected": [1, "#", 2, "#", 3, "#", 4, "#"]
        },

        # 9. Missing nodes in middle
        {
            "input": [1, 2, 3, None, 5, None, 7],
            "expected": [1, "#", 2, 3, "#", 5, 7, "#"]
        },

        # 10. Sparse tree
        {
            "input": [1, 2, 3, 4, None, None, 7],
            "expected": [1, "#", 2, 3, "#", 4, 7, "#"]
        },

        # 11. Nodes only on alternating sides
        {
            "input": [1, 2, 3, None, 4, 5, None],
            "expected": [1, "#", 2, 3, "#", 4, 5, "#"]
        },

        # 12. Important case: next-level children are far apart
        {
            "input": [1, 2, 3, 4, None, None, 5, None, 6],
            "expected": [1, "#", 2, 3, "#", 4, 5, "#", 6, "#"]
        },

        # 13. Multiple gaps
        {
            "input": [1, 2, 3, None, 4, None, 5, 6, None, None, 7],
            "expected": [1, "#", 2, 3, "#", 4, 5, "#", 6, 7, "#"]
        },

        # 14. Irregular tree
        {
            "input": [
                1,
                2, 3,
                4, None, None, 5,
                None, 6, None, None, None, None, 7
            ],
            "expected": [
                1, "#",
                2, 3, "#",
                4, 5, "#",
                6, 7, "#"
            ]
        },

        # 15. Larger irregular tree
        {
            "input": [
                1,
                2, 3,
                4, 5, None, 7,
                None, None, 6, None, None, None, 8
            ],
            "expected": [
                1, "#",
                2, 3, "#",
                4, 5, 7, "#",
                6, 8, "#"
            ]
        },
    ]

    # -----------------------------------------------------
    # Run tests
    # -----------------------------------------------------
    for i, test in enumerate(test_cases, 1):

        root = build_tree(test["input"])

        result_root = solution.connect(root)

        actual = get_next_output(result_root)

        print(f"Test Case {i}")
        print(f"Input:    {test['input']}")
        print(f"Expected: {test['expected']}")
        print(f"Actual:   {actual}")

        if actual == test["expected"]:
            print("✅ PASS")
        else:
            print("❌ FAIL")

        print("-" * 60)