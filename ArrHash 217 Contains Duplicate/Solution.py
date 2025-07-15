'''
O(n) space and time
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_values = set()
        for num in nums:
            if num in num_values:
                return True
            num_values.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,3,3,4,3,2,4,2]  # Example input
    result = solution.containsDuplicate(nums)
    print(result)