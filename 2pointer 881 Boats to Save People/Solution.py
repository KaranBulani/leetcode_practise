'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Your implementation here
        pass

if __name__ == "__main__":
    solution = Solution()

    # Each tuple is (people_list, limit, expected_output)
    test_cases = [
        # Examples from the problem statement
        ([1, 2], 3, 1),                # one boat carries both
        ([3, 2, 2, 1], 3, 3),          # boats: (1,2), (2), (3)
        ([3, 5, 3, 4], 5, 4),          # boats: (3), (3), (4), (5)

        # Additional edge cases
        ([1], 1, 1),                   # single person fits exactly
        ([3, 3, 3], 3, 3),             # each person must go alone
        ([1, 1, 1, 1], 2, 2),          # pairs of two
        ([2, 2, 2, 2], 3, 4),          # nobody can pair, all alone
        ([1, 2, 2, 3], 3, 3),          # mix of pairable and not
        ([1, 1, 2, 2, 3, 3], 4, 4),    # optimal pairing across weights
        ([5, 1, 4, 2], 6, 2),          # boats: (5,1), (4,2)
    ]

    for people, limit, expected in test_cases:
        result = solution.numRescueBoats(people, limit)
        print(f"people={people}, limit={limit} -> result: {result}, expected: {expected}")