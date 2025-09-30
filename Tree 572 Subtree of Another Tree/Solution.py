'''
Time complexity:  O(root -> LCA)			path for root to LCA.
Space complexity: O(h)						recursion stack uses space proportional to the tree height h.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left.val if self.left else None}, right={self.right.val if self.right else None})"

class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False

        return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

if __name__ == "__main__":
    solution = Solution()

    # Example 1: From question
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Example 2: From question (subtree structure mismatch)
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 1: Both trees are exactly the same
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    subRoot = TreeNode(1)
    subRoot.left = TreeNode(2)
    subRoot.right = TreeNode(3)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 2: subRoot is a single node present in root
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    subRoot = TreeNode(3)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 3: subRoot is a single node NOT present in root
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    subRoot = TreeNode(10)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 4: root is None, subRoot is not
    root = None
    subRoot = TreeNode(1)
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 5: subRoot is None (by definition, empty tree is subtree of any tree)
    root = TreeNode(1)
    subRoot = None
    print(solution.isSubtree(root, subRoot))  # Expected: ?

    # Edge Case 6: Deep subtree match
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(4)
    subRoot = TreeNode(5)
    subRoot.left = TreeNode(4)
    print(solution.isSubtree(root, subRoot))  # Expected: ?