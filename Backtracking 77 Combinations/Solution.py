'''
####################################################################################################
####################################################################################################

						Example: n = 4, k = 2
						C(n,k) = n!/k!(n-k)!
							   = 4!/2!(4-2)!
							   = 6 output states

####################################################################################################
                             combine(1, [])
                                 |
      -------------------------------------------------
      |                     |                    |                     |
   pick 1                pick 2              pick 3                pick 4
      |                     |                    |                     |
 backtrack(2,[1])      backtrack(3,[2])     backtrack(4,[3])       backtrack(5,[4])
      |                     |                    |                     |
   i=2→[1,2]✔️           i=3→[2,3]✔️         i=4→[3,4]✔️           — (no next)
   i=3→[1,3]✔️           i=4→[2,4]✔️
   i=4→[1,4]✔️

####################################################################################################

										[]
					/			  /            \              \
                   /             |              |              \
               [1]              [2]            [3]             [4]
           /    |    \        /    \            |               ×
       [1,2] [1,3] [1,4]   [2,3] [2,4]        [3,4]

####################################################################################################

Time complexity:  O(k * C(n,k))											visits each valid combination once C(n,k)
																		and does O(k) work to build/copy it

Space complexity: O(k) + O(k * C(n,k))									Recursion Depth O(k)
																		output list stores C(n,k) combinations, each of length k
'''
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        totalCombination, currCombination = [], []

        def backtrack(curr):
            # if combo has k numbers, push a copy to results
            if len(currCombination) == k:
                totalCombination.append(currCombination.copy())
            # Below return is same as Subset I (78), II (90)
            if i > n:
                return

            # iterate candidates from curr to n
            for i in range(curr, n + 1):
                currCombination.append(i)
                backtrack(i + 1)
                currCombination.pop()

        backtrack(1)
        return totalCombination


if __name__ == "__main__":
    solution = Solution()

    # Example 1: From question
    print("Test 1:")
    print(solution.combine(4, 2))  # Expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

    # Example 2: From question
    print("Test 2:")
    print(solution.combine(1, 1))  # Expected: [[1]]

    # Edge Case 1: Smallest possible n and k
    print("Test 3:")
    print(solution.combine(1, 1))  # Single combination

    # Edge Case 2: k = n (only one combination possible)
    print("Test 4:")
    print(solution.combine(5, 5))  # Only [1,2,3,4,5]

    # Edge Case 3: k = 1 (each element separately)
    print("Test 5:")
    print(solution.combine(4, 1))  # [[1],[2],[3],[4]]

    # Normal Case: n > k, moderate size
    print("Test 6:")
    print(solution.combine(5, 3))  # 5 choose 3 combinations

    # Edge Case 4: Larger n but small k
    print("Test 7:")
    print(solution.combine(6, 2))  # 6 choose 2 combinations

    # Edge Case 5: Large but valid input limit
    print("Test 8:")
    print(solution.combine(8, 4))  # Larger test within constraints
