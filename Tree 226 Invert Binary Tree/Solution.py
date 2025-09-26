'''
####################################################################################################
##################################### Iterative BFS using queue ####################################
####################################################################################################

Time complexity: O(n)  					each node is visited and processed exactly once.
Space complexity: O(n)						queue can hold up to n/2 nodes in the worst case (a completely full last level of the tree).

from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Swap children
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

####################################################################################################
###################################### Recursive DFS PreOrder ######################################
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

from collections import deque

def tree_to_list(root):
    """Convert a binary tree to list (level order), trimming trailing None values."""
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # Trim trailing None values
    while res and res[-1] is None:
        res.pop()
    return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = TreeNode(4,
                     TreeNode(2, TreeNode(1), TreeNode(3)),
                     TreeNode(7, TreeNode(6), TreeNode(9)))
    result1 = solution.invertTree(root1)
    print("Example 1 Output:", tree_to_list(result1))  # Expected: [4,7,2,9,6,3,1]

    # Example 2
    root2 = TreeNode(2,
                     TreeNode(1),
                     TreeNode(3))
    result2 = solution.invertTree(root2)
    print("Example 2 Output:", tree_to_list(result2))  # Expected: [2,3,1]

    # Example 3 (Empty tree)
    root3 = None
    result3 = solution.invertTree(root3)
    print("Example 3 Output:", tree_to_list(result3))  # Expected: []

    # Edge Case 1: Single node tree
    root4 = TreeNode(10)
    result4 = solution.invertTree(root4)
    print("Edge Case 1 Output:", tree_to_list(result4))  # Expected: [10]

    # Edge Case 2: Only left children
    root5 = TreeNode(1,
                     TreeNode(2,
                              TreeNode(3,
                                       TreeNode(4))))
    result5 = solution.invertTree(root5)
    print("Edge Case 2 Output:", tree_to_list(result5))  # Expected: [1,null,2,null,3,null,4]

    # Edge Case 3: Only right children
    root6 = TreeNode(1, None,
                     TreeNode(2, None,
                              TreeNode(3, None,
                                       TreeNode(4))))
    result6 = solution.invertTree(root6)
    print("Edge Case 3 Output:", tree_to_list(result6))  # Expected: [1,2,null,3,null,4]
