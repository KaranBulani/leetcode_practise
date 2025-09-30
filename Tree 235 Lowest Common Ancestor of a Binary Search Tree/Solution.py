'''
####################################################################################################
########################################## Iterative DFS ###########################################
####################################################################################################

Time complexity:  O(root -> LCA)			path for root to LCA.
Space complexity: O(1)						No recursion, No Space

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            #curr bada hai toh left jaa
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            #curr chota hai toh right jaa
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            #split hua toh yehi hua LCA
            else:
                return curr
####################################################################################################
########################################## Recursive DFS ###########################################
####################################################################################################

Time complexity:  O(root -> LCA)			path for root to LCA.
Space complexity: O(h)						recursion stack uses space proportional to the tree height h.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    # Example 1
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    p1, q1 = root1.left, root1.right  # nodes 2 and 8
    print(solution.lowestCommonAncestor(root1, p1, q1).val)  # Expected: ?

    # Example 2
    p2, q2 = root1.left, root1.left.right  # nodes 2 and 4
    print(solution.lowestCommonAncestor(root1, p2, q2).val)  # Expected: ?

    # Example 3
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    p3, q3 = root2, root2.left  # nodes 2 and 1
    print(solution.lowestCommonAncestor(root2, p3, q3).val)  # Expected: ?

    # Additional edge cases
    # Case 4: Skewed BST (all right children)
    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.right = TreeNode(3)
    root3.right.right.right = TreeNode(4)
    p4, q4 = root3.right, root3.right.right  # nodes 2 and 3
    print(solution.lowestCommonAncestor(root3, p4, q4).val)  # Expected: ?

    # Case 5: Skewed BST (all left children)
    root4 = TreeNode(4)
    root4.left = TreeNode(3)
    root4.left.left = TreeNode(2)
    root4.left.left.left = TreeNode(1)
    p5, q5 = root4.left.left, root4.left.left.left  # nodes 2 and 1
    print(solution.lowestCommonAncestor(root4, p5, q5).val)  # Expected: ?

    # Case 6: Both nodes are the same node
    root5 = TreeNode(5)
    root5.left = TreeNode(3)
    root5.right = TreeNode(8)
    p6 = q6 = root5.left  # node 3 and node 3
    print(solution.lowestCommonAncestor(root5, p6, q6).val)  # Expected: ?

    # Case 7: Larger balanced BST
    root6 = TreeNode(20)
    root6.left = TreeNode(10)
    root6.right = TreeNode(30)
    root6.left.left = TreeNode(5)
    root6.left.right = TreeNode(15)
    root6.right.left = TreeNode(25)
    root6.right.right = TreeNode(35)
    p7, q7 = root6.left.left, root6.left.right  # nodes 5 and 15
    print(solution.lowestCommonAncestor(root6, p7, q7).val)  # Expected: ?
