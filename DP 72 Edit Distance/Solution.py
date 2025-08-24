'''
####################################################################################################
##################################### Backtracking & Recursion #####################################
####################################################################################################

Time Complexity:  O(3^(min(l1, l2)))            (Recursion in I,R,D)
Space Complexity: O(l1 + l2)              	    (for CallStack) Ignoring String Slicing

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        # Base case: if either word is empty, the only option is
        # to insert all characters of the other word
        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        # If the first characters of both words match,
        # no operation is needed for this character,
        # so just recurse on the remaining substrings
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])

        # Otherwise, try all three operations:

        # 1. Insert operation:
        # Insert the first character of word2 into word1.
        # That means we move forward in word2 but not in word1,
        # because word1 still needs to match the curr character.
        insert = 1 + self.minDistance(word1, word2[1:])

        # 2. Delete operation:
        # Delete the first character of word1.
        # That means we move forward in word1 but not in word2.
        # because word2 still needs to match the curr character.
        delete = 1 + self.minDistance(word1[1:], word2)

        # 3. Replace operation:
        # Replace the first character of word1 with that of word2.
        # That means both words move forward together.
        replace = 1 + self.minDistance(word1[1:], word2[1:])

        # The minimum of the three operations is the answer
        return min(insert, delete, replace)

####################################### This will throw TLE ########################################
####################################### Caching implemented ########################################

class Solution:
    def minDistance(self, word1: str, word2: str, memo = defaultdict(int)) -> int:
        l1, l2 = len(word1), len(word2)
        if l1 == 0 or l2 == 0:
            return max(l1, l2)

        if (word1, word2) not in memo:
            if word1[0] == word2[0]:
                return self.minDistance(word1[1:], word2[1:])
            insert = 1 + self.minDistance(word1, word2[1:])
            delete = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            memo [(word1, word2)] = min(insert, delete, replace)

        return memo[(word1, word2)]

####################################################################################################
####################################### Dynamic Programming ########################################
####################################################################################################

Time Complexity:  O(mn)            (Calculcating dp array)
Space Complexity: O(mn)            (Calculcating dp array)
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        # dp[i][j] will store the minimum number of operations required
        # to convert the first i characters of word1 into the first j characters of word2.
        # Dimensions: (m+1) x (n+1), because we include the empty prefix "" as well.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case 1:
        # To convert first i chars of word1 -> "" (empty word2),
        # we need i deletions.
        for i in range(1, m + 1):
            dp[i][0] = i

        # Base case 2:
        # To convert "" (empty word1) -> first j chars of word2,
        # we need j insertions.
        for j in range(1, n + 1):
            dp[0][j] = j

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # If curr characters match, no new operation is needed.
                    # Just take the result from previous substring comparison.
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If curr characters don't match, we have 3 choices:
                    # 1. Replace curr char of word1  -> dp[i-1][j-1] + 1
                    #    Both j/n/w2 & i/m/w1 decrements as we have implemented replace
                    # 2. Delete curr char from word1 -> dp[i-1][j] + 1
                    #    j/n/w2 stays at same place, i/m/w1 decrements as here we have implement delete
                    # 3. Insert curr char into word1 -> dp[i][j-1] + 1
                    #    j/n/w2 decrements, i/m/w1 points at same place as here we have implement insert
                    dp[i][j] = min(
                        dp[i - 1][j - 1],  # replace
                        dp[i - 1][j],  # delete
                        dp[i][j - 1]  # insert
                    ) + 1

        # Final answer: min operations to convert all of word1 -> all of word2
        return dp[m][n]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    word1, word2 = "horse", "ros"
    print(solution.minDistance(word1, word2))  # Expected: 3

    # Example 2
    word1, word2 = "intention", "execution"
    print(solution.minDistance(word1, word2))  # Expected: 5

    # Edge case 1: both strings empty
    word1, word2 = "", ""
    print(solution.minDistance(word1, word2))  # Expected: 0

    # Edge case 2: one string empty
    word1, word2 = "abc", ""
    print(solution.minDistance(word1, word2))  # Expected: 3

    word1, word2 = "", "abc"
    print(solution.minDistance(word1, word2))  # Expected: 3

    # Edge case 3: identical strings
    word1, word2 = "same", "same"
    print(solution.minDistance(word1, word2))  # Expected: 0

    # Edge case 4: completely different strings
    word1, word2 = "abc", "def"
    print(solution.minDistance(word1, word2))  # Expected: 3

    # Edge case 5: single character difference
    word1, word2 = "a", "b"
    print(solution.minDistance(word1, word2))  # Expected: 1

    # Edge case 6: one string is prefix of the other
    word1, word2 = "abc", "abcd"
    print(solution.minDistance(word1, word2))  # Expected: 1

    word1, word2 = "abcd", "abc"
    print(solution.minDistance(word1, word2))  # Expected: 1

    # Larger but simple case
    word1, word2 = "kitten", "sitting"
    print(solution.minDistance(word1, word2))  # Expected: 3
