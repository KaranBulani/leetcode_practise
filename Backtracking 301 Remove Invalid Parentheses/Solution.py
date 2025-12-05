'''
s = ( ) ( ) ) ( )
    0 1 2 3 4 5 6  (indices)

remL = 0
remR = 1 (only one ')' is invalid)

                            "" (i=0)
                                |
                            keep '('
                                |
                         "(" (bal=1)
                               |
                   -----------------------
                   |                     |
               skip ')'               keep ')'
               remR->0                bal->0
                   |                     |
              "(“ (bal=1)             "()" (bal=0)
                   |                     |
                 keep '('             keep '('
                   |                     |
              "((“ (bal=2)         "()(" (bal=1)
                   |                     |
              keep ')‘             -------------
                   |               |           |
              "(()" (1)      skip ')'       keep ')' (bal=0)
                   |            |                 |
              keep ')'       "()(" (1)          "()()" (0)
                   |            |                 |
             "(())" (0)       keep ')‘       skip only allowed
                   |            |                 |
            keep '(' (1)    "()(“ (0)         "()()" (0)
                   |            |                 |
            "(())(" (1)    keep '(' (1)      keep '('
                   |            |                 |
            keep ')' (0)  "()((" (1)         "()()(" (1)
                   |            |                 |
           "(())()" VALID   keep ')' (0)     keep ')' (0)
                               |                 |
                           "()()()" VALID   "()()()" VALID


Time complexity:    O(2^n)
    In the worst case, how many choices do you have for each character?
    A letter → 1 choice
    A parenthesis → up to 2 choices (keep or skip)
    So if every character is a parenthesis, each char gives 2 branches.

Space complexity:	O(n + number of results which is 2^n if all are brackets)
                    for Recursion Depth + recursion stack
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        remL, remR, openCount = 0, 0, 0
        for c in s:
            if c == '(':
                openCount += 1
            elif c == ")":
                if openCount > 0:
                    openCount -= 1
                else:
                    remR += 1
        remL = openCount

        self.res = set()
        def dfs(i: int, curr_str: str, balance: int, remL: int, remR: int):
            if balance < 0:
                return

            if i == len(s):
                if balance == 0 and remL == 0 and remR == 0:
                    self.res.add(curr_str)
                return

            # If it's a letter, always include
            if s[i].isalpha():
                dfs(i+1, curr_str + s[i], balance, remL, remR)
                return
            else:
                if s[i] == '(':
                    # Option 1: skip '('
                    if remL > 0:
                        dfs(i+1, curr_str, balance, remL - 1, remR)
                    # Option 2: keep '('
                    dfs(i+1, curr_str + s[i], balance + 1, remL, remR)
                    return
                elif s[i] == ')':
                    if remR > 0:
                        dfs(i+1, curr_str, balance, remL, remR - 1)
                    if balance > 0:
                        dfs(i+1, curr_str + s[i], balance - 1, remL, remR)
                    return

        dfs(0, '', 0, remL, remR)
        return list(self.res)

if __name__ == "__main__":
    # Replace DummySolution() with Solution() after you paste your Solution class in this file
    solution = Solution()

    # Test cases: a mix of examples from the prompt and extra edge-cases.
    # The expected values are provided as sets (order doesn't matter) so the harness compares sets.
    tests = [
        # Examples from the problem statement
        ("()())()", {"(())()", "()()()"}),
        ("(a)())()", {"(a())()", "(a)()()"}),
        (")(", {""}),

        # Extra edge cases
        ("", {""}),                 # empty string
        ("abc", {"abc"}),           # no parentheses
        ("(((", {""}),              # only opens -> must remove all
        (")))", {""}),              # only closes -> must remove all
        ("())", {"()"}),            # simple single removal
        ("(a)()", {"(a)()"}),       # already valid with letters
        ("(())", {"(())"}),         # already valid nested
    ]

    all_passed = True
    for idx, (inp, expected_set) in enumerate(tests, 1):
        try:
            actual = solution.removeInvalidParentheses(inp)
        except Exception as e:
            print(f"Test {idx}: input={inp!r} -> Exception while running solution: {e}")
            all_passed = False
            continue

        # Normalize results to sets because LeetCode accepts any order, and result must be unique
        actual_set = set(actual) if actual is not None else set()

        passed = actual_set == expected_set
        status = "PASS" if passed else "FAIL"
        print(f"Test {idx}: input={inp!r}\n  Expected (set) = {expected_set}\n  Actual   (set) = {actual_set}\n  Result = {status}\n")
        if not passed:
            all_passed = False

    if all_passed:
        print("All tests passed (according to the provided expected outputs).")
    else:
        print("Some tests failed — check the printed diffs above.")

    # Tip: If your implementation returns more valid strings than expected here, consider whether
    # the extra strings are actually valid and created with the same minimum removals. The harness
    # uses a strict equality check against the expected sets above.
