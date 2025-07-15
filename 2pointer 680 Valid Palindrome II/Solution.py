'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    # Check if substring is Palindrome
    def isPalindrome(self, sub_s: str) -> bool:
        L, R = 0, len(sub_s) - 1
        while L < R:
            if sub_s[L] != sub_s[R]:
                return False
            L += 1
            R -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            # If something doesnt match that means one of substring (skipL, shipR) should be Palindrome else return False
            if s[L] != s[R]:
                skipL = s[L+1: R+1] #Skip L, Include R
                skipR = s[L:R] #Include L, Skip R
                return self.isPalindrome(skipL) or self.isPalindrome(skipR)
            L += 1
            R -= 1
        # Means whole str is Palindrome
        return True

if __name__ == "__main__":
    solution = Solution()

    # List of (input_string, expected_result)
    test_cases = [
        # LeetCode examples
        ("aba", True),
        ("abca", True),  # delete 'c'
        ("abc", False),
        # Edge cases
        ("a", True),  # single character
        ("aa", True),  # already palindrome
        ("ab", True),  # delete either 'a' or 'b'
        ("racecar", True),  # longer palindrome
        ("deeee", True),  # delete one of the front 'e's
        ("cbbcc", True),  # multiple same letters
        # Fails only if more than one deletion needed
        ("abcdba", False),  # needs two deletions
        ("abecbea", False),
        # Very long palindrome with one extra char in the middle
        ("a" * 50000 + "b" + "a" * 50000, True),
        # Same but two mismatches
        ("a" * 50000 + "bc" + "a" * 50000, False)
    ]

    for s, expected in test_cases:
        result = solution.validPalindrome(s)
        print(f"Input: {s[:10]}{'...' if len(s) > 10 else ''} (len={len(s)}) -> {result} (expected: {expected})")