'''
Time : O(n)
Space : O(n)
'''
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visitedValueIndex = {}
        for i,num in enumerate(nums):
            difference = target - num
            if difference in visitedValueIndex:
                return [visitedValueIndex[difference],i]
            visitedValueIndex[num] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [3,3]#[3,2,4]#[2,7,11,15]  # Example input
    target = 6#6#9
    result = solution.twoSum(nums, target)
    print(result)