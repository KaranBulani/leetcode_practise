'''
Time Complexity:  O(logn)               (for Binary Search)
Space Complexity: O(1)                  (for Variables, indexes)

Why return low works?
After the loop ends:
 * low is the smallest number such that isBadVersion(low) is True.
 * All values before it have already been checked and are False.

'''
# Mocking the LeetCode isBadVersion API for local testing
# We’ll drive it by setting a global `bad_version` before each test.
bad_version = None

def isBadVersion(version: int) -> bool:
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        mid = 0
        while low <= high:
            mid = (high + low)//2
            if isBadVersion(mid): #True
                high = mid - 1
            else: #False
                low = mid + 1
        return low

if __name__ == "__main__":
    solution = Solution()

    # List of test-cases: each is a tuple (n, bad, expected)
    tests = [
        # Provided examples
        (5, 4, 4),
        (1, 1, 1),

        # Edge cases
        (2, 1, 1),               # first is bad
        (2, 2, 2),               # only last is bad
        (10, 10, 10),            # bad starts at very end
        (10, 1, 1),              # bad starts at very beginning
        (2**31 - 1, 1, 1),       # max n, bad very first
        (2**31 - 1, 2**31 - 1, 2**31 - 1),  # max n, bad at end

        # Random mid-array checks
        (100, 37, 37),
        (1000, 500, 500),
    ]

    for n, bad, expected in tests:
        bad_version = bad
        result = solution.firstBadVersion(n)
        status = "✅" if result == expected else "❌"
        print(f"{status} n={n}, bad={bad} → got {result}, expected {expected}")