'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = (nums2, nums1) if len(nums1) > len(nums2) else (nums1, nums2)
        total = len(nums1) + len(nums2) #not 0 indexed twice
        half = total // 2 #not 0 indexed once

        # binary search on smaller array
        L, R = 0, len(A) - 1 #0 indexed
        while True: #True as Median is guranteed
            Amid = (L + R) // 2 #0 indexed
            Bmid = half - (Amid + 1) - 1
            # Amid is 0 indexed hence + 1 to subtract from half, - 1 again to 0 index Bmid

            Aleft = A[Amid] if Amid >= 0 else float("-inf")
            Aright = A[Amid + 1] if (Amid + 1) < len(A) else float("inf")
            Bleft = B[Bmid] if Bmid >= 0 else float("-inf")
            Bright = B[Bmid + 1] if (Bmid + 1) < len(B) else float("inf")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                #get less records from A
                R = Amid - 1
            else:
                #get more records from A
                L = Amid + 1

if __name__ == "__main__":
    solution = Solution()

    # Test cases: (nums1, nums2, expected)
    tests = [
        # From question
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),

        # Edge: one empty array
        ([], [1], 1.0),
        ([2], [], 2.0),

        # Edge: both arrays length 1
        ([0], [0], 0.0),
        ([-1], [1], 0.0),

        # Uneven lengths
        ([1, 3], [2, 4, 5], 3.0),
        ([1, 2, 3, 4], [5, 6, 7], 4.0),

        # Negative numbers
        ([-5, -3, -1], [-2, 0, 2], -1.5),
        ([-3, -2, -1], [1, 2, 3], 0.0),

        # Large arrays small numbers
        ([1, 1, 1, 1], [1, 1, 1, 1], 1.0),

        # Odd total length
        ([1, 2, 5], [3, 4], 3.0),

        # All negative
        ([-7, -6, -5], [-4, -3, -2, -1], -4.0),
    ]

    for i, (nums1, nums2, expected) in enumerate(tests, 1):
        result = solution.findMedianSortedArrays(nums1, nums2)
        print(f"Test case {i}: got {result}, expected {expected}")