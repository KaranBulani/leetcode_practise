'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)

'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Your implementation goes here
        pass

if __name__ == "__main__":
    solution = Solution()

    # Provided examples from the problem
    cases = [
        # Example 1: mix of positives and negatives
        {
            "nums": [-1, 2, 1, -4],
            "target": 1,
            "expected": 2,  # -1 + 2 + 1 = 2
        },
        # Example 2: all zeros
        {
            "nums": [0, 0, 0],
            "target": 1,
            "expected": 0,  # 0 + 0 + 0 = 0
        },

        # Additional edge cases

        # 1. Minimum length array (3 elements)
        {
            "nums": [1, 1, 1],
            "target": 3,
            "expected": 3,  # only one possible sum
        },
        {
            "nums": [1, 2, 3],
            "target": 100,
            "expected": 6,  # sum of all elements is the largest possible
        },

        # 2. Negative target and negatives in array
        {
            "nums": [-5, -4, -3, -2, -1],
            "target": -10,
            "expected": -9,  # -3 + -4 + -2 = -9 is closest to -10
        },
        {
            "nums": [-1, 2, 1, -4],
            "target": -1,
            "expected": -1,  # -4 + 2 + 1 = -1
        },

        # 3. Mix of duplicates
        {
            "nums": [1, 1, -1, -1, 3],
            "target": 1,
            "expected": 1,  # 1 + 1 + -1 = 1
        },

        # 4. Large values
        {
            "nums": [1000, -1000, 2000, -2000, 0],
            "target": 500,
            "expected": 500,  # 2000 + -1000 + -500? Actually 1000 + 0 + -500? but best is 1000 + -2000 + 1500?
        },

        # 5. Already sorted vs unsorted input
        {
            "nums": [3, -2, 5, 1, -4],
            "target": 2,
            "expected": 2,  # multiple combos, but closest sum is 2
        },
    ]

    for i, case in enumerate(cases, 1):
        result = solution.threeSumClosest(case["nums"], case["target"])
        print(f"Test case {i}: result = {result}, expected = {case['expected']}")