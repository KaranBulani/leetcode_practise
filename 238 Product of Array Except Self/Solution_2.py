'''
Time Complexity: O(2n) for left and right
Space Complexity: O(2n) for space left, res
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]
        for i in range(0,len(nums) - 1):
            res.append(res[-1] * nums[i])

        right = 0
        #starting with len(nums) - 1 as its inclusive
        for i in range(len(nums) - 1, -1, -1):
            right = 1 if i == len(nums) - 1 else right * nums[i+1]
            res[i] = res[i] * right
        return  res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]  # Example input
    nums1 = [-1,1,0,-3,3]
    result = solution.productExceptSelf(nums1)
    print(result)