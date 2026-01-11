'''
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        res = []
        for x, m in queries:
            i = 0
            maxComp = -1
            while i < len(nums) and nums[i] <= m:
                maxComp = max(maxComp, x ^ nums[i])
                i += 1
            res.append(maxComp)
        return res

Time Com: O(nlogn) + O(q * n)				For sorting + num of queries with having comparison with n
Space Complexity: O(1) + O(q) 				as few variables + res len

####################################################################################################
####################################################################################################
⏱️ Time Complexity: O((N + Q) * 31)

Step 1: Sorting
nums.sort()
sorted_queries = sorted(...)
* Sorting nums → O(N log N)
* Sorting queries → O(Q log Q)

Step 2: Inserting numbers into the Trie
Each number:
* Is inserted once
* Has at most 31 bits (since nums[i] ≤ 10^9)
for bit in format(nums[idx], "031b"):
So insertion cost:
N numbers × 31 bits = O(N * 31)

Step 3: Processing each query
Each query:
* Traverses the Trie once
* Again, 31 bits
for bit in format(x, "031b"):
So query cost:
Q queries × 31 bits = O(Q * 31)

✅ Total Time
Sorting	   → O(N log N) + O(Q log Q)
Insertion  → O(N * 31)
Queries    → O(Q * 31)
--
Total      → O(N log N) + O(Q log Q) + O((N + Q) * 31)

🧠 Space Complexity: O(N * 31)
Where does memory go?
The Trie stores bits of inserted numbers.
Worst case:
    * All numbers are unique
    * No shared prefixes
Each number creates: 31 Trie nodes

'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        root = TrieNode()
        idx = 0

        def insertNumsLessThanEqualTo(limit: int):
            nonlocal idx
            while idx < len(nums) and nums[idx] <= limit:
                node = root
                for bit in format(nums[idx], "031b"):
                    if bit not in node.children:
                        node.children[bit] = TrieNode()
                    node = node.children[bit]
                idx += 1

        res = [-1] * len(queries)

        # sort by mi
        sorted_queries = sorted((m, x, i) for i, (x, m) in enumerate(queries))

        for m, x, i in sorted_queries:
            insertNumsLessThanEqualTo(m)

            if not root.children:
                res[i] = -1
                continue

            node = root
            curr_xor = 0

            for bit in format(x, "031b"):
                opp = '1' if bit == '0' else '0'   # ✅ FIX
                if opp in node.children:
                    curr_xor = (curr_xor << 1) | 1
                    node = node.children[opp]
                else:
                    curr_xor = (curr_xor << 1)
                    node = node.children[bit]

            res[i] = curr_xor

        return res

if __name__ == "__main__":
    solution = Solution()

    # -------------------------
    # Basic examples (from problem)
    # -------------------------
    nums1 = [0, 1, 2, 3, 4]
    queries1 = [[3, 1], [1, 3], [5, 6]]
    print("Test 1:", solution.maximizeXor(nums1, queries1))

    nums2 = [5, 2, 4, 6, 6, 3]
    queries2 = [[12, 4], [8, 1], [6, 3]]
    print("Test 2:", solution.maximizeXor(nums2, queries2))

    # -------------------------
    # Edge case: nums has single element
    # -------------------------
    nums3 = [7]
    queries3 = [[7, 7], [7, 6], [0, 7]]
    print("Test 3:", solution.maximizeXor(nums3, queries3))

    # -------------------------
    # Edge case: all nums > mi
    # -------------------------
    nums4 = [10, 20, 30]
    queries4 = [[5, 1], [8, 9], [0, 0]]
    print("Test 4:", solution.maximizeXor(nums4, queries4))

    # -------------------------
    # Edge case: all nums <= mi
    # -------------------------
    nums5 = [1, 2, 3, 4]
    queries5 = [[0, 10], [5, 10], [7, 10]]
    print("Test 5:", solution.maximizeXor(nums5, queries5))

    # -------------------------
    # Edge case: duplicate values in nums
    # -------------------------
    nums6 = [5, 5, 5, 5]
    queries6 = [[5, 5], [1, 5], [10, 5]]
    print("Test 6:", solution.maximizeXor(nums6, queries6))

    # -------------------------
    # Edge case: xi = 0
    # -------------------------
    nums7 = [1, 2, 4, 8]
    queries7 = [[0, 1], [0, 8], [0, 0]]
    print("Test 7:", solution.maximizeXor(nums7, queries7))

    # -------------------------
    # Edge case: mi = 0
    # -------------------------
    nums8 = [0, 1, 2]
    queries8 = [[5, 0], [0, 0], [1, 0]]
    print("Test 8:", solution.maximizeXor(nums8, queries8))

    # -------------------------
    # Large-bit values (stress logic, not size)
    # -------------------------
    nums9 = [0, 2 ** 30, 2 ** 29]
    queries9 = [[2 ** 30, 2 ** 30], [2 ** 30, 0], [2 ** 29, 2 ** 29]]
    print("Test 9:", solution.maximizeXor(nums9, queries9))

    # -------------------------
    # Queries unordered by mi (important for offline sorting solutions)
    # -------------------------
    nums10 = [3, 10, 5, 25, 2, 8]
    queries10 = [[5, 28], [5, 2], [5, 25], [5, 8]]
    print("Test 10:", solution.maximizeXor(nums10, queries10))