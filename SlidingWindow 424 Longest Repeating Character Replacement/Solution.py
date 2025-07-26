'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countCharDict = {}
        L, res = 0, 0
        for R in range(len(s)):
            countCharDict[s[R]] = 1 + countCharDict.get(s[R], 0)

            #window is invalid/ COULD USE WHILE BELOW
            if R-L+1 - max(countCharDict.values()) > k:
                countCharDict[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res

Time Complexity:  O(26 * 2n)         (for L,R & max(countCharDict.values()))
                  O(n)

Space Complexity: O(26)              (for countCharDict, L & R)
                  O(1)

################################################################################################

Time Complexity:  O(2n)         (for L,R)
                  O(n)

Space Complexity: O(26)         (for countCharDict, L & R)
                  O(1)

⚠️ What if maxF becomes stale as the window shifts (i.e. if the most frequent character was on the left and got removed)?

Consider example: "AAA BCDEF GGGGGGGG" and k = 1
Note: Window never shrinks, it either expands(R+=1) or its shifts (L+=1, R+=1)

Old Code:
1. During AAA.. window expands (R+=1) and max(countCharDict.values()) increases.
2. During ..BCDEF.. window shifts (L+=1, R+=1) and max(countCharDict.values()) decreases. As R - L + 1 stay's same, no new res
3. During ..GGGGGGGG window expands compared to even previous (R+=1) and max(countCharDict.values()) increases eventually, new res comes when R - L + 1 is bigger than previous.

New Code:
1. During AAA.. window expands (R+=1) and maxF increases.
2. During ..BCDEF.. window shifts (L+=1, R+=1) and maxF stay's same.
	Note: Both a & b below stay same. No new res
	a) R-L+1 - maxF  (in old code R-L+1 stays same whereas max(countCharDict.values()) decreases)
	b) max(res, R-L+1) (in old code both stay same)
3. During ..GGGGGGGG window expands compared to even previous (R+=1) and maxF increases eventually, new res comes when it is bigger than previous max.

Hence, It's okay if maxF becomes stale!
'''

from typing import List, Tuple

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countCharDict = {}
        L, res, maxF = 0, 0, 0
        for R in range(len(s)):
            countCharDict[s[R]] = 1 + countCharDict.get(s[R], 0)
            maxF = max(maxF, countCharDict[s[R]])
            #window is invalid
            if R-L+1 - maxF > k:
                countCharDict[s[L]] -= 1
                L += 1
            res = max(res, R-L+1)
        return res

if __name__ == "__main__":
    solution = Solution()

    # List of test cases: (input_string, k, expected_output)
    test_cases: List[Tuple[str, int, int]] = [
        # Examples from the problem statement
        ("AAABCDEFGGGGGGGG",1,9),
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        # Edge cases
        ("A", 0, 1),  # Single character, no replacements
        ("AAAA", 2, 4),  # All same characters
        ("ABCDE", 2, 3),  # All unique characters with limited replacements
        ("ABBB", 2, 4),  # One dominant character
        ("XYZ", 3, 3),  # k equals string length
        ("ABCABC", 3, 4),  # Replacements spread evenly
        ("BACBACBA", 2, 5),  # Mixed pattern
    ]

    for s, k, expected in test_cases:
        result = solution.characterReplacement(s, k)
        print(f"Input: s = \"{s}\", k = {k} | Expected: {expected}, Got: {result}")