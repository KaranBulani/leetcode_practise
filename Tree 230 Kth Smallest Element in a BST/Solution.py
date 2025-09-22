'''
####################################################################################################
######################################## Iterative Solution ########################################
####################################################################################################

Time Complexity:  O(k + h)      				    (where h is height, k is nth smallest element)
                  O(n) in worst case
Space Complexity: O(h)               	            (for stack)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while True:
            # Go left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop from stack
            # curr: From None goes to Stack[-1]
            curr = stack.pop()
            k -= 1
            if k == 0:   # Found kth smallest
                return curr.val

            # Move to right child
            curr = curr.right

####################################################################################################
######################################## Recursive Solution ########################################
####################################################################################################

Time Complexity:  O(k + h)      				   (where h is height, k is nth smallest element)
                  O(n) in worst case
Space Complexity: O(k + h)               	       (for k for res and h for Recursive Call Stack)
                  O(n) in worst case
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inorder(node):
            if not node or len(res) >= k:  # stop when enough elements collected
                return
            inorder(node.left)
            # Still check as child nodes would be inserted
            # but parent calls are yet pending to be executed
            if len(res) < k:
                res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[-1]  # kth smallest will be the last appended

def build_tree_from_list(values):
    """Helper to build a tree from level-order list with None as missing nodes."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = build_tree_from_list([3, 1, 4, None, 2])
    print("Test 1:", solution.kthSmallest(root1, 1), "Expected:", 1)

    # Example 2
    root2 = build_tree_from_list([5, 3, 6, 2, 4, None, None, 1])
    print("Test 2:", solution.kthSmallest(root2, 3), "Expected:", 3)

    # Edge Case 1: Single node tree
    root3 = build_tree_from_list([10])
    print("Test 3:", solution.kthSmallest(root3, 1), "Expected:", 10)

    # Edge Case 2: Complete BST
    root4 = build_tree_from_list([4, 2, 6, 1, 3, 5, 7])
    print("Test 4:", solution.kthSmallest(root4, 4), "Expected:", 4)  # Middle element

    # Edge Case 3: Left-skewed tree (all nodes to left)
    root5 = build_tree_from_list([5, 4, None, 3, None, 2, None, 1])
    print("Test 5:", solution.kthSmallest(root5, 1), "Expected:", 1)
    print("Test 6:", solution.kthSmallest(root5, 4), "Expected:", 4)

    # Edge Case 4: Right-skewed tree (all nodes to right)
    root6 = build_tree_from_list([1, None, 2, None, 3, None, 4])
    print("Test 7:", solution.kthSmallest(root6, 3), "Expected:", 3)

    # Edge Case 5: Larger k (last element in tree)
    root7 = build_tree_from_list([3, 1, 4, None, 2])
    print("Test 8:", solution.kthSmallest(root7, 4), "Expected:", 4)
