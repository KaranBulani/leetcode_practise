'''
####################################################################################################
                                            DP EXPLANATION
####################################################################################################
🧠 1. Observation

Problem in our words
We need to check:
> Can we split string s into valid words from wordDict?
* We can reuse words
* Order matters (substring-based)
* Exact segmentation required (no leftovers)

Key observations
* This is prefix-based decision making
* At any index i, we ask:
  > “Can I break the string starting from i?”
* If a word matches prefix → move forward
* Otherwise → try another word

Constraints insight
* s.length ≤ 300
* wordDict ≤ 1000
👉 Brute force recursion will TLE
👉 We must cache results → DP

####################################################################################################
🔍 2. Simulation

Example: s = "leetcode", wordDict = ["leet","code"]
Start at index 0:  "leet" matches → go to index 4
At index 4: "code" matches → go to index 8
Index 8 == len(s) → success ✅

Example 3 (failure case)
s = "catsandog"

"cats" → remaining "andog"
"and" → remaining "og" ❌

"cat" → remaining "sandog"
"sand" → remaining "og" ❌

👉 No valid path → FALSE

Generalization
Define: f(i) = can we segment s[i:]
Goal: f(0)

####################################################################################################
🔁 3. Recursion

Recurrence

For index i:
    f(i) = True if any word matches prefix AND f(i + len(word)) is True

Base case
    f(len(s)) = True   (we successfully segmented entire string)

Recursive logic
for each word in wordDict:
    if s[i:i+len(word)] == word and f(i + len(word)) == True:
        return True
return False

####################################################################################################
⚡ 4. Dynamic Programming (Memoization)

Why DP?
* Many overlapping states
* Same index computed repeatedly

State definition
dp[i] = True/False → can s[i:] be segmented

Transition
dp[i] = True if:
    any word matches AND dp[i + len(word)] is True

############################################ BOTTOM UP - DP ##########################################

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True   base case

        for i in range(n - 1, -1, -1):
            for word in word_set:
                if s.startswith(word, i) and dp[i + len(word)]:
                    dp[i] = True
                    break

        return dp[0]

############################################ TOP DOWN - DP ###########################################

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def canBreak(i):
            Base case
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            # Try all possible words
            for word in word_set:
                if s.startswith(word, i) and canBreak(i + len(word)):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return canBreak(0)

####################################################################################################
Time Complexity
* States: O(n)
* Work per state: O(len(wordDict) * word_length)
* Total: O(n * len(wordDict) * word_length)

Space Complexity:
* States: O(n)

####################################################################################################
                                                  TRIE
####################################################################################################
👉 Trie does NOT change the DP nature
👉 It optimizes word matching, not the core problem

🧠 1. Observation (Why Trie helps)

Current bottleneck in DP:
for word in wordDict:
    if s.startswith(word, i)

👉 This is expensive:
* You iterate over all words
* Then compare strings repeatedly

Key idea

Instead of: “Check all words at index i”

We do:
> “Start from index i and walk character by character in Trie”
👉 This avoids scanning all words every time

####################################################################################################
🔍 2. Simulation (Trie thinking)

Example:
s = "leetcode", wordDict = ["leet","code"]

Trie:
l → e → e → t (end)
c → o → d → e (end)

From index 0:
l → e → e → t ✅ (word found)
→ jump to index 4

From index 4:
c → o → d → e ✅
→ reach end

####################################################################################################
🔁 3. Recursion with Trie

Define:
f(i) = can break s[i:]

At each index:
* Traverse Trie starting from s[i]
* Whenever you hit a word → recurse

############################################ TOP DOWN - TRIE ###########################################

⚡ 4. Trie + Memoization (Optimal)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Build Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEnd = True

        memo = {}

        def dfs(i):
            # Base case
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            node = root

            # Try extending substring using Trie
            for j in range(i, len(s)):
                ch = s[j]

                if ch not in node.children:
                    break   # no further match possible

                node = node.children[ch]

                if node.isEnd and dfs(j + 1):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

############################################ BOTTOM UP - TRIE ###########################################

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Build Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEnd = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True   # base case

        # Fill DP from back
        for i in range(n - 1, -1, -1):
            node = root

            for j in range(i, n):
                ch = s[j]

                if ch not in node.children:
                    break

                node = node.children[ch]

                # Found a word
                if node.isEnd and dp[j + 1]:
                    dp[i] = True
                    break

        return dp[0]

####################################################################################################
⏱️ Time Complexity
* Each index processed once → O(n)
* Each traversal max length = 20 (constraint)

👉 O(n * max_word_length) ≈ O(n * 20)

Better than:
O(n * len(wordDict) * word_length)

Space

* Trie: O(total characters in wordDict)
* DP: O(n)

🧠 Mental Model
Without Trie:   i → try 1000 words ❌
With Trie:  i → follow only valid paths ✅

'''

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start: int):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start+1, min(len(s) + 1, start + 21)):
                if s[start:end] in wordSet and dfs(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(0)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ✅ Basic examples from problem
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),

        # ✅ Single character cases
        ("a", ["a"], True),
        ("a", ["b"], False),

        # ✅ Reuse of same word multiple times
        ("aaaaaaa", ["aaaa", "aaa"], True),

        # ❌ Almost valid but fails at end
        ("aaaaaaa", ["aaaa", "aa"], False),

        # ✅ Multiple segmentation options
        ("catsanddog", ["cats", "dog", "sand", "and", "cat"], True),

        # ❌ Prefix works but suffix doesn't
        ("abcd", ["a", "abc", "b", "cd"], True),  # valid: "a b cd"
        ("abcd", ["a", "abc", "b"], False),

        # ✅ Overlapping words
        ("cars", ["car", "ca", "rs"], True),

        # ❌ Long string edge
        ("a" * 50 + "b", ["a", "aa", "aaa", "aaaa"], False),

        # ✅ Large valid segmentation
        ("a" * 50, ["a", "aa", "aaa", "aaaa"], True),

        # ❌ Dictionary irrelevant
        ("hello", ["cat", "dog", "mouse"], False),

        # ✅ Exact match word
        ("apple", ["apple"], True),

        # ❌ Empty-like scenario (edge thinking)
        ("b", ["a", "aa", "aaa"], False),
    ]

    for i, (s, wordDict, expected) in enumerate(test_cases, 1):
        result = solution.wordBreak(s, wordDict)
        print(f"Test Case {i}:")
        print(f"Input: s = '{s}', wordDict = {wordDict}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"PASS: {result == expected}")
        print("-" * 50)