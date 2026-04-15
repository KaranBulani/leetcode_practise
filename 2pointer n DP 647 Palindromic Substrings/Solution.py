'''
                                        BRUTE FORCE

class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        total = 0
        n = len(s)
        for i in range(n):
            for j in range(i+1, n+1):
                if is_palindrome(s[i:j]):
                    total += 1

        return total

| Aspect | Complexity |
| ------ | ---------- |
| Time   |   O(n³)    |
| Space  |   O(n)     |

####################################################################################################
####################################################################################################
                                        DP METHOD

dp[i][j] = True if substring s[i:j] is a palindrome

 * If s[i] == s[j]
 * And:
   * Length ≤ 2 ("aa" or "a") → automatically palindrome
   * OR inner substring is palindrome

dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i+1][j-1])

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count

| Approach             | Time  | Space | Use Case                            |
| -------------------- | ----- | ----- | ----------------------------------- |
| DP                   | O(n²) | O(n²) | When substring relationships matter |

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

class Solution:
    def countSubstrings(self, s: str) -> int:

        total = 0
        def expand_n_count(l: int, r: int) -> None:
            nonlocal total
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
            return

        n = len(s)
        for i in range(n):
            expand_n_count(i, i)
            expand_n_count(i, i+1)

        return total

⏱ Complexity
    Time: O(n²)
    Space: O(1)
'''


class Solution:
    def countSubstrings(self, s: str) -> int:


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Basic examples from question
        ("abc", 3),
        ("aaa", 6),

        # Single character (minimum constraint)
        ("a", 1),

        # Two characters
        ("aa", 3),  # "a", "a", "aa"
        ("ab", 2),  # "a", "b"

        # Mixed palindromes
        ("aba", 4),  # "a", "b", "a", "aba"
        ("abba", 6),  # "a","b","b","a","bb","abba"
        ("racecar", 10),

        # No large palindromes
        ("abcd", 4),

        # Repeating pattern
        ("aaaa", 10),

        # Palindromes in middle
        ("abccba", 9),

        # Long-ish string
        ("banana", 10),

        # Edge: alternating characters
        ("abababa", 16),

        # Edge: all same characters (stress-like)
        ("zzzzzz", 21),
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = solution.countSubstrings(s)
        print(f"Test Case {i + 1}: Input = '{s}'")
        print(f"Output = {result}, Expected = {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 50)