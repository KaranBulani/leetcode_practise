'''
Time complexity:  O(n log n + n + q log n)
		n log n: Sorting
			  n: Prefix Sum
		q log n: Binary Search

Space complexity: O(n+m)						n for prefixSum, m for res
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
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