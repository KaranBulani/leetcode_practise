'''
🧠 1. Observation
  We need to find the length of the longest subsequence (not substring) of a string that is a palindrome.

👉 Key difference:
  * Subsequence → can skip characters
  * Substring → must be contiguous

🔹 Key Observations
  * If s[i] == s[j], they can be part of a palindrome
  * If not equal, we must exclude one side and try both options
  * This naturally creates overlapping subproblems

🔹 Constraints Insight
  * n ≤ 1000 → brute force (2ⁿ) is too slow
  * Strong hint toward Dynamic Programming

🔹 Core Idea
  We are repeatedly solving:
  > “What is the LPS between index i and j?”
  This is a range DP problem

####################################################################################################

🔁 2. Simulation
Let’s take:
  s = "bbbab"

Try to think in terms of range [i, j]:
  * If characters match → include both
  * Else → skip one side

Example:
  "bbbab"
  Compare first and last:
  b == b → good → 2 + solve("bba")

Inside "bba":
* First != last → try both:
  * solve("bb")
  * solve("ba")

🔹 Generalization
    f(i, j) = length of LPS in s[i...j]

####################################################################################################

🔁 3. Recursion

  If i > j → 0
  If i == j → 1
  If s[i] == s[j]:
      f(i, j) = 2 + f(i+1, j-1)
  Else:
      f(i, j) = max(f(i+1, j), f(i, j-1))

🔹 Meaning of f(i, j)
  👉 Maximum palindrome length in substring s[i...j]

🔹 Base Cases
  * Single character → palindrome → 1
  * Empty → 0

####################################################################################################

🔹 DP Filling Order
⚠️ Important:
  * We need i+1 and j-1 → so compute from bottom-up
  * Iterate:
    * i from n-1 → 0
    * j from i → n-1

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]

                                VS

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]

💡 Solution 1 Philosophy:
“Let invalid ranges naturally return 0”

💡 Solution 2 Philosophy:
“Initialize everything as valid and fix edge cases manually”

####################################################################################################

🔹 Time Complexity - O(n²)
    * Total states = n × n
    * Each state takes O(1)

🔹 Space Complexity - O(n²)

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ("bbbab", 4),
        ("cbbd", 2),

        # Edge cases
        ("a", 1),  # Single character
        ("aa", 2),  # All same characters
        ("ab", 1),  # No palindrome longer than 1

        # Small variations
        ("aba", 3),
        ("abc", 1),
        ("aaa", 3),

        # Medium complexity
        ("agbdba", 5),  # "abdba"
        ("character", 5),  # "carac"
        ("bbbabbbb", 7),

        # Tricky DP cases
        ("abcba", 5),
        ("abdbca", 5),
        ("abcdba", 5),

        # Non-contiguous subsequence focus
        ("aebcbda", 5),  # "abcba"
        ("abcde", 1),

        # Larger repetitive pattern
        ("aaaaabaaaa", 10),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = solution.longestPalindromeSubseq(s)
        print(f"Test Case {i + 1}: Input = '{s}'")
        print(f"Expected = {expected}, Got = {result}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)