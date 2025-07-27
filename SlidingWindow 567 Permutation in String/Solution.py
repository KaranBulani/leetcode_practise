'''
Time Complexity:   O(n + k)                        (for  k = len(s1),  n = len(s2))
Space Complexity:  O(alphabet) or 2*O(26)          (for all 2 dictionary)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)

        L = 0
        s2_dict = {}
        for R in range(len(s2)):

            # If window size exceeds len(s1), shrink it from the left
            if R - L + 1 > len(s1):

                # Remove or decrement the count of the outgoing character s2[L]
                if s2_dict[s2[L]] == 1:
                    # If its count is 1, fully remove it to keep dicts comparable
                    del s2_dict[s2[L]]
                else:
                    # Otherwise, just decrement its count
                    s2_dict[s2[L]] -= 1

                # Move left edge rightward
                L += 1
            s2_dict[s2[R]] = 1 + s2_dict.get(s2[R], 0)

            # Matching freq map means current window in s2 is a permutation of s1.
            if s1_dict == s2_dict:
                return True
        return False

####################################################################################################

Below is same solution just clubbed some operations and used list instead of dictionary
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        #count first len(s1) characters in both s1,s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        #variable indicating how many a-z characters are matching
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            #all matching return
            if matches == 26: return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                #increase if it matches
                matches += 1
            elif s2Count[index] - 1 == s1Count[index]:
                # Decrease matches iff it was matching before
                # earlier it might be 2b, 0b now its 3b, 0b
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] + 1 == s1Count[index]:
                # Decrease matches iff it was matching before
                # earlier it might be 3b, 0b now its 2b, 0b
                matches -= 1
            l += 1

        return matches == 26

if __name__ == "__main__":
    solution = Solution()

    # List of test cases: (s1, s2, expected_result)
    test_cases = [
        # Prompt examples
        ("abc",       "bbbca",    True),
        ("ab",        "eidbaooo",    True),   # contains "ba"
        ("ab",        "eidboaoo",    False),  # no permutation

        # Edge cases
        ("a",         "a",           True),   # single char, exact match
        ("a",         "b",           False),  # single char, no match
        ("aa",        "aaaaa",       True),   # repeated char, many matches
        ("abc",       "bbbca",       True),   # permutation "bca" at end
        ("abcd",      "abc",         False),  # s1 longer than s2

        # Additional variations
        ("xyz",       "afdgzyxksldfm", True),  # interleaved match "zyx"
        ("hello",     "ooolleoooleh", False), # almost but not contiguous
    ]

    for s1, s2, expected in test_cases:
        result = solution.checkInclusion(s1, s2)
        print(f"s1={s1!r}, s2={s2!r}  ➞  Got: {result!r}  |  Expected: {expected!r}")
