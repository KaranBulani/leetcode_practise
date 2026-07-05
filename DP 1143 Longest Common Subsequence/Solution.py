'''
1. Observation

Read the problem statement

We need to find the length of the longest subsequence that appears in both strings.
A subsequence:
* can skip characters.
* must preserve relative order.
We're not asked to return the subsequence itself, only its length.

Identify key words and phrases
* Characters can be skipped.
* Order must remain the same.
* Need the longest possible common subsequence.
* String lengths are up to 1000, so brute force is impossible.

Identify processing direction
Suppose we are comparing prefixes of the two strings.
If we already know the answer for smaller prefixes, can we build the answer for larger prefixes?
	Yes.
This naturally suggests solving progressively larger prefix pairs.

Core Observations

For the last characters of two prefixes, only two situations exist:
Case 1: Characters match
	text1[:i] ends with x
	text2[:j] ends with x

	Since they are equal, this character must be part of the LCS.
	So,	LCS(text1[:i], text2[:j]) = LCS(text1[:i-1], text2[:j-1]) + 1

Case 2: Characters don't match

	* text1[:i] ends with a
	* text2[:j] ends with b
	They cannot both appear as the last character of the same common subsequence.

	One of them has to be ignored.

	Two possibilities:
	* Ignore last character of text1
	* Ignore last character of text2
	Take whichever gives the longer subsequence.

Example:

	text1 = "cab"
	text2 = "ca"

	Compute: dp[3][2]

	Comparing:		"cab"		"ca"
	Last characters: 'b' vs 'a'
	No match.
	Now:
	* dp[2][2] = LCS("ca", "ca") = 2
	* dp[3][1] = LCS("cab", "c") = 1
	* dp[2][1] = LCS("ca", "c") = 1

	If you used only dp[i-1][j-1], you'd get:
	dp[2][1] = 1   ❌

	But the correct answer is:
	max(dp[2][2], dp[3][1])
	= max(2, 1)
	= 2 ✅

Why did dp[i-1][j-1] fail?

    Because removing both characters at once is too aggressive.

    In this example:
    * The optimal LCS "ca" is obtained by ignoring only 'b' from text1.
    * If you also remove the last 'a' from text2 (i.e., use dp[i-1][j-1]), you've thrown away a character that actually belongs to the optimal LCS.

    That's why, when characters don't match, we consider ignoring one character at a time:
    * dp[i-1][j] (ignore from text1)
    * dp[i][j-1] (ignore from text2)
    and take the maximum. This ensures we don't accidentally discard a character that should remain in the LCS.

####################################################################################################
2. Simulation

	Consider
		text1 = "abcde"
		text2 = "ace"
	Suppose we're comparing
		"abcde"
		"ace"
	Last characters:		e == e
	They match.
	So,		LCS("abcde","ace") = 1 + LCS("abcd","ac")

	Now compare
		"abcd"
		"ac"
	Last characters
		d
		c
	They don't match.
	We have two choices.
	Ignore 'd'		LCS("abc","ac")
	Ignore 'c'		LCS("abcd","a")
	Take the larger answer.

	Now compare
		"abc"
		"ac"
	Last characters		c == c
	They match.			1 + LCS("ab","a")

	Eventually we reach		LCS("a","a")
	Characters match.		1 + LCS("","")
	Base case returns 0.
	Answer becomes	3

	Generalization

	Whenever the last characters match:
		Answer = 1 + smaller diagonal problem

	Whenever they don't match:
		Answer = max(
		ignore from first string,
		ignore from second string
		)

	This same structure repeats for every pair of prefixes.

####################################################################################################
3. Recursion

Since every problem reduces into smaller problems having exactly the same structure, recursion is a natural approach.

## Define the recursive function

	Let
			LCS(i, j)
	represent:
	> Length of the LCS between text1[:i] and text2[:j].
	Notice this matches exactly what our DP state will represent.

## Base Case

	If either prefix is empty,
		i == 0
		or
		j == 0

	then
		LCS(i, j) = 0
	because an empty string has no common subsequence with anything.

## Recursive Cases

	Case 1
	Last characters match.
		text1[i-1] == text2[j-1]
	Then
		LCS(i, j) = 1 + LCS(i-1, j-1)

	Case 2
	Last characters don't match.
		text1[i-1] != text2[j-1]
	Then
		LCS(i, j) = max(
		LCS(i-1, j),
		LCS(i, j-1)
		)

## Complete Recurrence

	LCS(i, j) =
	{
		0                                  if i == 0 or j == 0

		1 + LCS(i-1, j-1)                  if text1[i-1] == text2[j-1]

		max(LCS(i-1,j), LCS(i,j-1))        otherwise
	}

Time Complexity
	Without memoization:	O(2^(m+n))
	because the same subproblems are solved repeatedly.

    ---

    ## Recursive Function

    We defined: LCS(i, j)
    where
        * i = length of prefix of text1
        * j = length of prefix of text2

    ## When characters match
    There is only one recursive call.

                    LCS(i, j)
                            |
                            |
                    LCS(i-1, j-1)
    So this path doesn't branch.

    ## When characters don't match
    We branch into two recursive calls.

                             LCS(i, j)
                             /       \
                            /         \
                   LCS(i-1,j)      LCS(i,j-1)
    Each of these again may branch into two more calls.

    ## Worst Case

    Suppose the strings never match.

    Example
        text1 = "aaaaaa"
        text2 = "bbbbbb"

    Every comparison is unequal.
    So every node creates two children.

                        (6,6)
                      /       \
                  (5,6)       (6,5)
                 /    \       /    \
             (4,6) (5,5) (5,5) (6,4)
              ...

    Notice something important:	(5,5) is solved twice.
    Later, (4,5) gets solved many times.
    Eventually almost every state is recomputed repeatedly.

    ## How deep can the recursion go?

    Every recursive call decreases either
    * i, or
    * j.
    Eventually one of them becomes zero.

    Suppose
    i = m
    j = n

    The maximum number of decreases before stopping is m + n
    because together you can decrease i exactly m times and j exactly n times.
    So the recursion tree has height roughly m + n

    ## How many nodes?

    In the worst case, every node has 2 children.
    A binary tree of height h has approximately 2^h nodes.
    Here,
        h = m + n
    Therefore,
    Number of recursive calls ≈ 2^(m+n)

    Hence,
    Time Complexity = O(2^(m+n))

####################################################################################################
4. Dynamic Programming

The recursive solution repeatedly computes the same (i, j) states.
Since:
* the recurrence is pure,
* each state depends only on smaller states,
we can cache every state exactly once using DP.

## DP State

	Let
		dp[i][j]

	represent:
	> Length of the LCS between text1[:i] and text2[:j].
	This is exactly the same meaning as our recursive function.

## DP Transition

	Base Case
		dp[0][j] = 0
		dp[i][0] = 0

	Matching characters
	If,
			text1[i-1] == text2[j-1]
	then,
			dp[i][j] = dp[i-1][j-1] + 1

	Different characters

	Otherwise,
		dp[i][j] = max(
		dp[i-1][j],
		dp[i][j-1]
		)

## Filling Order

	Since each state depends on:
	* top
	* left
	* top-left

	fill row by row (or column by column).
			  ""  a  c  e
		   -
		"" | 0  0  0  0
		a  | 0
		b  | 0
		c  | 0
		d  | 0
		e  | 0

	Each cell only uses values already computed.

####################################################################################################
## Python Solution

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

## Complexity Analysis

Time Complexity
	There are (m + 1) × (n + 1) states.
	Each state takes constant time.
	Time = O(m × n)

Space Complexity
	The DP table contains (m + 1) × (n + 1) entries.
	Space = O(m × n)

####################################################################################################
Space Optimized DP (1D DP)

Notice the transition:
dp[i][j] =
    dp[i-1][j-1] + 1
or
    max(dp[i-1][j], dp[i][j-1])

To compute row i, we only need:
* the previous row (i-1)
* the current row being built

So instead of storing all m + 1 rows, we can keep just two 1D arrays:
* prev → represents dp[i-1][*]
* curr → represents dp[i][*]

After finishing a row:
	prev = curr
	curr = [0] * (n + 1)

This reduces the space complexity from O(m × n) to O(n) while keeping the time complexity O(m × n).

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)

            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            prev = curr

        return prev[n]

Time Complexity: O(m × n)
Space Complexity: O(n)
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # =========================
        # Examples from Question
        # =========================
        ("abcde", "ace"),  # Expected: 3
        ("abc", "abc"),  # Expected: 3
        ("abc", "def"),  # Expected: 0

        # =========================
        # Single Character Cases
        # =========================
        ("a", "a"),  # Expected: 1
        ("a", "b"),  # Expected: 0

        # =========================
        # One String is Subsequence of Other
        # =========================
        ("abcdef", "ace"),  # Expected: 3
        ("ace", "abcdef"),  # Expected: 3

        # =========================
        # Completely Different Lengths
        # =========================
        ("abcdefgh", "bdg"),  # Expected: 3
        ("xyz", "abcdefghijkl"),  # Expected: 0

        # =========================
        # Repeated Characters
        # =========================
        ("aaaa", "aa"),  # Expected: 2
        ("aaaaa", "aaa"),  # Expected: 3
        ("ababab", "bababa"),  # Expected: 5
        ("abcabcaa", "acbacba"),  # Expected: 5

        # =========================
        # Order Matters
        # =========================
        ("abc", "cba"),  # Expected: 1
        ("abcd", "dcba"),  # Expected: 1

        # =========================
        # Partial Match
        # =========================
        ("abcxyz", "xyzabc"),  # Expected: 3
        ("abcdgh", "aedfhr"),  # Expected: 3
        ("aggtab", "gxtxayb"),  # Expected: 4

        # =========================
        # Larger Mixed Cases
        # =========================
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"),  # Expected: 4
        ("ezupkr", "ubmrapg"),  # Expected: 2
    ]

    for i, (text1, text2) in enumerate(test_cases, start=1):
        result = solution.longestCommonSubsequence(text1, text2)
        print(f"Test Case {i}")
        print(f"text1 = {text1}")
        print(f"text2 = {text2}")
        print(f"Output   : {result}")
        print("-" * 50)