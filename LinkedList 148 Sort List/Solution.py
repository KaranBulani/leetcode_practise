'''
Time Complexity:  O(nlogn)               (for Merge Sort)
Space Complexity: O(1)               	 (for As only repointing)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, first, second):
        dummy = ListNode(0)
        prev = dummy
        while first and second:
            if first.val < second.val:
                prev.next = first
                first = first.next
            else:
                prev.next = second
                second = second.next
            prev = prev.next
            prev.next = None

        if first:
            prev.next = first
        if second:
            prev.next = second

        return dummy.next

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = slow
        prev.next = None

        first = self.mergeSort(head)
        second = self.mergeSort(mid)

        return self.merge(first, second)

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        dummy.next = self.mergeSort(dummy.next)
        return dummy.next

if __name__ == "__main__":
    solution = Solution()


    # Helper function to convert Python list -> Linked List
    def build_linked_list(values):
        dummy = ListNode(0)
        curr = dummy
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return dummy.next


    # Helper function to convert Linked List -> Python list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result


    # Test cases
    test_cases = [
        [],  # empty list
        [4, 2, 1, 3],  # example 1
        [-1, 5, 3, 4, 0],  # example 2
        [1],  # single node
        [2, 1],  # two nodes unsorted
        [1, 2],  # two nodes already sorted
        [5, 4, 3, 2, 1],  # reverse sorted
        [1, 1, 1, 1],  # all duplicates
        [-5, -1, -3, -2],  # all negatives
        [10, -1, 0, 10, 5],  # mix of positive, negative, duplicates
    ]

    for i, case in enumerate(test_cases, 1):
        head = build_linked_list(case)
        sorted_head = solution.sortList(head)
        result = linked_list_to_list(sorted_head)
        print(f"Test case {i}: Input={case} -> Output={result}")