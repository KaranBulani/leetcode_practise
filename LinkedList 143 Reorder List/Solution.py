'''
Time Complexity:  O(n)              	(for BinarySearch)
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

def build_linked_list(values):
    """Helper to build linked list from Python list"""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def linked_list_to_list(head):
    """Helper to convert linked list back to Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Since at least one element exists,
        # skip checking the current element, only check the next.
        if not head.next:
            return

        # 1. Find mid
        # while fast.next and fast.next.next:     -> stops at 1st mid incase of even len
        # while fast and fast.next:               -> stops at 2nd mid incase of even len
        # Always stops at correct mid, incase of odd len
        # we want to get this right as we will cut LinkedList later
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # cut the list into two halves
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 3. Merge two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head = build_linked_list([1,2,3,4])
    solution.reorderList(head)
    print("Test 1:", linked_list_to_list(head))  # Expected: [1,4,2,3]

    # Example 2
    head = build_linked_list([1,2,3,4,5])
    solution.reorderList(head)
    print("Test 2:", linked_list_to_list(head))  # Expected: [1,5,2,4,3]

    # Edge Case 1: Single element
    head = build_linked_list([1])
    solution.reorderList(head)
    print("Test 3:", linked_list_to_list(head))  # Expected: [1]

    # Edge Case 2: Two elements
    head = build_linked_list([1,2])
    solution.reorderList(head)
    print("Test 4:", linked_list_to_list(head))  # Expected: [1,2]

    # Edge Case 3: Three elements
    head = build_linked_list([1,2,3])
    solution.reorderList(head)
    print("Test 5:", linked_list_to_list(head))  # Expected: [1,3,2]

    # Edge Case 4: Even number of nodes (6 elements)
    head = build_linked_list([10,20,30,40,50,60])
    solution.reorderList(head)
    print("Test 6:", linked_list_to_list(head))  # Expected: [10,60,20,50,30,40]

    # Edge Case 5: Odd number of nodes (7 elements)
    head = build_linked_list([1,2,3,4,5,6,7])
    solution.reorderList(head)
    print("Test 7:", linked_list_to_list(head))  # Expected: [1,7,2,6,3,5,4]