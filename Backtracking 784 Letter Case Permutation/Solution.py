'''
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = [""]

        for ch in s:
            if ch.isalpha():
                # For each current result, append both lower and upper case versions
                res = [prefix + new_ch for prefix in res for new_ch in [ch.lower(), ch.upper()]]
            else:
                # For digits, just append as is
                res = [prefix + ch for prefix in res]

        return res

Time complexity:  O(2^n) 					each letter can branch into 2 possibilities
Space complexity: O(2^n) 					for recursion + result storage
'''
class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return

            if s[i].isalpha():
                backtrack(i + 1, path + s[i].lower())
                backtrack(i + 1, path + s[i].upper())
            else:
                backtrack(i + 1, path + s[i])

        backtrack(0, "")
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example 1 (from question)
    s = "a1b2"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["a1b2","a1B2","A1b2","A1B2"]

    # Example 2 (from question)
    s = "3z4"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["3z4","3Z4"]

    # Edge Case 1: All digits (no letter permutations)
    s = "1234"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["1234"]

    # Edge Case 2: Single lowercase letter
    s = "a"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["a","A"]

    # Edge Case 3: Single uppercase letter
    s = "Z"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["z","Z"]

    # Edge Case 4: Mix of letters and digits, upper + lower
    s = "mN9"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output: {result}")  # Expected: ["mn9","mN9","Mn9","MN9"]

    # Edge Case 5: Longest valid length (stress test)
    s = "a1b2c3d4e5f"
    result = solution.letterCasePermutation(s)
    print(f"Input: {s} -> Output size: {len(result)}")  # Just checking count to avoid printing all