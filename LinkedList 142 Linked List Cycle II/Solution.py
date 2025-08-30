'''
Time Complexity:  O(n)              (for concatenation check)
Space Complexity: O(1)              (for slow, fast pointer)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = head

        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle
            return None

        # Step 2: Find cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

if __name__ == "__main__":
    solution = Solution()

    # Example 1: cycle at index 1
    head1 = ListNode(3)
    head1.next = ListNode(2)
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(-4)
    head1.next.next.next.next = head1.next  # cycle
    print("Example 1:", solution.detectCycle(head1))  # expected: node with val=2

    # Example 2: cycle at index 0
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = head2  # cycle
    print("Example 2:", solution.detectCycle(head2))  # expected: node with val=1

    # Example 3: no cycle
    head3 = ListNode(1)
    print("Example 3:", solution.detectCycle(head3))  # expected: None

    # Edge Case 1: empty list
    head4 = None
    print("Edge Case 1:", solution.detectCycle(head4))  # expected: None

    # Edge Case 2: single node, no cycle
    head5 = ListNode(10)
    print("Edge Case 2:", solution.detectCycle(head5))  # expected: None

    # Edge Case 3: single node, cycle to itself
    head6 = ListNode(20)
    head6.next = head6
    print("Edge Case 3:", solution.detectCycle(head6))  # expected: node with val=20

    # Edge Case 4: longer list, cycle at last node
    head7 = ListNode(1)
    curr = head7
    for v in [2, 3, 4, 5]:
        curr.next = ListNode(v)
        curr = curr.next
    curr.next = curr  # last node cycles to itself
    print("Edge Case 4:", solution.detectCycle(head7))  # expected: node with val=5

    # Edge Case 5: longer list, cycle somewhere in middle
    head8 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    head8.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3  # cycle at node 3
    print("Edge Case 5:", solution.detectCycle(head8))  # expected: node with val=3