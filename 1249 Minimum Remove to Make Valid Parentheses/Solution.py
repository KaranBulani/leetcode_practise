'''
Time Complexity: O(n) (go through)
Space Complexity: O(n) for stack
'''

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
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