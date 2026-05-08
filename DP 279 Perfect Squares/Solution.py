'''

1. Observation
Read the problem statement
We need to return the minimum number of perfect squares whose sum equals n.

Examples:
* 12 = 4 + 4 + 4 → answer = 3
* 13 = 4 + 9 → answer = 2

A perfect square is:
1, 4, 9, 16, 25, ...

Identify key observations

For every number n, we can try:
* subtracting 1²
* subtracting 2²
* subtracting 3²
* ...
* subtracting every square <= n
Then solve the remaining smaller problem.

Example for 12:
* choose 1 → solve 11
* choose 4 → solve 8
* choose 9 → solve 3
We want the minimum among all choices.

Core Idea
This is a minimum choices problem.
The remaining problem after choosing a square has the same structure:
> "minimum perfect squares needed to make remaining value"

That strongly suggests:
* Recursion
* Dynamic Programming
####################################################################################################
2. Simulation

Take:
n = 12

Possible first choices:
| Square Chosen | Remaining | Total Count   |
| ------------- | --------- | ------------- |
| 1             | 11        | 1 + solve(11) |
| 4             | 8         | 1 + solve(8)  |
| 9             | 3         | 1 + solve(3)  |

So:
solve(12) = 1 + min(solve(11), solve(8), solve(3))

Now: solve(8)

Choices:
| Square Chosen | Remaining |
| ------------- | --------- |
| 1             | 7         |
| 4             | 4         |

solve(8) = 1+ min(solve(7), solve(4))

Eventually: solve(4)=1
because 4 itself is a perfect square.

Generalization

For every number remaining:

Try every square:
square = i^2

such that:
square <= remaining

Then:
solve(remaining)= 1 + min(solve(remaining-square))
####################################################################################################
3. Recursion

Define:
solve(remaining) = minimum perfect squares needed to form remaining.

Base Case

If:
	remaining = 0

then no numbers are needed.

	solve(0)=0

Recurrence Relation

For every square:
	square = i^2
	solve(remaining) = 1 + min(solve(remaining-square))
####################################################################################################
4. Dynamic Programming

Why DP?
Many states repeat.

Example:
* solve(8) can be reached from multiple paths
* solve(4) can be computed repeatedly
So we cache results.

State - remaining

Transition
	dp[remaining] = 1+ min(dp[remaining-square])

for every perfect square:
	square <= remaining

Complexity

Number of states: n

For each state, we try: sqrt{n} perfect squares.

So: O(n * sqrt{n})

DP Formula

Inline recurrence:
dp[x] = 1 + min(dp[x-i^2])

####################################################################################################
Bottom-Up DP Solution

class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            square = 1

            while square * square <= target:
                perfect_square = square * square
                dp[target] = min(
                    dp[target],
                    1 + dp[target - perfect_square]
                )
                square += 1

        return dp[n]
####################################################################################################
Complexity Analysis

Time Complexity O(n * sqrt{n})
Space Complexity O(n)
####################################################################################################
Top-Down Memoization Solution

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def minSquares(remaining):
            if remaining == 0:
                return 0
            if remaining in memo:
                return memo[remaining]

            answer = float('inf')

            square = 1

            while square * square <= remaining:
                perfect_square = square * square
                answer = min(
                    answer,
                    1 + minSquares(remaining - perfect_square)
                )
                square += 1

            memo[remaining] = answer
            return answer

        return minSquares(n)
'''
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            square = 1

            while square * square <= target:
                perfect_square = square * square
                dp[target] = min(
                    dp[target],
                    1 + dp[target - perfect_square]
                )
                square += 1

        return dp[n]

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        (1, 1),
        (12, 3),
        (13, 2),

        # Smallest input
        (1, 1),

        # Perfect squares
        (4, 1),
        (9, 1),
        (16, 1),
        (100, 1),

        # Requires multiple squares
        (2, 2),  # 1 + 1
        (3, 3),  # 1 + 1 + 1
        (5, 2),  # 4 + 1
        (6, 3),  # 4 + 1 + 1
        (7, 4),  # 4 + 1 + 1 + 1
        (8, 2),  # 4 + 4
        (10, 2),  # 9 + 1
        (11, 3),  # 9 + 1 + 1
        (17, 2),  # 16 + 1
        (18, 2),  # 9 + 9
        (19, 3),  # 9 + 9 + 1
        (23, 4),
        (24, 3),
        (25, 1),  # perfect square
        (26, 2),  # 25 + 1
        (27, 3),  # 9 + 9 + 9
        (28, 4),

        # Larger cases
        (43, 3),
        (50, 2),  # 25 + 25
        (99, 3),
        (999, 4),
        (1000, 2),  # 30^2 + 10^2
        (9999, 4),

        # Constraint upper bound
        (10000, 1),  # 100^2
    ]

    for n, expected in test_cases:
        result = solution.numSquares(n)

        status = "PASS" if result == expected else "FAIL"

        print(
            f"n = {n:<5} | Expected = {expected:<2} | "
            f"Got = {result:<2} | {status}"
        )