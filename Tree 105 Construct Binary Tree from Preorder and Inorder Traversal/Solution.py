'''
Time Complexity:  O(n*2)					(n to build tree, n for inorder.index())
Space Complexity: O(n^2)               		(n for recursion stack, n for list slicings)
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Base case there's no tree to build
        if not preorder or not inorder:
            return None

        # The first element of preorder is always the root
        root = TreeNode(preorder[0])

        # Find root value in "inorder" to split left, right subtrees
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree
        # Left subtree preorder → elements after root up to length of left subtree
        # Left subtree inorder  → all elements before the root index
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[: mid])

        # Recursively build the right subtree
        # Right subtree preorder → remaining elements after left subtree
        # Right subtree inorder  → all elements after the root index
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1:])

        # Return the constructed tree
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

    # Example 1: From question
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [3,9,20,null,null,15,7]

    # Example 2: Single node
    preorder = [-1]
    inorder = [-1]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [-1]

    # Edge case: Only left children (degenerate tree like a linked list)
    preorder = [4, 3, 2, 1]
    inorder = [1, 2, 3, 4]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [4,3,null,2,null,1]

    # Edge case: Only right children (mirror of above)
    preorder = [1, 2, 3, 4]
    inorder = [1, 2, 3, 4]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [1,null,2,null,3,null,4]

    # Balanced tree
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [1,2,3,4,5,6,7]

    # Mixed shape (not perfectly balanced)
    preorder = [10, 5, 2, 7, 15, 12, 20]
    inorder = [2, 5, 7, 10, 12, 15, 20]
    result = solution.buildTree(preorder, inorder)
    print(tree_to_list(result))  # Expected tree: [10,5,15,2,7,12,20]
