'''
Time Complexity:  O(n)					(n as going through each node)
Space Complexity: O(q)               	(len(n) of queue)
'''

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []

        if root:
            q.append(root)

        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level)
        return res


def build_tree(values):
    """Helper to build a tree from list (like LeetCode input)."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1:", solution.levelOrder(root1))  # Expected [[3],[9,20],[15,7]]

    # Example 2
    root2 = build_tree([1])
    print("Test 2:", solution.levelOrder(root2))  # Expected [[1]]

    # Example 3 (Empty tree)
    root3 = build_tree([])
    print("Test 3:", solution.levelOrder(root3))  # Expected []

    # Additional edge case: Single node with children only on one side
    root4 = build_tree([1, 2, None, 3, None, 4])
    print("Test 4:", solution.levelOrder(root4))  # Expected [[1],[2],[3],[4]]

    # Additional edge case: Complete binary tree
    root5 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("Test 5:", solution.levelOrder(root5))  # Expected [[1],[2,3],[4,5,6,7]]

    # Additional edge case: Larger unbalanced tree
    root6 = build_tree([1, 2, 3, 4, None, None, 5, 6])
    print("Test 6:", solution.levelOrder(root6))
    # Expected [[1],[2,3],[4,5],[6]]