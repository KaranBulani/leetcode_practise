'''
####################################################################################################
####################################### ITERATIVE & RECURSIVE ######################################
####################################################################################################

Same Time Complexity

Time Complexity:  O(n)              	(for LinkedList Nodes)
Space Complexity: O(n)              	(for LinkedList Nodes)

####################################################################################################
##################################### Dry Run Recursive + CODE #####################################
####################################################################################################

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        nextHead = self.reverseList(head.next)
        #cant do .next.next if single element
        head.next.next = head
        head.next = None
        return nextHead

Input :		1 → 2 → 3 → None
________________________________________
Call Stack Walkthrough
Step 1: First Call
reverseList(1)
•	head = 1
•	Since head and head.next exist → go deeper:
new_head = reverseList(2)
________________________________________
Step 2: Second Call
reverseList(2)
•	head = 2
•	Go deeper:
new_head = reverseList(3)
________________________________________
Step 3: Third Call
reverseList(3)
•	head = 3
•	Base case hit (head.next is None) → return 3
So now:
reverseList(3) returns node 3
________________________________________
Unwinding the recursion
Back to Step 2 (head = 2)
•	new_head = 3
•	Rewiring:
	head.next.next = head   # 3.next = 2
	head.next = None        # 2.next = None
•	Now list looks like:
	3 → 2 → None
•	Return new_head = 3
________________________________________
Back to Step 1 (head = 1)
•	new_head = 3
•	Rewiring:
	head.next.next = head   # 2.next = 1
	head.next = None        # 1.next = None
•	Now list looks like:
	3 → 2 → 1 → None
•	Return new_head = 3
________________________________________
Final Result
3 → 2 → 1 → None
####################################################################################################
############################################ DONE ##################################################
####################################################################################################

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Helper function to build a linked list from Python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
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

    test_cases = [
        # From question
        ([1,2,3,4,5], [5,4,3,2,1]),
        ([1,2], [2,1]),
        ([], []),

        # Additional edge cases
        ([1], [1]),                         # single node
        ([0,0,0,0], [0,0,0,0]),             # all elements same
        ([-1,-2,-3,-4], [-4,-3,-2,-1]),     # negative numbers
        ([5000,-5000,123,-123], [-123,123,-5000,5000])  # mixed extremes
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        head = build_linked_list(inp)
        result_head = solution.reverseList(head)
        result_list = linked_list_to_list(result_head)
        print(f"Test case {i}: input={inp} | expected={expected} | got={result_list}")