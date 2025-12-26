'''
Note: WHEN WE MENTION TIME COMPLEXITY WE MENTION WORST TIME & SPACE COMPLEXITY

N = number of words (≤ 10^4)
L = maximum length of a word (≤ 7)

Time Complexity:
    Constructor: O(N * L^2)
                 Generate all suffix and club with "#" + word,
                 For 1 suffix, in worst case suffix would be entire word so O(L) + 1 + O(L) -> O(2L) + 1
                 There would be L suffixes, so for L suffixes assuming each of them of L len it would be -> L * ( O(2L) + 1 )

                 There can be N words for which above would be repeated - > N * ( L * ( O(2L) + 1 ) )

      Searching: O(L)
                 We build string which is suff + # + pref & we just traverse Trie, This value is always less than 2L + 1, So we can say its O(L)

Space Complexity:
            Trie: (N * L^2)
                  There will be similar number of TrieNode required which be equivalent to Time Complexity.

'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()

        for idx, word in enumerate(words):
            length = len(word)
            for i in range(length):
                suffix = word[i:]
                self.addWord(idx, suffix + "#" + word)

    def addWord(self, idx: int, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.index = idx

    def f(self, pref: str, suff: str) -> int:
        node = self.root
        word = suff + "#" + pref

        for ch in word:
            if ch not in node.children:
                return -1
            node = node.children[ch]

        return node.index

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

if __name__ == "__main__":

    # -------- Test Case 1: Basic single word --------
    words = ["apple"]
    wf = WordFilter(words)
    print(wf.f("a", "e"))     # basic prefix + suffix
    print(wf.f("ap", "le"))   # full match
    print(wf.f("b", "e"))     # prefix does not exist


    # -------- Test Case 2: Multiple words, overlapping prefixes --------
    words = ["apple", "apply", "ape"]
    wf = WordFilter(words)
    print(wf.f("ap", "e"))
    print(wf.f("ap", "ly"))
    print(wf.f("a", "e"))


    # -------- Test Case 3: Duplicate words (index matters) --------
    words = ["test", "test", "testing"]
    wf = WordFilter(words)
    print(wf.f("te", "st"))    # should return largest valid index
    print(wf.f("test", "test"))
    print(wf.f("tes", "ing"))


    # -------- Test Case 4: Prefix and suffix both full word --------
    words = ["a", "aa", "aaa"]
    wf = WordFilter(words)
    print(wf.f("a", "a"))
    print(wf.f("aa", "aa"))
    print(wf.f("aaa", "aaa"))


    # -------- Test Case 5: No valid match --------
    words = ["hello", "world"]
    wf = WordFilter(words)
    print(wf.f("x", "o"))
    print(wf.f("he", "x"))


    # -------- Test Case 6: Same prefix/suffix, different lengths --------
    words = ["prefixsuffix", "prefix", "suffix"]
    wf = WordFilter(words)
    print(wf.f("pre", "fix"))
    print(wf.f("pre", "suffix"))
    print(wf.f("suf", "fix"))


    # -------- Test Case 7: Stress-style small but tricky --------
    words = ["abc", "bc", "c", "abc"]
    wf = WordFilter(words)
    print(wf.f("a", "c"))
    print(wf.f("ab", "c"))
    print(wf.f("abc", "abc"))