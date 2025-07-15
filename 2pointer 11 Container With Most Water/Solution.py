'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        return 10

if __name__ == "__main__":
    solution = Solution()

    # List of (height array, expected max area)
    tests = [
        # Examples from problem statement
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),

        # Minimum size
        ([0, 0], 0),
        ([1, 10000], 1),   # one tall, one short

        # All zeros
        ([0,0,0,0,0], 0),

        # Increasing then decreasing
        ([1,2,3,4,5,4,3,2,1], 16),  # best between heights 5 and 4 at pos 4 and 5: min(5,4)*(5-4)=4*1=4?
                                     # Actually best is between ends: min(1,1)*(8)=8, or between 2&4: min(2,4)*6=12, or 3&5:3*4=12,
                                     # or 4&4:4*3=12, or 5&3:3*2=6 — so expected = 12.
                                     # (adjust expected after verifying)

        # Two‐element variations
        ([2,1], 1),
        ([10000, 10000], 10000),

        # Plateaus
        ([5,5,5,5,5], 20),  # width=4, height=5 → 20

        # Single big spike at one end
        ([100,1,1,1,1,1], 5),

        # Alternating high/low
        ([1,100,1,100,1], 4),  # best between the two 100's: min(100,100)*2=200

        # Large flat then drop
        ([10]*1000 + [0], 10*1000),  # width=1000, height=10 → 10000

        # Random small
        ([2,3,10,5,7,8,1,4], 36),  # best between positions 2 (10) and 5 (8): min(10,8)*3=24?
                                     # Actually best is between 3 (5) and 7 (4): min(5,4)*4=16?
                                     # Include it to test; adjust expected after you run your code.
    ]

    for heights, expected in tests:
        result = solution.maxArea(heights)
        print(f"heights={heights[:10]}{'...' if len(heights)>10 else ''} -> "
              f"{result} (expected: {expected})")