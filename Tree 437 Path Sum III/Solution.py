'''
####################################################################################################
################################## BRUTE FORCE DFS FROM EACH NODE ##################################
####################################################################################################

Time complexity:  O(n^2)				DFS through each node
Space complexity: O(h)					recursion stack h

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def countFromNode(node, target):
            if not node:
                return 0

            count = 1 if node.val == target else 0

            count += countFromNode(node.left, target - node.val)
            count += countFromNode(node.right, target - node.val)
            return count

        # count paths starting from every node
        return (countFromNode(root, targetSum) +
                self.pathSum(root.left, targetSum) +
                self.pathSum(root.right, targetSum))

####################################################################################################
############################################ PREFIX SUM ############################################
####################################################################################################

							 (10)[sum=10]
							/          \
					(10)[sum=20] 	 (-3)[sum=7]
					/	          	      \
			(5)[sum=25]        	  	      (11)[sum=18]
			/        \
	(3)[sum=28]     (2)[sum=27]
		/      \           \
 (3)[31]     (-2)[26]    (1)[28]
				\
				(2)[28]

Time complexity:  O(n^2)				DFS through each node
Space complexity: O(h)					recursion stack h
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        # Show value and existence of children for debugging
        # TreeNode(val=10, left=5, right=15)
        return f"TreeNode(val={self.val}, left={self.left.val if self.left else None}, right={self.right.val if self.right else None})"

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict

        prefix = defaultdict(int)
        prefix[0] = 1  # base case: zero-sum before starting

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val
            count = prefix[currSum - targetSum]  # paths ending here

            prefix[currSum] += 1
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)
            prefix[currSum] -= 1  # backtrack

            return count

        return dfs(root, 0)


if __name__ == "__main__":
    # Helper function to build binary tree from list (LeetCode style)
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

    # --- Test Case 1 (Example 1 from question) ---
    root1 = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    targetSum1 = 8
    print("Test 1 Output:", solution.pathSum(root1, targetSum1))
    print("Expected Output: 3\n")

    # --- Test Case 2 (Example 2 from question) ---
    root2 = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    targetSum2 = 22
    print("Test 2 Output:", solution.pathSum(root2, targetSum2))
    print("Expected Output: 3\n")

    # --- Test Case 3 (Single node equals target) ---
    root3 = build_tree([7])
    targetSum3 = 7
    print("Test 3 Output:", solution.pathSum(root3, targetSum3))
    print("Expected Output: 1\n")

    # --- Test Case 4 (Single node not equals target) ---
    root4 = build_tree([5])
    targetSum4 = 10
    print("Test 4 Output:", solution.pathSum(root4, targetSum4))
    print("Expected Output: 0\n")

    # --- Test Case 5 (Empty tree) ---
    root5 = build_tree([])
    targetSum5 = 5
    print("Test 5 Output:", solution.pathSum(root5, targetSum5))
    print("Expected Output: 0\n")

    # --- Test Case 6 (Multiple overlapping paths) ---
    root6 = build_tree([1,-2,-3,1,3,-2,None,-1])
    targetSum6 = -1
    print("Test 6 Output:", solution.pathSum(root6, targetSum6))
    print("Expected Output: 4\n")

    # --- Test Case 7 (Negative numbers with mixed paths) ---
    root7 = build_tree([-2,None,-3])
    targetSum7 = -5
    print("Test 7 Output:", solution.pathSum(root7, targetSum7))
    print("Expected Output: 1\n")