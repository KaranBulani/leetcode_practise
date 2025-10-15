'''
Time complexity:  O(logn)^2					computing heights costs logn recursion depth is logn
Space complexity: O(logn)					Recursion Stack
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(curr):
            h = 0
            while curr:
                h += 1
                curr = curr.left
            return h

        def right_height(curr):
            h = 0
            while curr:
                h += 1
                curr = curr.right
            return h

        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            # perfect tree
            return 2 ** lh - 1
        # not perfect -> recurse
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# Helper function to build a binary tree from a list (level order)
from collections import deque
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
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

    # Test Case 1: Example from question
    root1 = build_tree([1, 2, 3, 4, 5, 6])
    print(solution.countNodes(root1))  # Expected: ?

    # Test Case 2: Empty tree
    root2 = build_tree([])
    print(solution.countNodes(root2))  # Expected: ?

    # Test Case 3: Single node tree
    root3 = build_tree([1])
    print(solution.countNodes(root3))  # Expected: ?

    # Test Case 4: Complete but not perfect (last level partially filled)
    root4 = build_tree([1, 2, 3, 4, 5])
    print(solution.countNodes(root4))  # Expected: ?

    # Test Case 5: Perfect tree with 7 nodes (full 3 levels)
    root5 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(solution.countNodes(root5))  # Expected: ?

    # Test Case 6: Larger complete tree missing last two nodes
    root6 = build_tree([1, 2, 3, 4, 5, 6, None])
    print(solution.countNodes(root6))  # Expected: ?

    # Test Case 7: Tree with missing right subtree in last level
    root7 = build_tree([1, 2, 3, 4, None, None, None])
    print(solution.countNodes(root7))  # Expected: ?