'''
Time Complexity:  O(nlogn)          (sort)
                + O(n)              (for 2 pointer scan)

Space Complexity: O(1) for L, R

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4

'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass

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