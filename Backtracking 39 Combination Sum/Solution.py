'''
####################################################################################################
########################################### Recursive DFS ##########################################
####################################################################################################
Just like : Backtracking 78 Subsets/Solution.py

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i: int, amount: int, curr: list[int]):
            if not amount:
                res.append(curr.copy())
                return
            if amount < 0 or i >= len(candidates):
                return

            curr.append(candidates[i])
            dfs(i, amount - candidates[i], curr)
            curr.pop()
            dfs(i + 1, amount, curr)

        dfs(0, target, [])
        return res

####################################################################################################
########################################### Iterative DFS ##########################################
####################################################################################################
Just like : Backtracking 78 Subsets/Solution.py

####################################################################################################

Time complexity:  O(2^(t/m))		 			where t is target, m is minimum value in nums
Space complexity: O(2^(t/m))		 			where t is target, m is minimum value in nums
'''


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort() #not needed as its written "You may return the combinations in any order."

        def backtrack(i: int, curr, amount):
            if not amount:
                res.append(curr.copy())
                return
            if amount < 0 or i >= len(candidates):
                return
            for i in range(i, len(candidates)): #acts as a base case
                curr.append(candidates[i])
                backtrack(i, curr, amount - candidates[i])
                curr.pop()

        backtrack(0, [], target)
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1: From question
    candidates = [2, 3, 6, 7]
    target = 7
    print(solution.combinationSum(candidates, target))  # Expected: [[2,2,3],[7]]

    # Example 2: From question
    candidates = [2, 3, 5]
    target = 8
    print(solution.combinationSum(candidates, target))  # Expected: [[2,2,2,2],[2,3,3],[3,5]]

    # Example 3: From question (no valid combination)
    candidates = [2]
    target = 1
    print(solution.combinationSum(candidates, target))  # Expected: []

    # Edge Case 1: Single element equal to target
    candidates = [4]
    target = 4
    print(solution.combinationSum(candidates, target))  # Expected: [[4]]

    # Edge Case 2: Multiple combinations possible with repeated use
    candidates = [2, 4, 6, 8]
    target = 8
    print(solution.combinationSum(candidates, target))  # Expected: multiple valid lists

    # Edge Case 3: Large target but small candidates
    candidates = [3, 5, 7]
    target = 30
    print(solution.combinationSum(candidates, target))  # Expected: multiple valid lists

    # Edge Case 4: Target smaller than all candidates
    candidates = [5, 6, 7]
    target = 3
    print(solution.combinationSum(candidates, target))  # Expected: []