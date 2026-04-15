'''

1. Observation
Key Idea
* A substring s[i:j] is a palindrome if:
  1. s[i] == s[j]
  2. The inner substring s[i+1:j-1] is also a palindrome
👉 This gives a clear recurrence relation

####################################################################################################

2. Simulation
Take:
s = "babad"

We build a DP table:
dp[i][j] = True if s[i:j] is palindrome

Base cases:
* Single character → always palindrome
  dp[i][i] = True
* Two characters:
  dp[i][i+1] = (s[i] == s[i+1])

Transition:
dp[i][j] = (s[i] == s[j]) AND dp[i+1][j-1]

Filling order (VERY IMPORTANT)
* We must fill from bottom to top, start from bottom right
* Because dp[i][j] depends on dp[i+1][j-1]
* we eventually populate top right part of table

👉 Loop:
i from n-1 → 0
j from i → n-1

####################################################################################################

3. Recursion (Underlying idea)

Recurrence:
f(i, j) = True if:
    s[i] == s[j] AND f(i+1, j-1)
But we convert this into DP to avoid recomputation.

####################################################################################################

4. Dynamic Programming

State
dp[i][j] = whether substring s[i:j] is palindrome

Transition
dp[i][j] = True if:
    s[i] == s[j] AND (j - i <= 2 OR dp[i+1][j-1])


👉 Why j - i <= 2?
* Covers:
  * length 1 → already palindrome
  * length 2 → just compare chars
  * length 3 → middle 1 char is automatically palindrome

5. Technique Selection
* Overlapping subproblems ✔
* Optimal substructure ✔

✅ So DP is valid

DP Solution Code
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        res = ""
        res_len = 0

        # Fill DP table
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if (j - i + 1) > res_len:
                        res = s[i:j+1]
                        res_len = j - i + 1

        return res

####################################################################################################
Time & Space Complexity

Time
* Filling DP table: O(n²)

Space
* DP table: O(n²)

####################################################################################################
####################################################################################################
                                        2 POINTER METHOD

Important observation
 * A palindrome is defined by its center
 * From a center, we can expand outward

Core Idea
 * Instead of checking all substrings:
 * ➡️ Fix a center and expand outward

Generalization
For every index i, we consider:
 * Odd length palindrome → center = i
 * Even length palindrome → center = (i, i+1)

Time Complexity
    For each index → expand up to O(n)
    Total: O(n²)

Space Complexity
    O(1) (no extra memory)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):
            res = (0, -1) # while range calculates its r - l + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res = (l, r)
                l -= 1
                r += 1
            return res

        res = ""
        res_len = 0

        for i in range(len(s)):
            # Odd length
            l, r = expand(i, i)
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1

            # Even length
            l, r = expand(i, i + 1)
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        "babad",
        "cbbd",

        # Edge cases
        "a",  # single character
        "aa",  # two same chars
        "ab",  # two different chars
        "",  # empty string (not in constraints but good to test)

        # All same characters
        "aaaaaa",

        # No palindrome longer than 1
        "abcdefg",

        # Even length palindrome
        "abba",

        # Odd length palindrome
        "racecar",

        # Palindrome in middle
        "xyzracecarabc",

        # Multiple valid answers
        "abacdfgdcaba",

        # Long string with palindrome inside
        "forgeeksskeegfor",

        # Mixed characters
        "a1b2b1a",

        # Large input pattern
        "a" * 1000
    ]

    for i, test in enumerate(test_cases):
        result = solution.longestPalindrome(test)
        print(f"Test Case {i + 1}: Input = {test}")
        print(f"Output = {result}")
        print("-" * 50)