'''
Time Complexity:  O(n)              (for Brute Force)
Space Complexity: O(1)              (for Variables, indexes)
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # remove leading/trailing spaces
        if not s:
            return False

        # Split into base and exponent
        if 'e' in s or 'E' in s:
            parts = s.lower().split('e')
            if len(parts) != 2:
                return False
            base, exp = parts
            return self.isDecimal(base) and self.isInteger(exp)
        else:
            return self.isDecimal(s)

    def isInteger(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        return s.isdigit() and len(s) > 0

    def isDecimal(self, s: str) -> bool:
        if not s:
            return False
        if s[0] in ['+', '-']:
            s = s[1:]
        if '.' not in s:
            return s.isdigit() and len(s) > 0

        left, right = s.split('.', 1)

        # At least one digit somewhere
        if left == '' and right == '':
            return False
        if left != '' and not left.isdigit():
            return False
        if right != '' and not right.isdigit():
            return False
        return True

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Valid numbers from question
        "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
        "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",

        # Invalid numbers from question
        "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53",

        # Extra tricky valid cases
        ".1", "3.", "+.8", "-.0", "0e0", "46.e3", ".5E+10",

        # Extra tricky invalid cases
        ".", "+", "-", "e", ".e1", "1e1.5", "1ee2", "e9", "1.2.3",
        "+.", "-.", "4e+", "4e-", "6e-+1", "++6", "  3  ",  # contains spaces
    ]

    for case in test_cases:
        result = solution.isNumber(case)
        print(f"Input: {repr(case)} --> Output: {result}")