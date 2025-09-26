'''
####################################################################################################
##################################### Iterative BFS using queue ####################################
####################################################################################################

Time complexity: O(n)  					each node is visited and processed exactly once.
Space complexity: O(n)						queue can hold up to n/2 nodes in the worst case (a completely full last level of the tree).

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        res = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res += 1
        return res

####################################################################################################
########################################## Iterative DFS ###########################################
####################################################################################################

Time complexity:  O(n)						each node is visited and processed exactly once.
Space complexity: O(h)						stack uses space proportional to the tree height h.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root,1)] # node, depth
        res = 0

        while stack:
            curr, level = stack.pop()
            res = max(res, level)
            if curr.left:
                stack.append([curr.left, level + 1])
            if curr.right:
                stack.append([curr.right, level + 1])

        return res

####################################################################################################
########################################## Recursive DFS ###########################################
####################################################################################################

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Normal case from problem statement
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print("Test 1:", solution.maxDepth(root1))  # Expected: ?

    # Example 2: Skewed tree (only right child)
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print("Test 2:", solution.maxDepth(root2))  # Expected: ?

    # Edge Case 1: Empty tree
    root3 = None
    print("Test 3:", solution.maxDepth(root3))  # Expected: ?

    # Edge Case 2: Single node tree
    root4 = TreeNode(10)
    print("Test 4:", solution.maxDepth(root4))  # Expected: ?

    # Edge Case 3: Skewed tree (only left children)
    root5 = TreeNode(5)
    root5.left = TreeNode(4)
    root5.left.left = TreeNode(3)
    root5.left.left.left = TreeNode(2)
    print("Test 5:", solution.maxDepth(root5))  # Expected: ?

    # Edge Case 4: Complete binary tree
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.right = TreeNode(3)
    root6.left.left = TreeNode(4)
    root6.left.right = TreeNode(5)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(7)
    print("Test 6:", solution.maxDepth(root6))  # Expected: ?