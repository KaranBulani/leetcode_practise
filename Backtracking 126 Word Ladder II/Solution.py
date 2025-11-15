'''

✅ Problem Summary
We must transform beginWord → endWord using only words from wordList,
changing one letter at a time, and we must return all shortest transformation sequences.
This is NOT just finding one shortest path…
We must return all shortest paths → this is why we need a graph + DFS.

✅ High-Level Strategy
1. Convert list to a set for O(1) lookup
2. Use BFS to:
    Build a map:
        parents[word] = list of words that can reach it in shortest path
    Stop BFS when we reach endWord
    Ensure we only explore shortest paths (layer-by-layer)
3. Use DFS to backtrack from endWord → beginWord
    Using the parents map
    Collect all valid sequences

🔥 Why BFS + DFS?
    BFS ensures shortest distance
    DFS enumerates all paths inside the shortest graph built by BFS

| Component      | Time          | Space         |
| -------------- | ------------- | ------------- |
| Neighbor check | O(N²)         | —             |

Time:   For every word visited, we scan all words in the wordSet. One-edit check takes O(L) (constant).
        O(N) words × O(N) comparisons each × O(L)

| BFS            | O(N²)         | O(N)          |
| Parents graph  | —             | O(N²)         |
| Backtracking   | O(S)          | O(S)          |
| **Total**      | **O(N² + S)** | **O(N² + S)** |

Quite confusing so skipped details
https://chatgpt.com/c/6918039d-ef00-8322-8b9a-5f39369b9630

'''
from collections import defaultdict, deque

class Solution:
    def one_edit(self, w1: str, w2: str) -> bool:
        diff = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff += 1
                if diff > 1:
                    return False
        return diff == 1

    def get_neighbors(self, word: str, words: set[str]) -> list[str]:
        res = []
        for w in words:
            if self.one_edit(word, w):
                res.append(w)
        return res

    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        queue = deque([beginWord])
        parents = defaultdict(list)
        visited = set([beginWord])
        found_end = False

        # BFS
        while queue and not found_end:
            next_level_visited = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                neighbors = self.get_neighbors(word, wordSet)

                for n in neighbors:
                    if n not in visited:
                        # Always record parent (may be multiple parents on same level)
                        parents[n].append(word)
                        # Enqueue n only once per level
                        if n not in next_level_visited:
                            queue.append(n)
                            next_level_visited.add(n)

            visited.update(next_level_visited)
            # remove visited words from wordSet to speed up neighbor checks
            wordSet -= next_level_visited

            if endWord in next_level_visited:
                found_end = True

        # If endWord was never reached
        if not found_end:
            return []

        # Backtracking from endWord to beginWord
        result = []

        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return
            for p in parents[word]:
                backtrack(p, path + [p])

        backtrack(endWord, [endWord])
        return result


if __name__ == "__main__":
    solution = Solution()

    print("---- Test Case 1: Basic Example ----")
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected:
    # [
    #   ["hit","hot","dot","dog","cog"],
    #   ["hit","hot","lot","log","cog"]
    # ]

    print("---- Test Case 2: No endWord in list ----")
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected: []

    print("---- Test Case 3: beginWord one step away ----")
    beginWord = "aab"
    endWord = "abb"
    wordList = ["abb","aab","aba","aaa"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected:
    # [["aab","abb"]]

    print("---- Test Case 4: Multiple branching but only shortest returned ----")
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted","tex","red","tax","tad","den","rex"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected:
    # [
    #   ["red","ted","tad","tax"],
    #   ["red","rex","tex","tax"]
    # ]

    print("---- Test Case 5: No possible path even though endWord exists ----")
    beginWord = "aaa"
    endWord = "bbb"
    wordList = ["aac","bbc","aba","abb","baa","bbb"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected: []

    print("---- Test Case 6: Single-character words ----")
    beginWord = "a"
    endWord = "c"
    wordList = ["a","b","c"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected:
    # [["a","c"]]

    print("---- Test Case 7: Word list contains beginWord already ----")
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hit","hot","dot","dog","lot","log","cog"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected: same as Test Case 1

    print("---- Test Case 8: Path exists but longer paths must be excluded ----")
    beginWord = "aaa"
    endWord = "bbb"
    wordList = ["aab","abb","bbb","aba","baa"]
    result = solution.findLadders(beginWord, endWord, wordList)
    print(result)
    # Expected:
    # [["aaa","aab","abb","bbb"]]