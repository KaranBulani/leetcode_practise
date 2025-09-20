'''
Time Complexity:  O(h)					(Where h is height of tree)
Space Complexity: O(h)               	(for recursive stack)
'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If root is None, insert here
        if not root:
            return TreeNode(val)

        # Go left if val is smaller
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)

        # Go right if val is larger
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        # Return root after insertion, (Above doesnt change)
        return root

def tree_to_list(root: Optional[TreeNode]) -> list:
    """Convert binary tree to list using level-order traversal (like LeetCode)."""
    if not root:
        return []  # Empty tree → return empty list

    result = []
    q = deque([root])  # Queue for BFS, start with root

    while q:
        node = q.popleft()  # Pop from front of queue
        if node:
            result.append(node.val)  # Store current node value
            q.append(node.left)  # Add left child (even if None)
            q.append(node.right)  # Add right child (even if None)
        else:
            result.append(None)  # Mark missing node as None

    # Trim trailing None values (not needed in LeetCode format)
    while result and result[-1] is None:
        result.pop()

    return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7))
    val = 5
    result = solution.insertIntoBST(root, val)
    print("Test 1:", tree_to_list(result))  # Expected: [4,2,7,1,3,5]

    # Example 2
    root = TreeNode(40,
                    TreeNode(20, TreeNode(10), TreeNode(30)),
                    TreeNode(60, TreeNode(50), TreeNode(70)))
    val = 25
    result = solution.insertIntoBST(root, val)
    print("Test 2:", tree_to_list(result))  # Expected: [40,20,60,10,30,50,70,null,null,25]

    # Example 3
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7))
    val = 5
    result = solution.insertIntoBST(root, val)
    print("Test 3:", tree_to_list(result))  # Expected: [4,2,7,1,3,5]

    # Edge Case 1: Empty tree
    root = None
    val = 10
    result = solution.insertIntoBST(root, val)
    print("Edge Case 1:", tree_to_list(result))  # Expected: [10]

    # Edge Case 2: Insert as leftmost child
    root = TreeNode(10, TreeNode(5), TreeNode(15))
    val = 1
    result = solution.insertIntoBST(root, val)
    print("Edge Case 2:", tree_to_list(result))  # Expected: node 1 gets inserted left of 5

    # Edge Case 3: Insert as rightmost child
    root = TreeNode(10, TreeNode(5), TreeNode(15))
    val = 20
    result = solution.insertIntoBST(root, val)
    print("Edge Case 3:", tree_to_list(result))  # Expected: node 20 gets inserted right of 15

    # Edge Case 4: Deep insertion
    root = TreeNode(8,
                    TreeNode(4, TreeNode(2), TreeNode(6)),
                    TreeNode(12, TreeNode(10), TreeNode(14)))
    val = 11
    result = solution.insertIntoBST(root, val)
    print("Edge Case 4:", tree_to_list(result))  # Expected: node 11 goes as left child of 12’s right (14)
