'''
| Metric    | Value                    |
| --------- | ------------------------ |
| Time      | **O(n × 32)** ≈ **O(n)** |
| Space     | **O(n × 32)**            |
| Scales to | **2 × 10⁵ elements** ✔   |
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        # Populate Trie
        for num in nums:
            node = root
            binary_string = format(num, "031b")
            for bit in binary_string:
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        # Find max xor
        max_xor = 0
        for num in nums:
            node = root
            curr_xor = 0
            for bit in format(num, '031b'):
                opp = '1' if bit == '0' else '0'
                if opp in node.children:
                    curr_xor = (curr_xor << 1) | 1
                    node = node.children[opp]
                else:
                    curr_xor = curr_xor << 1
                    node = node.children[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # ===== Examples from the problem =====
        ([3, 10, 5, 25, 2, 8], 28),  # Expected: 28
        ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127),  # Expected: 127

        # ===== Edge cases =====
        ([0], 0),  # Single element → XOR with itself
        ([0, 0], 0),  # All zeros
        ([1, 1], 0),  # Same numbers
        ([0, 1], 1),  # Simple XOR
        ([1, 2], 3),  # 01 ^ 10 = 11

        # ===== Small sanity cases =====
        ([2, 4, 8], 12),  # 4 ^ 8 = 12
        ([5, 25], 28),  # Given explanation case
        ([7, 7, 7], 0),  # All same values

        # ===== Bit-pattern focused =====
        ([8, 1, 2, 15], 14),  # 1 ^ 15 = 14
        ([1024, 512, 256, 128], 1536),  # 1024 ^ 512 = 1536
        ([1 << 30, (1 << 30) - 1], (1 << 31) - 1),  # Max 31-bit XOR

        # ===== Mixed range =====
        ([0, 2 ** 31 - 1], 2 ** 31 - 1),  # Extreme bounds
        ([3, 6, 9, 12, 15], 15),  # Patterned multiples
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.findMaximumXOR(nums)
        print(f"Test Case {i}: Result = {result}, Expected = {expected}")