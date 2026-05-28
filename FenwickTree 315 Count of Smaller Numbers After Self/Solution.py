'''
####################################################################################################
                                            Top-Down DP
####################################################################################################
'''
class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example cases
        {
            "nums": [5, 2, 6, 1],
            "expected": [2, 1, 1, 0]
        },
        {
            "nums": [-1],
            "expected": [0]
        },
        {
            "nums": [-1, -1],
            "expected": [0, 0]
        },

        # Edge cases
        {
            "nums": [1, 2, 3, 4, 5],  # strictly increasing
            "expected": [0, 0, 0, 0, 0]
        },
        {
            "nums": [5, 4, 3, 2, 1],  # strictly decreasing
            "expected": [4, 3, 2, 1, 0]
        },
        {
            "nums": [2, 2, 2, 2],  # all duplicates
            "expected": [0, 0, 0, 0]
        },
        {
            "nums": [1, 0, 2],  # small mixed
            "expected": [1, 0, 0]
        },
        {
            "nums": [3, 2, 2, 6, 1],
            "expected": [3, 1, 1, 1, 0]
        },
        {
            "nums": [10, 9, 8, 7],
            "expected": [3, 2, 1, 0]
        },
        {
            "nums": [1, 9, 7, 8, 5],
            "expected": [0, 3, 1, 1, 0]
        },
        {
            "nums": [-1, -2, -3, -4],
            "expected": [3, 2, 1, 0]
        },
        {
            "nums": [-4, -3, -2, -1],
            "expected": [0, 0, 0, 0]
        },
        {
            "nums": [0, 0, -1, 0],
            "expected": [1, 1, 0, 0]
        },
        {
            "nums": [10000, -10000],
            "expected": [1, 0]
        },
        {
            "nums": [4, 1, 2, 3],
            "expected": [3, 0, 0, 0]
        },
        {
            "nums": [7],
            "expected": [0]
        }
    ]

    for idx, test in enumerate(test_cases, 1):
        nums = test["nums"]
        expected = test["expected"]

        result = solution.countSmaller(nums)

        print(f"Test Case {idx}")
        print(f"Input     : {nums}")
        print(f"Expected  : {expected}")
        print(f"Your Output: {result}")
        print(f"Passed    : {result == expected}")
        print("-" * 50)