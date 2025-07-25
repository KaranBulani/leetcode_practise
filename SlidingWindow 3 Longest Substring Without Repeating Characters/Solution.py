'''
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		res = 0
		if len(s) == 0:
			return res

		L, distinctChar = 0, set()

		for R in range(len(s)):
			if s[R] not in distinctChar:
				distinctChar.add(s[R])
				res = max(res, len(distinctChar))
			else:
                # If s[R] is already in the set, we have a duplicate.
                # Shrink the window from the left until that duplicate is removed.
                while s[R] in distinctChar:
					distinctChar.remove(s[L])
					L += 1
				# Now the duplicate is gone, add the current character
                distinctChar.add(s[R])

		return res

Time Complexity:  O(2n)              (for R,L)
Space Complexity: O(re)              (for res due to distinctChar)

'''

# MY SOLUTION IS ABOVE WITH COMMENTS,
# THIS IS OPTIMIZED
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		res = 0
		if len(s) == 0:
			return res

		L, distinctChar = 0, set()
		for R in range(len(s)):
			while s[R] in distinctChar:
				distinctChar.remove(s[L])
				L += 1
			distinctChar.add(s[R])
			res = max(res, len(distinctChar))
		return res

if __name__ == "__main__":
	solution = Solution()

	# Example test cases from the problem
	test_cases = [
		("abcabcbb", 3),    # "abc"
		("bbbbb", 1),       # "b"
		("pwwkew", 3),      # "wke"
	]

	# Additional edge cases
	edge_cases = [
		("", 0),                                   # empty string
		(" ", 1),                                 # single space
		("au", 2),                                # two distinct characters
		("dvdf", 3),                              # "vdf"
		("anviaj", 5),                            # "nviaj"
		("abba", 2),                              # "ab" or "ba"
		("tmmzuxt", 5),                           # "mzuxt"
		("一二三一二四五", 5),                     # unicode characters: "三一二四五"
		("abcdefghijklmnopqrstuvwxyz", 26),     # all unique letters
		("aaaaaa", 1),                            # all same character
		("abc def!#abc", 8),                     # space and symbols: " def!#ab"
	]

	all_tests = test_cases + edge_cases

	for s, expected in all_tests:
		result = solution.lengthOfLongestSubstring(s)
		print(f"Input: '{s}' -> Output: {result} (Expected: {expected})")