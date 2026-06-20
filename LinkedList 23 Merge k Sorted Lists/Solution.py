'''
Key Idea

At any moment, you only need the smallest current node among the k lists.
So:
1. Put the first node of every non-empty list into a min-heap.
2. Pop the smallest node.
3. Append it to the answer.
4. Push its next node (if it exists) into the heap.
5. Repeat until the heap is empty.

####################################################################################################
Example

Input:
	1 -> 4 -> 5
	1 -> 3 -> 4
	2 -> 6

Initial heap:		[(1,list1), (1,list2), (2,list3)]

Pop 1 (list1)
	result: 1
	push 4
	heap: [1,2,4]

Pop 1 (list2)
	result: 1 -> 1
	push 3
	heap: [2,4,3]

Continue until heap is empty.

####################################################################################################
Since heap elements must be comparable, we add a unique index.

import heapq

class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next) )

        return dummy.next

####################################################################################################
Why do we need idx?

If two nodes have the same value:
	(node1.val, node1)
	(node2.val, node2)

Python tries to compare:	node1 < node2

which raises:
	TypeError: '<' not supported between instances of 'ListNode'

Adding a unique integer:
	(val, idx, node)

ensures tuples remain comparable.

####################################################################################################
Complexity

Let:
* N = total number of nodes across all lists
* k = number of lists

Time
	Each node:
	* pushed once
	* popped once

	Heap size is at most k.
	O(N log k)

Space
	Heap stores at most one node from each list. O(k)

####################################################################################################
####################################################################################################
For more solution visit: https://neetcode.io/solutions/merge-k-sorted-lists

Time Complexity:  O(1)               (for get, put as its just pointer manipulation)
Space Complexity: O(2n)              (for LinkedList + dictionary)
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: #Both condn same
            return None

        while len(lists) > 1: #if only 1 list then why merge
            joinedList = []
            for i in range (0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                joinedList.append(self.merge(l1, l2)) #"=" mai reset everytime
            lists = joinedList #Joined len() < original len()
        return lists[0]

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next #need to advance else everytime tail.next will be overridden with l1,l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Helper function to build linked list from list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to convert linked list to Python list (for easy checking)
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    lists1 = [build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])]
    result1 = solution.mergeKLists(lists1)
    print(linked_list_to_list(result1))  # Expected: [1,1,2,3,4,4,5,6]

    # Example 2
    lists2 = []
    result2 = solution.mergeKLists(lists2)
    print(linked_list_to_list(result2))  # Expected: []

    # Example 3
    lists3 = [build_linked_list([])]
    result3 = solution.mergeKLists(lists3)
    print(linked_list_to_list(result3))  # Expected: []

    # Edge Case 1: Single list only
    lists4 = [build_linked_list([0, 2, 5])]
    result4 = solution.mergeKLists(lists4)
    print(linked_list_to_list(result4))  # Expected: [0,2,5]

    # Edge Case 2: All empty lists
    lists5 = [build_linked_list([]), build_linked_list([]), build_linked_list([])]
    result5 = solution.mergeKLists(lists5)
    print(linked_list_to_list(result5))  # Expected: []

    # Edge Case 3: Negative and positive values
    lists6 = [build_linked_list([-10, -5, 0]), build_linked_list([-6, -3, 2]), build_linked_list([1, 4, 7])]
    result6 = solution.mergeKLists(lists6)
    print(linked_list_to_list(result6))  # Expected: [-10,-6,-5,-3,0,1,2,4,7]

    # Edge Case 4: Large k but many empty
    lists7 = [build_linked_list([]) for _ in range(50)]
    lists7[10] = build_linked_list([1, 2, 3])
    result7 = solution.mergeKLists(lists7)
    print(linked_list_to_list(result7))  # Expected: [1,2,3]