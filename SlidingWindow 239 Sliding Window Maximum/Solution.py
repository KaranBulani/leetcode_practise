'''
Time Complexity:  O(2n)              (for sliding window & deque popping)
Space Complexity: O(n)              (for deque)
'''
import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        L = 0
        Q = collections.deque() # Store indices, not value to handle duplicate values
        res = []

        for R in range(len(nums)):

            # Remove indices from the back Q[-1] ≤ nums[R], kept "=" as can delete older duplicate entry
            # they're no longer useful as they can't be max in current or future windows.
            while Q and nums[ Q[-1] ] <= nums[ R ]:
                Q.pop()
            Q.append(R) # Add index R to the back of the deque.

            # Front index of the deque is outside the current window
            if L > Q[0]:
                Q.popleft()

            # If Processed at least k elements, stand appending res[] and moving L
            if R >= k - 1:
                res.append(nums[Q[0]])
                L += 1

        return res

if __name__ == "__main__":
    sol = Solution()

    tests = [
        # From prompt
        {"nums": [1, 3, -1, -3, 5, 3, 6, 7], "k": 3, "expected": [3, 3, 5, 5, 6, 7]},
        {"nums": [1],               "k": 1, "expected": [1]},

        # Additional edge cases
        {"nums": [5, 5, 5, 5],       "k": 2, "expected": [5, 5, 5]},      # all equal
        {"nums": [1, 2, 3, 4, 5],    "k": 5, "expected": [5]},           # k == n
        {"nums": [5, 4, 3, 2, 1],    "k": 3, "expected": [5, 4, 3]},      # strictly decreasing
        {"nums": [1, -1, 1, -1, 1],  "k": 2, "expected": [1, 1, 1, 1]},   # alternating signs
        {"nums": [2, 1, 2, 3, 4],    "k": 1, "expected": [2, 1, 2, 3, 4]},# k = 1 (just the elements themselves)
        {"nums": [1, 3, 1, 2, 0, 5], "k": 4, "expected": [3, 3, 2]},      # mix of ups and downs
        {"nums": [0, 0, 0],          "k": 3, "expected": [0]},           # all zeros
        {"nums": [-5, -2, -3, -4],   "k": 2, "expected": [-2, -2, -3]},  # all negative
    ]

    for i, tc in enumerate(tests, 1):
        nums, k, expected = tc["nums"], tc["k"], tc["expected"]
        result = sol.maxSlidingWindow(nums, k)
        print(f"Test #{i}: nums={nums}, k={k}")
        print(f"  → result:   {result}")
        print(f"  → expected: {expected}")
        print(f"  → {'PASS' if result == expected else 'FAIL'}\n")