'''
#########################################################################################

Time Complexity:  O(2n)       (Creating nums & 2 pointer)
                : O(n)

Space Complexity: O(n)        (for nums)
                : O(n)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        test = head
        while head:
            nums.append(head.val)
            head = head.next

        L, R = 0, len(nums) - 1
        while L <= R:
            if nums[L] != nums[R]:
                return False
            L += 1
            R -= 1
        return True

#########################################################################################

Time Complexity:  O(n + n/2)       (2 pointer & finding mid)
                : O(n)

Space Complexity: O(1)        (for reversing linkedlist)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find middle (slow)

        # for even → slow will be on 2nd half → fast at None
            # [1] → [2] → [3] → [3](slow) → [2] → [1] → None(fast)

        # for odd → slow will be at middle → fast at last
            # [1] → [2] → [3](slow) → [2] → [1](fast) → None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse 2nd half

        # BEFORE
        # for even: [1] → [2] → [3] → [3](slow) → [2] → [1] → None(fast)
        # for odd:  [1] → [2] → [3](slow) → [2] → [1](fast) → None
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        #AFTER
        # for even          None
        #                    ↑
        # [1] → [2] → [3] → [3] ← [2] ← [1](prev)         None

        # for odd     None
        #              ↑
        # [1] → [2] → [3] ← [2] ← [1](prev)               None

        #check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


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
        ([1, 2, 3, 2, 1], True),    # even-length palindrome
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

