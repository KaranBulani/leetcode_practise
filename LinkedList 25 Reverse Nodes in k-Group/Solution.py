'''
####################################################################################################
########################################### BRUTE FORCE ############################################
####################################################################################################

Time Complexity:  O(3n)                 (for extracting, reversing and recreating)
Space Complexity: O(n)                  (for values list)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Extract values into an array
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Step 2: Reverse in groups of k
        n = len(values)
        for i in range(0, n, k):
            if i + k <= n:  # only reverse if full group
                values[i:i+k] = reversed(values[i:i+k])

        # Step 3: Convert back into linked list
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

####################################################################################################
######################################### DP BRUTE FORCE ###########################################
####################################################################################################
Time Complexity:  O(n)                  (for reversing)
Space Complexity: O(1)                  (for pointers)
'''
from typing import Optional

# Helper functions
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev  # main reassingment
                prev = curr
                curr = tmp

            tmp = groupPrev.next  #groupPrev.next was the first node before reversal, which is now the last node of the reversed group. We store it in tmp because this node will be the groupPrev for the next group.
            groupPrev.next = kth  # We connect the groupPrev (node before the group, maybe dummy) to the new first node of the group (kth).
            groupPrev = tmp  # move groupPrev forward to the end of the newly reversed group. This ensures that in the next iteration, we start reversing from the right spot.

            return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
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

    # Example 1: Basic case k=2
    head = build_linked_list([1,2,3,4,5])
    k = 2
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [2,1,4,3,5]

    # Example 2: k=3
    head = build_linked_list([1,2,3,4,5])
    k = 3
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [3,2,1,4,5]

    # Edge Case 1: k=1 (no change)
    head = build_linked_list([1,2,3,4,5])
    k = 1
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [1,2,3,4,5]

    # Edge Case 2: k = length of list
    head = build_linked_list([1,2,3,4,5])
    k = 5
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [5,4,3,2,1]

    # Edge Case 3: List length not a multiple of k
    head = build_linked_list([1,2,3,4,5,6,7])
    k = 3
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [3,2,1,6,5,4,7]

    # Edge Case 4: Single node
    head = build_linked_list([1])
    k = 1
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [1]

    # Edge Case 5: Two nodes with k=2
    head = build_linked_list([1,2])
    k = 2
    result = solution.reverseKGroup(head, k)
    print(linked_list_to_list(result))  # Expected: [2,1]