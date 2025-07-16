'''
#### Recurrence Relation:
Let T(n) represent the number of operations (recursive calls) required for n pairs of parentheses.
- When n = 0, no operations are needed, so ( T(0) = 1 ) (base case).
- For any other n, we can add either an open or close parenthesis, and both cases will lead to further recursive calls until we reach the base case where all parentheses are balanced.

Thus, the recurrence can be expressed as:
T(n) = 2T(n-1) + O(1)

This is because, for each level of recursion, we can branch in two ways: add an open or a close parenthesis.

### Solving the Recurrence:

The recurrence relation ( T(n) = 2T(n-1) + O(1) ) is similar to the classic binary tree recursion where the number of calls doubles at each level. Here's how to solve it:

- At level 0 (the root of the recursion tree), we have 1 recursive call.
- At level 1, we have 2 recursive calls.
- At level 2, we have 4 recursive calls.
- In general, at level ( i ), we have ( 2^i ) recursive calls.

The recursion continues until we have 2n levels, since the depth of the recursion is proportional to the total number of open and close parentheses, i.e., ( 2n ).

Thus, the total number of recursive calls can be approximated as:
T(n) approx 2^0 + 2^1 + 2^2 + .... + 2^{2n}

The sum of this geometric series is approximately ( 2^{2n+1} - 1 ), which simplifies to ( O(2^{2n}) ).

### Time Complexity:
Given that ( T(n) = O(2^{2n}) ), and since generating parentheses corresponds to exploring all possible combinations, we can approximate the time complexity as:
O(2^{2n}) = O(4^n)

This matches the previous explanation that the number of valid parentheses is proportional to the Catalan number, which grows as ( O(4^n / sqrt{n}) ).

### Space Complexity:
- Recursive call stack: The recursion depth is at most 2n, so the space complexity due to the call stack is O(n).
- Result storage: The list res stores all valid combinations, which is O(4^n) in size.

Thus, the overall space complexity is:
O(4^n)

### Conclusion:
- Time complexity: O(4^n)
- Space complexity: O(4^n)


Another Way To Solve

def generateParenthesis(self, n):
    stack, res = [], []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        s, res = "", []
        def backtrack(s: str, open: int, close: int) -> None:
            if open == close == n:
                res.append(s)
                return
            if open < n:
                backtrack(s + "(", open + 1, close)
            if close < open:
                backtrack(s + ")", open, close + 1)
        backtrack(s,0,0)
        return res

if __name__ == "__main__":
    solution = Solution()
    n1 = 1
    n2 = 2
    n3 = 3
    result = solution.generateParenthesis(n3)
    print(result)