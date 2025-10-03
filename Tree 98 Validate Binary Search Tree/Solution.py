'''
####################################################################################################
###################################### PREORDER TRAVERSAL ##########################################
####################################################################################################

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, left, right):
        if not node:
            #Null always true
            return True

        if not (left < node.val < right):
            #at any moment this doesnt match then stop recursive and fail
            return False

        #if all good for current node then keep going Left, Right
        return ( self.valid(node.left, left, node.val) and
                 self.valid(node.right, node.val, right) )

####################################################################################################
###################################### IN ORDER TRAVERSAL ##########################################
####################################################################################################
Time complexity:  O(n)				Traversing through all nodes
Space complexity: O(h)				recursion stack uses space proportional to the tree height h.
'''
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr: Optional[TreeNode]):
            if not curr:
                # Note: How I reversing float(inf/-inf), automatically helps in currCond, currMin, currMax during base case
                return [float("inf"), float("-inf"), True]
            Lmin, Lmax, LCond = dfs(curr.left)
            Rmin, Rmax, RCond = dfs(curr.right)
            currCond = Lmax < curr.val < Rmin
            currMin = min(Lmin, Rmin, curr.val)
            currMax = max(Lmax, Rmax, curr.val)
            return [currMin, currMax, LCond and currCond and RCond]

        return dfs(root)[2]

if __name__ == "__main__":
    solution = Solution()

    # Example 1 from the question
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(solution.isValidBST(root1))  # Expected: True

    # Example 2 from the question
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4, TreeNode(3), TreeNode(6))
    print(solution.isValidBST(root2))  # Expected: False

    # Edge case: Single node tree
    root3 = TreeNode(1)
    print(solution.isValidBST(root3))  # Expected: True

    # Edge case: Left child equal to root (invalid, should be strictly less)
    root4 = TreeNode(10, TreeNode(10), TreeNode(15))
    print(solution.isValidBST(root4))  # Expected: False

    # Edge case: Right child equal to root (invalid, should be strictly greater)
    root5 = TreeNode(10, TreeNode(5), TreeNode(10))
    print(solution.isValidBST(root5))  # Expected: False

    # Valid larger BST
    root6 = TreeNode(20,
                     TreeNode(10, TreeNode(5), TreeNode(15)),
                     TreeNode(30, TreeNode(25), TreeNode(35)))
    print(solution.isValidBST(root6))  # Expected: True

    # Invalid because a left-descendant is greater than root
    root7 = TreeNode(20,
                     TreeNode(10, TreeNode(5), TreeNode(25)),  # 25 invalid here
                     TreeNode(30, TreeNode(25), TreeNode(35)))
    print(solution.isValidBST(root7))  # Expected: False

    # Edge case: Skewed increasing tree (like a linked list, all to the right)
    root8 = TreeNode(1, None,
                     TreeNode(2, None,
                              TreeNode(3, None,
                                       TreeNode(4))))
    print(solution.isValidBST(root8))  # Expected: True

    # Edge case: Skewed decreasing tree (like a linked list, all to the left)
    root9 = TreeNode(4,
                     TreeNode(3,
                              TreeNode(2,
                                       TreeNode(1))))
    print(solution.isValidBST(root9))  # Expected: True

    # Edge case: Very large and very small values
    root10 = TreeNode(0,
                      TreeNode(-2 ** 31),
                      TreeNode(2 ** 31 - 1))
    print(solution.isValidBST(root10))  # Expected: True