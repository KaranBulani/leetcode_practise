'''
Time complexity:  O(n)				Traversing through all nodes
Space complexity: O(h)				recursion stack uses space proportional to the tree height h.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        currMax = float("-inf")

        def dfs(curr: TreeNode, currMax) -> int:
            if not curr:
                return 0
            newMax = max(currMax, curr.val)
            isGoodOne = 1 if newMax == curr.val else 0
            return isGoodOne + dfs(curr.left, newMax) + dfs(curr.right, newMax)

        return dfs(root, currMax)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    print(solution.goodNodes(root1))  # Expected: 4

    # Example 2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)
    print(solution.goodNodes(root2))  # Expected: 3

    # Example 3
    root3 = TreeNode(1)
    print(solution.goodNodes(root3))  # Expected: 1

    # Edge Case 1: Skewed increasing tree (all good)
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    root4.right.right.right = TreeNode(4)
    print(solution.goodNodes(root4))  # Expected: 4

    # Edge Case 2: Skewed decreasing tree (only root good)
    root5 = TreeNode(10)
    root5.right = TreeNode(9)
    root5.right.right = TreeNode(8)
    root5.right.right.right = TreeNode(7)
    print(solution.goodNodes(root5))  # Expected: 1

    # Edge Case 3: Mixed positives & negatives
    root6 = TreeNode(0)
    root6.left = TreeNode(-1)
    root6.right = TreeNode(1)
    root6.left.left = TreeNode(-2)
    root6.right.right = TreeNode(2)
    print(solution.goodNodes(root6))  # Expected: 4

    # Edge Case 4: All nodes have same value
    root7 = TreeNode(5)
    root7.left = TreeNode(5)
    root7.right = TreeNode(5)
    root7.left.left = TreeNode(5)
    root7.left.right = TreeNode(5)
    root7.right.left = TreeNode(5)
    root7.right.right = TreeNode(5)
    print(solution.goodNodes(root7))  # Expected: 7