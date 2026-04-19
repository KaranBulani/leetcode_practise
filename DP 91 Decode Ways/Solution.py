'''
####################################################################################################
                                    TOP DOWN BRUTE FORCE + DP
####################################################################################################
                                            BRUTE FORCE
####################################################################################################
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        n = len(s)

        def dfs(start: int) -> None:
            nonlocal res

            # base case
            if start == n:
                res += 1
                return

            # invalid case
            if s[start] == "0":
                return

            # ✅ take 1 digit (always valid if not '0')
            dfs(start + 1)

            # ✅ take 2 digits (only if valid)
            if start + 1 < n:
                # no need to build substring
                if (s[start] == "1") or (s[start] == "2" and s[start + 1] <= "6"):
                    dfs(start + 2)

        dfs(0)
        return res

Time: O(2^n)
Space: O(n)
####################################################################################################
                                                DP
####################################################################################################
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            # take 1 digit
            res = dfs(i + 1)

            # take 2 digits
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)

            memo[i] = res
            return res

        return dfs(0)

Time: O(n)
Space: O(n)
####################################################################################################
                                        BOTTOM UP - DP
####################################################################################################
1. Observation

We are given a string of digits. Each digit or pair of digits (1–26) maps to a letter.
We need to count how many valid ways we can decode the entire string.

Key observations
* Single digit:
  * Valid if '1' → '9'
  * Invalid if '0'
* Two digits:
  * Valid if "10" → "26"
  * Invalid if:
    * starts with '0'
    * greater than 26

Core Insight
At any index i, we decide:
* Take 1 digit
* Take 2 digits (if valid)
→ This is a choice-based counting problem
####################################################################################################
2. Simulation

Let’s take:
s = "226"

At index 0:
* Take "2" → solve "26"
* Take "22" → solve "6"
So:	f(0) = f(1) + f(2)

At index 1:
* Take "2" → solve "6"
* Take "26" → solve ""
f(1) = f(2) + f(3)

At index 2:
* Take "6" → valid
f(2) = f(3)

At index 3 (end):
f(3) = 1

Generalization
Define:		dp[i] = number of ways to decode substring starting at i
####################################################################################################
3. Recursion

Recurrence relation
f(i) = 0					if s[i] == '0'
f(i) = f(i+1)				(take 1 digit)
	 + f(i+2) 				if s[i:i+2] is valid (10–26)

        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i+1]

            if valid 2-digit:
                dp[i] += dp[i+2]


Base case
f(n) = 1   # empty string → valid decoding

Recursive structure
* Parameter → index i
* Return → number of ways
* Shrinks → i → i+1 or i+2
####################################################################################################
Time Complexity O(n)
Space Complexity O(n) → can optimize to O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        next1 = 1  # dp[i+1]
        next2 = 0  # dp[i+2]

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = next1
                if (i + 1 < n) and (10 <= int(s[i:i+2]) <= 26):
                    curr += next2

            next2 = next1
            next1 = curr

        return next1
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [0] * (n + 1)
        dp[n] = 1  # base case

        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

                if (i + 1 < n) and (10 <= int(s[i:i+2]) <= 26):
                    dp[i] += dp[i + 2]

        return dp[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic cases
        "12",  # Expected: 2
        "226",  # Expected: 3
        "06",  # Expected: 0

        # Edge cases with zeros
        "10",  # Expected: 1
        "101",  # Expected: 1
        "100",  # Expected: 0
        "110",  # Expected: 1
        "230",  # Expected: 0

        # Single character
        "1",  # Expected: 1
        "0",  # Expected: 0

        # Larger combinations
        "11106",  # Expected: 2
        "111111",  # Expected: 13

        # Invalid patterns
        "301",  # Expected: 0
        "00",  # Expected: 0

        # Mixed complexity
        "2611055971756562",  # Expected: 4

        # Long repetitive (stress DP)
        "111111111111111111111111111111111111111111111",  # Large Fibonacci-like
    ]

    for s in test_cases:
        result = solution.numDecodings(s)
        print(f"Input: {s} -> Output: {result}")