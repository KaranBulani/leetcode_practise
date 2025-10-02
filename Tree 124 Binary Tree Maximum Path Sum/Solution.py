'''
Time complexity:  O(n)				Traversing through all nodes
Space complexity: O(h)				recursion stack uses space proportional to the tree height h.
'''
# Helper to build tree from list (LeetCode style input)
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0

            L = max(dfs(curr.left), 0)
            R = max(dfs(curr.right), 0)
            self.res = max(self.res, L + curr.val + R)
            return curr.val + max(L, R)

        dfs(root)
        return self.res

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = build_tree([1, 2, 3])
    print("Test 1:", solution.maxPathSum(root1))  # Expected 6

    # Example 2
    root2 = build_tree([-10, 9, 20, None, None, 15, 7])
    print("Test 2:", solution.maxPathSum(root2))  # Expected 42

    # Single node (edge case)
    root3 = build_tree([5])
    print("Test 3:", solution.maxPathSum(root3))  # Expected 5

    # Skewed tree (all left)
    root4 = build_tree([1, 2, None, 3, None, 4, None])
    print("Test 4:", solution.maxPathSum(root4))  # Expected ?

    # Skewed tree (all right)
    root5 = build_tree([1, None, 2, None, 3, None, 4])
    print("Test 5:", solution.maxPathSum(root5))  # Expected ?

    # Tree with all negatives
    root6 = build_tree([-3, -2, -1])
    print("Test 6:", solution.maxPathSum(root6))  # Expected ?

    # Mixed positives and negatives
    root7 = build_tree([2, -1, -2])
    print("Test 7:", solution.maxPathSum(root7))  # Expected ?

    # Bigger balanced tree
    root8 = build_tree([10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4])
    print("Test 8:", solution.maxPathSum(root8))  # Expected ?