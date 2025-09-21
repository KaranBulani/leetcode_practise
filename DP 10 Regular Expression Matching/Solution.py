'''
####################################################################################################
####################################### BottomUp Tabulation ########################################
####################################################################################################
Time Complexity:  O(n*m)					(where n is len(s) and m is len(p), as that many states will be there)
Space Complexity: O(n*m)               	    (for Caching n,m states)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        # dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True  # empty string matches empty pattern

        # Initialize for patterns like a*, a*b*, etc
        # Consider s = "", p = "a*b*c*"
        #   	0	a	*	b	*	c	*
        #   0	T	F	T	F	T	F	T
        for j in range(1, m + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # Fill dp table
        # Consider s = "aab", p = "c*a*b"
        #   	0  	 c	 *	 a	 *	 b
        #   0	T	 F	 T	 F	 T	 F
        #   a	F	 F	 F	 T	 T	 F
        #   a	F	 F	 F	 F	 T	 F
        #   b	F	 F	 F	 F	 F	 T

        # We use a 1-indexed DP table but strings are 0-indexed, So remember to do index minus one.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if current char matches, then result would be whatever without current char each side is
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # if current pattern is * check if 0 or some occurrence will work?

                    # Zero occurrence
                    # If you drop both the preceding element and the * from the pattern, you reduce
                    # the pattern length by two & you still need to match the same string prefix (i.e. i doesn't change).
                    # That is why we check dp[i][j-2] for the “zero occurrence” case.
                    dp[i][j] = dp[i][j - 2]

                    # Some occurrence
                    # if char before star (in pattern) matches current char
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        # Result would be value of "Either 0 OR Some occurrence"
                        dp[i][j] |= dp[i - 1][j]

                        # Why do we do decrement i in dp[i-1] while taking OR but decrement j p[j - 2] while comparing char
                        # One short example: string "aaa" vs pattern a*.
                        # To decide whether the whole string matches the pattern at the last character, you ask: can "aa" match a*? That is dp[i-1][j]. If yes, then a* can absorb the final a too.
                        # Asking dp[i][j-1] would instead ask whether "aaa" matches pattern "a" (pattern without *), which is the wrong question for allowing repetition.
        return dp[n][m]


####################################################################################################
####################################### TOP-DOWN Memoization #######################################
####################################################################################################

Time Complexity:  O(n*m)					(where n is len(s) and m is len(p), as that many states will be there)
Space Complexity: O(n*m)               	    (for Caching n,m states)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # ✅ Base case: both string and pattern fully consumed → match
            # s = "ab" p = "ab"
            if i >= len(s) and j >= len(p):
                return True

            # ❌ Pattern consumed but string still left → no match
            # s = "aa"  p = "a"
            if j >= len(p):
                return False

            # Answer is separate for both case
            # s = "a"  p = "ab","a*b*"

            # Check if current chars match (only if s is not exhausted)
            # '.' matches any char OR exact same char
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Case 1: Next char in pattern is '*'
            if (j + 1) < len(p) and p[j + 1] == "*":
                # Two possibilities:
                # 1. Skip "char*" in pattern (treat '*' as 0 occurrence)
                # 2. If current chars match → consume one char from s and stay at same pattern position
                cache[(i, j)] = (dfs(i, j + 2) or  # Dont use star
                                 (match and dfs(i + 1, j)))  # Use star
                return cache[(i, j)]

            # Case 2: Normal match (no '*'), so move to next positions if current chars match
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # Otherwise → no match
            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # From problem statement
        ("aa", "a", False),  # single 'a' cannot match double 'a'
        ("aa", "a*", True),  # '*' allows multiple 'a'
        ("ab", ".*", True),  # '.*' can match any string

        # Additional edge cases
        ("", ".*", True),  # empty string matches '.*'
        ("", "", True),  # empty matches empty
        ("", "a*", True),  # '*' allows zero occurrence
        ("", "a", False),  # empty cannot match 'a'
        ("a", "", False),  # non-empty cannot match empty
        ("mississippi", "mis*is*p*.", False),  # classic tricky case
        ("mississippi", "mis*is*ip*.", True),  # valid matching
        ("ab", ".*c", False),  # cannot match extra 'c'
        ("aaa", "a*a", True),  # 'a*' can be expanded to fit
        ("aaa", "ab*a*c*a", True),  # '*' gives flexibility
        ("aaa", "aaaa", False),  # lengths mismatch
        ("aab", "c*a*b", True),  # 'c*' disappears, match "aab"
        ("abcd", "d*", False),  # must match entire string
        ("abcd", ".*d", True),  # any chars ending with 'd'
        ("ab", ".*..", True),  # '.*' + two dots matches "ab"
        ("ab", ".*...", False),  # needs one more char
    ]

    for s, p, expected in test_cases:
        result = solution.isMatch(s, p)
        print(f"s='{s}', p='{p}' => {result}, expected={expected}")