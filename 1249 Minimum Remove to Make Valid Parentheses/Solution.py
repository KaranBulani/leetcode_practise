'''
Time Complexity: O(n) (go through)
Space Complexity: O(n) for stack
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Convert the string to a list of characters so we can modify it in-place
        s = list(s)

        # Stack will hold indices of unmatched '(' characters
        stack = []

        # First pass: iterate through characters and mark invalid ')' for removal
        for i, char in enumerate(s):
            if char == '(':
                # Record the index of every '(' we see
                stack.append(i)
            elif char == ')':
                if stack:
                    # There is a matching '(' available, so pair them by popping
                    stack.pop()
                else:
                    # No matching '(', so this ')' is invalid—mark it as empty
                    s[i] = ''

        # After the pass, any indices left in stack are '(' without matches
        # Remove all those unmatched '('
        while stack:
            unmatched_index = stack.pop()
            s[unmatched_index] = ''

        # Reconstruct the string, skipping over empty slots
        return ''.join(s)

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "lee(t(c)o)de)",
        "a)b(c)d",
        "))(("
    ]

    for s in test_cases:
        result = solution.minRemoveToMakeValid(s)
        print(f"Input: {s!r}  →  Output: {result!r}")