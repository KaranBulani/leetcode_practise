'''
####################################################################################################
####################################### TWO POINTER SOLUTION #######################################
####################################################################################################

Time Complexity:  O(n+m)				(for Traversing both)
Space Complexity: O(n)               	(for seen)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        curr = headA
        while curr:
            seen.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in seen:
                return curr
            curr = curr.next
        return None

####################################################################################################
####################################### TWO POINTER SOLUTION #######################################
####################################################################################################

Time Complexity:  O(n+m)				(for Traversing both)
Space Complexity: O(1)               	(for pA, pB)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA, pB = headA, headB

        #n+m == m+n so they will become equal at intersection point
        while pA != pB:
            # move to next node, or switch to other list's head
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA

# Helper function to build linked lists with intersection
def build_lists(intersectVal, listA, listB, skipA, skipB):
    # Build listA
    dummyA = ListNode(0)
    currA = dummyA
    for val in listA:
        currA.next = ListNode(val)
        currA = currA.next
    headA = dummyA.next

    # Build listB
    dummyB = ListNode(0)
    currB = dummyB
    for val in listB:
        currB.next = ListNode(val)
        currB = currB.next
    headB = dummyB.next

    if intersectVal == 0:
        return headA, headB

    # Find intersection point
    interA = headA
    for _ in range(skipA):
        interA = interA.next
    interB = headB
    for _ in range(skipB):
        interB = interB.next

    # Link intersection
    interB.next = interA.next
    interB.val = interA.val  # sync value for realism
    return headA, headB


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    headA, headB = build_lists(8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3)
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 8

    # Example 2
    headA, headB = build_lists(2, [1, 9, 1, 2, 4], [3, 2, 4], 3, 1)
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 2

    # Example 3
    headA, headB = build_lists(0, [2, 6, 4], [1, 5], 3, 2)
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: None

    # Extra Edge Case 1: Intersection at head
    headA, headB = build_lists(3, [3, 4, 5], [3, 4, 5], 0, 0)
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 3

    # Extra Edge Case 2: Same single node
    single = ListNode(42)
    headA = single
    headB = single
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: 42

    # Extra Edge Case 3: Different lengths, no intersection
    headA, headB = build_lists(0, [1, 2, 3, 4], [6, 7], 0, 0)
    result = solution.getIntersectionNode(headA, headB)
    print(result.val if result else None)  # Expected: None
