'''
Time complexity:  O(n log n + n + q log n)
		n log n: Sorting
			  n: Prefix Sum
		q log n: Binary Search

Space complexity: O(n+m)						n for prefixSum, m for res
'''
class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)

        def binarySearch(val) -> int:
            L, R = 0, len(prefixSum) - 1
            index = 0
            while L <= R:
                mid = (L + R) // 2
                if prefixSum[mid] <= val:
                    index = mid
                    L = mid + 1
                else:
                    R = mid - 1
            return index

        res = []
        for q in queries:
            res.append(binarySearch(q))
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1 (from problem)
    nums = [4, 5, 2, 1]
    queries = [3, 10, 21]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?]

    # Example 2 (from problem)
    nums = [2, 3, 4, 5]
    queries = [1]
    print(solution.answerQueries(nums, queries))  # Expected: [?]

    # Edge Case 1: All numbers same
    nums = [5, 5, 5, 5]
    queries = [5, 10, 20]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?]

    # Edge Case 2: Very small nums and queries
    nums = [1]
    queries = [0, 1, 2]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?]

    # Edge Case 3: Increasing numbers
    nums = [1, 2, 3, 4, 5]
    queries = [5, 7, 15]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?]

    # Edge Case 4: Large query (greater than total sum)
    nums = [10, 20, 30]
    queries = [5, 60, 1000]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?]

    # Edge Case 5: Mixed random
    nums = [7, 2, 5, 10, 8]
    queries = [10, 15, 20, 25]
    print(solution.answerQueries(nums, queries))  # Expected: [?, ?, ?, ?]