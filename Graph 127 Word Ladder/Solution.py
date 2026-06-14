'''
## Algorithm
1. Put all words into a set.
2. If endWord is absent, return 0.
3. Start BFS from beginWord.
4. For every popped word:
   * Change each character to 'a'..'z'
   * Generate candidate words.
   * If candidate equals endWord, return answer.
   * If candidate exists in set:
     * Push into queue.
     * Remove from set (mark visited).
5. If BFS finishes, return 0.

## Time Complexity
For each word visited:
	L positions
	26 character choices

Work per word: O(26 × L)

If N words are visited: O(N × 26 × L) = O(NL)

## Space Complexity
Word Set : O(N)
Queue    : O(N)

Total: O(N)

'''
from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        if beginWord in wordSet:
            wordSet.remove(beginWord)

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps

            word_chars = list(word)

            for i in range(len(word)):

                original = word_chars[i]
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == original:
                        continue
                    word_chars[i] = c
                    new_word = "".join(word_chars)

                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))
                        wordSet.remove(new_word)
                word_chars[i] = original

        return 0

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example 1
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            5
        ),

        # Example 2
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            0
        ),

        # Direct transformation
        (
            "hit",
            "hot",
            ["hot"],
            2
        ),

        # Single valid path
        (
            "cat",
            "dog",
            ["cot", "cog", "dog"],
            4
        ),

        # Multiple shortest paths
        (
            "red",
            "tax",
            ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"],
            4
        ),

        # End word exists but unreachable
        (
            "aaa",
            "bbb",
            ["aac", "acc", "ccc", "bbb"],
            0
        ),

        # Large branching but short answer
        (
            "lost",
            "cost",
            ["most", "fost", "lost", "cost"],
            2
        ),

        # Transformation requires exploring many options
        (
            "talk",
            "tail",
            ["tall", "tail", "balk", "bail", "tell", "tale"],
            3
        ),

        # Longer chain
        (
            "game",
            "thee",
            ["fame", "fate", "date", "data", "dada", "dead", "deed", "thee"],
            0
        ),

        # Standard interview-style case
        (
            "leet",
            "code",
            ["lest", "leet", "lose", "code", "lode", "robe", "lost"],
            6
        ),
    ]

    for i, (beginWord, endWord, wordList, expected) in enumerate(test_cases, start=1):
        result = solution.ladderLength(beginWord, endWord, wordList)

        print(f"Test Case {i}")
        print(f"beginWord = {beginWord}")
        print(f"endWord   = {endWord}")
        print(f"Expected  = {expected}")
        print(f"Got       = {result}")
        print(f"PASS      = {result == expected}")
        print("-" * 50)