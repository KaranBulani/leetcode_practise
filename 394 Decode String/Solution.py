'''
Time complexity: O(n) for going through decoded string
                 No time complexity for multiplication etc

Space complexity: O(n) for stack
                  not count result as a space

I missed:
1. After extracting the substring, don’t forget to pop the [ with stack.pop().
2. While identifying substr I was trying to reverse like:
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                substr = ''.join(reversed(temp))
    I could've just done this:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
3. Always check the stack isn’t empty before peeking (e.g. while stack and stack[-1].isdigit(): …).
4. Call .isdigit() on the string itself—no need to wrap with int(): int(stack[-1]).isdigit()
5. The final result should be the join of the entire stack, not just the top value:
       result = "".join(stack)
   Top Value works for inputs like 3[a2[c]], but joining handles cases like 3[a]2[c].
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    input1 = "3[a]2[bc]"
    result1 = solution.decodeString(input1)
    print(result1)  # Expected: "aaabcbc"

    # Example 2
    input2 = "3[a2[c]]"
    result2 = solution.decodeString(input2)
    print(result2)  # Expected: "accaccacc"

    # Example 3
    input3 = "2[abc]3[cd]ef"
    result3 = solution.decodeString(input3)
    print(result3)  # Expected: "abcabccdcdcdef"