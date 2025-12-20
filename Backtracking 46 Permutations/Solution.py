'''
####################################################################################################
########################################### Recursive DFS ##########################################
####################################################################################################

                                 dfs(curr, remaining, i)
                                    dfs([], [1,2], 0)
                                            |
                        +-------------------+-----------------------+
                        |                                           |
                   Take i=0 (1)                                Skip i++ (i=1)
                 dfs([1], [2], 0)                             dfs([], [1,2], 1)
                        |                                           |
            +-----------+------------+                  +-----------+-----------+
            |                        |                  |                       |
       Take i=0 (2)             Skip i++ (i=1)     Take i=1 (2)            Skip i++ (i=2)
     dfs([1,2], [], 0)           i>=len(REM)     dfs([2], [1], 0)           i>=len(REM)
            |                       STOP                  |                    STOP
      +-----+-----+                              +--------+--------+
      |           |                              |                 |
  ✓ [1,2]   Skip i++ (i=1)                  Take i=0 (1)      Skip i++ (i=1)
  NOT REM    i>=len(REM)                  dfs([2,1], [], 0)    i>=len(REM)
   STOP         STOP                             |                STOP
                                           +-----+-----+
                                           |           |
                                       ✓ [2,1]   Skip i++ (i=1)
                                        NOT REM    i>=len(REM)
                                         STOP         STOP
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(curr: list[int], remaining: list[int], i: int):
            # base case: permutation complete
            if not remaining:
                res.append(curr)
                return

            # if index crosses remaining length, stop
            if i >= len(remaining):
                return

            # choice 1: take current element & remove from remaining
            dfs(curr + [remaining[i]], remaining[:i] + remaining[i+1:], 0)
            # choice 2: skip to next index (simulate for loop)
            dfs(curr, remaining, i+1)

        dfs([], nums, 0)
        return res

Time complexity:  O(n * n!)		 		    n: For copy, n!: For permutations
Space complexity: O(n * n!)		 			n: For recursive depth, n!: For output

####################################################################################################
##################################### Recursive + Iterative DFS ####################################
####################################################################################################

                        backtrack([], [1,2])
                                |
                +---------------+---------------+
                |                               |
             i=0 (1)                         i=1 (2)
         backtrack([1], [2])            backtrack([2], [1])
                |                               |
             i=0 (2)                         i=0 (1)
         backtrack([1,2], [])           backtrack([2,1], [])
                |                               |
            ✓ [1,2]                          ✓ [2,1]
             NOT REM                          NOT REM

####################################################################################################

                                            backtrack([], [1,2,3])
                                                    |
                        +---------------------------+---------------------------+
                        |                           |                           |
                     i=0 (1)                     i=1 (2)                     i=2 (3)
               backtrack([1],[2,3])        backtrack([2],[1,3])        backtrack([3],[1,2])
                        |                           |                           |
            +-----------+-----------+               |               +-----------+-----------+
            |                       |               |               |                       |
         i=0 (2)                 i=1 (3)            |            i=0 (1)                 i=1 (2)
   backtrack([1,2],[3])    backtrack([1,3],[2])     |      backtrack([3,1],[2])    backtrack([3,2],[1])
            |                       |               |               |                       |
            |                       |               |               |                       |
         i=0 (3)                 i=0 (2)            |            i=0 (2)                 i=0 (1)
  backtrack([1,2,3],[])    backtrack([1,3,2],[])    |      backtrack([3,1,2],[])   backtrack([3,2,1],[])
            |                       |               |               |                       |
            |                       |               |               |                       |
        ✓ [1,2,3]               ✓ [1,3,2]           |           ✓ [3,1,2]              ✓ [3,2,1]
          NOT REM                NOT REM            |            NOT REM                NOT REM
                                                    |
                                        +-----------+-----------+
                                        |                       |
                                     i=0 (1)                 i=1 (3)
                              backtrack([2,1],[3])      backtrack([2,3],[1])
                                        |                       |
                                        |                       |
                                     i=0 (3)                 i=0 (1)
                              backtrack([2,1,3],[])     backtrack([2,3,1],[])
                                        |                       |
                                        |                       |
                                    ✓ [2,1,3]               ✓ [2,3,1]
                                      NOT REM                NOT REM

Results: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr: List[int], remaining: List[int]):
            if not remaining:
                res.append(curr)
                return

            for i in range(len(remaining)):
                backtrack(curr + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return res

Time complexity:  O(n * n!)		 		    n: For copy, n!: For permutations
Space complexity: O(n * n!)		 			n: For recursive depth, n!: For output

####################################################################################################
############################################ Iterative #############################################
####################################################################################################

Start: [[]]
Add 3 → [[3]]
Add 2 → [[2,3], [3,2]]
Add 1 → [[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def iterate(i, nums):
            if i == len(nums):
                return [[]]

            resPerms = []
            perms = iterate(i + 1, nums)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms

        return iterate(0, nums)

####################################################################################################

Start: [[]]
Add 1 → [[1]]
Add 2 → [[2,1], [1,2]]
Add 3 → [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # start with an empty permutation

        for num in nums:
            new_res = []
            for perm in res:
                # insert current number in all possible positions
                for i in range(len(perm) + 1):
                    new_res.append(perm[:i] + [num] + perm[i:])
            res = new_res

        return res

Time: O(n × n!)
    n!
     * Number of permutations = nPr = n! / (n−r)!
       3P3 = 3!
       But n! counts how many complete permutations exist, NOT how much work is done to build them.
    n
     * To build each permutation:
       We need to make n recursive decisions.
    So it can be said that for each n! permutation we had to go through n steps, making it O(n * n!)

Space: O(n × n!)
    n x n!
     * Storing n! permutations.
     * Each permutation has n elements.
    n
     * Recursion Stack
'''

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def dfs(curr: list[int], remaining: list[int], i: int):
            # base case: permutation complete
            if not remaining:
                res.append(curr)
                return

            # if index crosses remaining length, stop
            if i >= len(remaining):
                return

            # choice 1: take current element & remove from remaining
            dfs(curr + [remaining[i]], remaining[:i] + remaining[i+1:], 0)
            # choice 2: skip to next index (simulate for loop)
            dfs(curr, remaining, i+1)

        dfs([], nums, 0)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 2
    nums = [0, 1]
    # Expected: [[0,1],[1,0]]
    print(solution.permute(nums))

    # Example 1
    nums = [1, 2, 3]
    # Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(solution.permute(nums))

    # Example 3
    nums = [1]
    # Expected: [[1]]
    print(solution.permute(nums))

    # Edge Case 1: Smallest possible array (single negative)
    nums = [-5]
    # Expected: [[-5]]
    print(solution.permute(nums))

    # Edge Case 2: Include negatives and zero
    nums = [-1, 0, 1]
    # Expected: All 6 permutations of [-1, 0, 1]
    print(solution.permute(nums))

    # Edge Case 3: Four distinct numbers
    nums = [1, 2, 3, 4]
    # Expected: 24 permutations (4!)
    print(solution.permute(nums))

    # Edge Case 4: Mixed positive and negative numbers
    nums = [10, -10, 0]
    # Expected: 6 permutations of [10, -10, 0]
    print(solution.permute(nums))
