'''
Time Complexity:  O(n)              (for sliding window)

Space Complexity: O(k)              (for window set)
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # hold unique values in the current sliding window
        window = set()
        # Left boundary
        L = 0

        # Expand the window by moving the right boundary
        for R in range(len(nums)):
            # If window size exceeds k, shrink it from the left
            if R - L > k:
                # Remove element at index L from the set
                window.remove(nums[L])
                # Move the left boundary forward
                L += 1

            # If the current number is already in the window, we found a duplicate
            # within k distance (because window size has been maintained to at most k+1)
            if nums[R] in window:
                return True

            # Otherwise, add the current number to the window and continue
            window.add(nums[R])

        # If we finish scanning without finding any nearby duplicates, return False
        return False

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from the prompt
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),

        # Additional edge cases
        ([], 5, False),                             # empty array => no duplicates
        ([42], 0, False),                           # single element, k=0
        ([7, 7], 0, False),                         # duplicate but k=0 disallows pairing
        ([7, 7], 1, True),                          # duplicate at distance exactly 1
        ([1,2,3,4,5], 10, False),                   # no duplicates, large k
        ([5,5,5,5,5], 1, True),                     # all same, many valid pairs
        ([1,2,1,3,1], 2, True),                     # duplicate at i=0, j=2 (dist=2)
        ([1,2,1,3,1], 1, False),                    # same numbers but distances >1
        ([0, -1, -1, 0], 2, True),                  # negative values, valid window
    ]

    for nums, k, expected in test_cases:
        result = solution.containsNearbyDuplicate(nums, k)
        print(f"nums={nums}, k={k} -> {result} (expected: {expected})")