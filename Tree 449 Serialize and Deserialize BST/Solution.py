'''
Time complexity:  O(logn)^2					computing heights costs logn recursion depth is logn
Space complexity: O(logn)					Recursion Stack
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def preorder(curr):
            if not curr:
                return
            res.append(str(curr.val))
            preorder(curr.left)
            preorder(curr.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        preorder = list(map(int, data.split(",")))
        self.i = 0

        def build(lower, upper):
            # stop if out of values
            if self.i >= len(preorder):
                return None

            val = preorder[self.i]
            # if val is not in current valid BST range, skip
            # below avoids any skewed tree
            if not lower < val < upper:
                return None

            node = TreeNode(val)
            self.i += 1
            node.left = build(lower, val)
            node.right = build(val, upper)
            return node

        return build(float("-inf"), float("inf"))


if __name__ == "__main__":
    # Helper function to print tree as level order list for checking correctness
    from collections import deque


    def level_order(root):
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
        # Trim trailing Nones for cleaner output
        while result and result[-1] is None:
            result.pop()
        return result


    # Instantiate Codec
    ser = Codec()
    deser = Codec()

    # ------------------------------
    # 🧪 Test Case 1: Basic example
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print("Test 1 Expected:", [2, 1, 3])
    print("Test 1 Got:", level_order(deser.deserialize(ser.serialize(root1))))
    print()

    # ------------------------------
    # 🧪 Test Case 2: Empty tree
    root2 = None
    print("Test 2 Expected:", [])
    print("Test 2 Got:", level_order(deser.deserialize(ser.serialize(root2))))
    print()

    # ------------------------------
    # 🧪 Test Case 3: Skewed Right (increasing BST)
    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.right = TreeNode(3)
    root3.right.right.right = TreeNode(4)
    print("Test 3 Expected:", [1, None, 2, None, 3, None, 4])
    print("Test 3 Got:", level_order(deser.deserialize(ser.serialize(root3))))
    print()

    # ------------------------------
    # 🧪 Test Case 4: Skewed Left (decreasing BST)
    root4 = TreeNode(4)
    root4.left = TreeNode(3)
    root4.left.left = TreeNode(2)
    root4.left.left.left = TreeNode(1)
    print("Test 4 Expected:", [4, 3, None, 2, None, 1])
    print("Test 4 Got:", level_order(deser.deserialize(ser.serialize(root4))))
    print()

    # ------------------------------
    # 🧪 Test Case 5: Larger mixed BST
    root5 = TreeNode(8)
    root5.left = TreeNode(3)
    root5.right = TreeNode(10)
    root5.left.left = TreeNode(1)
    root5.left.right = TreeNode(6)
    root5.left.right.left = TreeNode(4)
    root5.left.right.right = TreeNode(7)
    root5.right.right = TreeNode(14)
    root5.right.right.left = TreeNode(13)
    print("Test 5 Expected:", [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    print("Test 5 Got:", level_order(deser.deserialize(ser.serialize(root5))))
    print()

    # ------------------------------
    # 🧪 Test Case 6: Single node
    root6 = TreeNode(42)
    print("Test 6 Expected:", [42])
    print("Test 6 Got:", level_order(deser.deserialize(ser.serialize(root6))))