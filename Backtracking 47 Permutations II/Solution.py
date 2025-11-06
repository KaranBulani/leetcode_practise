'''


   i=0                                  []
                             /          |           \
                            |      (this state      |
                            |      is repeated)     |
   i=1                     [1]         [1]         [2]
                        /     \         | \         | \
                       /      |        /   \       /  (this state
                      /       |       |    |      |   is repeated)
   i=2             [1,1]   [1,2]   [1,1] [1,2]   [2,1] [2,1]
                    |        |        |     |       |     |
   i=3          [1,1,2]  [1,2,1]  [1,1,2] [1,2,1] [2,1,1] [2,1,1]

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sorting helps handle duplicates
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                # In 46 Permutations - we remove an element. But if we remove? How will i know upcoming element is a dup
                # In 39 Combination Sum - At each iteration We increment i to i+1 and no prev index can be accessed.
                # Then at i+1 How will I know i & i+1 were dup ?

                # Hence kept this
                # skip used elements
                if used[i]:
                    continue

                # skip duplicates: if current num == previous num and previous wasn't used
                # Don’t start with the second identical number until the first identical number has already been used in this path.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                dfs(path + [nums[i]])
                used[i] = False

        dfs([])
        return res

Time complexity:  O(n * n!)						 		n: For copy, n!: For permutations (but fewer due to duplicates)
Space complexity: O(n * n!)		 	                    n: For recursive depth, used, n!: for output (but fewer due to duplicates)

####################################################################################################
######################################## HASH MAP SOLUTION #########################################
####################################################################################################

nums = [1,1,2]
                        nums = [1:2, 2:1]
   i=0                               []
                             /               \
   i=1                     [1]                 [2]
                        /        \                 \
   i=2             [1,1]        [1,2]             [2,1]
                   /                 \                 \
   i=3       [1,1,2]           [1,2,1]           [2,1,1]

All Unique
Time complexity:  O(n * n!)						 		n: For copy, n!: For permutations
Space complexity: O(n * n!)		 	                    n: For recursive depth, n!: For output

All Same
Time complexity:  O(n)						 		    n: For copy, 1: For permutations as all same numbers
Space complexity: O(n + n)		 	                    n: For recursive depth, n: For only n len output possible

'''
from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        numsCounter = Counter(nums)
        res = []

        def dfs(curr: list[int]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in numsCounter:
                if numsCounter[i] > 0:
                    curr.append(i)
                    numsCounter[i] -= 1

                    dfs(curr)

                    curr.pop()
                    numsCounter[i] += 1

        dfs([])
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1: From the question
    nums1 = [1, 1, 2]
    print("Test Case 1 Input:", nums1)
    result1 = solution.permuteUnique(nums1)
    print("Test Case 1 Output:", result1)
    print()

    # Example 2: From the question
    nums2 = [1, 2, 3]
    print("Test Case 2 Input:", nums2)
    result2 = solution.permuteUnique(nums2)
    print("Test Case 2 Output:", result2)
    print()

    # Edge Case 1: Single element
    nums3 = [1]
    print("Test Case 3 Input:", nums3)
    result3 = solution.permuteUnique(nums3)
    print("Test Case 3 Output:", result3)
    print()

    # Edge Case 2: All elements same
    nums4 = [2, 2, 2]
    print("Test Case 4 Input:", nums4)
    result4 = solution.permuteUnique(nums4)
    print("Test Case 4 Output:", result4)
    print()

    # Edge Case 3: Mix of negatives and positives
    nums5 = [-1, 1, 1]
    print("Test Case 5 Input:", nums5)
    result5 = solution.permuteUnique(nums5)
    print("Test Case 5 Output:", result5)
    print()

    # Edge Case 4: Larger input with duplicates
    nums6 = [1, 1, 2, 2]
    print("Test Case 6 Input:", nums6)
    result6 = solution.permuteUnique(nums6)
    print("Test Case 6 Output:", result6)
    print()

    # Edge Case 5: 8 elements (max constraint test)
    nums7 = [1, 1, 2, 2, 3, 3, 4, 4]
    print("Test Case 7 Input:", nums7)
    result7 = solution.permuteUnique(nums7)
    print("Test Case 7 Output Length:", len(result7))  # print length only to avoid clutter
    print()