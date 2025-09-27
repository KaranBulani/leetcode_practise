'''
Time complexity:  O(n)						total but individual hasNext, next calls are O(1)
Space complexity: O(h)						max stack size
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        curr = self.stack.pop()
        self.pushAll(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Helper function to build tree from list (level order representation)
from collections import deque

def build_tree(values):
    """Builds binary tree from level-order list with 'None' as null markers."""
    if not values or values[0] is None:
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
    # Example 1 (from problem statement)
    root1 = build_tree([7, 3, 15, None, None, 9, 20])
    it1 = BSTIterator(root1)
    print(it1.next())  # Expected 3
    print(it1.next())  # Expected 7
    print(it1.hasNext())  # Expected True
    print(it1.next())  # Expected 9
    print(it1.hasNext())  # Expected True
    print(it1.next())  # Expected 15
    print(it1.hasNext())  # Expected True
    print(it1.next())  # Expected 20
    print(it1.hasNext())  # Expected False

    # Edge case 1: Single node
    root2 = build_tree([42])
    it2 = BSTIterator(root2)
    print(it2.next())  # Expected 42
    print(it2.hasNext())  # Expected False

    # Edge case 2: Completely skewed left tree
    root3 = build_tree([5, 4, None, 3, None, 2, None, 1])
    it3 = BSTIterator(root3)
    while it3.hasNext():
        print(it3.next())  # Expected [1, 2, 3, 4, 5]

    # Edge case 3: Completely skewed right tree
    root4 = build_tree([1, None, 2, None, 3, None, 4, None, 5])
    it4 = BSTIterator(root4)
    while it4.hasNext():
        print(it4.next())  # Expected [1, 2, 3, 4, 5]

    # Edge case 4: Larger balanced tree
    root5 = build_tree([10, 5, 15, 3, 7, 12, 18])
    it5 = BSTIterator(root5)
    res5 = []
    while it5.hasNext():
        res5.append(it5.next())
    print(res5)  # Expected [3, 5, 7, 10, 12, 15, 18]
