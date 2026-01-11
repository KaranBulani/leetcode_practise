'''
Time complexity:  O(total characters in words) For setting TrieNode
                                +
                  O(maxLen) for 1 Query
                  but for Q queries it will be Q * O(maxLen)

Space complexity: O(total characters in words) For TrieNodes
                                +
                  O(maxLen) for the stream buffer
'''
from typing import List
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def add(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True

class StreamChecker:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.streamTillNow = deque()
        self.maxLen = 0
        for word in words:
            self.root.add(word[::-1])
            self.maxLen = max(self.maxLen, len(word))

    def query(self, letter: str) -> bool:
        self.streamTillNow.appendleft(letter)
        # Keep stream length bounded
        if len(self.streamTillNow) > self.maxLen:
            self.streamTillNow.pop()

        node = self.root
        for char in self.streamTillNow:
            if char not in node.children:
                return False
            node = node.children[char]
            if node.isEndOfWord:
                return True

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

if __name__ == "__main__":

    def run_test(words, queries, expected, test_name):
        print(f"\nRunning {test_name}")
        streamChecker = StreamChecker(words)
        result = []
        for ch in queries:
            result.append(streamChecker.query(ch))
        print("Words:      ", words)
        print("Queries:    ", queries)
        print("Output:     ", result)
        print("Expected:   ", expected)
        print("PASS ✅" if result == expected else "FAIL ❌")


    # --------------------------------------------------
    # Test Case 1: Example from problem statement
    # --------------------------------------------------
    run_test(
        words=["cd", "f", "kl"],
        queries=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
        expected=[False, False, False, True, False, True, False, False, False, False, False, True],
        test_name="Test Case 1: Problem Example"
    )

    # --------------------------------------------------
    # Test Case 2: Single-character words
    # --------------------------------------------------
    run_test(
        words=["a", "b", "c"],
        queries=["a", "b", "c", "a", "a"],
        expected=[True, True, True, True, True],
        test_name="Test Case 2: Single Character Words"
    )

    # --------------------------------------------------
    # Test Case 3: Overlapping suffixes
    # --------------------------------------------------
    run_test(
        words=["ab", "bab", "b"],
        queries=["a", "b", "a", "b"],
        expected=[False, True, False, True],
        test_name="Test Case 3: Overlapping Suffixes"
    )

    # --------------------------------------------------
    # Test Case 4: Long word only matches at the end
    # --------------------------------------------------
    run_test(
        words=["leetcode"],
        queries=list("leetcode"),
        expected=[False, False, False, False, False, False, False, True],
        test_name="Test Case 4: Long Word Match"
    )

    # --------------------------------------------------
    # Test Case 5: No match ever
    # --------------------------------------------------
    run_test(
        words=["xyz"],
        queries=["a", "b", "c", "d", "e"],
        expected=[False, False, False, False, False],
        test_name="Test Case 5: No Match"
    )

    # --------------------------------------------------
    # Test Case 6: Repeated characters in stream
    # --------------------------------------------------
    run_test(
        words=["aa", "aaa"],
        queries=["a", "a", "a", "a"],
        expected=[False, True, True, True],
        test_name="Test Case 6: Repeated Characters"
    )

    # --------------------------------------------------
    # Test Case 7: Multiple words ending at same position
    # --------------------------------------------------
    run_test(
        words=["x", "yx", "zyx"],
        queries=["z", "y", "x"],
        expected=[False, False, True],
        test_name="Test Case 7: Multiple Valid Suffixes"
    )