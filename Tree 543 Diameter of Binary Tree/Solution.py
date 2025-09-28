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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        #returns Height, not res
        def dfs(curr: Optional[TreeNode]) -> int:
            # Use nonlocal to modify the outer 'res'
            # or just add res in self so we can directly assign
            nonlocal res

            if not curr:
                return 0

            L = dfs(curr.left)
            R = dfs(curr.right)

            res = max(res, L + R) #diameter
            return 1 + max(L, R) #height

        dfs(root)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1: [1,2,3,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    print("Expected:", 3, "Got:", solution.diameterOfBinaryTree(root1))

    # Example 2: [1,2]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print("Expected:", 1, "Got:", solution.diameterOfBinaryTree(root2))

    # Edge Case 1: Single node [1]
    root3 = TreeNode(1)
    print("Expected:", 0, "Got:", solution.diameterOfBinaryTree(root3))

    # Edge Case 2: Completely skewed tree (like a linked list) [1,2,3,4]
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    root4.right.right.right = TreeNode(4)
    print("Expected:", 3, "Got:", solution.diameterOfBinaryTree(root4))

    # Edge Case 3: Perfectly balanced tree
    root5 = TreeNode(1)
    root5.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root5.right = TreeNode(3, TreeNode(6), TreeNode(7))
    print("Expected:", 4, "Got:", solution.diameterOfBinaryTree(root5))

    # Edge Case 4: Larger tree with imbalance
    root6 = TreeNode(1)
    root6.left = TreeNode(2, TreeNode(4, TreeNode(8, TreeNode(9))))
    root6.right = TreeNode(3)
    print("Expected:", 5, "Got:", solution.diameterOfBinaryTree(root6))