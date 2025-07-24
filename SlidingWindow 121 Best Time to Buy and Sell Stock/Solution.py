'''
Time Complexity:  O(n)              (for sliding window)
Space Complexity: O(1)              (for window L, R)
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        totalProfit = 0
        # L will represent the index of the lowest price (best day to buy) seen so far
        L = 0
        # Iterate through each day R as a potential selling day
        for R in range(len(prices)):
            # If current price is lower than price at L, update L to be this day
            # since buying at a cheaper price could yield higher profit later
            if prices[R] < prices[L]:
                L = R
            # Calculate profit by selling on day R after buying on day L
            # and update totalProfit if this profit is greater than previous max
            totalProfit = max(totalProfit, prices[R] - prices[L])
        return totalProfit

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        # Examples from the problem description
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        # Edge cases
        ([5], 0),                    # only one day → no transaction possible
        ([1, 2], 1),                 # simple increase
        ([2, 1], 0),                 # simple decrease
        ([3, 3, 3, 3], 0),           # all same prices
        ([2, 1, 4], 3),              # valley then peak
        ([1, 2, 3, 2, 5, 1, 7], 6),   # multiple ups and downs
        ([0, 10000], 10000),         # boundary values (min/max)
    ]

    for prices, expected in test_cases:
        result = solution.maxProfit(prices)
        print(f"prices={prices} -> result={result}, expected={expected}")