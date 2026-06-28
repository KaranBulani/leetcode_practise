'''
1. Understand the Problem
Given the root of a binary tree, modify it in-place so that:
* Every node's left pointer becomes None.
* Every node's right pointer points to the next node in preorder traversal (Root → Left → Right).

Example:
Input
        1
       / \
      2   5
     / \   \
    3   4   6

Preorder:
1 2 3 4 5 6

Output:
            1
             \
              2
               \
                3
                 \
                  4
                   \
                    5
                     \
                      6

####################################################################################################
2. Brute Force

Idea
1. Perform preorder traversal.
2. Store all nodes in an array.
3. Reconnect them.

nodes = [1,2,3,4,5,6]

	1.right = 2
	2.right = 3
	...
	left = None


Time
* Traversal: O(n)
* Reconnecting: O(n)
Time: O(n)
Space: O(n)

####################################################################################################
3. Optimal Idea (Reverse Preorder)

Instead of storing nodes, we can build the linked list backwards.

Normally preorder is
	Root
	Left
	Right

Process it in reverse:
	Right
	Left
	Root

Maintain one variable:	prev
which stores the already flattened part.

Suppose we're at node 4.

Already flattened: 4 -> 5 -> 6

Then
4.right = prev
4.left = None
prev = 4

Eventually the root becomes the head.

####################################################################################################
4. Dry Run

Initial tree
        1
       / \
      2   5
     / \   \
    3   4   6

Initially
	prev = None

Visit 6
	6.right = None
	6.left = None

prev = 6
Result - 6

Visit 5
	5.right = 6
	5.left = None

prev = 5
5 -> 6

Visit 4
	4.right = 5
	prev = 4
4 -> 5 -> 6

Visit 3
	3 -> 4 -> 5 -> 6

Visit 2
	2 -> 3 -> 4 -> 5 -> 6

Visit 1
	1 -> 2 -> 3 -> 4 -> 5 -> 6

Done.

####################################################################################################
5. Why Reverse Preorder?

When processing a node, we already want its flattened right side to be ready.

Reverse preorder guarantees:
	Right processed
	↓
	Left processed
	↓
	Current node attaches to them

So every node only needs
node.right = prev

####################################################################################################
6. Algorithm

prev = None

DFS(node):
    if node is None:
        return

    DFS(node.right)
    DFS(node.left)

    node.right = prev
    node.left = None

    prev = node

####################################################################################################
7. Python Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def dfs(node):
            nonlocal prev

            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node

        dfs(root)

####################################################################################################
8. Complexity

* Time: O(n) (every node visited once)
* Space: O(h) (recursion stack), where h is the tree height.

  * Worst case: O(n) (skewed tree)
  * Balanced tree: O(log n)

####################################################################################################
9. Follow-up: Morris Traversal (O(1) Extra Space)

An iterative solution achieves O(1) extra space by rewiring pointers as it traverses the tree.

For each node:
1. If it has a left child, find the rightmost node of its left subtree.
2. Connect that rightmost node's right pointer to the current node's original right subtree.
3. Move the left subtree to the right.
4. Set left = None.
5. Move to node.right.

Whenever a node has a left subtree, insert that entire left subtree between the node and its right subtree.

                Start
                  |
                  v
            curr = root
                  |
                  v
          Is curr == None?
            /           \
          Yes            No
          |              |
         End             |
                         v
              Does curr have left?
                /              \
              No                Yes
              |                  |
              |          pred = curr.left
              |                  |
              |          Find rightmost node
              |          in left subtree
              |                  |
              |                  v
              |     pred.right = curr.right
              |                  |
              |     curr.right = curr.left
              |                  |
              |     curr.left = None
              |                  |
               \_________________/
                        |
                        v
               curr = curr.right
                        |
                        |
                     Repeat

####################################################################################################
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root

        while curr:
            if curr.left:
                pred = curr.left

                while pred.right:
                    pred = pred.right

                pred.right = curr.right
                curr.right = curr.left
                curr.left = None

            curr = curr.right

####################################################################################################
Complexity

* Time: O(n)
* Space: O(1)

This Morris-style solution is the most space-efficient and is often the preferred follow-up answer in interviews.

####################################################################################################

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None

        def dfs(node):
            nonlocal prev

            if not node:
                return

            # Save children before rewiring pointers
            left = node.left
            right = node.right

            if prev:
                prev.right = node

            prev = node
            node.left = None
            node.right = None

            dfs(left)
            dfs(right)

        dfs(root)

✅ Time: O(n)
✅ Space: O(h)
'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        

# Helper function to build a binary tree from level-order list
from collections import deque

def build_tree(values):
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


# Helper function to print flattened tree
def print_flattened(root):
    result = []
    while root:
        result.append(root.val)

        if root.left is not None:
            result.append("LEFT_NOT_NULL")  # Should never happen

        root = root.right

    print(result)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            [1, 2, 5, 3, 4, None, 6],
            [1, 2, 3, 4, 5, 6]
        ),

        # Example 2
        (
            [],
            []
        ),

        # Example 3
        (
            [0],
            [0]
        ),

        # Only left children
        (
            [1, 2, None, 3, None, 4],
            [1, 2, 3, 4]
        ),

        # Only right children
        (
            [1, None, 2, None, 3, None, 4],
            [1, 2, 3, 4]
        ),

        # Complete binary tree
        (
            [1, 2, 5, 3, 4, 6, 7],
            [1, 2, 3, 4, 5, 6, 7]
        ),

        # Zig-zag tree
        (
            [1, 2, None, None, 3, 4],
            [1, 2, 3, 4]
        ),

        # Left subtree only
        (
            [1, 2, None, 3, 4],
            [1, 2, 3, 4]
        ),

        # Right subtree only
        (
            [1, None, 2, 3, 4],
            [1, 2, 3, 4]
        ),

        # Larger mixed tree
        (
            [1, 2, 3, 4, None, 5, 6, None, 7],
            [1, 2, 4, 7, 3, 5, 6]
        ),
    ]

    for i, (tree, expected) in enumerate(test_cases, 1):
        print(f"Test Case {i}")

        root = build_tree(tree)
        solution.flatten(root)

        print("Expected:", expected)
        print("Your Output:", end=" ")
        print_flattened(root)
        print("-" * 50)