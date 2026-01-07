'''
from typing import List, Set

class MagicDictionary:
    def __init__(self) -> None:
        self.words: Set[str] = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words.update(dictionary)

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            if self.__is_exactly_one_edit_away(searchWord, word):
                return True

        return False

    def __is_exactly_one_edit_away(self, w1: str, w2: str) -> bool:
        differences = 0

        for ch1, ch2 in zip(w1, w2):
            if ch1 != ch2:
                differences += 1
                if differences > 1:
                    return False

        return differences == 1

| Operation         | Time           | Space          |
| ----------------- | -------------- | -------------- |
| `buildDict`       | `O(N · L)`     | `O(N · L)`     |
| `search` (single) | `O(N · L)`     | `O(1)`         |
| **Overall**       | **`O(N · L)`** | **`O(N · L)`** |

Here N · L is N words with average L len
and space is primarily for wordSet

###############################################################################################################
###############################################################################################################

'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEndOfWord = True

    def search(self, searchWord: str) -> bool:

        def dfs(node: TrieNode, diff: int, index: int) -> bool:
            if index == len(searchWord) and node.isEndOfWord and diff == 1:
                return True

            if index >= len(searchWord):
                return False

            if diff > 1:
                return False

            for key in node.children:
                newdiff = diff + 1 if key != searchWord[index] else diff
                if dfs(node.children[key], newdiff, index + 1):
                    return True
            return False

        return dfs(self.root, 0, 0)


if __name__ == "__main__":
    # Instantiate object
    magicDictionary = MagicDictionary()

    # -------------------------
    # Test Case 1: Example from problem statement
    # -------------------------
    magicDictionary.buildDict(["hello", "leetcode"])

    print(magicDictionary.search("hello"))  # Expected: False (0 changes not allowed)
    print(magicDictionary.search("hhllo"))  # Expected: True  (change 1 char)
    print(magicDictionary.search("hell"))  # Expected: False (length mismatch)
    print(magicDictionary.search("leetcoded"))  # Expected: False (length mismatch)

    # -------------------------
    # Test Case 2: Single word dictionary
    # -------------------------
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["a"])

    print(magicDictionary.search("a"))  # Expected: False (0 changes)
    print(magicDictionary.search("b"))  # Expected: True  (a -> b)

    # -------------------------
    # Test Case 3: Multiple words, same length
    # -------------------------
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["abc", "xyz", "abx"])

    print(magicDictionary.search("abc"))  # Expected: True  (abc -> abx)
    print(magicDictionary.search("abx"))  # Expected: True  (abx -> abc)
    print(magicDictionary.search("abd"))  # Expected: True  (abd -> abc)
    print(magicDictionary.search("axx"))  # Expected: False (needs >1 change)

    # -------------------------
    # Test Case 4: Different lengths in dictionary
    # -------------------------
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["abcd", "abc", "ab"])

    print(magicDictionary.search("abc"))  # Expected: False (exact match, 0 change)
    print(magicDictionary.search("abx"))  # Expected: True  (abx -> abc)
    print(magicDictionary.search("abcd"))  # Expected: False (0 change)
    print(magicDictionary.search("abce"))  # Expected: True  (abce -> abcd)

    # -------------------------
    # Test Case 5: Edge case – change at first / last character
    # -------------------------
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["hello"])

    print(magicDictionary.search("cello"))  # Expected: True  (first char change)
    print(magicDictionary.search("hella"))  # Expected: True  (last char change)
    print(magicDictionary.search("helpo"))  # Expected: True  (middle char change)
    print(magicDictionary.search("hello"))  # Expected: False (0 change)

    # -------------------------
    # Test Case 6: Requires more than one change
    # -------------------------
    magicDictionary = MagicDictionary()
    magicDictionary.buildDict(["abcdef"])

    print(magicDictionary.search("abcxyz"))  # Expected: False (>1 char change)
