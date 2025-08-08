'''
Time Complexity:  O(Log(max(piles)))              (for Binary Search)
                  O(n)                            (for hours_needed Calculation)

                  O(n⋅log(max(piles)))

Space Complexity: O(1)                  (for Variables, indexes)
'''
import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        # Define a helper function to calculate total hours needed
        # if Koko eats at speed 'k' bananas per hour.
        def hours_needed(k: int) -> int:
            total_hours = 0
            for p in piles:
                # ceil division makes it upper
                total_hours += math.ceil(p/k)
            return total_hours

        # Set binary search boundaries:
        # Minimum speed is 1 (slowest she can eat)
        # Maximum speed is max(piles) (fastest needed, eating one whole pile per hour)
        low, high = 0, max(piles)
        res = high

        while low <= high:
            k = (high + low)//2
            if hours_needed(k) <= h:
                # If Koko can eat all bananas at speed 'k', try a slower speed
                res = min(res, k)
                high = k - 1
            else:
                # If she needs more than 'h' hours, increase speed
                low = k + 1
        return res

if __name__ == "__main__":
    solution = Solution()

    # Format: (piles, h, expected_k)
    test_cases = [
        # LeetCode examples
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),

        # Additional edge cases
        # Single pile, must eat it all in 1 hour
        ([1], 1, 1),
        ([10**9], 1, 10**9),

        # Many small piles but plenty of time => slowest speed = 1
        ([1,1,1,1,1], 10, 1),

        # Many small piles, limited time => need to eat more per hour
        ([1,1,1,1,1], 3, 2),

        # Large piles, h equals number of piles => can finish one pile per hour
        ([5,5,5,5], 4, 5),

        # Large piles, h less than piles => must split some hours over
        ([5,5,5,5], 6, 4),

        # Uniform large values
        ([100,100,100], 50, 6),

        # Mixed sizes, huge h => minimum speed 1
        ([7,2,5,10,8], 100, 1),
    ]

    for piles, h, expected in test_cases:
        result = solution.minEatingSpeed(piles, h)
        print(f"piles={piles}, h={h} → expected: {expected}, got: {result}")