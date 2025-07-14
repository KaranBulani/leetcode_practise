'''
Time Complexity: O(n/1) (go through)
Space Complexity: O(1) for L, R
'''
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L, R = 0, len(numbers) - 1
        #right will shift leftwards to reduce total
        #left will shift rightwards to increase total
        #will work as asc order, exactly 1 soln
        while L < R:
            curSum = numbers[L] + numbers[R]
            if curSum == target:
                return [L + 1,R + 1]
            elif curSum >= target:
                R -= 1
            elif curSum <= target:
                L += 1

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # LeetCode examples
        ([2, 7, 11, 15], 9, [1, 2]),  # 2 + 7 = 9
        ([2, 3, 4], 6, [1, 3]),  # 2 + 4 = 6
        ([-1, 0], -1, [1, 2]),  # -1 + 0 = -1

        # Additional edge cases
        ([1, 2], 3, [1, 2]),  # smallest length
        ([1, 1, 2, 3], 2, [1, 2]),  # duplicates at start
        ([-1000, 0, 1000], 0, [1, 3]),  # extreme values summing to zero
    ]

    for nums, target, expected in test_cases:
        result = solution.twoSum(nums, target)
        print(f"nums={nums}, target={target} -> result={result}, expected={expected}")
