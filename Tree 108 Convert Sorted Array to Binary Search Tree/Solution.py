'''
Approach (Divide & Conquer)

Since the array is sorted, the middle element naturally becomes the root of a height-balanced BST.

Algorithm:
1. Pick the middle element as the root.
2. Recursively build the left subtree from the left half.
3. Recursively build the right subtree from the right half.
4. Return the root.

Because each recursive call halves the array, the resulting BST is balanced.
####################################################################################################

Example

Input: nums = [-10, -3, 0, 5, 9]

Recursive construction:
            0
          /   \
       -10     5
         \      \
         -3      9

Another valid balanced BST is:
            0
          /   \
        -3     9
       /      /
    -10      5

Both are accepted.
####################################################################################################

Time Complexity
* Every element is visited exactly once.
* O(n)

Space Complexity
* Recursive call stack:
  * Height of balanced BST = O(log n)
* No extra data structures.
Overall: O(log n) auxiliary space.
'''
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)

# Helper to serialize tree into LeetCode level-order format
def serialize(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        node = q.popleft()

        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)

    # Remove trailing nulls
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([-10, -3, 0, 5, 9], "Height-balanced BST"),
        ([1, 3], "Height-balanced BST"),

        # Single element
        ([1], [1]),

        # Three elements
        ([1, 2, 3], "Height-balanced BST"),

        # Four elements (even length)
        ([1, 2, 3, 4], "Height-balanced BST"),

        # Five elements
        ([1, 2, 3, 4, 5], "Height-balanced BST"),

        # Negative numbers
        ([-5, -4, -3, -2, -1], "Height-balanced BST"),

        # Mixed negative/positive
        ([-7, -3, 0, 2, 5, 8], "Height-balanced BST"),

        # Larger odd length
        (list(range(1, 8)), "Height-balanced BST"),

        # Larger even length
        (list(range(1, 9)), "Height-balanced BST"),

        # Maximum-ish variety
        ([-10000, -5000, 0, 5000, 10000], "Height-balanced BST"),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        root = solution.sortedArrayToBST(nums)

        print(f"Test Case {i}")
        print("Input    :", nums)
        print("Output   :", serialize(root))
        print("Expected :", expected)
        print("-" * 60)