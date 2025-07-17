'''
############################################################################################

Time Complexity:  O(n)       (For MaxR, MaxL)
                + O(n)       (For Total)
                : O(2n) or O(n)

Space Complexity: O(2n)       (For MaxR, MaxL)
                + O(1)       (For Total)
                : O(2n) or O(n)
class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        if n <= 2:
            return 0

        # Arrays to store the maximum height to the left/right of each index
        left_max = [0] * n
        right_max = [0] * n

        # Build left_max and right_max in a single pass
        for i in range(n):
            # From the left
            if i == 0:
                left_max[i] = height[i]
            else:
                left_max[i] = max(left_max[i - 1], height[i])

            # From the right
            j = n - 1 - i
            if i == 0:
                right_max[j] = height[j]
            else:
                right_max[j] = max(right_max[j + 1], height[j])

        # Calculate trapped water at each position
        total_water = 0
        for i, h in enumerate(height):
            # Water level is limited by the shorter side
            water = min(left_max[i], right_max[i]) - h
            if water > 0:
                total_water += water

        return total_water
############################################################################################

Time Complexity:  O(n)       (For R, L)

Space Complexity: O(1)       (For R,L,Result)
'''

class Solution:
    def trap(self, height: list[int]) -> int:
        # If there are fewer than 3 bars, no water can be trapped
        if len(height) <= 2:
            return 0

        # Initialize two pointers at the ends of the array
        L, R = 0, len(height) - 1
        # Track the maximum height seen so far from the left and right
        maxL, maxR = height[L], height[R]
        # Accumulate the total trapped water volume
        totalVolume = 0

        # Process the elevation map until the two pointers meet
        while L < R:
            # Always move the side with the lower current max height inward
            if maxL > maxR:
                # Move the right pointer leftward
                R -= 1
                # Update the maximum seen on the right
                maxR = max(maxR, height[R])
                # Water trapped at R is the difference between maxR and current height
                # This is non-negative since maxR >= height[R]
                totalVolume += (maxR - height[R])
            else:
                # Move the left pointer rightward
                L += 1
                # Update the maximum seen on the left
                maxL = max(maxL, height[L])
                # Water trapped at L is the difference between maxL and current height
                totalVolume += (maxL - height[L])

        # Return the total accumulated water
        return totalVolume

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
