'''
Time complexity:
T(n) = 6 × n(n−1)/2 = 3n(n−1) * T(n-1)

Picking 2 numbers from n numbers --> (n * (n−1)) / 2
    This is implemented for n = 4,3,2 and values are 6, 3, 1

For each pair we implement 6 operation +, -, *, /, Rev -, Rev / -->
 --> 6 × 6 × 6 × 3 × 6 × 1

Space complexity: O(n)		recursion stack

'''
class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        if len(cards) == 1:
            EPS = 1e-6
            return abs(cards[0] - 24.0) < EPS

        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                x = cards[i]
                y = cards[j]

                # operations
                ops = []
                ops.append(x + y)
                ops.append(x * y)
                ops.append(x - y)
                ops.append(y - x)

                if y != 0:
                    ops.append(x / y)
                if x != 0:
                    ops.append(y / x)

                # build rest list
                rest = []
                for k in range(len(cards)):
                    if k != i and k != j:
                        rest.append(cards[k])

                # try adding each result
                for val in ops:
                    rest.append(val)
                    if self.judgePoint24(rest):  # IMPORTANT: if any path True, stop early
                        return True
                    rest.pop()

        # if nothing worked
        return False


# Paste this below your Solution class (which must implement judgePoint24(self, cards: List[int]) -> bool)
if __name__ == "__main__":
    from typing import List

    solution = Solution()

    # test cases (diverse + edge cases) and their expected outputs
    tests: List[List[int]] = [
        [4, 1, 8, 7],  # example 1 (given) -> True
        [1, 2, 1, 2],  # example 2 (given) -> False
        [1, 1, 1, 1],  # all ones -> False
        [1, 3, 4, 6],  # classic solvable case -> True (6 / (1 - 3/4) = 24)
        [2, 2, 2, 2],  # all twos -> False
        [3, 3, 8, 8],  # tricky but solvable -> True
        [5, 2, 7, 8],  # solvable -> True
        [9, 1, 1, 1],  # typically not solvable -> False
        # Order-invariance checks (same numbers different order)
        [8, 7, 4, 1],  # permutation of example 1 -> True
        [6, 1, 3, 4],  # permutation of [1,3,4,6] -> True
    ]

    # expected answers for the tests above (as booleans)
    expected = [
        True,  # [4,1,8,7]
        False,  # [1,2,1,2]
        False,  # [1,1,1,1]
        True,  # [1,3,4,6]
        False,  # [2,2,2,2]
        True,  # [3,3,8,8]
        True,  # [5,2,7,8]
        False,  # [9,1,1,1]
        True,  # [8,7,4,1]
        True,  # [6,1,3,4]
    ]

    # run tests and print results
    all_passed = True
    for i, case in enumerate(tests):
        try:
            result = solution.judgePoint24(case)
        except Exception as e:
            print(f"Test {i + 1}: input={case} -> RAISED EXCEPTION: {e!r}")
            all_passed = False
            continue

        ok = (result == expected[i])
        status = "PASS" if ok else "FAIL"
        print(f"Test {i + 1}: input={case}, expected={expected[i]}, got={result} -> {status}")
        if not ok:
            all_passed = False

    if all_passed:
        print("\nAll tests passed (actual results matched expected values).")
    else:
        print("\nSome tests failed — check the outputs above and debug accordingly.")