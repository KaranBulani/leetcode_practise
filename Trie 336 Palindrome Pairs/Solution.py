'''
####################################################################################################
####################################################################################################

For a word w, split it into: w = left | right

If:
    left is a palindrome, and
    there exists a word = reverse(right)
    → that word can be placed before w. We append in same sequence

    right is a palindrome, and
    there exists a word = reverse(left)
    → that word can be placed after w. We append in same sequence

We must check all possible splits of every word and ensure no word split should be repeated
When right == "", Case B creates pairs already covered by Case A of another split, so we skip it to avoid duplicates.

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            return s == s[::-1]

        word_to_index = {word: i for i, word in enumerate(words)}

        res = []
        for i, word in enumerate(words):
            n = len(word)

            for j in range(n + 1):
                left = word[:j]
                right = word[j:]

                rev_right = right[::-1]
                rev_left = left[::-1]

                # Case 1: left is palindrome → check reverse(right), And check if same number is not considered
                if is_palindrome(left) and rev_right in word_to_index and word_to_index[rev_right] != i:
                    res.append([word_to_index[rev_right], i])

                # Case 2: right is palindrome → check reverse(left)
                # j != n avoids duplicates
                if j != n and is_palindrome(right) and rev_left in word_to_index and word_to_index[rev_left] != i:
                    res.append([i, word_to_index[rev_left]])

        return res
####################################################################################################
####################################################################################################

For two words A and B:
A + B is a palindrome iff the unmatched part on one side is itself a palindrome and the rest matches in reverse order.

We use a Trie built on reversed words, and during both insert and search.
Why reversed? Because while scanning word A from left → right, we want to match it against suffixes of other words.

🧠 High-Level Plan

Step 1 — Build a Trie of *reversed* words
	Each node stores:
	1. Children (letters)
	2. word_index → index of the word that ends here (or -1)
	3. palindrome_suffix_indices
	   → list of word indices whose remaining prefix (before this point) is a palindrome
	This extra list is critical to keep the solution linear.

Step 2 — While inserting a word into the Trie
	Insert reversed(word) character by character.
	At each position:
	* Check:	  > “Is the remaining part of the original word (prefix) a palindrome?”
	* If YES:	  → Store this word’s index in palindrome_suffix_indices at the current Trie node.
	Finally:
	* At the end of the word, store word_index.
	💡 This lets us later form palindromes where current word is shorter than the match.

Step 3 — Search for palindrome pairs
	Now, for each word W, traverse the Trie normally (not reversed).
	While traversing:

	Case A — Trie word ends early
	At any node:
	* If node.word_index != -1
	* And the remaining part of W is a palindrome
	  → Then (current_word_index, node.word_index) is a valid pair.
	📌 This handles cases like: "lls" + "s" where both words are already in Trie

	Case B — Word fully consumed
	Once all characters of W are matched:
	* For every index in node.palindrome_suffix_indices
	  → (current_word_index, that_index) is valid.
	📌 This handles: "s" + "lls"

| Word  | Index | Reversed |
| ----- | ----- | -------- |
| abcd  | 0     | dcba     |
| dcba  | 1     | abcd     |
| lls   | 2     | sll      |
| s     | 3     | s        |
| sssll | 4     | llsss    |

ROOT
├── d
│   └── c
│       └── b
│           └── a
│               ├── word_index = 0
│               └── palindrome_suffixes = [0]
│
├── a
│   └── b
│       └── c
│           └── d
│               ├── word_index = 1
│               └── palindrome_suffixes = [1]
│
├── s
│   ├── word_index = 3
│   ├── palindrome_suffixes = [3]
│   └── l
│       └── l
│           ├── word_index = 2
│           └── palindrome_suffixes = [2]
│
└── l
    └── l
        └── s
            └── s
                └── s
                    ├── word_index = 4
                    └── palindrome_suffixes = [4]

| Metric            | Value                      |
| ----------------- | -------------------------- |
| Time              | **O(sum of word lengths)** |
| Space             | **O(sum of word lengths)** |
| Palindrome checks | Linear & bounded           |

'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_index = -1
        self.palindrome_suffixes = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root = TrieNode()

        def is_palindrome(s):
            return s == s[::-1]

        for idx, word in enumerate(words):
            node = root
            for i, ch in enumerate(reversed(word)):
                if is_palindrome(word[:len(word) - i]):
                    # Here we append on parent TrieNode(ch)
                    # When we append we mention that remaining part (prefix not suffix) is a palindrome
                    node.palindrome_suffixes.append(idx)
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word_index = idx
            # at end also we append, to specify remaining string which is "" is also palindrome.
            node.palindrome_suffixes.append(idx)

        res = []

        for i, word in enumerate(words):
            node = root
            for j, ch in enumerate(word):
                # Case 1: matched full word in trie, Word in Trie ended early
                if node.word_index != -1 and node.word_index != i:
                    if is_palindrome(word[j:]):
                        res.append([i, node.word_index])
                if ch not in node.children:
                    break
                node = node.children[ch]

            # The else block executes ONLY IF the for loop finishes normally (i.e. no break was executed).
            else:
                for idx in node.palindrome_suffixes:
                    if idx != i:
                        res.append([i, idx])
        return res

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ===============================
        # Examples from the problem
        # ===============================

        (
            ["bat", "tab", "cat"],
            # Expected:
            [[0,1],[1,0]]
        ),

        (
            ["abcd", "dcba", "lls", "s", "sssll"],
            # Expected (order may vary):
            [[0,1],[1,0],[3,2],[2,4]]
        ),

        (
            ["a", ""],
            # Expected:
            [[0,1],[1,0]]
        ),

        # ===============================
        # Edge cases
        # ===============================

        (
            [""],
            # Expected:
            []
        ),

        (
            ["a"],
            # Expected:
            []
        ),

        (
            ["aa", "aa"],
            # Note: words are supposed to be unique in constraints,
            # but useful to test robustness
            # Expected:
            [[0,1],[1,0]]
        ),

        (
            ["a", "b", "c"],
            # Expected:
            []
        ),

        (
            ["aba", "xyz"],
            # Expected:
            []
        ),

        (
            ["", "aba", "xyz"],
            # Expected:
            [[0,1],[1,0]]
        ),

        # ===============================
        # Prefix / suffix palindrome checks
        # ===============================

        (
            ["lls", "s", "sssll"],
            # Expected:
            [[1,0],[0,2]]
        ),

        (
            ["race", "car"],
            # Expected:
            [[0,1]]
        ),

        (
            ["abc", "cba", "bc"],
            # Expected:
            [[0,1],[1,0]]
        ),

        # ===============================
        # Stress-style logical cases
        # ===============================

        (
            ["a", "aa", "aaa"],
            # Expected:
            [
              [0,1],[1,0],
              [0,2],[2,0],
              [1,2],[2,1]
            ]
        ),

        (
            ["abcd", "dcba", "lls", "s"],
            # Expected:
            [[0,1],[1,0],[3,2]]
        ),
    ]

    for idx, (words, _) in enumerate(test_cases):
        print(f"\nTest Case {idx + 1}: {words}")
        result = solution.palindromePairs(words)
        print("Output:", result)