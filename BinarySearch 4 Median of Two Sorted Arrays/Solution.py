'''
Time Complexity:  O(log(len(A))              (for Binary Search)
Space Complexity: O(1)                       (for Variables, indexes)
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