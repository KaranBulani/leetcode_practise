from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped_dict = defaultdict(list)
        for word in strs:
            keyArr = [0] * 26
            for char in word:
                keyArr[ord(char) - 97] += 1
            #cant use ''.join(map(str,keyArr)) because
            # 1b and 10d will lead to 0 1 0 10  and
            # 10b 1c would lead to    0 10 1 0 which is same number
            key = tuple(keyArr)
            grouped_dict[key].append(word)
        return grouped_dict.values()

if __name__ == "__main__":
    solution = Solution()
    strs = ["bdddddddddd","bbbbbbbbbbc"] #["eat","tea","tan","ate","nat","bat"] #[""]#["a"]
    result = solution.groupAnagrams(strs)
    print(result)
