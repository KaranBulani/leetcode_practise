'''
Time Complexity: O(N)
Space Complexity: O(1)
XOR '^=' returns 1 for differing bits and 0 for identical ones, so identical numbers cancel out (1^1 = 0), leaving the unique number when all pairs are XOR-ed.
'''
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,1]#[1]#[4,1,2,1,2]
    result = solution.singleNumber(nums)
    print(result)