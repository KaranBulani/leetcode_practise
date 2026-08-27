'''
Time complexity: O(n + m)
Space complexity: O(n)
####################################################################################################
'''
class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)

        # Step-1: Find the earliest valid occurrence of skills
        earliest = [0] * n
        pos = 0
        for i in range(n):
            while skill[i] != station[pos]:
                pos += 1
            earliest[i] = pos
            pos += 1

        # Step-2: Find the latest valid occurrence of skills
        latest = [0] * n
        pos = len(station) - 1
        for i in range(n - 1, -1, -1):
            while skill[i] != station[pos]:
                pos -= 1
            latest[i] = pos
            pos -= 1

        # Step-3: Compute max_gap
        max_gap = 0
        for i in range(n - 1):
            max_gap = max(max_gap, latest[i + 1] - earliest[i])

        return max_gap

if __name__ == "__main__":
    solution = Solution()

    # 1. Example 1: Same skill, many matching stations
    skill = "aa"
    station = "aaaa"
    result = solution.maximumGap(skill, station)
    print("Test 1:", result)

    # 2. Example 2: Different skills
    skill = "xyz"
    station = "xyzz"
    result = solution.maximumGap(skill, station)
    print("Test 2:", result)

    # 3. Example 3: Repeated skill with a large possible gap
    skill = "cbc"
    station = "cbcdbc"
    result = solution.maximumGap(skill, station)
    print("Test 3:", result)

    # 4. Edge case: Only one worker
    skill = "a"
    station = "aaaaa"
    result = solution.maximumGap(skill, station)
    print("Test 4:", result)

    # 5. Edge case: Exactly enough stations
    skill = "abc"
    station = "abc"
    result = solution.maximumGap(skill, station)
    print("Test 5:", result)

    # 6. All workers have the same skill
    skill = "aaa"
    station = "aaaaaa"
    result = solution.maximumGap(skill, station)
    print("Test 6:", result)

    # 7. Large gap between consecutive assignments
    skill = "ab"
    station = "a" + "x" * 10 + "b"
    result = solution.maximumGap(skill, station)
    print("Test 7:", result)

    # 8. Repeated skills with many extra matching stations
    skill = "aba"
    station = "a" * 5 + "b" + "a" * 5
    result = solution.maximumGap(skill, station)
    print("Test 8:", result)

    # 9. Matching characters are spread throughout station
    skill = "abc"
    station = "a" + "x" * 5 + "b" + "y" * 5 + "c"
    result = solution.maximumGap(skill, station)
    print("Test 9:", result)

    # 10. Reverse-looking pattern requiring careful subsequence assignment
    skill = "aaa"
    station = "a" * 10
    result = solution.maximumGap(skill, station)
    print("Test 10:", result)

    # 11. Repeated different skills
    skill = "abab"
    station = "aabb" + "aabb"
    result = solution.maximumGap(skill, station)
    print("Test 11:", result)

    # 12. Many extra irrelevant stations
    skill = "abc"
    station = "xxxxaxxxxxbxxxxcxxxx"
    result = solution.maximumGap(skill, station)
    print("Test 12:", result)