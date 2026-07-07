'''
1. Observation

Read the problem statement

We need to divide the string into the maximum number of partitions such that every character appears in only one partition.
The output should be the length of each partition.

Identify key words and phrases
* Every character must belong to exactly one partition.
* A character cannot appear again after its partition ends.
* We need maximum number of partitions, meaning whenever it is safe to cut, we should.

Define constraints
* 1 <= n <= 500
* Only lowercase English letters.
* Only 26 unique characters.

What is possible?
	We may cut after an index only if no character inside the current partition appears later.

What is NOT possible?
	If any character in the current partition appears later, cutting now would split that character across two partitions, making the partition invalid.

Identify processing direction
	We naturally process left → right because partitions are formed in order.

Before that, we need to know:
	> Where does every character appear for the last time?
    This immediately tells us how far a partition must extend.

Core Observation

Suppose we're building a partition.
While scanning characters, each character tells us:
	> "You cannot finish before my last occurrence."

Therefore,
The partition's ending position is always
	maximum(last occurrence of every character seen so far)

Once our current index reaches that maximum, we know every character inside this partition has completely finished.

So we can safely cut.
####################################################################################################

2. Simulation

Consider
	s = "ababcbacadefegdehijhklij"

Step 1: Find last occurrence
	a -> 8
	b -> 5
	c -> 7
	d -> 14
	e -> 15
	f -> 11
	g -> 13
	h -> 19
	i -> 22
	j -> 23
	k -> 20
	l -> 21

Step 2: Scan the string
Start
	start = 0
	end = 0

i = 0 ('a')
	end = max(0,8)=8
	Current partition must reach index 8.

i = 1 ('b')
	end=max(8,5)=8
	No change.

i = 2 ('a')
	end=max(8,8)=8

i = 3 ('b')
	end=8

i = 4 ('c')
	end=max(8,7)=8

Continue...

At i=8
	Current index equals partition end.
	Everything inside [0...8] never appears again.

Partition size		8-0+1=9
Answer		[9]

Start next partition		start=9
Repeat
Eventually obtain		[9,7,8]

Generalization

    While traversing,
    Maintain
            end = farthest last occurrence
    Whenever
            current index == end
    the partition is complete.
####################################################################################################

3. Technique Selection

Observation tells us
* Need last occurrence of each character.
* Single left-to-right traversal.
* Make greedy cuts whenever safe.
This naturally leads to a Greedy solution.

# Greedy Algorithm

1. Compute the last occurrence of every character.
2. Initialize:
   * start = 0
   * end = 0
3. Traverse the string.
4. Update
	end = max(end, last[s[i]])
5. If		i == end

then
* Current partition is complete.
* Append its length.
* Start next partition.

Why does Greedy work?

At any position,		end
stores the latest index that any character in the current partition must reach.

If we cut earlier,
some character would appear again later, violating the rules.

If we cut later,
we unnecessarily merge two valid partitions, reducing the number of partitions.

Therefore,
Cutting exactly when i == end is both:
* Necessary (can't cut earlier)
* Optimal (shouldn't cut later)

Hence the greedy strategy always produces the maximum number of partitions.
####################################################################################################

Dry Run
	s = "eccbbbbdec"

Last occurrence
	e -> 8
	c -> 9
	b -> 6
	d -> 7

Traverse
	i=0 ('e')
	end=8

	i=1 ('c')
	end=9

	i=2 ('c')
	end=9

	i=3 ('b')
	end=9

	...

	i=9

Current index reaches end.

Partition size
	9-0+1=10

Answer		[10]
####################################################################################################

Complexity Analysis

Time Complexity
* Computing last occurrences: O(n)
* One traversal to form partitions: O(n)
Overall: O(n)

Space Complexity
* Last occurrence map stores at most 26 characters.
So,
* O(1) (constant extra space, since the alphabet is fixed)
* More generally, O(k) where k is the number of distinct characters.
'''
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        # Store last occurrence of each character
        for i, ch in enumerate(s):
            last[ch] = i

        answer = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                answer.append(end - start + 1)
                start = i + 1

        return answer


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from the question
        "ababcbacadefegdehijhklij",
        "eccbbbbdec",

        # Edge Cases
        "a",  # Single character
        "aa",  # Same character repeated
        "ab",  # Two distinct characters
        "abc",  # All unique characters
        "aaaaaa",  # Only one unique character

        # Small Cases
        "aba",
        "abac",
        "abca",
        "aabbcc",
        "abcabc",

        # Characters force one large partition
        "abab",
        "abcab",
        "abccba",
        "abcabcabc",

        # Multiple valid partitions
        "abacdefegde",
        "caedbdedda",

        # Alternating characters
        "abababab",
        "abcde",

        # Larger mixed cases
        "qiejxqfnqceocmy",
        "abcdefghijklmnopqrstuvwxyz",
        "zxyzzxyabcabc",

        # Random-looking cases
        "cabac",
        "baaab",
        "aebbedaddc",
    ]

    for i, s in enumerate(test_cases, 1):
        print(f"Test Case {i}")
        print(f"Input : {s}")
        result = solution.partitionLabels(s)
        print(f"Output: {result}")
        print("-" * 50)