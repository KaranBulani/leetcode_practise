'''
Time Complexity:  O(2n)					(L -> R, R -> L)
Space Complexity: O(n)               	(for candies)
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    ratings = [1, 0, 2]
    result = solution.candy(ratings)
    print(f"Example 1 result: {result}")  # Expected output: 5

    # Example 2
    ratings = [1, 2, 2]
    result = solution.candy(ratings)
    print(f"Example 2 result: {result}")  # Expected output: 4

    # Edge Case 1: Single child (only 1 candy needed)
    ratings = [1]
    result = solution.candy(ratings)
    print(f"Edge Case 1 result: {result}")  # Expected output: 1

    # Edge Case 2: All ratings are the same
    ratings = [2, 2, 2, 2, 2]
    result = solution.candy(ratings)
    print(f"Edge Case 2 result: {result}")  # Expected output: 5 (One candy per child)

    # Edge Case 3: Strictly increasing ratings
    ratings = [1, 2, 3, 4, 5]
    result = solution.candy(ratings)
    print(f"Edge Case 3 result: {result}")  # Expected output: 15 (1 + 2 + 3 + 4 + 5)

    # Edge Case 4: Strictly decreasing ratings
    ratings = [5, 4, 3, 2, 1]
    result = solution.candy(ratings)
    print(f"Edge Case 4 result: {result}")  # Expected output: 15 (1 + 2 + 3 + 4 + 5)

    # Edge Case 5: Large number of children with a small variation in ratings
    ratings = [1] * 20000  # Large input with all ratings the same
    result = solution.candy(ratings)
    print(f"Edge Case 5 result: {result}")  # Expected output: 20000 (1 candy per child)

    # Edge Case 6: Large input with alternating peaks and valleys
    ratings = [1, 3, 2, 4, 3, 5, 4]
    result = solution.candy(ratings)
    print(f"Edge Case 6 result: {result}")  # Expected output: 15

    # Edge Case 7: Single peak in the middle
    ratings = [1, 3, 2]
    result = solution.candy(ratings)
    print(f"Edge Case 7 result: {result}")  # Expected output: 4

    # Edge Case 8:
    ratings = [1, 3, 2, 2, 1]
    result = solution.candy(ratings)
    print(f"Edge Case 7 result: {result}")  # Expected output: 7

    # Edge Case 9:
    ratings = [29, 51, 87, 87, 72, 12]
    result = solution.candy(ratings)
    print(f"Edge Case 7 result: {result}")  # Expected output: 12