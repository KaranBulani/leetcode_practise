'''
⏱️ Time & Space Complexity

Time
* Trie build: O(sum(len(words)))
                +
* DFS: O(m × n × 3^L) worst case #
    3^L because only at 1st char we can go 4 direction, but for rest its 3 per char
  (practically much less due to pruning)

Space
* Trie: O(sum(len(words)))
             +
* DFS recursion stack: O(L)
             +
* Board reused (in-place marking)
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()

        for w in words:
            node = self.root
            for char in w:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = w

        res = []
        rows, cols = len(board), len(board[0])

        def backtrack(x: int, y: int, node: TrieNode):
            # at any point if word matches we add word to res, but there maybe more char pending hence we dont return
            if node.word:
                res.append(node.word)
                node.word = None

            tmp = board[x][y]
            board[x][y] = '$'

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] in node.children and board[nx][ny] != '$':
                    backtrack(nx, ny, node.children[board[nx][ny]])

            board[x][y] = tmp

        for r in range(rows):
            for c in range(cols):
                # start backtracking only if starting character matches
                if board[r][c] in self.root.children:
                    backtrack(r, c, self.root.children[board[r][c]])

        return res

if __name__ == "__main__":
    solution = Solution()

    # -------------------------------
    # Example 0 (from problem)
    # -------------------------------
    board0 = [["a"]]

    words0 = ["a"]
    result1 = solution.findWords(board0, words0)
    print("Test 0 Output:", result1)
    # Expected: should return exactly the valid words present on board (order doesn't matter)

    # -------------------------------
    # Example 1 (from problem)
    # -------------------------------
    board1 = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    result1 = solution.findWords(board1, words1)
    print("Test 1 Output:", result1)
    # Expected: should return exactly the valid words present on board (order doesn't matter)

    # -------------------------------
    # Example 2 (from problem)
    # -------------------------------
    board2 = [
        ["a", "b"],
        ["c", "d"]
    ]
    words2 = ["abcb"]
    result2 = solution.findWords(board2, words2)
    print("Test 2 Output:", result2)
    # Expected: should return empty list

    # -------------------------------
    # Edge Case 1: Single cell board
    # -------------------------------
    board3 = [["a"]]
    words3 = ["a", "b"]
    result3 = solution.findWords(board3, words3)
    print("Test 3 Output:", result3)
    # Expected: should only return words that exactly match the cell

    # -------------------------------
    # Edge Case 2: Word longer than total cells
    # -------------------------------
    board4 = [
        ["a", "b"],
        ["c", "d"]
    ]
    words4 = ["abcdc"]
    result4 = solution.findWords(board4, words4)
    print("Test 4 Output:", result4)
    # Expected: should return empty list

    # -------------------------------
    # Edge Case 3: Reuse of same cell not allowed
    # -------------------------------
    board5 = [
        ["a", "a"]
    ]
    words5 = ["aaa"]
    result5 = solution.findWords(board5, words5)
    print("Test 5 Output:", result5)
    # Expected: should return empty list

    # -------------------------------
    # Edge Case 4: All cells same character
    # -------------------------------
    board6 = [
        ["a", "a"],
        ["a", "a"]
    ]
    words6 = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    result6 = solution.findWords(board6, words6)
    print("Test 6 Output:", result6)
    # Expected: should return all constructible words without reusing a cell

    # -------------------------------
    # Edge Case 5: No words
    # -------------------------------
    board7 = [
        ["a", "b"],
        ["c", "d"]
    ]
    words7 = []
    result7 = solution.findWords(board7, words7)
    print("Test 7 Output:", result7)
    # Expected: should return empty list
