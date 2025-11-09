'''
Diagram: https://leetcode.com/problems/palindrome-partitioning/description/comments/2320577/

Time complexity:  O(n * 2^n)                                2^n states if all str same then all subset is palindrome
                                                            n for palindrome check

Space complexity: O(n) recursion + O(n * 2^n) result        n for recursion stack depth

                                                            You might generate up to 2ⁿ partitions
                                                            Each partition can store up to n substrings
'''
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def dfs(start: int):
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res

    def isPalindrome(self, s, l, r) -> bool:
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

if __name__ == "__main__":
    solution = Solution()

    # Example 1: From the problem statement
    s1 = "aab"
    result1 = solution.partition(s1)
    print("Input:", s1)
    print("Output:", result1)
    # Expected: [["a","a","b"], ["aa","b"]]

    # Example 2: Single character string
    s2 = "a"
    result2 = solution.partition(s2)
    print("\nInput:", s2)
    print("Output:", result2)
    # Expected: [["a"]]

    # Edge Case 1: All characters same
    s3 = "aaa"
    result3 = solution.partition(s3)
    print("\nInput:", s3)
    print("Output:", result3)
    # Expected: [["a","a","a"], ["aa","a"], ["a","aa"], ["aaa"]]

    # Edge Case 2: No palindromic combinations except single chars
    s4 = "abc"
    result4 = solution.partition(s4)
    print("\nInput:", s4)
    print("Output:", result4)
    # Expected: [["a","b","c"]]

    # Edge Case 3: Palindrome as whole string
    s5 = "aba"
    result5 = solution.partition(s5)
    print("\nInput:", s5)
    print("Output:", result5)
    # Expected: [["a","b","a"], ["aba"]]

    # Edge Case 4: Longer mix of palindromic and non-palindromic parts
    s6 = "aabb"
    result6 = solution.partition(s6)
    print("\nInput:", s6)
    print("Output:", result6)
    # Expected: [["a","a","b","b"], ["aa","b","b"], ["a","a","bb"], ["aa","bb"]]