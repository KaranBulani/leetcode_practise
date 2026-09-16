'''
####################################################################################################
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        # Default: <__main__.TreeNode object at 0x0000020A0DB0AC50>

        # If you want to see the whole tree recursively (careful with big trees), you can do this:
        # TreeNode(val=10, left=TreeNode(val=5, left=None, right=None), right=TreeNode(val=15, left=None, right=None))
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        inorder_index = {value: i for i, value in enumerate(inorder)}
        postorder_idx = len(postorder) - 1

        def dfs(left: int, right: int) -> TreeNode | None:
            nonlocal postorder_idx

            if left > right:
                return None

            # Last element of postorder is the root
            root_value = postorder[postorder_idx]
            postorder_idx -= 1

            root = TreeNode(root_value)

            mid = inorder_index[root_value]

            # IMPORTANT: build right subtree first
            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)


def tree_to_list(root):
    """
    Convert Binary Tree -> LeetCode-style level-order list.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove unnecessary trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # --------------------------------------------------
        # 1. Example from question
        # --------------------------------------------------
        {
            "inorder": [9, 3, 15, 20, 7],
            "postorder": [9, 15, 7, 20, 3],
            "expected": [3, 9, 20, None, None, 15, 7]
        },

        # --------------------------------------------------
        # 2. Single node
        # --------------------------------------------------
        {
            "inorder": [-1],
            "postorder": [-1],
            "expected": [-1]
        },

        # --------------------------------------------------
        # 3. Two nodes - left child
        #       2
        #      /
        #     1
        # --------------------------------------------------
        {
            "inorder": [1, 2],
            "postorder": [1, 2],
            "expected": [2, 1]
        },

        # --------------------------------------------------
        # 4. Two nodes - right child
        #       1
        #        \
        #         2
        # --------------------------------------------------
        {
            "inorder": [1, 2],
            "postorder": [2, 1],
            "expected": [1, None, 2]
        },

        # --------------------------------------------------
        # 5. Completely left-skewed tree
        #
        #       4
        #      /
        #     3
        #    /
        #   2
        #  /
        # 1
        # --------------------------------------------------
        {
            "inorder": [1, 2, 3, 4],
            "postorder": [1, 2, 3, 4],
            "expected": [4, 3, None, 2, None, None, None, 1]
        },

        # --------------------------------------------------
        # 6. Completely right-skewed tree
        #
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        # --------------------------------------------------
        {
            "inorder": [1, 2, 3, 4],
            "postorder": [4, 3, 2, 1],
            "expected": [1, None, 2, None, 3, None, 4]
        },

        # --------------------------------------------------
        # 7. Perfectly balanced tree
        #
        #        4
        #       / \
        #      2   6
        #     / \ / \
        #    1  3 5  7
        # --------------------------------------------------
        {
            "inorder": [1, 2, 3, 4, 5, 6, 7],
            "postorder": [1, 3, 2, 5, 7, 6, 4],
            "expected": [4, 2, 6, 1, 3, 5, 7]
        },

        # --------------------------------------------------
        # 8. Only left subtree at root
        #
        #       5
        #      /
        #     3
        #    / \
        #   2   4
        # --------------------------------------------------
        {
            "inorder": [2, 3, 4, 5],
            "postorder": [2, 4, 3, 5],
            "expected": [5, 3, None, 2, 4]
        },

        # --------------------------------------------------
        # 9. Only right subtree at root
        #
        #   1
        #    \
        #     3
        #    / \
        #   2   4
        # --------------------------------------------------
        {
            "inorder": [1, 2, 3, 4],
            "postorder": [2, 4, 3, 1],
            "expected": [1, None, 3, 2, 4]
        },

        # --------------------------------------------------
        # 10. Negative + positive values
        #
        #       0
        #      / \
        #    -3   5
        #    /   / \
        #   -5  2   8
        # --------------------------------------------------
        {
            "inorder": [-5, -3, 0, 2, 5, 8],
            "postorder": [-5, -3, 2, 8, 5, 0],
            "expected": [0, -3, 5, -5, None, 2, 8]
        },

        # --------------------------------------------------
        # 11. Uneven tree
        #
        #        1
        #       / \
        #      2   3
        #       \
        #        4
        #         \
        #          5
        # --------------------------------------------------
        {
            "inorder": [2, 4, 5, 1, 3],
            "postorder": [5, 4, 2, 3, 1],
            "expected": [1, 2, 3, None, 4, None, None, None, 5]
        },

        # --------------------------------------------------
        # 12. Larger asymmetric tree
        #
        #          10
        #         /  \
        #        5    15
        #       / \     \
        #      2   7     20
        #         /
        #        6
        # --------------------------------------------------
        {
            "inorder": [2, 5, 6, 7, 10, 15, 20],
            "postorder": [2, 6, 7, 5, 20, 15, 10],
            "expected": [10, 5, 15, 2, 7, None, 20, None, None, 6]
        },
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.buildTree(
            test["inorder"],
            test["postorder"]
        )

        result = tree_to_list(result)

        print(f"Test Case {i}:")
        print(f"  Inorder:   {test['inorder']}")
        print(f"  Postorder: {test['postorder']}")
        print(f"  Your Output: {result}")
        print(f"  Expected:    {test['expected']}")
        print(f"  {'PASS ✅' if result == test['expected'] else 'FAIL ❌'}")
        print()