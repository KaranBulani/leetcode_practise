'''
Time Complexity: O(N)
Space Complexity: O(1)

def majorityElement(self, nums: List[int]) -> int:
    count, res = 0, 0
    for num in nums:
        if count == 0:
            res = num
        if num == res:
            count += 1
        else:
            count -= 1
    return res

Time Complexity: O(N)
Space Complexity: O(N)
The key parameter lets you customize how Python decides what the "maximum" is by passing a function that returns a value to be used for comparison.
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        countDict = {}
        for n in nums:
            countDict[n] = 1 + countDict.get(n,0)
        return max(countDict, key=countDict.get)

if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,1,1,1,2,2]#[3,2,3]
    result = solution.majorityElement(nums)
    print(result)