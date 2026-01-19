'''
####################################################################################################
################################################ DP ################################################
####################################################################################################

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        wordSet = set()
        res = []

        def canForm(word: str):
            if not wordSet:
                return False

            dp = [False] * (len(word) + 1)
            dp[0] = True
            for end in range(1, len(word) + 1):
                for start in range(end):
                    if dp[start] and word[start:end] in wordSet:
                        dp[end] = True
                        break

            return dp[-1]

        for word in words:
            if canForm(word):
                res.append(word)
            wordSet.add(word)

        return res

| Component   | Time            | Space      |
| ----------- | --------------- | ---------- |
| Sorting     | `O(N log N)`    | `O(1)`     |
| DP per word | `O(L²)`         | `O(L)`     |
| Total DP    | `O(N × L²)`     | —          |
| Set         | —               | `O(S)`     |
| **Overall** | **`O(N × L²)`** | **`O(S)`** |

####################################################################################################
Why Trie Is Faster

| Aspect             | Without Trie        | With Trie           |
| ------------------ | ------------------- | ------------------- |
| Substring checking | All possible splits | Only valid prefixes |
| DP states          | `L`                 | `L`                 |
| Work per state     | `O(L)`              | `O(1)` (Trie step)  |
| Per-word cost      | `O(L²)`             | `O(L)`              |
| Total cost         | `O(N × L²)`         | `O(T)`              |

####################################################################################################
Time Complexity:
    Sorting: N logN
    Building Trie: Total Trie Insertion Cost
                   O(len(word1) + len(word2) + ... + len(wordN))
                   O(T)
    DFS Cost for ALL Words: O(T)
                            Each index of a word is computed at most once

Space Complexity:
    Trie Storage: O(T)
                  One Trie node per character (worst case)

    DFS Memoization: O(L) This does NOT accumulate across words.
    Recursion Stack: O(L) Max depth = word length
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        trie = Trie()
        result = []

        def canForm(word: str, start: int, count: int, memo: dict):
            if start == len(word):
                return count >= 2

            if start in memo:
                return memo[start]

            node = trie.root
            for i in range(start, len(word)):
                ch = word[i]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end and canForm(word, i + 1, count + 1, memo):
                    memo[start] = True
                    return memo[start]

            memo[start] = False
            return memo[start]

        for word in words:
            if not word:
                continue

            memo = {}
            if canForm(word, 0, 0, memo):
                result.append(word)

            trie.insert(word)

        return result

if __name__ == "__main__":
    solution = Solution()

    # -------------------------
    # Example 1 (from question)
    # -------------------------
    words1 = [
        "cat", "cats", "catsdogcats",
        "dog", "dogcatsdog",
        "hippopotamuses",
        "rat", "ratcatdogcat"
    ]
    result1 = solution.findAllConcatenatedWordsInADict(words1)
    print("Test Case 1 Output:", result1)
    # Expected (order may vary):
    # ["catsdogcats", "dogcatsdog", "ratcatdogcat"]

    # -------------------------
    # Example 2 (from question)
    # -------------------------
    words2 = ["cat", "dog", "catdog"]
    result2 = solution.findAllConcatenatedWordsInADict(words2)
    print("Test Case 2 Output:", result2)
    # Expected:
    # ["catdog"]

    # -------------------------
    # Edge Case 1: No concatenated words
    # -------------------------
    words3 = ["a", "b", "c"]
    result3 = solution.findAllConcatenatedWordsInADict(words3)
    print("Test Case 3 Output:", result3)
    # Expected:
    # []

    # -------------------------
    # Edge Case 2: Word can be formed multiple ways
    # -------------------------
    words4 = ["a", "aa", "aaa", "aaaa"]
    result4 = solution.findAllConcatenatedWordsInADict(words4)
    print("Test Case 4 Output:", result4)
    # Expected:
    # ["aa", "aaa", "aaaa"]

    # -------------------------
    # Edge Case 3: Long chain concatenation
    # -------------------------
    words5 = ["rat", "cat", "dog", "ratcat", "catdog", "ratcatdog"]
    result5 = solution.findAllConcatenatedWordsInADict(words5)
    print("Test Case 5 Output:", result5)
    # Expected:
    # ["ratcat", "catdog", "ratcatdog"]

    # -------------------------
    # Edge Case 4: Single word only
    # -------------------------
    words6 = ["alone"]
    result6 = solution.findAllConcatenatedWordsInADict(words6)
    print("Test Case 6 Output:", result6)
    # Expected:
    # []

    # -------------------------
    # Edge Case 5: Reuse of same word allowed
    # -------------------------
    words7 = ["go", "goal", "goals", "goalgoalsgo"]
    result7 = solution.findAllConcatenatedWordsInADict(words7)
    print("Test Case 7 Output:", result7)
    # Expected:
    # ["goalgoalsgo"]
