"""
Approach: Traverse from right to left (carry propagation).

Explanation

We need to add 1 to a number represented as an array of digits.
The key observation is that we only need to handle carry propagation.

Case 1: Last digit is less than 9

Example: [1, 2, 3]
- Start from the last digit.
- 3 + 1 = 4.
- No carry is required.
- Return [1, 2, 4].

Case 2: Last digit is 9

Example: [1, 2, 9]
- 9 + 1 = 10, so replace 9 with 0.
- Carry moves to the previous digit.
- 2 + 1 = 3.
- Return [1, 3, 0].

Case 3: All digits are 9

Example: [9, 9, 9]
- Every digit becomes 0.
- Carry propagates beyond the first digit.
- Add 1 at the beginning.
- Return [1, 0, 0, 0].

######################################################################################################################################################################
Dry Run

Input:
digits = [9, 9, 9]

| Index | Current digit | Operation | Array     |
| ----- | ------------- | --------- | --------- |
| 2     | 9             | Set to 0  | [9, 9, 0] |
| 1     | 9             | Set to 0  | [9, 0, 0] |
| 0     | 9             | Set to 0  | [0, 0, 0] |

Loop finishes, so:
    return [1] + digits

Output:
[1, 0, 0, 0]

######################################################################################################################################################################
Complexity Analysis

Let (n) be the length of digits.
| Complexity | Value        | Explanation                                |
| ---------- | ------------ | ------------------------------------------ |
| Time       |  O(n)        | In the worst case, we traverse all digits. |
| Space      |  O(1)        | No additional data structure is used.      |
The algorithm uses O(1) auxiliary space, excluding the output array created in the all-9s case.

######################################################################################################################################################################
Important Python Concepts

1. Reverse iteration

    range(len(digits) - 1, -1, -1)

This generates indices from the last index down to 0.

2. Why return immediately?

    if digits[i] < 9:
        digits[i] += 1
        return digits

If a digit is less than 9, incrementing it resolves the carry. There is no reason to continue processing earlier digits.

3. Why [1] + digits ?

When all digits are 9, the result needs one additional digit.

For example:
    [9, 9, 9]  ->  [0, 0, 0]
Adding 1 at the beginning produces:
    [1, 0, 0, 0]

Key takeaway: This is a simple example of carry propagation, similar to how addition works manually.
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):

            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from LeetCode
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9], [1, 0]),

        # Single digit cases
        ([0], [1]),
        ([1], [2]),
        ([8], [9]),

        # Carry propagation
        ([1, 2, 9], [1, 3, 0]),
        ([1, 9, 9], [2, 0, 0]),
        ([9, 9], [1, 0, 0]),
        ([9, 9, 9], [1, 0, 0, 0]),

        # Carry stops at different positions
        ([1, 2, 8, 9], [1, 2, 9, 0]),
        ([1, 9, 8, 9], [1, 9, 9, 0]),
        ([8, 9, 9, 9], [9, 0, 0, 0]),

        # Larger numbers
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 9, 0]),
        ([9, 9, 9, 9, 9, 9], [1, 0, 0, 0, 0, 0, 0]),

        # Maximum constraint length
        ([9] * 100, [1] + [0] * 100),
    ]

    for digits, expected in test_cases:
        result = solution.plusOne(digits)
        status = "PASS" if result == expected else "FAIL"

        print(f"Input:    {digits}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")
        print(f"Status:   {status}")
        print("-" * 60)