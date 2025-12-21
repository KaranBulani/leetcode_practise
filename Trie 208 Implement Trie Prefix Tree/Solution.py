'''
Insert Word: O(w)
Search Word: O(w)
Search Prefix: O(w)

where w is the length of the word.
'''
class TrieNode:
    def __init__(self):
        # 1st Word: TrieNode
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == "__main__":
    trie = Trie()

    # --- Basic example from problem ---
    trie.insert("apple")
    assert trie.search("apple") is True  # exact match
    assert trie.search("app") is False  # prefix but not full word
    assert trie.startsWith("app") is True  # valid prefix

    trie.insert("app")
    assert trie.search("app") is True  # now exists

    # --- Single character cases ---
    trie.insert("a")
    assert trie.search("a") is True
    assert trie.startsWith("a") is True
    assert trie.search("b") is False
    assert trie.startsWith("b") is False

    # --- Overlapping prefixes ---
    trie.insert("bat")
    trie.insert("bath")
    trie.insert("batman")

    assert trie.search("bat") is True
    assert trie.search("bath") is True
    assert trie.search("batman") is True
    assert trie.search("batmobile") is False

    assert trie.startsWith("bat") is True
    assert trie.startsWith("bath") is True
    assert trie.startsWith("batm") is True
    assert trie.startsWith("cat") is False

    # --- Re-inserting same word ---
    trie.insert("apple")
    trie.insert("apple")
    assert trie.search("apple") is True

    # --- Word vs prefix confusion ---
    assert trie.startsWith("appl") is True
    assert trie.search("appl") is False

    # --- Long word edge case ---
    long_word = "a" * 2000
    trie.insert(long_word)
    assert trie.search(long_word) is True
    assert trie.startsWith("a" * 1999) is True
    assert trie.search("a" * 1999) is False

    print("All Trie test cases passed ✅")