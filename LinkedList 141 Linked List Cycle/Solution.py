'''
Time Complexity:  O(logn)              	(for BinarySearch)
Space Complexity: O(1)              	(for Variables, indexes)

	141. Linked List Cycle

	Given head, the head of a linked list, determine if the linked list has a cycle in it.
	There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
	Return true if there is a cycle in the linked list. Otherwise, return false.

	Example 1:
	Input: head = [3,2,0,-4], pos = 1
	Output: true
	Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

	Example 2:
	Input: head = [1,2], pos = 0
	Output: true
	Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

	Example 3:
	Input: head = [1], pos = -1
	Output: false
	Explanation: There is no cycle in the linked list.

	Constraints:
	 * The number of the nodes in the list is in the range [0, 104].
	 * -105 <= Node.val <= 105
	 * pos is -1 or a valid index in the linked-list.

	Follow up: Can you solve it using O(1) (i.e. constant) memory?

'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # [1]  -> [2]  -> None
        # Curr -> Next -> None
        # if it's above state then we can do fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()

    # Helper function to build a linked list with an optional cycle
    def build_linked_list(values, pos):
        if not values:
            return None
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    # Test Case 1: Example from question
    head1 = build_linked_list([3, 2, 0, -4], 1)
    print(solution.hasCycle(head1))  # Expected: True

    # Test Case 2: Example from question
    head2 = build_linked_list([1, 2], 0)
    print(solution.hasCycle(head2))  # Expected: True

    # Test Case 3: Example from question
    head3 = build_linked_list([1], -1)
    print(solution.hasCycle(head3))  # Expected: False

    # Edge Case 4: Empty list
    head4 = build_linked_list([], -1)
    print(solution.hasCycle(head4))  # Expected: False

    # Edge Case 5: Single node with cycle to itself
    head5 = build_linked_list([1], 0)
    print(solution.hasCycle(head5))  # Expected: True

    # Edge Case 6: Two nodes, no cycle
    head6 = build_linked_list([1, 2], -1)
    print(solution.hasCycle(head6))  # Expected: False

    # Edge Case 7: Longer list, no cycle
    head7 = build_linked_list([1, 2, 3, 4, 5], -1)
    print(solution.hasCycle(head7))  # Expected: False

    # Edge Case 8: Longer list with cycle in the middle
    head8 = build_linked_list([1, 2, 3, 4, 5], 2)
    print(solution.hasCycle(head8))  # Expected: True