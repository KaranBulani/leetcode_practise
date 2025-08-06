'''
Time Complexity:  O(logn)               (for Binary Search)
Space Complexity: O(1)                  (for Variables)
'''
# ---------------- simulating LeetCode's guess API for local testing ----------------
# this global will hold the current “picked” number for each test
_pick = None

def guess(num: int) -> int:
    """
    Simulates the LeetCode guess API:
      -1 : num > _pick
       1 : num < _pick
       0 : num == _pick
    """
    if num > _pick:
        return -1
    if num < _pick:
        return 1
    return 0
# ------------------------------------------------------------------------------------

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high  = 0, n
        while low <= high:
            pick = (high + low)//2
            if guess(pick) == -1:
                high = pick - 1
            elif guess(pick) == 1:
                low = pick + 1
            elif guess(pick) == 0:
                return pick

if __name__ == "__main__":
    solution = Solution()

    # format: (n, pick, expected)
    test_cases = [
        # prompt examples
        (10,                        6,          6),           # Example 1
        (1,                         1,          1),           # Example 2
        (2,                         1,          1),           # Example 3

        # additional small cases
        (2,                         2,          2),           # both versions bad after 2
        (3,                         2,          2),           # middle of 1..3

        # edge of constraint range
        (2**31 - 1,                 1,          1),           # pick is min
        (2**31 - 1, 2**31 - 1, 2**31 - 1),            # pick is max

        # some random-ish checks
        (100,                      57,         57),
        (1000,                     999,        999),
    ]

    for n, pick_val, expected in test_cases:
        # set the global for this run
        _pick = pick_val

        result = solution.guessNumber(n)
        print(f"n={n:11d}, pick={pick_val:11d} → result={result:11d}   (expected={expected})")
