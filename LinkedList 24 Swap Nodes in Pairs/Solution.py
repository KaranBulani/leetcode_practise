'''
Time: O(n) — each node is visited once.
Space: O(1) — only a few pointers are used.
'''
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next
            next_pair = second.next

            prev.next = second
            second.next = first
            first.next = next_pair

            prev = first

        return dummy.next


def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy

    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next

    return dummy.next

def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # Examples from question
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),

        # Additional edge cases
        ([5, 6, 7, 8, 9], [6, 5, 8, 7, 9]),          # Odd length
        ([10, 20, 30, 40, 50, 60], [20, 10, 40, 30, 60, 50]),  # Even length
        ([7, 7], [7, 7]),                            # Duplicate values
        ([1, 1, 2, 2], [1, 1, 2, 2]),                # Duplicates swapped
        ([100], [100]),                             # Single maximum value
        ([0, 100], [100, 0]),                        # Min and max values
        (list(range(1, 11)), [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]),  # Longer list
    ]

    for i, (input_list, expected) in enumerate(test_cases, 1):
        head = create_linked_list(input_list)
        result = solution.swapPairs(head)
        output = linked_list_to_list(result)

        print(f"Test Case {i}")
        print(f"Input    : {input_list}")
        print(f"Output   : {output}")
        print(f"Expected : {expected}")
        print(f"Pass     : {output == expected}")
        print("-" * 50)