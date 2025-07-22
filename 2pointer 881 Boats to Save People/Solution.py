'''
Time Complexity:  O(nlogn)          (sort)
                + O(n)              (for 2 pointer scan)

Space Complexity: O(1) for L, R
'''

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Sort the array so we can efficiently pair lightest with heaviest
        people.sort()
        L, R = 0, len(people) - 1
        boats = 0

        # A. Pair lightest and heaviest if possible.
        # B. If pairing fails, the heaviest still boards alone.
        # C. Include any unpaired middle person, then adjust pointers thereby breaking the loop.

        # Continue until all people have been assigned to boats
        while L <= R:
            if people[L] + people[R] <= limit:
                L += 1  # Move to the next lightest person
            R -= 1  # Move to the next heaviest person
            boats += 1  # One more boat is utilized

        return boats

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
        ([1, 1, 2, 2, 3, 3], 4, 3),    # optimal pairing across weights
        ([5, 1, 4, 2], 6, 2),          # boats: (5,1), (4,2)
    ]

    for people, limit, expected in test_cases:
        result = solution.numRescueBoats(people, limit)
        print(f"people={people}, limit={limit} -> result: {result}, expected: {expected}")