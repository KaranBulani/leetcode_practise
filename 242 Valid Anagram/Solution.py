'''
Time Complexity => S + T + distinct S char => S + T
Space Complexity => Distinct S + Distinct T (both dictionary)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        for char in s:
            s_count[char] = 1 + s_count.get(char, 0)

        t_count = {}
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)

        for key in s_count:
            if s_count[key] != t_count.get(key,0):
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = "anagram"#"rat"
    t = "nagaram"#"car"
    result = solution.isAnagram(s, t)
    print(result)