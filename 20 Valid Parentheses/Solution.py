'''
Time Complexity: O(n) as we have to go through entire brackets
Space Complexity: O(n) as all brackets might be open brackets
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pair = { "(" : ")" , "[" : "]" , "{" : "}" }
        for bracket in s:
            if bracket in bracket_pair:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if bracket_pair[stack[-1]] == bracket:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
if __name__ == "__main__":
    solution = Solution()
    s = "({["
    s0 = "]"
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])"
    result = solution.isValid(s3)
    print(result)