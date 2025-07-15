'''
Time Complexity: O(n) (go through)
Space Complexity: O(1) for L, R
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        L, R = 1, 1
        while R < len(nums):
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L

if __name__ == "__main__":
    solution = Solution()

    tests = [
        # Provided examples
        {
            "input": [1, 1, 2],
            "expected_k": 2,
            "expected_nums": [1, 2]
        },
        {
            "input": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            "expected_k": 5,
            "expected_nums": [0, 1, 2, 3, 4]
        },
        # Edge: single element
        {
            "input": [42],
            "expected_k": 1,
            "expected_nums": [42]
        },
        # Edge: all elements the same
        {
            "input": [7, 7, 7, 7, 7],
            "expected_k": 1,
            "expected_nums": [7]
        },
        # Edge: already all unique
        {
            "input": [-2, -1, 0, 1, 2],
            "expected_k": 5,
            "expected_nums": [-2, -1, 0, 1, 2]
        },
        # Edge: negatives and positives mixed
        {
            "input": [-3, -3, -1, 0, 0, 2, 2, 2, 5],
            "expected_k": 5,
            "expected_nums": [-3, -1, 0, 2, 5]
        },
        # Edge: long run of duplicates then unique
        {
            "input": [1] * 100 + [2] * 50 + [3] * 25 + [4],
            "expected_k": 4,
            "expected_nums": [1, 2, 3, 4]
        }
    ]

    for i, tc in enumerate(tests):
        nums_copy = tc["input"]  # copy so we can inspect post-call
        k = solution.removeDuplicates(nums_copy)
        print(f"Test {i}:")
        print(f" Input: {tc['input']}")
        print(f" Returned k = {k!r}, first k elements = {nums_copy[:k]!r}")
        print(f" Expected k = {tc['expected_k']!r}, expected elems = {tc['expected_nums']!r}")
        print("-" * 40)
