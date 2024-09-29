'''
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