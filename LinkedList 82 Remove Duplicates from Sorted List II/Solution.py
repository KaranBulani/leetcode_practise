'''
Time Complexity:  O(n)               (for traversing)
Space Complexity: O(1)               (for prev & curr)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, dummy
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            # If it happens, that prev.next equal to curr...
            # It means, that we have only 1 element in the group of duplicated elements...
            if prev.next == curr:
                # Don't need to delete it, we move both pointers to right...
                prev = prev.next
                curr = curr.next
            else:
                # Otherwise, we need to skip a group of duplicated elements...
                # set prev.next = curr.next, and curr = prev.next...
                prev.next = curr.next
                curr = curr.next
        return dummy.next

# Helper function to build linked list from Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to convert linked list back to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head = build_linked_list([1, 2, 3, 3, 4, 4, 5])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [1,2,3,3,4,4,5] => Output:", result, "Expected: [1,2,5]")

    # Example 2
    head = build_linked_list([1, 1, 1, 2, 3])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [1,1,1,2,3] => Output:", result, "Expected: [2,3]")

    # Edge Case: Empty list
    head = build_linked_list([])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [] => Output:", result, "Expected: []")

    # Edge Case: No duplicates
    head = build_linked_list([1, 2, 3, 4, 5])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [1,2,3,4,5] => Output:", result, "Expected: [1,2,3,4,5]")

    # Edge Case: All elements are duplicates
    head = build_linked_list([2, 2, 2, 2])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [2,2,2,2] => Output:", result, "Expected: []")

    # Edge Case: Duplicates only at start
    head = build_linked_list([1, 1, 2, 3, 4])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [1,1,2,3,4] => Output:", result, "Expected: [2,3,4]")

    # Edge Case: Duplicates only at end
    head = build_linked_list([1, 2, 3, 4, 4])
    result = linked_list_to_list(solution.deleteDuplicates(head))
    print("Input: [1,2,3,4,4] => Output:", result, "Expected: [1,2,3]")