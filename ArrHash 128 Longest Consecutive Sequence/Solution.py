'''

class UnionFind:
    def __init__(self, nums):
        self.parent = {}
        self.size = {}
        for n in nums:
            self.parent[n] = n
            self.size[n] = 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        # union by size
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = set(nums)  # remove duplicates
        uf = UnionFind(nums)

        for n in nums:
            if n + 1 in nums:
                uf.union(n, n + 1)

        return max(uf.size[uf.find(n)] for n in nums)

####################################################################################################
####################################################################################################

Time Complexity: O(n) as going through each nums
Space Complexity: O(n) because of the nums_set
'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set = set(nums)
        res = 0
        for num in nums:
            longest = 1
            if (num - 1) not in nums_set:#means it's the start
                while (num + longest) in nums_set:
                    longest += 1
                res = max(longest, res)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [100,4,200,1,3,2]
    nums1 = [0,3,7,2,5,8,4,6,0,1]
    result = solution.longestConsecutive(nums1)
    print(result)