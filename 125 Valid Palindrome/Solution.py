'''
Can create isalnum() function like this:
    def isalnum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))

Time Complexity: O(n/1) (go through)
Space Complexity: O(1) for L, R
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        condition =  True
        L, R = 0, len(s) - 1
        while condition and L <= R:
            if s[L].isalnum() and s[R].isalnum() and s[L].lower() != s[R].lower():
                condition =  False
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            else:
                L += 1
                R -= 1
        return condition

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # Examples from the problem statement
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        # Additional edge cases
        (".,", True),  # only punctuation
        ("a.", True),  # single alphanumeric with punctuation
        ("0P", False),  # mixed alphanumeric non-palindrome
        ("No 'x' in Nixon", True),  # mixed case with spaces/punctuation
        ("12321", True),  # numeric palindrome
        ("1231", False),  # numeric non-palindrome
        ("Able was I, ere I saw Elba!", True),  # well‑known palindrome phrase
    ]

    for s, expected in test_cases:
        result = solution.isPalindrome(s)
        print(f"Input:    {s!r}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print("-" * 40)
