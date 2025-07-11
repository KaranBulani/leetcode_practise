'''
Time Complexity: O(n) (go through)
Space Complexity: O(n) for stack
'''

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Stack to hold either '(' markers or integer scores
        stack = []

        # Iterate through each character in the input string
        for char in s:
            if char == '(':
                # Push a marker for an opening parenthesis
                stack.append('(')
            else:
                # We've encountered a closing parenthesis ')'
                if stack and stack[-1] == '(':
                    # Direct "()" pair: pop the '(' and push score 1
                    stack.pop()
                    stack.append(1)
                else:
                    # We're closing a group: sum all inner scores until '('
                    inner_score = 0
                    # Pop and accumulate numbers
                    while stack and isinstance(stack[-1], int): #or str(stack[-1]).isdigit()
                        inner_score += stack.pop()
                    # Pop the matching '('
                    stack.pop()
                    # Score for "(A)" is 2 * A
                    stack.append(2 * inner_score)

        # At the end, the stack contains only integer scores;
        # the total score is their sum.
        # sum() function calculates the total of all numeric elements in an iterable, such as a list, tuple, or set.
        return sum(stack)

if __name__ == "__main__":
    # Instantiate the Solution
    solution = Solution()

    # Test cases from the prompt
    test_cases = [
        "()",      # Expected output: 1
        "(())",    # Expected output: 2
        "()()",    # Expected output: 2
        # Add more diverse examples here:
        "((()()))",  # e.g., complex nested Expected output: 8
        "(()(()))"   # e.g., mixed structure Expected output: 6
    ]

    for s in test_cases:
        result = solution.scoreOfParentheses(s)
        print(f"Input: {s!r} -> Output: {result}")
