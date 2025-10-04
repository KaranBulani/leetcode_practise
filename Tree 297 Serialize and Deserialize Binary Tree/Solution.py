'''
Time complexity:  O(n)				Traversing through all nodes
Space complexity: O(h + n)			recursion stack uses h, res len would be n.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def preorder(curr):
            if not curr:
                res.append("null")
                return
            res.append(str(curr.val))
            preorder(curr.left)
            preorder(curr.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def reversePreOrder():
            if vals[self.i] == "null":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = reversePreOrder()
            node.right = reversePreOrder()
            return node
        return reversePreOrder()

if __name__ == "__main__":
    ser = Codec()
    deser = Codec()

    # Example 1
    # Input: [1,2,3,null,null,4,5]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    print("Test 1 ->", deser.serialize(deser.deserialize(ser.serialize(root1))))
    # Expected: [1,2,3,null,null,4,5] (same structure)

    # Example 2
    # Input: []
    root2 = None
    print("Test 2 ->", deser.serialize(deser.deserialize(ser.serialize(root2))))
    # Expected: []

    # Edge Case 1: Single node
    root3 = TreeNode(10)
    print("Test 3 ->", deser.serialize(deser.deserialize(ser.serialize(root3))))
    # Expected: [10]

    # Edge Case 2: Only left children
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    root4.left.left.left = TreeNode(4)
    print("Test 4 ->", deser.serialize(deser.deserialize(ser.serialize(root4))))
    # Expected: [1,2,null,3,null,4]

    # Edge Case 3: Only right children
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    root5.right.right.right = TreeNode(4)
    print("Test 5 ->", deser.serialize(deser.deserialize(ser.serialize(root5))))
    # Expected: [1,null,2,null,3,null,4]

    # Edge Case 4: Larger balanced tree
    root6 = TreeNode(5)
    root6.left = TreeNode(3)
    root6.right = TreeNode(7)
    root6.left.left = TreeNode(2)
    root6.left.right = TreeNode(4)
    root6.right.left = TreeNode(6)
    root6.right.right = TreeNode(8)
    print("Test 6 ->", deser.serialize(deser.deserialize(ser.serialize(root6))))
    # Expected: [5,3,7,2,4,6,8]