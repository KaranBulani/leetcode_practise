'''
| Metric      | Complexity                           |
| ----------- | ------------------------------------ |
| Build Trie  | **O(S)**                             |
| Search      | **O(M)** where `M = len(searchWord)` |
| Space       | **O(S)**                             |
| Insert cost | **O(1)** (max 3 items only)          |
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        # Build Trie
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        # Search
        res = []
        node = root
        for char in searchWord:
            if char not in node.children:
                res.append([])
                node = TrieNode()   # dead path
            else:
                node = node.children[char]
                res.append(node.suggestions)

        return res

if __name__ == "__main__":
    solution = Solution()

    test_cases = [

        # 2. Single product, exact match
        {
            "products": ["havana"],
            "searchWord": "havana",
            # Expected:
            # [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]
        },

        # 1. Example from problem statement
        {
            "products": ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "searchWord": "mouse",
            # Expected:
            # [
            #   ["mobile","moneypot","monitor"],
            #   ["mobile","moneypot","monitor"],
            #   ["mouse","mousepad"],
            #   ["mouse","mousepad"],
            #   ["mouse","mousepad"]
            # ]
        },

        # 3. No product matches after some prefix
        {
            "products": ["apple", "banana", "carrot"],
            "searchWord": "cat",
            # Expected:
            # [["carrot"], [], []]
        },

        # 4. All products share prefix, more than 3 matches
        {
            "products": ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"],
            "searchWord": "aaa",
            # Expected:
            # [
            #   ["aa","aaa","aaaa"],
            #   ["aaa","aaaa","aaaaa"],
            #   ["aaa","aaaa","aaaaa"]
            # ]
        },

        # 5. Lexicographical ordering check
        {
            "products": ["bags", "baggage", "banner", "box", "cloths"],
            "searchWord": "bags",
            # Expected:
            # [
            #   ["baggage","bags","banner"],
            #   ["baggage","bags","banner"],
            #   ["bags"],
            #   ["bags"]
            # ]
        },

        # 6. Prefix longer than any product
        {
            "products": ["abc", "ab"],
            "searchWord": "abcd",
            # Expected:
            # [["ab","abc"], ["ab","abc"], ["abc"], []]
        },

        # 7. Products with no common starting letter
        {
            "products": ["dog", "cat", "fish"],
            "searchWord": "zoo",
            # Expected:
            # [[], [], []]
        },
    ]

    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}")
        products = test["products"]
        searchWord = test["searchWord"]

        result = solution.suggestedProducts(products, searchWord)
        print("Products:", products)
        print("SearchWord:", searchWord)
        print("Result:", result)