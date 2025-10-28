'''
####################################################################################################
######################################### Recursive DFS ############################################
####################################################################################################
Just like : Backtracking 90 Subsets ||/Solution.py

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def dfs(i: int, currPath: list[int], amount: int):
            if amount == 0:
                res.append(currPath.copy())
                return
            if amount < 0 or i >= len(candidates):
                return

            currPath.append(candidates[i])
            dfs(i + 1, currPath, amount - candidates[i])

            currPath.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, currPath, amount)

        dfs(0, [], target)
        return res

Time complexity:  O(2ⁿ) + O(n log n)

DFS explores every subset (include/exclude path), and sorting cost

Space complexity: O(n) + O(n) + O(k * n)
                  O(k * n)

Recursion stack depth — at most n.
currPath — also up to length n.
Result storage (res) - In the worst case, this can be O(k × n), where k = number of valid combinations.

####################################################################################################
########################################### Iterative DFS ##########################################
####################################################################################################
Just like : Backtracking 90 Subsets ||/Solution.py

Time complexity:  O(2ⁿ) + O(n log n)

DFS explores every subset (include/exclude path), and sorting cost

Space complexity: O(n) + O(n) + O(k * n)
                  O(k * n)

Recursion stack depth — at most n.
currPath — also up to length n.
Result storage (res) - In the worst case, this can be O(k × n), where k = number of valid combinations.

'''

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start: int, currPath: list[int], amount: int):
            if amount == 0:
                res.append(currPath.copy())
                return
            if amount < 0 or start >= len(candidates):
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                currPath.append(candidates[i])
                backtrack(i + 1, currPath, amount - candidates[i])
                currPath.pop()

        backtrack(0, [], target)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 0 from question
    candidates = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21,
                  29, 24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34,
                  18, 12]
    target = 27
    print("Test 0:", solution.combinationSum2(candidates, target))  # Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]

    # Example 1 from question
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print("Test 1:", solution.combinationSum2(candidates, target))  # Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]

    # Example 2 from question
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print("Test 2:", solution.combinationSum2(candidates, target))  # Expected: [[1,2,2],[5]]

    # Edge case: single element equal to target
    candidates = [3]
    target = 3
    print("Test 3:", solution.combinationSum2(candidates, target))  # Expected: [[3]]

    # Edge case: single element less than target
    candidates = [2]
    target = 3
    print("Test 4:", solution.combinationSum2(candidates, target))  # Expected: []

    # Edge case: all elements same, sum equals target
    candidates = [1, 1, 1, 1]
    target = 2
    print("Test 5:", solution.combinationSum2(candidates, target))  # Expected: [[1,1]]

    # Edge case: no combination possible
    candidates = [4, 5, 11]
    target = 3
    print("Test 6:", solution.combinationSum2(candidates, target))  # Expected: []

    # Edge case: larger input with duplicates
    candidates = [1, 1, 2, 5, 6, 7, 10]
    target = 8
    print("Test 7:", solution.combinationSum2(candidates, target))  # Expected: combinations summing to 8
