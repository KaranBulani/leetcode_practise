'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count, windowSum = 0, 0
        L = 0
        for R in range(len(arr)):
            windowSum += arr[R] # Add the new element to the current window's sum

            # If the window size is less than k, continue expanding
            if R - L < k - 1:
                continue

            # At this point, the window has exactly k elements
            # Compute the average and compare with threshold
            if windowSum/ k >= threshold:
                count += 1

            # Slide the window forward:
            windowSum -= arr[L]
            L += 1
        return count
'''

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        # Calculate the minimum required sum for a window to meet the threshold
        required_sum = threshold * k

        # Initialize the first window sum, k exclusive
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= required_sum else 0

        # Slide the window: subtract the element going out, add the new element, k inclusive
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= required_sum:
                count += 1
        return count

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # LeetCode examples
        ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3),          # Example 1: output 3
        ([11,13,17,23,29,31,7,5,2,3], 3, 5, 6),        # Example 2: output 6

        # Smallest possible array
        ([5], 1, 5, 1),                               # one subarray [5], avg=5 >=5 → 1
        ([5], 1, 6, 0),                               # one subarray [5], avg=5 <6 → 0

        # k equals array length
        ([1,2,3,4,5], 5, 3, 1),                       # only [1,2,3,4,5], avg=3 → 1
        ([1,2,3,4,5], 5, 4, 0),                       # avg=3 <4 → 0

        # threshold zero (always true since arr[i] ≥ 1)
        ([1,1,1,1], 2, 0, 3),                         # windows: [1,1]×3 → all 3 true

        # all elements the same
        ([7,7,7,7], 3, 7, 2),                         # [7,7,7] twice → 2
        ([7,7,7,7], 3, 8, 0),                         # avg=7 <8 → 0

        # mixed values
        ([4,1,6,5,2,8,3], 4, 5, 2),                   # subarrays ≥5: [4,1,6,5]=4, [1,6,5,2]=3.5, [6,5,2,8]=5.25, [5,2,8,3]=4.5 → 1

        # large values but small array
        ([10000,10000,10000], 2, 10000, 2),           # two windows, both avg=10000 → 2
    ]

    for arr, k, threshold, expected in test_cases:
        result = solution.numOfSubarrays(arr, k, threshold)
        print(f"arr={arr}, k={k}, threshold={threshold} → result: {result} (expected: {expected})")