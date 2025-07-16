'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        # Your implementation here
        pass

if __name__ == "__main__":
    solution = Solution()

    # Example cases from the prompt
    test_cases = [
        # Format: (input_list, expected_output)
        ([2, 2, 3, 4], 3),        # Explanation: combinations: (2,3,4) twice, (2,2,3)
        ([4, 2, 3, 4], 4),        # Two 4s with 2 and 3 in different positions

        # Additional edge cases
        ([], 0),                  # No sides at all
        ([1], 0),                 # Only one side
        ([1, 2], 0),              # Only two sides
        ([0, 0, 0], 0),           # Zero-length sides cannot form a triangle
        ([1, 1, 1], 1),           # Exactly one possible triangle
        ([2, 2, 2, 2], 4),        # All combinations of 3 out of 4 equal sides: C(4,3)=4
        ([1, 1, 2], 0),           # Degenerate: 1+1 == 2, not strictly greater
        ([3, 4, 5, 6], 4),        # Multiple valid triples in sorted order
        ([5, 1, 3, 4, 2], 3),     # Unsorted input; valid triples after sorting [1,2,3,4,5]
        ([1000, 1000, 1000], 1),  # Large equal sides
    ]

    for nums, expected in test_cases:
        result = solution.triangleNumber(nums)
        print(f"nums = {nums!r} -> {result}  (expected: {expected})")
