'''
Time complexity:  O(n)				traversing through each node
Space complexity: O(h)				recursion stack h
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res = []

        def dfs(curr, currList, targetSum):
            if not curr:
                return

            targetSum -= curr.val
            currList.append(curr.val)

            if targetSum == 0 and not curr.left and not curr.right:
                res.append(list(currList))  # make a copy here

            dfs(curr.left, currList, targetSum)
            dfs(curr.right, currList, targetSum)
            currList.pop()  # backtrack to remove the last node

        dfs(root, [], targetSum)
        return res


if __name__ == "__main__":
    # Helper to build a binary tree from list input (level order)
    from collections import deque


    def build_tree(values):
        if not values:
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


    solution = Solution()

    # Test case 1 (from example 1)
    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    print(solution.pathSum(root1, 22))
    # Expected: [[5,4,11,2], [5,8,4,5]]

    # Test case 2 (from example 2)
    root2 = build_tree([1, 2, 3])
    print(solution.pathSum(root2, 5))
    # Expected: []

    # Test case 3 (from example 3)
    root3 = build_tree([1, 2])
    print(solution.pathSum(root3, 0))
    # Expected: []

    # Test case 4 (edge: single node equals target)
    root4 = build_tree([5])
    print(solution.pathSum(root4, 5))
    # Expected: [[5]]

    # Test case 5 (edge: single node not equal to target)
    root5 = build_tree([1])
    print(solution.pathSum(root5, 2))
    # Expected: []

    # Test case 6 (negative values)
    root6 = build_tree([-2, None, -3])
    print(solution.pathSum(root6, -5))
    # Expected: [[-2, -3]]

    # Test case 7 (empty tree)
    root7 = build_tree([])
    print(solution.pathSum(root7, 0))
    # Expected: []

    # Test case 8 (multiple paths same sum)
    root8 = build_tree([1, 2, 2, 3, 1, 1, 3])
    print(solution.pathSum(root8, 6))
    # Expected: [[1,2,3], [1,2,3]]  # Two symmetric paths