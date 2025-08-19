'''
####################################################################################################
######################################### DP BRUTE FORCE ###########################################
####################################################################################################

Time Complexity:  O(nlogn) + O(n^2)              (sorting + for i,j loop)
                  O(n^2)

Space Complexity: O(n)                           (for dp array)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width and then by height in ascending order
        envelopes.sort(key=lambda x: (x[0], x[1]))

        n = len(envelopes)

        # DP: dp[i] is max envelopes ending at i
        dp = [1] * n # Each envelope alone is a valid sequence of length 1

        # Variable to keep track of the overall maximum result
        max_val = 1

        # Step 3: Nested loop to check all pairs (classic LIS approach in 2D)
        for i in range(n):
            for j in range(i):
                # Envelope i can fit after envelope j if both width and height are strictly greater
                if (envelopes[i][0] > envelopes[j][0] and
                    envelopes[i][1] > envelopes[j][1]):
                    # Update dp[i]: either keep current value or extend sequence ending at j
                    dp[i] = max(dp[i], dp[j] + 1)
            # Update global maximum after processing each i
            max_val = max(max_val, dp[i])
        return max_val

####################################################################################################
########################################## Binary Search ###########################################
####################################################################################################

Time Complexity:  O(nlogn) + O(n*logn)              (sorting + Binary Search N times)
                  O(nlogn)
Space Complexity: O(n)                              (for dp array)
'''

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        # Sort envelopes - width ascending, height descending

        # envelopes = [(5,4), (5,5)]; heights = [4, 5]
        # LIS on heights [4,5] = 2
        # ❌ But they cannot nest because widths are equal.

        # By sorting height descending when widths are equal, we get:
        # envelopes = [(5,5), (5,4)]; heights = [5, 4]
        # Now LIS correctly counts only one of them. ✅
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract heights (since widths are already sorted)
        # Problem reduces to finding Longest Increasing Subsequence (LIS) on heights
        heights = [h for _, h in envelopes]

        # current LIS (sequence of smallest possible tail values for each length)
        lis = []

        # Check LC 300, Step 3: Process each height and build LIS using binary search
        for h in heights:
            left, right = 0, len(lis) - 1
            pos = len(lis)  # default position is end (append)

            # Binary search: find first index in lis where lis[mid] >= h
            while left <= right:
                mid = (left + right) // 2
                if lis[mid] >= h:
                    pos = mid       # found a spot to replace
                    right = mid - 1
                else:
                    left = mid + 1

            # Step 4: Insert or replace
            # - If h is larger than all elements in lis, append it (extend LIS)
            # - Otherwise, replace the element at pos (keep lis optimized)
            if pos == len(lis):
                lis.append(h)
            else:
                lis[pos] = h

        # Step 5: Length of lis = maximum number of envelopes
        return len(lis)

if __name__ == "__main__":
    solution = Solution()

    # Example 0: My test case
    envelopes = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
    # Expected: 1
    print(solution.maxEnvelopes(envelopes))

    # Example 1: From question
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    # Expected: 3 ([2,3] => [5,4] => [6,7])
    print(solution.maxEnvelopes(envelopes))

    # Example 2: From question - identical envelopes
    envelopes = [[1, 1], [1, 1], [1, 1]]
    # Expected: 1
    print(solution.maxEnvelopes(envelopes))

    # Edge Case 1: Single envelope
    envelopes = [[10, 10]]
    # Expected: 1
    print(solution.maxEnvelopes(envelopes))

    # Edge Case 2: Increasing widths but decreasing heights
    envelopes = [[1, 10], [2, 9], [3, 8]]
    # Expected: 1 (cannot nest because height decreases)
    print(solution.maxEnvelopes(envelopes))

    # Edge Case 3: Perfect nesting chain
    envelopes = [[1, 1], [2, 2], [3, 3], [4, 4]]
    # Expected: 4
    print(solution.maxEnvelopes(envelopes))

    # Edge Case 4: Random order, some duplicates
    envelopes = [[5, 4], [5, 5], [6, 4], [6, 7], [2, 3], [2, 3]]
    # Expected: 3 ([2,3] => [5,4] => [6,7])
    print(solution.maxEnvelopes(envelopes))

    # Large input test (performance check)
    envelopes = [[i, i] for i in range(1, 1001)]
    # Expected: 1000 (strictly increasing sizes)
    print(solution.maxEnvelopes(envelopes))