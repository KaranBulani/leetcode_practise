'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for Variables, indexes)

30. Substring with Concatenation of All Words

You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation:
There is no concatenated substring.

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation:
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
'''

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Implementation goes here
        pass

if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    tests = [
        {
            "s": "barfoothefoobarman",
            "words": ["foo", "bar"],
            "expected": [0, 9]
        },
        {
            "s": "wordgoodgoodgoodbestword",
            "words": ["word", "good", "best", "word"],
            "expected": []
        },
        {
            "s": "barfoofoobarthefoobarman",
            "words": ["bar", "foo", "the"],
            "expected": [6, 9, 12]
        },

        # Additional edge cases
        # 1. Empty string and non-empty words
        {
            "s": "",
            "words": ["a", "b"],
            "expected": []
        },
        # 2. Non-empty string and empty words list
        {
            "s": "abcdef",
            "words": [],
            "expected": []
        },
        # 3. Single word equal to string
        {
            "s": "hello",
            "words": ["hello"],
            "expected": [0]
        },
        # 4. Single word not present
        {
            "s": "hello",
            "words": ["world"],
            "expected": []
        },
        # 5. Words longer than string
        {
            "s": "short",
            "words": ["longerword"],
            "expected": []
        },
        # 6. Repeating words with overlap
        {
            "s": "aaaaaa",
            "words": ["aa", "aa", "aa"],
            "expected": [0, 1, 2]
        },
        # 7. Mixed overlap but non-matching
        {
            "s": "foobarfoobar",
            "words": ["foo", "bar", "baz"],
            "expected": []
        }
    ]

    for i, test in enumerate(tests, 1):
        s = test["s"]
        words = test["words"]
        expected = test["expected"]
        result = solution.findSubstring(s, words)
        print(f"Test case {i}: s={s!r}, words={words!r}")
        print(f"Expected: {expected}, Got: {result}\n")
