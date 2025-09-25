'''
Time Complexity:  O(n) 					(n = number of nodes; each node visited once)
Space Complexity: O(q) 					(q = maximum number of nodes stored in the queue at once, i.e., the tree's maximum width)
'''

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node in this level, add it to result
                if i == level_size - 1:
                    res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    print(solution.rightSideView(root1))  # Expected: [1,3,4]

    # Example 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.left.left = TreeNode(5)
    print(solution.rightSideView(root2))  # Expected: [1,3,4,5]

    # Example 3
    root3 = TreeNode(1)
    root3.right = TreeNode(3)
    print(solution.rightSideView(root3))  # Expected: [1,3]

    # Example 4 - Empty tree
    root4 = None
    print(solution.rightSideView(root4))  # Expected: []

    # Custom Case 1 - Single Node
    root5 = TreeNode(42)
    print(solution.rightSideView(root5))  # Expected: [42]

    # Custom Case 2 - Right Skewed Tree
    root6 = TreeNode(10)
    root6.right = TreeNode(20)
    root6.right.right = TreeNode(30)
    root6.right.right.right = TreeNode(40)
    print(solution.rightSideView(root6))  # Expected: [10,20,30,40]

    # Custom Case 3 - Left Skewed Tree
    root7 = TreeNode(5)
    root7.left = TreeNode(4)
    root7.left.left = TreeNode(3)
    root7.left.left.left = TreeNode(2)
    print(solution.rightSideView(root7))  # Expected: [5,4,3,2]

    # Custom Case 4 - Mixed Tree
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    root8.right.left = TreeNode(6)
    root8.right.right = TreeNode(7)
    print(solution.rightSideView(root8))  # Expected: [1,3,7]