'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        pass

if __name__ == "__main__":
    solution = Solution()

    # List of (input, expected_output) pairs
    test_cases = [
        # From prompt
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),

        # Edge/corner cases
        ([], 0),                # empty elevation map
        ([0], 0),               # single bar
        ([5], 0),               # single non-zero bar
        ([1,2,3,4], 0),         # strictly increasing
        ([4,3,2,1], 0),         # strictly decreasing
        ([2,0,2], 2),           # simple valley
        ([3,0,2,0,4], 7),       # multiple pits
        ([3,3,3,3], 0),         # all same height
        ([0,1,0,1,0,1,0], 2),   # repeated small valleys
    ]

    for heights, expected in test_cases:
        result = solution.trap(heights)
        print(f"heights = {heights!r}\n"
              f"  -> trapped water = {result}    "
              f"(expected: {expected})\n")
