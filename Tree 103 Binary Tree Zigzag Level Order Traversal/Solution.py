'''
Approach: BFS + Reverse Every Alternate Level

This is a standard level-order BFS problem.

The only difference from normal level-order traversal is:

* Level 0 → left → right
* Level 1 → right → left
* Level 2 → left → right
* Level 3 → right → left
* ...

We can use a queue and keep track of the level number.

####################################################################################################

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level.reverse()

            result.append(level)
            left_to_right = not left_to_right

        return result

####################################################################################################

Dry run

For:
        3
       / \
      9   20
         /  \
        15   7

Queue processing:

Level 0:
queue = [3]
level = [3]
direction = L → R

result = [[3]]


Next:


Level 1:
queue = [9, 20]
level = [9, 20]

direction = R → L
reverse → [20, 9]

result = [[3], [20, 9]]


Next:


Level 2:
queue = [15, 7]
level = [15, 7]

direction = L → R
don't reverse

result = [[3], [20, 9], [15, 7]]

So:		[[3], [20, 9], [15, 7]]

####################################################################################################

Complexity

For n nodes:
	* Time: O(n)
	* Space: O(n)

Every node enters and leaves the queue exactly once.

####################################################################################################

A slightly cleaner version
	Instead of maintaining a boolean, we can use the level number:
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        level_num = 0

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if level_num % 2 == 1:
                level.reverse()

            result.append(level)
            level_num += 1

        return result


def build_tree(values):
    """
    Build a binary tree from level-order representation.

    None represents a missing child.

    Example:
    [3, 9, 20, None, None, 15, 7]

            3
           / \
          9  20
             / \
            15  7
    """

    if not values:
        return None

    nodes = [
        TreeNode(value) if value is not None else None
        for value in values
    ]

    child_index = 1

    for node in nodes:
        if node is not None:
            if child_index < len(nodes):
                node.left = nodes[child_index]
                child_index += 1

            if child_index < len(nodes):
                node.right = nodes[child_index]
                child_index += 1

    return nodes[0]


def run_test(solution, values, expected, test_name):
    root = build_tree(values)

    result = solution.zigzagLevelOrder(root)

    print(f"\n{test_name}")
    print(f"Input:    {values}")
    print(f"Output:   {result}")
    print(f"Expected: {expected}")

    if result == expected:
        print("PASS")
    else:
        print("FAIL")


if __name__ == "__main__":
    solution = Solution()

    # ---------------------------------------------------------
    # 1. Empty tree
    # ---------------------------------------------------------
    run_test(
        solution,
        [],
        [],
        "Test 1 - Empty Tree"
    )

    # ---------------------------------------------------------
    # 2. Single node
    # ---------------------------------------------------------
    run_test(
        solution,
        [1],
        [[1]],
        "Test 2 - Single Node"
    )

    # ---------------------------------------------------------
    # 3. Basic example from question
    #
    #         3
    #        / \
    #       9  20
    #          / \
    #         15  7
    #
    # Levels:
    # [3]
    # [20, 9]
    # [15, 7]
    # ---------------------------------------------------------
    run_test(
        solution,
        [3, 9, 20, None, None, 15, 7],
        [[3], [20, 9], [15, 7]],
        "Test 3 - Basic Example"
    )

    # ---------------------------------------------------------
    # 4. Complete binary tree
    #
    #             1
    #          /     \
    #         2       3
    #        / \     / \
    #       4   5   6   7
    #
    # Expected:
    # [1]
    # [3, 2]
    # [4, 5, 6, 7]
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 2, 3, 4, 5, 6, 7],
        [[1], [3, 2], [4, 5, 6, 7]],
        "Test 4 - Complete Binary Tree"
    )

    # ---------------------------------------------------------
    # 5. Left-skewed tree
    #
    #       1
    #      /
    #     2
    #    /
    #   3
    #  /
    # 4
    #
    # Every level contains one node, so direction doesn't
    # visibly change the result.
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 2, None, 3, None, 4],
        [[1], [2], [3], [4]],
        "Test 5 - Left Skewed Tree"
    )

    # ---------------------------------------------------------
    # 6. Right-skewed tree
    #
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, None, 2, None, 3, None, 4],
        [[1], [2], [3], [4]],
        "Test 6 - Right Skewed Tree"
    )

    # ---------------------------------------------------------
    # 7. Only left children at first, then branching
    #
    #       1
    #      /
    #     2
    #    / \
    #   4   5
    #      / \
    #     6   7
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 2, None, 4, 5, None, None, None, None, 6, 7],
        [[1], [2], [4, 5], [7, 6]],
        "Test 7 - Uneven Tree"
    )

    # ---------------------------------------------------------
    # 8. Missing nodes in the middle
    #
    #         1
    #        / \
    #       2   3
    #        \   \
    #         5   7
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 2, 3, None, 5, None, 7],
        [[1], [3, 2], [5, 7]],
        "Test 8 - Missing Middle Children"
    )

    # ---------------------------------------------------------
    # 9. Negative values
    # ---------------------------------------------------------
    run_test(
        solution,
        [-1, -2, -3, -4, -5, -6, -7],
        [[-1], [-3, -2], [-4, -5, -6, -7]],
        "Test 9 - Negative Values"
    )

    # ---------------------------------------------------------
    # 10. Duplicate values
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 1, 1, 1, 1, 1, 1],
        [[1], [1, 1], [1, 1, 1, 1]],
        "Test 10 - Duplicate Values"
    )

    # ---------------------------------------------------------
    # 11. Zero values
    # ---------------------------------------------------------
    run_test(
        solution,
        [0, 0, 0, 0, 0],
        [[0], [0, 0], [0, 0]],
        "Test 11 - Zero Values"
    )

    # ---------------------------------------------------------
    # 12. Larger irregular tree
    #
    #             10
    #           /    \
    #          5      15
    #         / \       \
    #        3   7       20
    #           / \     /
    #          6   8   18
    # ---------------------------------------------------------
    run_test(
        solution,
        [
            10,
            5,
            15,
            3,
            7,
            None,
            20,
            None,
            None,
            6,
            8,
            18
        ],
        [
            [10],
            [15, 5],
            [3, 7, 20],
            [18, 8, 6]
        ],
        "Test 12 - Larger Irregular Tree"
    )

    # ---------------------------------------------------------
    # 13. Single child at alternating levels
    # ---------------------------------------------------------
    run_test(
        solution,
        [1, 2, None, None, 3, None, None, 4],
        [[1], [2], [3], [4]],
        "Test 13 - Alternating Single Children"
    )

    # ---------------------------------------------------------
    # 14. Maximum/minimum allowed values
    # ---------------------------------------------------------
    run_test(
        solution,
        [100, -100, 100, -100, 100, -100, 100],
        [
            [100],
            [100, -100],
            [-100, 100, -100, 100]
        ],
        "Test 14 - Boundary Values"
    )