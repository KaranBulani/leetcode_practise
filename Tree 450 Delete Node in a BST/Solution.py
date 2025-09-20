'''
Time Complexity:  O(h)					(Where h is height of tree)
Space Complexity: O(h)               	(for recursive stack)
'''

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minValueNode(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    # Remove a node and return the root of the BST.
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValueNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)

        return root


# Helper: Build tree from list (level order)
def build_tree(values):
    if not values:
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


# Helper: Convert tree back to list (level order)
def tree_to_list(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values to match LeetCode output
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    key = 3
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [5,4,6,2,None,None,7] or [5,2,6,None,4,None,7]

    # Example 2
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    key = 0
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [5,3,6,2,4,None,7]

    # Example 3
    root = build_tree([])
    key = 0
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: []

    # Edge Case 1
    root = build_tree([1])
    key = 1
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: []

    # Edge Case 2
    root = build_tree([2, 1])
    key = 2
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [1]

    # Edge Case 3
    root = build_tree([2, None, 3])
    key = 2
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [3]

    # Edge Case 4
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    key = 7
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [5,3,6,2,4]

    # Edge Case 5
    root = build_tree([50, 30, 70, 20, 40, 60, 80])
    key = 50
    new_root = solution.deleteNode(root, key)
    print(tree_to_list(new_root))  # Expected: [60,30,70,20,40,None,80]
