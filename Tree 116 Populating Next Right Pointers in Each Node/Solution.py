'''
####################################################################################################
##################################### Iterative BFS using queue ####################################
####################################################################################################
Time complexity:  O(logn)   				height of tree
Space complexity: O(q)					    Queue

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # edge case, NOTE: q = deque([ [] ]) is considered TRUE hence we handle it seperately
        if not root:
            return None

        q = deque([root])
        while q:

            size = len(q)
            for i in range(size):

                node = q.popleft()
                if i < size - 1:
                    # if i == size-1(last) then its already pointing to null So dont do anything
                    # after popping q[0] is the next node, so point it there
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

####################################################################################################
############################################# ALSO BFS #############################################
####################################################################################################
Time complexity:  O(logn)					height of tree
Space complexity: O(1)					    leftMost, curr
'''
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftMost = root

        # "node's next linking" is done at parent's level
        # hence we check leftMost.left & not just leftMost
        while leftMost.left:
            curr = leftMost

            # For each node we link left and right
            # and right to next's left
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next

            leftMost = leftMost.left
        return root


if __name__ == "__main__":
    solution = Solution()

    # Helper function to build perfect binary tree from list
    def build_tree(nodes):
        if not nodes:
            return None
        node_list = [Node(val) if val is not None else None for val in nodes]
        for i in range(len(nodes)):
            if node_list[i]:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(nodes):
                    node_list[i].left = node_list[left_idx]
                if right_idx < len(nodes):
                    node_list[i].right = node_list[right_idx]
        return node_list[0]

    # Helper function to print levels using next pointers
    def print_levels(root):
        levels = []
        while root:
            curr = root
            level = []
            while curr:
                level.append(curr.val)
                curr = curr.next
            levels.append(level)
            root = root.left
        return levels

    # 🧩 Test Case 1: Example from question
    root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
    result1 = solution.connect(root1)
    print("Test Case 1 Output:", print_levels(result1))
    print("Expected: [[1], [2,3], [4,5,6,7]]\n")

    # 🧩 Test Case 2: Empty tree
    root2 = build_tree([])
    result2 = solution.connect(root2)
    print("Test Case 2 Output:", print_levels(result2))
    print("Expected: []\n")

    # 🧩 Test Case 3: Single node
    root3 = build_tree([1])
    result3 = solution.connect(root3)
    print("Test Case 3 Output:", print_levels(result3))
    print("Expected: [[1]]\n")

    # 🧩 Test Case 4: Perfect tree with 3 levels, different values
    root4 = build_tree([10, 20, 30, 40, 50, 60, 70])
    result4 = solution.connect(root4)
    print("Test Case 4 Output:", print_levels(result4))
    print("Expected: [[10], [20,30], [40,50,60,70]]\n")

    # 🧩 Test Case 5: Perfect tree with 4 levels (to test deeper structure)
    root5 = build_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    result5 = solution.connect(root5)
    print("Test Case 5 Output:", print_levels(result5))
    print("Expected: [[1], [2,3], [4,5,6,7], [8,9,10,11,12,13,14,15]]\n")