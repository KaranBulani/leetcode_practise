'''
####################################################################################################
                                            BOTTOM UP - DP
####################################################################################################
1. Observation

Read the problem statement

We need to count the number of different ways to completely tile a 2 × n board using:
* Dominoes (2 × 1) (vertical or horizontal)
* L-shaped Trominoes (all rotations allowed)

Since the answer can become very large, return it modulo 10⁹ + 7.
####################################################################################################

Identify key words and phrases
* Every square must be covered.
* Tiles cannot overlap.
* Rotations of trominoes are allowed.
* We need the count of all valid tilings.
* n ≤ 1000, so exponential recursion is impossible.
####################################################################################################

Define constraints
* Board height is fixed (2 rows).
* Width varies (n columns).
* Need an O(n) or O(n log n) solution.
####################################################################################################

Identify processing direction

Since we are filling the board from left to right, the natural direction is:
> Solve smaller boards first, then extend them to larger boards.
####################################################################################################

Core Observation

Suppose we already know the number of ways to tile smaller boards.
To build a 2 × n board, look only at how the last few columns are completed.
The final placement determines which smaller board remains.
This immediately suggests a recurrence relation, making Dynamic Programming a natural choice.
####################################################################################################

2. Simulation
Let dp[i] = number of ways to tile a 2 × i board.

Case 1: End with one vertical domino
	Previous board: XXXX
	Add:
		|
		|
	Remaining board: 2 × (i-1)
	Contribution: dp[i-1]

Case 2: End with two horizontal dominoes
		==
		==
	Remaining board: 2 × (i-2)
	Contribution: dp[i-2]

Case 3: End with trominoes
	A single tromino always leaves one missing square.
	Therefore, trominoes must appear in combinations that eventually repair that missing corner.
	Instead of explicitly storing the "missing corner" state, all such possibilities can be mathematically combined.
	The resulting contribution becomes: 2 × (dp[0] + dp[1] + ... + dp[i-3])

	The factor 2 exists because the missing square can be either:
	* Top corner
	* Bottom corner

####################################################################################################

Combining everything

dp[i] = dp[i-1] + dp[i-2] + 2 × (dp[0] + dp[1] + ... + dp[i-3])

Although correct, this recurrence requires summing many previous states each time, leading to O(n²).
We need to simplify it.

####################################################################################################
Optimizing the recurrence

Write the recurrence for consecutive states.

For i:
	dp[i] = dp[i-1] + dp[i-2] + 2 × S
where
	S = dp[0] + ... + dp[i-3]

For i−1:
	dp[i-1] = dp[i-2] + dp[i-3] + 2 × (S - dp[i-3])

Subtract the two equations:
    dp[i] - dp[i-1] = dp[i-1] - dp[i-3]

Rearranging,
    dp[i] = 2 × dp[i-1] + dp[i-3]

This removes the expensive summation and gives an O(1) transition.

####################################################################################################

3. Dynamic Programming

State
	dp[i] = Number of ways to tile a 2 × i board.

Recurrence
    dp[i] = 2 × dp[i-1] + dp[i-3]

Base Cases
    dp[0] = 1
        Empty board has one valid tiling.

    dp[1] = 1
        Only one vertical domino.

    dp[2] = 2
        * Two vertical dominoes
        * Two horizontal dominoes

DP Order
    Compute from    3 → n
    since every state depends only on earlier states.

####################################################################################################
4. Correctness Proof

We prove by induction that the recurrence computes the correct number of tilings.

Base Cases
* dp[0] = 1 is correct because the empty board has exactly one tiling.
* dp[1] = 1 is correct because only one vertical domino fits.
* dp[2] = 2 is correct because there are exactly two tilings.

Thus, all base cases are correct.
####################################################################################################

Inductive Hypothesis
    Assume every value dp[0] ... dp[i-1]
    correctly stores the number of tilings.

####################################################################################################

Inductive Step

Every valid tiling of a 2 × i board must end in one of the following ways:
* A vertical domino extending a 2 × (i−1) tiling.
* A configuration equivalent to the optimized recurrence derived from domino and tromino endings.

The optimized recurrence	dp[i] = 2 × dp[i-1] + dp[i-3]
counts each valid tiling exactly once and misses none.
Therefore, dp[i] is correct.
Hence, by induction, the algorithm correctly computes the number of tilings for every n.

####################################################################################################

5. Complexity Analysis

Time Complexity - O(n)
Each DP state is computed once.

Space Complexity - O(n)
For the DP array.
Can be optimized to O(1) since only the previous three states are required.

####################################################################################################

class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[n]

####################################################################################################
                                            TOP DOWN - DP
####################################################################################################

State Definition

dfs(r1, r2)
means
> Number of ways to tile a board where
* Top row has r1 cells remaining.
* Bottom row has r2 cells remaining.

For example,
dfs(5,5)

means
	XXXXX
	XXXXX

Both rows have 5 cells left.

####################################################################################################

Suppose
	dfs(3,1)

. means filled, X means filled
means
	XXX...
	X.....

where the right part has already been filled.
Notice we don't actually care what happened earlier.
We only care how many cells remain.

####################################################################################################

Why can r1 and r2 differ?

Because trominoes create an overhang.
Example
	XXX..
	XXXX.

Bottom row has one extra cell remaining.
That is exactly what dfs(3,4) represents.
####################################################################################################

Equal Case
	if r1 == r2:

Both rows end at the same column.

Example
XXXX
XXXX

Now we have four possibilities.

1. Vertical domino
            |
            |

    Consumes
        1 top
        1 bottom
    Transition - dfs(r1-1,r2-1)

2. Two horizontal dominoes
            ==
            ==

    Consumes
        2 top
        2 bottom
    Transition - dfs(r1-2,r2-2)

3. Tromino

    Example
        XX
         X

    Consumes
        1 top
        2 bottom
    Transition - dfs(r1-1,r2-2)

4. Mirror tromino

     X
    XX

    Consumes
        2 top
        1 bottom

    Transition - dfs(r1-2,r2-1)

So
    count += dfs(r1-2,r2-2)
    count += dfs(r1-1,r2-1)
    count += dfs(r1-1,r2-2)
    count += dfs(r1-2,r2-1)

matches exactly these four endings.

####################################################################################################

When r1 < r2

Example
	XXX
	XXXX

Bottom row sticks out.

Top : XXX
Bottom : XXXX

What can fill the extra bottom cell?
Only two possibilities.


Horizontal domino
        ====
    on bottom row

    Consumes two bottom cells.

    Transition - dfs(r1,r2-2)


Tromino
        XX
         X

    It consumes
        1 top
        2 bottom

    Transition - dfs(r1-1,r2-2)

Hence
	count += dfs(r1,r2-2)
	count += dfs(r1-1,r2-2)

####################################################################################################

When r1 > r2
Symmetric.

Only
	dfs(r1-2,r2)
	dfs(r1-2,r2-1)

####################################################################################################

Base Case

    if r1==r2==0:
        return 1

Nothing left.
Exactly one valid tiling.

####################################################################################################

Negative indices

if r1<0 or r2<0:
    return 0

Impossible configuration.

####################################################################################################

Why doesn't the difference become arbitrarily large?

A nice property of this recurrence is that it never creates a gap larger than 1.

Starting from -(n,n)
the only unequal transitions are
	(r-1,r-2)
	(r-2,r-1)
whose difference is exactly 1.

From there, (r,r+1)
can only go to
	(r,r-1)
	or
	(r-1,r-1)

so the difference stays at 0 or 1.
Therefore, although the DP table is (n+1) × (n+1), only a narrow band around the diagonal is ever visited.

####################################################################################################

Complexity

Although the table is
(n+1) × (n+1)

only states satisfying
|r1-r2| ≤ 1
are reachable.

Number of reachable states:
3n + O(1)

Each state performs constant work.

Time Complexity: O(n)
Space Complexity: O(n²) (because of the allocated table, even though only O(n) states are used)

If you stored the memo in a dictionary instead of a full 2D list, the space would also become O(n).

'''


class Solution:
    def numTilings(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def dfs(r1: int, r2: int):
            if dp[r1][r2] != -1:
                return dp[r1][r2]
            if r1 == r2 == 0:
                return 1
            if r1 < 0 or r2 < 0:
                return 0

            count = 0
            if r1 == r2:
                count += dfs(r1 - 2, r2 - 2)
                count += dfs(r1 - 1, r2 - 1)
                count += dfs(r1 - 1, r2 - 2)
                count += dfs(r1 - 2, r2 - 1)
            elif r1 < r2:
                count += dfs(r1, r2 - 2)
                count += dfs(r1 - 1, r2 - 2)
            else:
                count += dfs(r1 - 2, r2)
                count += dfs(r1 - 2, r2 - 1)

            dp[r1][r2] = count % modulo
            return count

        dfs(n, n)
        return dp[n][n]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Example cases
        (1, None),  # Expected: 1
        (3, None),  # Expected: 5

        # Small edge cases
        (2, None),
        (4, None),
        (5, None),
        (6, None),

        # Medium cases
        (7, None),
        (8, None),
        (10, None),
        (15, None),
        (20, None),

        # Larger cases
        (30, None),
        (50, None),
        (100, None),
        (250, None),
        (500, None),

        # Maximum constraint
        (1000, None),
    ]

    for n, expected in test_cases:
        result = solution.numTilings(n)
        print(f"n = {n}")
        print(f"Output   : {result}")
        print(f"Expected : {expected}")
        print("-" * 40)