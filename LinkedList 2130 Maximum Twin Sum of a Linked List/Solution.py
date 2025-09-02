'''
Time Complexity:  O(2n)             (n for finding mid and reversing, n for max_sum)
Space Complexity: O(1)              (for various pointer)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find middle (slow will end at node before second half)
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Cut the list into two halves
        curr = slow.next
        slow.next = None  # cut here

        # Step 3: Reverse the second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 4: Compute twin sums
        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum


def build_linked_list(values):
    """Helper to build a linked list from a list of values"""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    solution = Solution()

    # Example cases
    head1 = build_linked_list([5, 4, 2, 1])
    print("Case 1 Output:", solution.pairSum(head1))  # Expected: 6

    head2 = build_linked_list([4, 2, 2, 3])
    print("Case 2 Output:", solution.pairSum(head2))  # Expected: 7

    head3 = build_linked_list([1, 100000])
    print("Case 3 Output:", solution.pairSum(head3))  # Expected: 100001

    # Additional diverse cases
    head4 = build_linked_list([1, 2])
    print("Case 4 Output:", solution.pairSum(head4))  # Expected: 3

    head5 = build_linked_list([10, 20, 30, 40])
    print("Case 5 Output:", solution.pairSum(head5))  # Expected: 50

    head6 = build_linked_list([1, 2, 3, 4, 5, 6])
    print("Case 6 Output:", solution.pairSum(head6))  # Expected: 7

    head7 = build_linked_list([100000, 1, 1, 100000])
    print("Case 7 Output:", solution.pairSum(head7))  # Expected: 100001