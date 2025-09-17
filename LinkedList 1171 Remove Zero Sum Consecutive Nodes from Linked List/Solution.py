'''
Time Complexity:  O(nlogn)               (for Merge Sort)
Space Complexity: O(1)               	 (for As only repointing)

Tried a single pass solution which didnt work because for:

1, 3, 2, -3, -2, 5, 5, -5, 1
      ^          ^
because prefix sum till 1st arrow and 2nd arrow is same

    dummy = ListNode(0, head)
    prefixSum, currSum = {0: dummy}, 0
    curr = dummy.next

    while curr:
        currSum += curr.val
        if currSum in prefixSum:
            prefixSum[currSum].next = curr.next
        else:
            prefixSum[currSum] = curr
        curr = curr.next
    return dummy.next

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f"{self.val}->{self.next}"


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        prefix_sum = 0
        seen = {}

        # 1st pass: record last occurrence of each prefix sum
        curr = dummy
        while curr:
            prefix_sum += curr.val
            seen[prefix_sum] = curr
            curr = curr.next

        # 2nd pass: remove zero-sum sequences
        prefix_sum = 0
        curr = dummy
        while curr:
            prefix_sum += curr.val
            curr.next = seen[prefix_sum].next
            curr = curr.next
        return dummy.next

# Helper function to build linked list from list
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to convert linked list back to list
def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    solution = Solution()

    # Example -1
    head = build_linked_list([1, 3, 2, -3, -2, 5, 5, -5, 1])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [3,1] OR [1,2,1]

    # Example 0
    head = build_linked_list([0, 0])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [3,1] OR [1,2,1]

    # Example 1
    head = build_linked_list([1, 2, -3, 3, 1])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [3,1] OR [1,2,1]

    # Example 2
    head = build_linked_list([1, 2, 3, -3, 4])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [1,2,4]

    # Example 3
    head = build_linked_list([1, 2, 3, -3, -2])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [1]

    # Edge Case 1: All elements cancel to 0
    head = build_linked_list([1, -1])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: []

    # Edge Case 2: Zero at beginning
    head = build_linked_list([0, 1, 2])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [1,2]

    # Edge Case 3: Zero at end
    head = build_linked_list([1, 2, -3, 0])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: []

    # Edge Case 4: Multiple nested zero-sum sequences
    head = build_linked_list([2, -2, 3, 1, -1])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: [3]

    # Edge Case 5: Large values within range
    head = build_linked_list([1000, -1000, 5, -3, -2])
    result = linked_list_to_list(solution.removeZeroSumSublists(head))
    print(result)  # Expected: []