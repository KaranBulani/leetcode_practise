'''

✅ 1. Brute Force (Time: O(n³), TLE on large cases)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2: return 0
        max_len = 0
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n, 2):  # Only even-length substrings can be valid
                if self.is_valid(s[i: j+1]): # We want to include jth index in list slicing
                    max_len = max(max_len, j - i + 1) # Off by 1 error which happens in 2 pointer
        return max_len

    def is_valid(self, sub):
        stack = []
        for char in sub:
            if char == '(':
                stack.append(char)
            elif stack:
                stack.pop()
            else:
                return False
        return not stack

####################################################################################################

✅ 2. Stack-Based Approach (Time: O(n), Space: O(n))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1] # Use a stack of indices, starting with –1 as the base.

        maxLen = 0
        for i, char in enumerate(s):
            if char == "(":
                # Push the '(' index onto the stack as the new base
                # This i as a base won't be considered if it gets popped(). Then Prev base would be considered.
                # Only considered as base when it doesn't get popped and future brackets are popped.
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # means ) more than (, which is bad, create a new base

                    # If stack is empty after popping, no base to compute valid length
                    # So push current index as the new base
                    stack.append(i)
                else:
                    # means valid pop happened, calculate len from base to current len
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen

####################################################################################################


✅ 3. Two-Pass Counters (Time: O(n), Space: O(1))
'''

class Solution:
    def longestValidParentheses(s: str) -> int:
        left = right = max_len = 0

        # Left to right
        # We count the number of '(' and ')' brackets using two counters: left and right.
        # Whenever left == right, we've found a valid substring.
        # If right > left (too many ')'), then reset both counters—it's invalid now.

        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right to left
        # But if we only go left to right, it misses some cases like `(()` (which is valid from the end).
        # So we also do right to left pass to catch such cases.

        left = right = 0
        for char in reversed(s): #Reversed is important
            if char == ')':
                right += 1
            else:
                left += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len


if __name__ == "__main__":
    sol = Solution()

    # List of test cases: (input_string, expected_output)
    test_cases = [
        # Examples from the problem statement
        ("(()", 2),            # simple unbalanced left
        (")()())", 4),        # alternating valid/invalid
        ("", 0),               # empty string

        # Additional edge cases
        ("()", 2),            # single valid pair
        ("((((((", 0),         # all opens, no closes
        ("))))))", 0),         # all closes, no opens
        ("()()()", 6),        # multiple adjacent pairs
        ("((()))", 6),        # nested valid
        ("())(())", 4),       # two valid segments separated by invalid
        ("(()(((()", 2),      # one small valid in larger invalid
        ("())()((()))", 8),   # mixed segments, largest nested at end
        # long edge cases
        ("(" * 15000 + ")" * 15000, 30000),  # long balanced
        ("(" * 15000 + ")" * 14999, 29998),  # long nearly balanced
    ]

    for idx, (s, expected) in enumerate(test_cases, 1):
        result = sol.longestValidParentheses(s)
        print(f"Case {idx}: Input: {repr(s[:30] + '...' if len(s) > 30 else s)} | Expected: {expected} | Got: {result}")