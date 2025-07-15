'''
Time Complexity: O(N^2)
Space Complexity: O(1)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i,n):
                current_sum += nums[j]
                if current_sum == k:
                    res += 1
        return res

Time Complexity: O(N^)
Space Complexity: O(N)
'''
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        totalSubarrays = 0
        currentPrefixSum = 0
        prefixSumFrequency = {0:1}
        for num in nums:
            currentPrefixSum += num
            requiredPrefixSum = currentPrefixSum - k
            if requiredPrefixSum in prefixSumFrequency:
                totalSubarrays += prefixSumFrequency.get(requiredPrefixSum)
            prefixSumFrequency[currentPrefixSum] = 1 + prefixSumFrequency.get(currentPrefixSum, 0)
        return totalSubarrays

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]#[1,1,1]
    k = 3#2
    result = solution.subarraySum(nums,k)
    print(result)