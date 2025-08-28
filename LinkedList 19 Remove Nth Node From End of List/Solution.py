'''
Time Complexity:  O(n)              	(for Traversing)
Space Complexity: O(1)              	(for Variables, indexes)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}" if self.next else f"{self.val}"

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Since head is the 1st node, deleting the 1st node (head) requires a previous node (dummy node)
        # Hence, dummy is introduced
        dummy = ListNode(0,head)
        L = R = dummy

        for _ in range(n):
            R = R.next

        # If next doesn't exist that means it's the last node
        while R.next:
            R = R.next
            L = L.next

        L.next = L.next.next
        return dummy.next

# Helper function to build a linked list from a Python list
def build_linked_list(values):
    if not values:
        return None
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to convert a linked list back to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1: Remove 2nd from end
    head = build_linked_list([1,2,3,4,5])
    result = solution.removeNthFromEnd(head, 2)
    print(linked_list_to_list(result))  # Expected: [1,2,3,5]

    # Example 2: Remove only element
    head = build_linked_list([1])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))  # Expected: []

    # Example 3: Remove last element in 2-node list
    head = build_linked_list([1,2])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))  # Expected: [1]

    # Extra Case 1: Remove head (n == size)
    head = build_linked_list([10,20,30,40])
    result = solution.removeNthFromEnd(head, 4)
    print(linked_list_to_list(result))  # Expected: [20,30,40]

    # Extra Case 2: Remove last node
    head = build_linked_list([7,8,9])
    result = solution.removeNthFromEnd(head, 1)
    print(linked_list_to_list(result))  # Expected: [7,8]

    # Extra Case 3: Middle removal
    head = build_linked_list([1,2,3,4,5,6])
    result = solution.removeNthFromEnd(head, 3)
    print(linked_list_to_list(result))  # Expected: [1,2,3,4,6]

    # Extra Case 4: Large list edge case
    head = build_linked_list(list(range(1, 31)))  # [1,...,30]
    result = solution.removeNthFromEnd(head, 30)
    print(linked_list_to_list(result))  # Expected: [2,...,30]