'''
Time complexity:  O(n)				traversing through each node
Space complexity: O(h)				recursion stack h
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if current node is None or equals p or q
        if not root or root == p or root == q:
            return root

        # Search both sides
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides found something, this node is the LCA
        if left and right:
            return root

        # Otherwise, bubble up the non-null one
        return left if left else right

# Helper function to build tree from list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# Helper function to find a node by value
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 3

    # Example 2
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 5)
    q = find_node(root, 4)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 5

    # Example 3
    root = build_tree([1, 2])
    p = find_node(root, 1)
    q = find_node(root, 2)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 1

    # Edge Case 1: Deep tree (LCA is root)
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    p = find_node(root, 4)
    q = find_node(root, 7)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 1

    # Edge Case 2: LCA is one of the nodes
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = find_node(root, 2)
    q = find_node(root, 7)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 2

    # Edge Case 3: Both nodes in the same subtree
    root = build_tree([10, 5, 15, 2, 7, 12, 20])
    p = find_node(root, 2)
    q = find_node(root, 7)
    result = solution.lowestCommonAncestor(root, p, q)
    print(result.val)  # Expected: 5