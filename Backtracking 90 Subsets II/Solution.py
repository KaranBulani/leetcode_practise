'''
####################################################################################################
####################################################################################################

                            AT EACH i = 0,1,2,3 I AM TAKING DECISION TO TAKE nums[i] OR NOT
												nums = [1, 2, 2, 3]

   i=0                                                           []
                                            /                                           \
   i=1                                   [1]                                             []
                             /                       \                             /           \
   i=2                   [1,2]                       [1]                       [2]            	  []
                    /             \              /         \               /         \          /     \
   i=3         [1,2,2]          '1,2'         '1,2'        [1]          [2,2]        '2'      '2'	    []
              /      \         /     \       /    \      /    \      /      \       /  \     /   \     /  \
   i=4   [1,2,2,3] [1,2,2] '1,2,3' '1,2' '1,2,3' '1,2' [1,3]  [1] [2,2,3]  [2,2] '2,3' '2' '2,3' '2' [3]  []

We need to avoid things in '' as those are repeated work. Below code does it but not optimally.

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res, currPath = [], []
        nums.sort()

        def backtracking(level):
            if level >= len(nums) and currPath not in res:
                res.append(currPath.copy())
                return
            elif level >= len(nums):
                return

            currPath.append(nums[level])
            backtracking(level + 1)

            currPath.pop()
            backtracking(level + 1)

        backtracking(0)
        return res

####################################################################################################
####################################################################################################

												nums = [1, 2, 2, 3]

   i=0                                                           []
                                            /                                               \
   i=1                                   [1]                                                  []
                             /                       \                             /                    \
   i=2                   [1,2]                       [1]                       [2]            	           []
                    /             \              /         \\                /          \            /          \\
                   |               |       Skipped Over     inc i           |           |     Skipped Over     inc i
   i=3         [1,2,2]          '1,2'         '1,2'          ||           [2,2]        '2'        '2'	        ||
              /      \         /     \       /    \        //  \\      /      \       /  \       /   \        //  \\
   i=4   [1,2,2,3] [1,2,2] '1,2,3' '1,2' '1,2,3' '1,2'   [1,3] [1]  [2,2,3] [2,2]  '2,3' '2'   '2,3' '2'     [3]   []

####################################################################################################
####################################################################################################

												nums = [1, 2, 2, 2]

   i=0                                                           []
                                            /                                                   \
   i=1                                   [1]                                                     []
                             /                      \\                             /                           \\
   i=2                   [1,2]                      inc i                       [2]               	           inc i
                    /            \\              /         \\                /          \\                 /             \\
                   |              ||        Skipped Over    \\              |            ||            Skipped Over       \\
   i=3         [1,2,2]           inc i         '1,2'         inc i         [2,2]        inc i              '2'	          inc i
              /      \          /    \\       /    \        /    \\      /      \       /     \\         /    \        //       \\
			 |        |     Skipped  ||      |      |    Skipped  ||    |        |    Skipped  ||       |      |    Skipped      ||
			 ↓        ↓	       |     ↓↓      |      |	   |      ↓↓    ↓        ↓	   |       ↓↓       |      |	   |         ↓↓
   i=4   [1,2,2,2] '1,2,2'  '1,2,2' '1,2' '1,2,2' '1,2'   '1,2'   [1]  [2,2,2] '2,2'  '2,2'    '2'    '2,2'   '2'     '2'        []

####################################################################################################
####################################################################################################

Time complexity:  O(n * 2^n)						2^n -> number of subsets(each element is either included or not)
													n   -> For each subset, copying takes O(n) in the worst case.

Space complexity: O(n * 2^n)						n   -> depth of recursion tree
													2^n -> 2^n subsets, with each can have n elements
'''

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res, currPath = [], []
        nums.sort()  # sort to bring duplicates together

        def backtracking(level):
            if level >= len(nums):
                res.append(currPath.copy())
                return

            # Include nums[level]
            currPath.append(nums[level])
            backtracking(level + 1)

            currPath.pop()
            # Skip duplicates for current nums[level] when excluding
            while (level + 1) < len(nums) and nums[level] == nums[level + 1]:
                level += 1
            backtracking(level + 1)

        backtracking(0)
        return res
'''
nums = [1,2,2,3]

                                                                                      []
                        ┌───────────────────────────────────────────┬──────────────────┴───────┬─────────────────────────┬───────────────┐
                        │                                           │                          │                         │               │
                                                                                        2nd 2 → SKIPPED ❌
for i in range         0,4                                         1,4                        2,4                       3,4             4,4
                       [1]                                         [2]                        [2]                       [3]            (done)
            ┌───────────┴──────┐──────────────┐           ┌─────────┴──────┐           ┌───────┴─────────┐               │
            │                  │              │           │                │           │                 │               │
                     2nd 2 → SKIPPED ❌             i > start cond
for i in   1,4                2,4            3,4         2,4              3,4         3,4               4,4             4,4
range     [1,2]              [1,2]          [1,3]       [2,2]            [2,3]       [2,3]             (end)           (end)
            │                  │              │           │                │
            ┌─────────┐        │              │           │                │
        i > start     │        │              │           │                │
for i in   2,4      3,4       3,4            4,4         3,4              4,4
range    [1,2,2]  [1,2,3]   [1,2,3]         (end)       [2,2,3]          (end)
            │         │        │
            │         │        │
for i in   3,4      4,4      4,4
range    [1,2,2,3] (end)    (end)
            │
           4,4
          (end)

[] <── backtrack(0, []) ──> Initial Call
│
├── i=0 ── [1] <── backtrack(1, [1]) ──> For loop call 1st
│          │
│          ├── i=1 ── [1,2] <── backtrack(2, [1,2]) ──> For loop call 2nd
│          │           │
│          │           ├── i=2 ── [1,2,2] <── backtrack(3, [1,2,2]) ──> skip duplicate handled after return
│          │           │            │
│          │           │            ├── i=3 ── [1,2,2,3] <── backtrack(4, [1,2,2,3])
│          │           │            │            └── (Returns)
│          │           │            └── (Returns)
│          │           │
│          │           ├── i=3 ── [1,2,3] <── backtrack(4, [1,2,3])
│          │           │            └── (Returns)
│          │           └── (Returns)
│          │
│          ├── i=2 (skip duplicate 2)  ←── skip this because nums[2] == nums[1]
│          │
│          ├── i=3 ── [1,3] <── backtrack(4, [1,3])
│          │            └── (Returns)
│          └── (Returns)
│
├── i=1 ── [2] <── backtrack(2, [2]) ──> For loop call 2nd
│          │
│          ├── i=2 ── [2,2] <── backtrack(3, [2,2])
│          │           │
│          │           ├── i=3 ── [2,2,3] <── backtrack(4, [2,2,3])
│          │           │            └── (Returns)
│          │           └── (Returns)
│          │
│          ├── i=3 ── [2,3] <── backtrack(4, [2,3])
│          │           └── (Returns)
│          └── (Returns)
│
├── i=2 (skip duplicate 2)  ←── skip because nums[2] == nums[1]
│
└── i=3 ── [3] <── backtrack(4, [3])
             └── (Returns)


'''

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: sort to handle duplicates

        def backtrack(start, path):
            res.append(path[:])  # add a copy of the current subset

            for i in range(start, len(nums)):
                # Step 2: skip duplicates on the same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 2]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [1], [2], [1,2], [2,2], [1,2,2]]

    print("-" * 60)

    # Example 2
    nums = [0]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [0]]

    print("-" * 60)

    # Edge Case 1: All elements same
    nums = [2, 2, 2]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [2], [2,2], [2,2,2]]

    print("-" * 60)

    # Edge Case 2: Negative numbers with duplicates
    nums = [-1, -1, 2]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [-1], [-1,-1], [2], [-1,2], [-1,-1,2]]

    print("-" * 60)

    # Edge Case 3: Mixed positives, negatives, and duplicates
    nums = [1, -1, 1]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [1], [1,1], [-1], [-1,1], [-1,1,1]]

    print("-" * 60)

    # Edge Case 4: Larger variety, no duplicates
    nums = [1, 2, 3]
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

    print("-" * 60)

    # Edge Case 5: Empty input (not in constraints but good test)
    nums = []
    result = solution.subsetsWithDup(nums)
    print("Input:", nums)
    print("Output:", result)
    # Expected: [[]]