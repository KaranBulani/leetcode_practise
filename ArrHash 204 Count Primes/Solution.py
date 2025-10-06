'''
🔹 Why do we only go up to √n?
We only need to check numbers up to the square root of n because any composite number (non-prime) n must have at least one factor ≤ √n.

Take n = 36.
* Factors of 36 are:
  1 × 36
  2 × 18
  3 × 12
  4 × 9
  6 × 6
  9 × 4
  12 × 3
  18 × 2
  36 × 1

Notice something?
Once you cross 6 (which is √36), the factor pairs start repeating (just swapped).
So if 36 had a factor bigger than √36, its complementary factor would be smaller than √36 — and you’d already have found it earlier.

####################################################################################################
####################################################################################################

🔹 Why do we use int(n0.5) + 1 in code?
* In Python range(a, b) goes up to b but not including b.
* √n may give a floating-point number slightly smaller than the true square root due to precision issues.
So to ensure we include the integer part of the square root in our loop, we add +1.

Example where +1 is needed:
Let’s say n = 25.
* √25 = 5 exactly.
* But if you write:
for i in range(2, int(√25)):  # int(5.0) = 5

The loop runs i = 2, 3, 4 — it misses 5, which is a crucial divisor of 25. So 25 would incorrectly be treated as prime if you’re doing a primality check.

####################################################################################################
####################################################################################################

🔹 Why do we mark multiples starting from i*i ?
Example: n = 30
Step 1 → 	i = 2
			We mark 4, 6, 8, 10, 12, …, 30.
Step 2 → 	i = 3
			We’d normally mark 6, 9, 12, 15, 18, …
			But wait — 6, 12, 18, 24, 30 were already marked by 2!
			The first number not yet marked that’s a multiple of 3 is 9 = 3×3.
			So we start marking from 3² = 9.
Hence, again — start from i².

####################################################################################################
####################################################################################################
TIME COMPLEXITY EXPLANATION:

🔁 What happens in the sieve?
We do two major things:
1. Loop i from 2 to √n.
2. For each such i, if it's still marked as prime, we mark all its multiples as non-prime (i.e., False in the array).

So the expensive part is:
for j in range(i*i, n+1, i):
	is_prime[j] = False

The question becomes: How many total operations does the inner loop do over the entire run?

✅ Naive Upper Bound
At most, we mark each multiple of a prime once. So for every prime p, the number of multiples up to n is about n/p.
So total number of operations is roughly:
n/2 + n/3 + n/5 + n/7 + n/11 + ... (over all primes ≤ n)

That is:
n × (1/2 + 1/3 + 1/5 + 1/7 + 1/11 + ...)

🧠 Important Result from Number Theory

The sum:
1/2 + 1/3 + 1/5 + 1/7 + ... (over all primes ≤ n) ≈ log log n
This is a well-known result in number theory called Mertens’ 2nd Theorem.

So:
Total number of operations ≈ n × log log n
Thus, time complexity = O(n log log n)

####################################################################################################
####################################################################################################
Time complexity:  O(n log log n)				single pass
Space complexity: O(n)							constant space
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        # 0,1 is neither prime nor composite
        if n <= 1:
            return 0

        n -= 1  # As question says stricly less

        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        primes = [i for i, prime in enumerate(is_prime) if prime]
        return len(primes)

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Basic case from question
    print(solution.countPrimes(10))  # Expected: 4  (Primes < 10 → 2, 3, 5, 7)

    # Example 2: Smallest possible input
    print(solution.countPrimes(0))  # Expected: 0

    # Example 3: Another small input
    print(solution.countPrimes(1))  # Expected: 0

    # Edge case: n = 2 (smallest prime number, but we count numbers < n)
    print(solution.countPrimes(2))  # Expected: 0  (since primes < 2 → none)

    # Edge case: n = 3 (primes less than 3)
    print(solution.countPrimes(3))  # Expected: 1  (only 2)

    # Slightly larger example
    print(solution.countPrimes(20))  # Expected: 8  (2, 3, 5, 7, 11, 13, 17, 19)

    # Medium size input for performance check
    print(solution.countPrimes(100))  # Expected: 25

    # Large input edge case (performance test)
    # Just for speed verification — no need to manually check output
    print(solution.countPrimes(5000000))  # Expected: ?