'''
Time Complexity:  O(n)              (n for mid finding and reversing, n for max_sum)
Space Complexity: O(n)              (for various pointer)
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            #vals
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #addition
            totalValue = val1 + val2 + carry
            carry = totalValue // 10
            add = totalValue % 10
            curr.next = ListNode(add)

            #update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



# Helper function to build linked list from Python list
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Helper function to convert linked list back to Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [7, 0, 8]

    # Example 2
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [0]

    # Example 3
    l1 = build_linked_list([9,9,9,9,9,9,9])
    l2 = build_linked_list([9,9,9,9])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [8,9,9,9,0,0,0,1]

    # Edge Case 1: Different lengths (carry overflow at end)
    l1 = build_linked_list([9,9])
    l2 = build_linked_list([1])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [0,0,1]

    # Edge Case 2: Large numbers within constraints
    l1 = build_linked_list([1] * 100)  # 100 nodes of "1"
    l2 = build_linked_list([9])        # just "9"
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [0,2,1,1,1,...,1] (length 100)

    # Edge Case 3: One list much shorter
    l1 = build_linked_list([5])
    l2 = build_linked_list([5, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected [0,0,0,1]
