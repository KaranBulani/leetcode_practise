'''
Intuition

The important thing I noticed is that every node has a depth in the tree.
The contribution of each node depends on its depth: contribution = nums[i] × (height - depth[i] + 1)

So first I calculate the depth of every node.

Instead of calculating the depth again and again, I store the already calculated depth in the depth[] array. This works like memoization.

Once I know the maximum depth (ht), I can calculate the contribution of every node.

####################################################################################################
Approach
1. Create a depth[] array.
2. The root has depth 1.
3. For every node whose depth is not calculated:
    * Recursively go to its parent.
    * Calculate the parent's depth.
    * Current node depth = parent's depth + 1.
4. Store the calculated depth so we don't calculate it again.
5. Find the maximum depth ht.
6. For every node, calculate:
        nums[i] × (ht - depth[i] + 1)
7. Add all contributions and return the answer.

####################################################################################################
Dry Run

Consider:
    parent = [-1, 0, 0, 1]
    nums   = [10, 20, 30, 40]

The tree is:
        0
       / \
      1   2
     /
    3

Calculate depths
depth[0] = 1
depth[1] = 2
depth[2] = 2
depth[3] = 3

So:
ht = 3

Now calculate the contribution.

Node 0
    10 × (3 - 1 + 1)
    = 10 × 3
    = 30
Node 1
    20 × (3 - 2 + 1)
    = 20 × 2
    = 40
Node 2
    30 × (3 - 2 + 1)
    = 30 × 2
    = 60
Node 3
    40 × (3 - 3 + 1)
    = 40 × 1
    = 40

Final answer: 30 + 40 + 60 + 40 = 170

####################################################################################################
Why Memoization?

Suppose many nodes have the same parent chain.
Without storing the calculated depth, we may repeatedly traverse the same parent nodes.
For example:
        0
       / \
      1   2
     /     \
    3       4
When calculating node 3, we calculate: 3 → 1 → 0
When calculating node 4, we calculate: 4 → 2 → 0
Since depth[0] is already stored, we don't need to calculate it again.

So depth[] works as a memoization array.
####################################################################################################
Complexity

Time complexity: O(n)
Each node's depth is calculated only once.

Space complexity: O(n)
For the depth[] array and recursive call stack.
'''

class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        depth = [0] * n

        depth[0] = 1
        ht = 1
        total = 0

        def fn(node):
            if parent[node] == -1:
                return 1

            if depth[node] != 0:
                return depth[node]

            depth[node] = fn(parent[node]) + 1
            return depth[node]

        for i in range(n):
            if depth[i] == 0:
                fn(i)

            ht = max(ht, depth[i])

        for i in range(n):
            total += nums[i] * (ht - depth[i] + 1)

        return total


if __name__ == "__main__":
    solution = Solution()

    # Example 1: Given example
    parent = [-1, 0, 0, 0, 2, 2]
    nums = [5, 2, 3, 1, 4, 6]
    result = solution.weightedSum(parent, nums)
    print("Example 1:", result, "Expected:", 37)

    # Example 2: Given example - completely skewed tree
    parent = [-1, 0, 1, 2]
    nums = [1, 2, 3, 4]
    result = solution.weightedSum(parent, nums)
    print("Example 2:", result, "Expected:", 20)

    # Edge Case 1: Single node
    parent = [-1]
    nums = [10]
    result = solution.weightedSum(parent, nums)
    print("Single node:", result, "Expected:", 10)

    # Edge Case 2: Two nodes
    parent = [-1, 0]
    nums = [5, 10]
    result = solution.weightedSum(parent, nums)
    print("Two nodes:", result, "Expected:", 20)

    # Edge Case 3: Star-shaped tree
    #       0
    #    /  |  \
    #   1   2   3
    parent = [-1, 0, 0, 0]
    nums = [10, 1, 2, 3]
    result = solution.weightedSum(parent, nums)
    print("Star tree:", result, "Expected:", 36)

    # Edge Case 4: Completely skewed tree
    # 0 -> 1 -> 2 -> 3 -> 4
    parent = [-1, 0, 1, 2, 3]
    nums = [1, 1, 1, 1, 1]
    result = solution.weightedSum(parent, nums)
    print("Skewed tree:", result, "Expected:", 15)

    # Edge Case 5: Root has many children, all leaves
    parent = [-1, 0, 0, 0, 0, 0]
    nums = [100, 10, 20, 30, 40, 50]
    result = solution.weightedSum(parent, nums)
    print("Root with many leaves:", result, "Expected:", 350)

    # Edge Case 6: Different depths
    #
    #          0
    #        /   \
    #       1     2
    #      /       \
    #     3         4
    #    /
    #   5
    parent = [-1, 0, 0, 1, 2, 3]
    nums = [1, 2, 3, 4, 5, 6]
    result = solution.weightedSum(parent, nums)
    print("Different depths:", result, "Expected:", 45)

    # Edge Case 7: Large values
    parent = [-1, 0, 0, 1, 1]
    nums = [1000000, 1000000, 1000000, 1000000, 1000000]
    result = solution.weightedSum(parent, nums)
    print("Large values:", result, "Expected:", 8000000)

    # Edge Case 8: Unbalanced tree
    #
    #          0
    #       /     \
    #      1       2
    #     /       / \
    #    3       4   5
    #   /
    #  6
    parent = [-1, 0, 0, 1, 2, 2, 3]
    nums = [5, 4, 3, 2, 1, 6, 7]
    result = solution.weightedSum(parent, nums)
    print("Unbalanced tree:", result, "Expected:", 65)