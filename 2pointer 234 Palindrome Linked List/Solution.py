'''
Time Complexity:  O(nlogn)       (sort)
                + O(n^2)        N(for A)* N(for L,R)
                : O(n^2)

Space Complexity: O(n) for sort
                + O(1) for L, R
                : O(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pass

def build_linked_list(vals):
    """Helper to build a linked list from a Python list of values."""
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

if __name__ == "__main__":
    solution = Solution()

    # Provided examples
    tests = [
        ([1, 2, 2, 1], True),    # even-length palindrome
        ([1, 2], False),         # two different nodes

        # Additional edge cases
        ([1], True),             # single node list
        ([2, 2], True),          # two-node palindrome
        ([3, 4], False),         # two-node non-palindrome
        ([1, 2, 3, 2, 1], True), # odd-length palindrome
        ([1, 2, 3, 4, 2, 1], False), # even-length non-palindrome
        ([5, 5, 5, 5], True),    # all nodes same
        (list(range(10)), False) # strictly increasing sequence
    ]

    for vals, expected in tests:
        head = build_linked_list(vals)
        result = solution.isPalindrome(head)
        print(f"Input: {vals} -> Output: {result}, Expected: {expected}")

