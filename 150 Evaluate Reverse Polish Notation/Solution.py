'''
Time Complexity: O(n) As going through entire list
Space Complexity: O(n) due to stack. but each operand reduces the stack size. However, the space usage is still proportional to the length of the input, which is n.
'''

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(char))
        return stack[-1]

if __name__ == "__main__":
    solution = Solution()
    token1 = ["2","1","+","3","*"] #9
    token2 = ["4","13","5","/","+"] #6
    token3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] #22
    result = solution.evalRPN(token3)
    print(result)