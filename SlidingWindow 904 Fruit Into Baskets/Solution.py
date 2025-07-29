'''
Time Complexity:  O(2n)              (for sliding window)
Space Complexity: O(1)              (for Hashmap but it will never be more than 2 keys)

'''
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        L, res, window = 0, 0, {}

        for R in range(len(fruits)):
            window[fruits[R]] = 1 + window.get(fruits[R], 0)

            # If there are more than 2 types of fruits, shrink the window from the left
            while len(window) > 2:
                ''' This can also work
                if not window[fruits[L]]:
                    window.pop(fruits[L]
                '''
                if window[fruits[L]] == 1:
                    del window[fruits[L]]
                else:
                    window[fruits[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from problem statement
        ([1, 2, 1], 3),  # pick all three
        ([0, 1, 2, 2], 3),  # best is [1,2,2]
        ([1, 2, 3, 2, 2], 4),  # best is [2,3,2,2]

        # Edge cases
        ([5], 1),  # single tree
        ([7, 7, 7, 7], 4),  # all same type
        ([1, 2], 2),  # exactly two trees, two types
        ([1, 2, 1, 2, 1, 2], 6),  # alternating two types
        ([1, 2, 3, 4, 5], 2),  # all distinct -> any two consecutive
        ([1, 1, 2, 3, 3, 2, 2, 1], 5),  # pick from [2,3,3,2,2]
        ([0, 1, 0, 1, 2, 1, 1], 4),  # pick from [0,1,0,1, then stop at 2] → actually best is [1,0,1,2,1]? verify
    ]

    for i, (fruits, expected) in enumerate(test_cases, 1):
        result = solution.totalFruit(fruits)
        print(f"Test case {i}: fruits = {fruits}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  " + ("PASS" if result == expected else "FAIL"), end="\n\n")