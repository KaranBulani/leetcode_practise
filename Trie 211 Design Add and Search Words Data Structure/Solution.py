'''
| Operation            | Time Complexity | Space Complexity |
| -------------------- | --------------- | ---------------- |
| `addWord`            | **O(L)**        | **O(L)**         |
| `search` (no dots)   | **O(L)**        | **O(L)**         |
| `search` (with dots) | **O(26^k · L)** | **O(L)**         | 	Where k is number of dots and there can be 26 character when k level came
| Overall storage      | —               | **O(N · L)**     |
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.isEndOfWord

            c = word[i]

            if c != ".":
                # not in also handles when input is 1 level but search is 3 level
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)
            else:
                for newNode in node.children.values():
                    if dfs(newNode, i + 1):
                        return True
                return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    wd = WordDictionary()

    tests = [
        # ===== Examples from the question =====
        ("add", "bad", None),
        ("add", "dad", None),
        ("add", "mad", None),
        ("search", "pad", False),
        ("search", "bad", True),
        ("search", ".ad", True),
        ("search", "b..", True),

        # ===== Edge cases =====
        # Single character words
        ("add", "a", None),
        ("search", "a", True),
        ("search", ".", True),

        # Word length mismatch
        ("search", "..", False),
        ("search", "....", False),

        # All dots (max 2 dots allowed by constraints)
        ("search", "..d", True),
        ("search", "..x", False),

        # Repeated add
        ("add", "bad", None),
        ("search", "bad", True),

        # Prefix vs full word
        ("search", "ba", False),
        ("search", "b.d", True),

        # Dot in middle
        ("search", "d.d", True),
        ("search", "m.d", True),

        # Non-existing but pattern-valid
        ("search", "c..", False),
    ]

    print("Running WordDictionary tests...\n")

    for i, (op, word, expected) in enumerate(tests, 1):
        if op == "add":
            wd.addWord(word)
            print(f"{i:02d}. addWord('{word}')")
        else:
            result = wd.search(word)
            print(f"{i:02d}. search('{word}') -> {result} | expected: {expected}")