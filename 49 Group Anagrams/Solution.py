'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grouped_dict = defaultdict(list)
        for word in strs:
            keyArr = [0] * 26
            for char in word:
                keyArr[ord(char) - 97] += 1
            key = ''.join(map(str,keyArr)) #Or use key = tuple(keyArr)
            grouped_dict[key].append(word)
        return grouped_dict.values()

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"] #[""]#["a"]
    result = solution.groupAnagrams(strs)
    print(result)
