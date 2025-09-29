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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [True, 0]

            left = dfs(curr.left)
            right = dfs(curr.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.isBalanced(root1))  # Expected: True

    # Example 2: Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(solution.isBalanced(root2))  # Expected: False

    # Example 3: Empty tree
    root3 = None
    print(solution.isBalanced(root3))  # Expected: True

    # Edge Case 1: Single node
    root4 = TreeNode(1)
    print(solution.isBalanced(root4))  # Expected: True

    # Edge Case 2: Completely skewed tree (like a linked list)
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    root5.left.left.left = TreeNode(4)
    print(solution.isBalanced(root5))  # Expected: False

    # Edge Case 3: Perfectly balanced full binary tree
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    print(solution.isBalanced(root6))  # Expected: True