'''
The key idea is to carry the number formed so far while traversing the tree.

For example:
        1
       / \
      2   3

Paths:
	1 → 2  => 12
	1 → 3  => 13
	answer = 12 + 13 = 25

####################################################################################################

DFS solution

At every node:
	current = previous * 10 + node.val

When we reach a leaf, current is a complete root-to-leaf number, so we add it to the answer.


####################################################################################################

Walkthrough

For:
        4
       / \
      9   0
     / \
    5   1

DFS proceeds like:
	4
	│
	├── 9
	│   │
	│   ├── 5 → 495  ← leaf
	│   │
	│   └── 1 → 491  ← leaf
	│
	└── 0 → 40       ← leaf

Therefore:
		495 + 491 + 40 = 1026


####################################################################################################

Why current * 10 + node.val?

Suppose we've built:		49
and move to a node containing 5.

We want:		495

Mathematically:
		49 * 10 + 5
		= 490 + 5
		= 495

####################################################################################################

Complexity

If there are N nodes:
* Time: O(N) — every node is visited once.
* Space: O(H) — recursion stack, where H is tree height.
  * Balanced tree: O(log N)
  * Skewed tree: O(N)

A useful pattern to remember

This is a classic DFS + carry state problem:

	def dfs(node, state):
		state = update(state, node.val)

		if leaf:
			return result_from(state)

		return dfs(left, state) + dfs(right, state)

Here, the state is simply the number constructed along the current root-to-node path.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:

        def dfs(node: TreeNode | None, current: int) -> int:
            if node is None:
                return 0

            current = current * 10 + node.val

            if node.left is None and node.right is None:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


if __name__ == "__main__":
    solution = Solution()

    # ============================================================
    # Example 1
    #
    #       1
    #      / \
    #     2   3
    #
    # Root-to-leaf numbers: 12, 13
    # Expected: 25
    # ============================================================
    root1 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    result = solution.sumNumbers(root1)
    print("Example 1:", result, "Expected: 25")


    # ============================================================
    # Example 2
    #
    #         4
    #        / \
    #       9   0
    #      / \
    #     5   1
    #
    # Root-to-leaf numbers: 495, 491, 40
    # Expected: 1026
    # ============================================================
    root2 = TreeNode(
        4,
        TreeNode(
            9,
            TreeNode(5),
            TreeNode(1)
        ),
        TreeNode(0)
    )

    result = solution.sumNumbers(root2)
    print("Example 2:", result, "Expected: 1026")


    # ============================================================
    # Edge Case 1: Single node
    #
    #       5
    #
    # Root-to-leaf number: 5
    # Expected: 5
    # ============================================================
    root3 = TreeNode(5)

    result = solution.sumNumbers(root3)
    print("Single node:", result, "Expected: 5")


    # ============================================================
    # Edge Case 2: Single node with value 0
    #
    #       0
    #
    # Expected: 0
    # ============================================================
    root4 = TreeNode(0)

    result = solution.sumNumbers(root4)
    print("Single zero:", result, "Expected: 0")


    # ============================================================
    # Edge Case 3: Completely left-skewed tree
    #
    #       1
    #      /
    #     2
    #    /
    #   3
    #  /
    # 4
    #
    # Root-to-leaf number: 1234
    # Expected: 1234
    # ============================================================
    root5 = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(
                3,
                TreeNode(4)
            )
        )
    )

    result = solution.sumNumbers(root5)
    print("Left skewed:", result, "Expected: 1234")


    # ============================================================
    # Edge Case 4: Completely right-skewed tree
    #
    #   1
    #    \
    #     2
    #      \
    #       3
    #        \
    #         4
    #
    # Root-to-leaf number: 1234
    # Expected: 1234
    # ============================================================
    root6 = TreeNode(
        1,
        right=TreeNode(
            2,
            right=TreeNode(
                3,
                right=TreeNode(4)
            )
        )
    )

    result = solution.sumNumbers(root6)
    print("Right skewed:", result, "Expected: 1234")


    # ============================================================
    # Edge Case 5: Zeros in the middle
    #
    #       1
    #      / \
    #     0   2
    #    /     \
    #   3       4
    #
    # Root-to-leaf numbers: 103, 124
    # ============================================================
    root7 = TreeNode(
        1,
        TreeNode(
            0,
            TreeNode(3)
        ),
        TreeNode(
            2,
            right=TreeNode(4)
        )
    )

    result = solution.sumNumbers(root7)
    print("Zeros in path:", result, "Expected: 227")


    # ============================================================
    # Edge Case 6: Root is zero with multiple paths
    #
    #       0
    #      / \
    #     1   2
    #    /     \
    #   3       4
    #
    # Root-to-leaf numbers: 013 (= 13), 024 (= 24)
    # ============================================================
    root8 = TreeNode(
        0,
        TreeNode(
            1,
            TreeNode(3)
        ),
        TreeNode(
            2,
            right=TreeNode(4)
        )
    )

    result = solution.sumNumbers(root8)
    print("Root zero:", result, "Expected: 37")


    # ============================================================
    # Edge Case 7: Uneven tree
    #
    #          1
    #         / \
    #        2   3
    #         \   \
    #          4   5
    #
    # Root-to-leaf numbers: 124, 135
    # ============================================================
    root9 = TreeNode(
        1,
        TreeNode(
            2,
            right=TreeNode(4)
        ),
        TreeNode(
            3,
            right=TreeNode(5)
        )
    )

    result = solution.sumNumbers(root9)
    print("Uneven tree:", result, "Expected: 259")


    # ============================================================
    # Edge Case 8: Multiple zeros
    #
    #          1
    #         / \
    #        0   0
    #       /     \
    #      0       5
    #
    # Root-to-leaf numbers: 100, 005 (= 5)
    # ============================================================
    root10 = TreeNode(
        1,
        TreeNode(
            0,
            TreeNode(0)
        ),
        TreeNode(
            0,
            right=TreeNode(5)
        )
    )

    result = solution.sumNumbers(root10)
    print("Multiple zeros:", result, "Expected: 105")