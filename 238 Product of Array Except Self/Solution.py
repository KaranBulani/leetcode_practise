class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left,right = [1],[1]
        for i in range(0,len(nums) - 1):
            left.append(left[-1] * nums[i])
            right.insert(0, right[0] * nums[len(nums) - 1 - i])

        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return  res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]  # Example input
    nums1 = [-1,1,0,-3,3]
    result = solution.productExceptSelf(nums1)
    print(result)