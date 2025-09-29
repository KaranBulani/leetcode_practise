'''
Time complexity:  O(n)						each node is visited and processed exactly once.
Space complexity: O(h)						recursion stack uses space proportional to the tree height h.
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # Both reach end
            return True

        if not p or not q:  # Only 1 reach end
            return False

        if p.val != q.val:  # Val doesnt match
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Example 1:", solution.isSameTree(p, q))  # Expected: ?

    # Example 2
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    print("Example 2:", solution.isSameTree(p, q))  # Expected: ?

    # Example 3
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    print("Example 3:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 1: Both trees are empty
    p = None
    q = None
    print("Edge Case 1:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 2: One tree empty, one not
    p = TreeNode(1)
    q = None
    print("Edge Case 2:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 3: Single node trees with same value
    p = TreeNode(5)
    q = TreeNode(5)
    print("Edge Case 3:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 4: Single node trees with different value
    p = TreeNode(5)
    q = TreeNode(6)
    print("Edge Case 4:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 5: Larger identical trees
    p = TreeNode(10,
                 TreeNode(5, TreeNode(3), TreeNode(7)),
                 TreeNode(15, None, TreeNode(18)))
    q = TreeNode(10,
                 TreeNode(5, TreeNode(3), TreeNode(7)),
                 TreeNode(15, None, TreeNode(18)))
    print("Edge Case 5:", solution.isSameTree(p, q))  # Expected: ?

    # Edge Case 6: Larger different trees (subtree mismatch)
    p = TreeNode(10,
                 TreeNode(5, TreeNode(3), TreeNode(7)),
                 TreeNode(15, None, TreeNode(18)))
    q = TreeNode(10,
                 TreeNode(5, TreeNode(3), TreeNode(8)),  # mismatch here (7 vs 8)
                 TreeNode(15, None, TreeNode(18)))
    print("Edge Case 6:", solution.isSameTree(p, q))  # Expected: ?