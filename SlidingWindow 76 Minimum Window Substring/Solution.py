'''
####################################################################################################
############################### BRUTE FORCE CHECKING countT & countS ###############################
####################################################################################################

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s) or t == "": return res

        # build the target counts
        countS, countT = {}, {}
        for i in range(len(t)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # if the first window already matches, return it
        if countT == countS:
            return s[0:len(t)]

        L = 0
        # expand the right bound R one char at a time
        for R in range(len(t), len(s)):
            # include s[R] into our window-count
            countS[s[R]] = 1 + countS.get(s[R], 0)

            # check if window covers t, and if so try to shrink it
            # we use a while because after shrinking once it may still cover
            while all(countS.get(c, 0) >= countT[c] for c in countT):
                # record the best (smallest) window so far
                window_len = R - L + 1
                if res == "" or window_len < len(res):
                    res = s[L:R+1]

                # shrink from the left: remove s[L] and move L forward
                countS[s[L]] -= 1
                L += 1
                # if you remove a char below its needed count, the while will break

        return res

Time Complexity:  O(n * m)              O(n) for loop × an O(m) while loop
Space Complexity: O(n + m)              two dictionaries countS and countT

####################################################################################################
############################ REMOVE BRUTE FORCE, USING HAVE & NEED VAR #############################
####################################################################################################

Time Complexity:  O(n + m)              O(n) for loop S + O(m) for loop T
Space Complexity: O(n + m)              two dictionaries countS and countT
'''
from typing import List, Tuple

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s) or t == "": return res

        # build T count
        countT, countSWindow = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        L = 0

        for R in range(len(s)):
            c = s[R]
            countSWindow[c] = 1 + countSWindow.get(c, 0)

            if c in countT and countSWindow[c] == countT[c]:
                have += 1

            while have == need:
                windowLen = R - L + 1
                if res == "" or windowLen < len(res):
                    res = s[L:R+1]

                countSWindow[s[L]] -= 1
                if s[L] in countT and countSWindow[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        return res

if __name__ == "__main__":
    solution = Solution()

    # List of test cases: each is a tuple (s, t, expected_output)
    test_cases: List[Tuple[str, str, str]] = [
        # Examples from the problem statement
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),

        # Additional edge cases
        ("ABC", "D", ""),                       # pattern character not in source
        ("ABBBBC", "BBC", "BBC"),               # repeated letters
        ("AAABBCDD", "ABC", "AABBC"),            # overlapping windows
        ("xyyzyzyx", "xyz", "zyx"),              # multiple valid windows
        ("bba", "ab", "ba"),                    # minimal at end
        ("cabwefgewcwaefgcf", "cae", "cwae"),   # longer example
    ]

    for idx, (s, t, expected) in enumerate(test_cases):
        result = solution.minWindow(s, t)
        print(f"Test case {idx}: s=\"{s}\", t=\"{t}\"")
        print(f"  Expected: \"{expected}\"")
        print(f"  Got:      \"{result}\"")
        print(f"  {'PASS' if result == expected else 'FAIL'}")
        print("-")
