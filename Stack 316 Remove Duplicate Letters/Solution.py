'''
I implemented: Solution shared here https://youtu.be/j313ttNJjo0?si=CgBxO_8m6HQhJCXC

ANOTHER SOLUTION

def removeDuplicateLetters(s: str) -> str:
	res = []
	seen = set()
	last_occurrence = {char: index for index, char in enumerate(s)}

	for index, char in enumerate(s):
		if char in seen:
			continue
		while res and res[-1] > char and index < last_occurrence[res[-1]]:
			seen.remove(res.pop())
		res.append(char)
		seen.add(char)

	return ''.join(res)

Instead of ___ above code has ___ :
    visited_dict , seen set.
    countDict , last_occurrence.

Instead of Code checking for ___ it check ___
    dict has value true/false , value is present in set or not
    count is positive or not , is this the last_occurence or not

Time Complexity: O(2n) (for count then for res)
Space Complexity: O(3n) for res, countDict, visited_dict
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count how many times each character appears
        countDict = {}
        for c in s:
            countDict[c] = countDict.get(c, 0) + 1

        res = []
        visited_dict = {}
        for c in s:
            # Decrement remaining count
            countDict[c] -= 1

            # Skip if already in res
            if visited_dict.get(c, False):
                continue

            # Greedy: remove larger chars as long as they will reappear later
            while res and res[-1] > c and countDict[res[-1]] > 0:
                visited_dict[res.pop()] = False

            # Add current character
            res.append(c)
            visited_dict[c] = True

        return ''.join(res)

if __name__ == "__main__":
    solution = Solution()

    # Test cases from the question
    test_cases = [
        "bcabc",  # expected "abc"
        "cbacdcbc",  # expected "acdb"
        # add more strings here to test edge cases,
        "a",  # expected "a"
        "bbcaac",  # expected "bac"
        "abacb"  # expected "abc"
    ]

    for s in test_cases:
        result = solution.removeDuplicateLetters(s)
        print(f'Input: {s!r} -> Output: {result}')
