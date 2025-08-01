'''
####################################################################################################
############################### BRUTE FORCE CHECKING countS & countP ###############################
####################################################################################################
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(p) > len(s): return res

        countP = {} # Frequency of each letter in p
        for char in p:
            countP[char] = 1 + countP.get(char, 0)

        L, countS = 0, {}
        for R in range(len(s)):
            rChar = s[R] # add new Char
            countS[rChar] = 1 + countS.get(rChar, 0)

            # remove the char that falls off once window exceeds p’s length
            if R >= len(p):
                lChar = s[L]
                if countS[lChar] == 1:
                    del countS[lChar]
                else:
                    countS[lChar] -= 1
                L+= 1

            # if they match
            if countS == countP: res.append(L)
        return res

Time Complexity:  O(s + p) * O(26)                          (for building dictionary, comparison of countS == countP )
Space Complexity: O(distinct char in s & p)                 (for dictionaries)
                  O(1)

####################################################################################################
############################ REMOVE BRUTE FORCE, USING HAVE & NEED VAR #############################
####################################################################################################

Time Complexity:  O(n + m)              O(n) for loop S + O(m) for loop T
Space Complexity: O(n + m)              two dictionaries countS and countT
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        if len(p) > len(s): return res

        # Build target frequency map and count distinct letters needed
        countT = {}
        for ch in p:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)

        # Sliding window counts and matched count
        L, countS = 0, {}
        for R in range(len(s)):
            rChar = s[R]
            countS[rChar] = countS.get(rChar, 0) + 1

            # If rChar is in target & we've just reached the needed count, increment have
            if rChar in countT:
                if countS[rChar] == countT[rChar]:
                    have += 1
                elif countS[rChar] == countT[rChar] + 1:
                    # We went over needed count, so we no longer have this char matching
                    have -= 1

            # Shrink window when size exceeds p
            if R - L + 1 > len(p):
                lChar = s[L]

                # If lChar is in target and was matching, adjust have
                if lChar in countT:
                    if countS[lChar] == countT[lChar]:
                        have -= 1
                    elif countS[lChar] == countT[lChar] + 1:
                        # Was over count, removing one makes it match
                        have += 1

                # Remove from window count
                countS[lChar] -= 1
                if countS[lChar] == 0:
                    del countS[lChar]
                L += 1

            if have == need:
                res.append(L)
        return res

if __name__ == "__main__":
    solution = Solution()

    # Example cases
    print(solution.findAnagrams("cbaebabacd", "abc"))  # Expected: [0,6]
    print(solution.findAnagrams("abab", "ab"))         # Expected: [0,1,2]

    # Edge case: p longer than s
    print(solution.findAnagrams("a", "abc"))           # Expected: []

    # Edge case: s and p are the same
    print(solution.findAnagrams("abc", "abc"))         # Expected: [0]

    # Edge case: multiple overlapping anagrams
    print(solution.findAnagrams("aaabaa", "aaa"))      # Expected: [0]

    # Edge case: no matches at all
    print(solution.findAnagrams("abcdefg", "hij"))     # Expected: []

    # Edge case: all characters same
    print(solution.findAnagrams("aaaaa", "aa"))        # Expected: [0,1,2,3]

    # Edge case: empty string cases (though constraints say length >= 1)
    print(solution.findAnagrams("", "a"))              # Expected: []
    print(solution.findAnagrams("a", ""))              # Expected: []

    # Edge case: both s and p are a single matching character
    print(solution.findAnagrams("a", "a"))             # Expected: [0]