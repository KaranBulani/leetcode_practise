'''
Idea
1. Count frequency of each character.
2. Build a max heap (freq, char).
3. Repeatedly pick the two most frequent characters.
4. Append both to answer.
5. Decrease their frequencies and push back if still available.
6. Handle the final remaining character carefully.

####################################################################################################

What happens when only 1 element remains?

	This is the part you were struggling with.
	Suppose we reach:
		max_heap = [(1, 'a')]
		res = ['a', 'b', 'a', 'b']

	We can safely append 'a': 	abab + a = ababa
	Valid.

But if:
	max_heap = [(2, 'a')]
	res = ['a', 'b', 'a', 'b']

Then we have:	abab + aa
Impossible because adjacent 'a's will occur.

So:
	if cnt > 1:
		return ""

####################################################################################################
Even simpler way to think

When only one character remains:
* If its frequency is 1 and it differs from the last character in res, append it.
* Otherwise return "".
That's the entire leftover-element logic.

####################################################################################################

Complexity
* Building heap: O(k)
* Each character pushed/popped once: O(n log k)
where:
* n = len(s)
* k = number of distinct characters

Space: O(k) for the heap.

'''
from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        max_heap = [(cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify_max(max_heap)

        res = []

        while len(max_heap) > 1:
            cnt1, ch1 = heapq.heappop_max(max_heap)
            cnt2, ch2 = heapq.heappop_max(max_heap)

            res.append(ch1)
            res.append(ch2)

            cnt1 -= 1
            cnt2 -= 1

            if cnt1 > 0:
                heapq.heappush_max(max_heap, (cnt1, ch1))

            if cnt2 > 0:
                heapq.heappush_max(max_heap, (cnt2, ch2))

        # One character left
        if max_heap:
            cnt, ch = heapq.heappop_max(max_heap)

            # More than one occurrence left of current char => impossible
            if cnt > 1:
                return ""

            # Same as previous character => impossible
            if res and res[-1] == ch:
                return ""

            res.append(ch)

        return "".join(res)

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        "aab",          # Expected: valid rearrangement, e.g. "aba"
        "aaab",         # Expected: ""

        # Single character
        "a",            # Expected: "a"

        # Two characters
        "ab",           # Expected: "ab" or "ba"
        "aa",           # Expected: ""

        # Small valid cases
        "aabb",         # Expected: valid rearrangement
        "aaabb",        # Expected: valid rearrangement
        "aabbc",        # Expected: valid rearrangement
        "aaabc",        # Expected: valid rearrangement

        # Boundary around impossibility condition
        "aaaab",        # Expected: ""
        "aaaabb",       # Expected: valid rearrangement
        "aaaaabb",      # Expected: ""

        # All unique
        "abcdef",       # Expected: any permutation

        # All same
        "zzzzz",        # Expected: ""

        # Multiple characters with same frequency
        "aabbcc",       # Expected: valid rearrangement
        "aaabbb",       # Expected: valid rearrangement
        "aaabbbccc",    # Expected: valid rearrangement

        # Dominant character but still possible
        "vvvlo",        # Famous LeetCode test case
        "aaadbbcc",     # Expected: valid rearrangement

        # Larger cases
        "aaaabbbb",     # Expected: valid rearrangement
        "aaaabbbbcc",   # Expected: valid rearrangement
        "aaaaabbbbbc",  # Expected: valid rearrangement
    ]

    for s in test_cases:
        result = solution.reorganizeString(s)

        print(f"Input    : {s}")
        print(f"Output   : {result}")

        # Optional validation
        valid = (
            (result == "" and max(s.count(c) for c in set(s)) > (len(s) + 1) // 2)
            or
            (
                sorted(result) == sorted(s)
                and all(result[i] != result[i + 1] for i in range(len(result) - 1))
            )
        )

        print(f"Valid    : {valid}")
        print("-" * 50)