'''
####################################################################################################
########################################### Recursive DFS ##########################################
####################################################################################################
                            nums = [1, 2, 3]
   i=0                                   []
                                 /                 \
   i=1                    [1]                          []
                       /        \                  /       \
   i=2            [1,2]         [1]              [2]       	[]
                 /   \         /   \          /   \         /    \
   i=3     [1,2,3]  [1,2]   [1,3]   [1]    [2,3]   [2]    [3]		[]

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subSet, currSet = [], []

        def dfs(i: int, currSet: list):
            if i >= len(nums):
                subSet.append(currSet.copy())
                return

            # decision to include nums[i]
            currSet.append(nums[i])
            dfs(i + 1, currSet)

            # decision to NOT include nums[i]
            currSet.pop()
            dfs(i + 1, currSet)

        dfs(0, currSet)
        return subSet

####################################################################################################
########################################### Iterative DFS ##########################################
####################################################################################################
Status of path, which appends to res

[] <── backtrack(0,[]) ──> Initial Call
│
├──i=0── [1] <── backtrack(1,[1]) ──> For loop call 1st
│        │
│        ├──i=1── [1,2] <── backtrack(2,[1,2]) ──> For loop call 2nd
pop()    │        │
│        pop()    ├──i=2── [1,2,3] <── backtrack(3,[1,2,3]) ──> For loop call 3rd
│        │        │        └── (Returns)
│        │        └── (Returns)
│        │
│        ├──i=2── [1,3] <── backtrack(3,[1,3]) ──> For loop call 2nd
│        │        └── (Returns)
│        └── (Returns)
│
├──i=1── [2] <── backtrack(2,[2]) ──> For loop call 2nd
│        │
pop()    ├──i=2── [2,3] <── backtrack(2,[2,3]) ──> For loop call 3rd
│        │        └── (Returns)
│        └── (Returns)
│
└──i=2── [3] <── backtrack(3,[3]) ──> For loop call 3rd
         └── (Returns)

####################################################################################################
####################################################################################################

Time complexity:  O(n * 2^n)						2^n -> number of subsets(each element is either included or not)
													n   -> For each subset, copying takes O(n) in the worst case.

Space complexity: O(n * 2^n)						n   -> depth of recursion tree
													2^n -> 2^n subsets, with each can have n elements
'''
class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            # Add the current subset to result
            res.append(path[:])

            # Explore further elements
            for i in range(start, len(nums)): # range() acts as base case
                path.append(nums[i])          # Choose
                backtrack(i + 1, path)        # Explore
                path.pop()                    # Unchoose (backtrack)

        backtrack(0, [])
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1: From question
    nums = [1, 2, 3]
    result = solution.subsets(nums)
    print("Test 1 Input:", nums)
    print("Expected Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]")
    print("Your Output:", result)
    print()

    # Example 2: From question
    nums = [0]
    result = solution.subsets(nums)
    print("Test 2 Input:", nums)
    print("Expected Output: [[], [0]]")
    print("Your Output:", result)
    print()

    # Additional Edge Case 1: Smallest possible input
    nums = []
    result = solution.subsets(nums)
    print("Test 3 Input:", nums)
    print("Expected Output: [[]]")
    print("Your Output:", result)
    print()

    # Additional Edge Case 2: Two elements
    nums = [1, 2]
    result = solution.subsets(nums)
    print("Test 4 Input:", nums)
    print("Expected Output: [[], [1], [2], [1,2]]")
    print("Your Output:", result)
    print()

    # Additional Edge Case 3: Negative numbers
    nums = [-1, 2]
    result = solution.subsets(nums)
    print("Test 5 Input:", nums)
    print("Expected Output: [[], [-1], [2], [-1,2]]")
    print("Your Output:", result)
    print()

    # Additional Edge Case 4: Mix of negative and positive
    nums = [-1, 0, 1]
    result = solution.subsets(nums)
    print("Test 6 Input:", nums)
    print("Expected Output: [[], [-1], [0], [1], [-1,0], [-1,1], [0,1], [-1,0,1]]")
    print("Your Output:", result)
    print()