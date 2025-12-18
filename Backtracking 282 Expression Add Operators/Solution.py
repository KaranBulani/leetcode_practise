'''
Time complexity:    O( 3^(n-1) * 2^(n-1) )     ≈    O(6^n)

1️⃣ Number of ways to split digits
Each digit can either:
    start a new number, or    be appended to the existing number
So there are 2 choices per digit, except the first.
Total ways to split digits into numbers:    ≈ 2^(n-1)

2️⃣ For each split, we choose operators
If the digit string splits into k numbers, then there are:      k − 1 operator positions
Each can be +, -, or *.
So operators contribute a factor of:        3^(k-1)
Worst-case, k = n (each digit is a separate operand).
So in worst case:       operator choices = 3^(n-1)


Space complexity:         O(n)

1️⃣ Recursive call stack depth
Depth at most n, since you process one digit at a time.         O(n)

2️⃣ Expression string building
Expression length is at most:
    digits = n
    operators = n-1
So expression length:           O(n)
You may store up to O(6^n) results, but in algorithmic space complexity we exclude output.
'''
class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res = []

        def dfs(start: int, curr_val: int, prev: int, expr: str):
            if start >= len(num):
                if curr_val == target:
                    res.append(expr)
                return

            for end in range(start, len(num)):
                # avoid leading zero numbers, but keep only "0"
                if num[start] == "0" and end > start:
                    break

                number = int(num[start:end+1])
                s = str(number)

                if start == 0:
                    dfs(end+1, number, number, s)
                else:
                    dfs(end+1, (curr_val - prev) + (prev * number), prev * number, expr + "*" + s)
                    dfs(end+1, curr_val + number, number, expr + "+" + s)
                    dfs(end+1, curr_val - number, -number, expr + "-" + s)

        dfs(0, 0, 0, "")
        return res

if __name__ == "__main__":
    solution = Solution()

    print("\n===== BASIC PROVIDED EXAMPLES =====")
    tests = [
        ("123", 6),  # Example 1
        ("232", 8),  # Example 2
        ("3456237490", 9191),  # Example 3
    ]
    for num, target in tests:
        print(f"\nInput: num={num}, target={target}")
        result = solution.addOperators(num, target)
        print("Output:", result)

    print("\n===== EDGE CASES =====")

    # 1. Single digit
    num, target = "5", 5
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 2. Single digit but target different
    num, target = "5", 7
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 3. Leading zero — only "0" itself is valid as a multi-digit operand is invalid if it starts with 0
    num, target = "105", 5
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 4. All zeros — many combinations possible but operands cannot have leading zeros
    num, target = "000", 0
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 5. Larger target with multi-digit numbers
    num, target = "1234", 10
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 6. Impossible target
    num, target = "999", 1
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 7. Negative target
    num, target = "123", -4
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 8. Long input but small target
    num, target = "123456789", 45
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 9. Multiple valid expressions expected
    num, target = "222", 6
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))

    # 10. Case where multiplication priority matters
    num, target = "2323", 15
    print(f"\nInput: num={num}, target={target}")
    print("Output:", solution.addOperators(num, target))