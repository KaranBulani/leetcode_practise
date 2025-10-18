'''
Time complexity:  O(nlogn)						because of sorting
Space complexity: O(n)							nodes list
'''
from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        nodes = []  # (col, row, val)

        def dfs(curr: Optional[TreeNode], row: int, col: int):
            if not curr:
                return
            # col is kept first as that will be used later for sorting
            nodes.append((col, row, curr.val))
            dfs(curr.left, row + 1, col - 1)
            dfs(curr.right, row + 1, col + 1)

        dfs(root, 0, 0)
        # Sort by column(-ve comes 1st), then row(top comes first),
        # then value (when row/col is same) sort by value size
        nodes.sort()

        res = defaultdict(list)
        for col, row, val in nodes:
            res[col].append(val)

        # Return columns in order of x
        return [res[x] for x in sorted(res)]


if __name__ == "__main__":
    solution = Solution()

    # Helper function to build tree easily
    def build_tree(values):
        from collections import deque
        if not values:
            return None
        root = TreeNode(values[0])
        q = deque([root])
        i = 1
        while q and i < len(values):
            node = q.popleft()
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1
        return root

    # Example 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print(solution.verticalTraversal(root1))  # Expected: [[9], [3, 15], [20], [7]]

    # Example 2
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(solution.verticalTraversal(root2))  # Expected: [[4], [2], [1, 5, 6], [3], [7]]

    # Example 3
    root3 = build_tree([1, 2, 3, 4, 6, 5, 7])
    print(solution.verticalTraversal(root3))  # Expected: [[4], [2], [1, 5, 6], [3], [7]]

    # Edge Case 1: Single node
    root4 = build_tree([1])
    print(solution.verticalTraversal(root4))  # Expected: [[1]]

    # Edge Case 2: Completely left-skewed tree
    root5 = build_tree([1, 2, None, 3, None, 4])
    print(solution.verticalTraversal(root5))  # Expected: [[4], [3], [2], [1]]

    # Edge Case 3: Completely right-skewed tree
    root6 = build_tree([1, None, 2, None, 3, None, 4])
    print(solution.verticalTraversal(root6))  # Expected: [[1], [2], [3], [4]]

    # Edge Case 4: Tree with duplicate values
    root7 = build_tree([1, 2, 2, 3, 3, 3, 3])
    print(solution.verticalTraversal(root7))  # Expected: [[3], [2, 3], [1, 3, 3], [2], [3]]

    # Edge Case 5: Random mixed structure
    root8 = build_tree([1, 2, 3, None, 4, 5, None, None, 6])
    print(solution.verticalTraversal(root8))  # Expected: [[2, 6], [1, 4, 5], [3]]