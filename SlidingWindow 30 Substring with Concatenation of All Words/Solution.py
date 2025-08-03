'''
Time Complexity:  O(N * W)
                  *  N is the length of string s
                  *  W is the number of words
Space Complexity: O(W)              (for  hash maps)
'''

from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        word_len = len(words[0])                # All words are of the same length
        word_count = len(words)                 # Total number of words

        word_freq = Counter(words)              # Frequency of each word in the list
        res = []

        # We only need to start from 0 to word_len - 1 to cover all window alignments
        for i in range(word_len):
            L = i                               # Start of the sliding window
            R = i                               # End of the sliding window
            window_words = Counter()            # Word frequency in the current window
            words_used = 0                      # Count of valid words used in the window

            while R + word_len <= len(s):
                # Extract word from current position
                word = s[R:R + word_len]
                R += word_len

                if word in word_freq:
                    window_words[word] += 1
                    words_used += 1

                    # If word used more than required, shrink window from left
                    while window_words[word] > word_freq[word]:
                        left_word = s[L:L + word_len]
                        window_words[left_word] -= 1
                        L += word_len
                        words_used -= 1

                    # If window contains exactly all the words
                    if words_used == word_count:
                        res.append(L)

                else:
                    # Invalid word found, reset window
                    window_words.clear()
                    words_used = 0
                    L = R
        return res

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
