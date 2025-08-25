'''
####################################################################################################
######################################## Iterative Solution ########################################
####################################################################################################

Time Complexity:  O(n + m)              	( for len(list1) & len(list1) )
Space Complexity: O(1)              	    ( for Variables, indexes )

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2

        return dummy.next

####################################################################################################
######################################## Recursive Solution ########################################
####################################################################################################

Time Complexity:  O(n + m)              	    ( for len(list1) & len(list1) )
Space Complexity: O(n + m)              	    ( for Stack Calls )

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # helper: convert linked list to Python list (for easier print)
    def to_list(self):
        result, curr = [], self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
        lil.next = self.mergeTwoLists(lil.next, big)
        return lil

# helper: convert Python list to linked list
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print("Example 1:", result.to_list())  # expected -> [1,1,2,3,4,4]

    # Example 2 (both empty)
    list1 = build_linked_list([])
    list2 = build_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print("Example 2:", result.to_list() if result else [])  # expected -> []

    # Example 3 (one empty, one non-empty)
    list1 = build_linked_list([])
    list2 = build_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print("Example 3:", result.to_list())  # expected -> [0]

    # Extra Edge Case 1: lists with negative values
    list1 = build_linked_list([-10, -5, 0])
    list2 = build_linked_list([-6, -3, 2])
    result = solution.mergeTwoLists(list1, list2)
    print("Edge Case 1:", result.to_list())  # expected -> ?

    # Extra Edge Case 2: one list much longer than the other
    list1 = build_linked_list([1, 2, 3, 4, 5, 6])
    list2 = build_linked_list([7])
    result = solution.mergeTwoLists(list1, list2)
    print("Edge Case 2:", result.to_list())  # expected -> ?

    # Extra Edge Case 3: both lists identical
    list1 = build_linked_list([2, 2, 2])
    list2 = build_linked_list([2, 2, 2])
    result = solution.mergeTwoLists(list1, list2)
    print("Edge Case 3:", result.to_list())  # expected -> ?

    # Extra Edge Case 4: values interleaved
    list1 = build_linked_list([1, 3, 5])
    list2 = build_linked_list([2, 4, 6])
    result = solution.mergeTwoLists(list1, list2)
    print("Edge Case 4:", result.to_list())  # expected -> ?