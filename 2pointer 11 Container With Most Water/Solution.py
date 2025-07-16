'''
Time Complexity:  O(n)       (for L,R)
Space Complexity: O(1)       (for L,R)
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        mostWater = float('-INF')
        L, R = 0, len(height) - 1
        while L < R:
            mostWater = max(mostWater,min(height[L], height[R]) * (R - L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return mostWater

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

        # Two‐element variations
        ([2,1], 1),
        ([10000, 10000], 10000),

        # Plateaus
        ([5,5,5,5,5], 20),  # width=4, height=5 → 20

        # Single big spike at one end
        ([100,1,1,1,1,1], 5),

        # Alternating high/low
        ([1,100,1,100,1], 200),  # best between the two 100's: min(100,100)*2=200
    ]

    for heights, expected in tests:
        result = solution.maxArea(heights)
        print(f"heights={heights[:10]}{'...' if len(heights)>10 else ''} -> "
              f"{result} (expected: {expected})")