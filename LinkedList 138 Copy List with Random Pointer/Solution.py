'''
Time Complexity:  O(n)              (for concatenation check)
Space Complexity: O(1)              (for slow, fast pointer)
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        # helper for printing
        random_val = self.random.val if self.random else None
        return f"[{self.val}, {random_val}]"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        curr = head
        # OldNodeWPointers : NewNodeWOPointers (K,V)
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        # Incase want to remove both if condition in while loop:
        # initialize old_to_new as old_to_new = {None : None}
        return old_to_new[head]


def build_linked_list(nodes):
    """
    nodes: list of [val, random_index]
    returns: head of the linked list
    """
    if not nodes:
        return None

    node_list = [Node(val) for val, _ in nodes]
    for i, (_, rand_idx) in enumerate(nodes):
        if i < len(nodes) - 1:
            node_list[i].next = node_list[i + 1]
        if rand_idx is not None:
            node_list[i].random = node_list[rand_idx]
    return node_list[0]


def linked_list_to_array(head):
    """
    Convert linked list back to [[val, random_index], ...] form
    """
    if not head:
        return []
    mapping = {}
    arr, idx = [], 0
    curr = head
    while curr:
        mapping[curr] = idx
        arr.append(curr)
        curr = curr.next
        idx += 1

    result = []
    for i, node in enumerate(arr):
        rand_idx = mapping[node.random] if node.random else None
        result.append([node.val, rand_idx])
    return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head1 = build_linked_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    result1 = solution.copyRandomList(head1)
    print("Output 1:", linked_list_to_array(result1))
    print("Expected:", [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])

    # Example 2
    head2 = build_linked_list([[1, 1], [2, 1]])
    result2 = solution.copyRandomList(head2)
    print("Output 2:", linked_list_to_array(result2))
    print("Expected:", [[1, 1], [2, 1]])

    # Example 3
    head3 = build_linked_list([[3, None], [3, 0], [3, None]])
    result3 = solution.copyRandomList(head3)
    print("Output 3:", linked_list_to_array(result3))
    print("Expected:", [[3, None], [3, 0], [3, None]])

    # Edge Case 1: Empty list
    head4 = build_linked_list([])
    result4 = solution.copyRandomList(head4)
    print("Output 4:", linked_list_to_array(result4))
    print("Expected:", [])

    # Edge Case 2: Single node, random -> null
    head5 = build_linked_list([[5, None]])
    result5 = solution.copyRandomList(head5)
    print("Output 5:", linked_list_to_array(result5))
    print("Expected:", [[5, None]])

    # Edge Case 3: Single node, random -> self
    head6 = build_linked_list([[7, 0]])
    result6 = solution.copyRandomList(head6)
    print("Output 6:", linked_list_to_array(result6))
    print("Expected:", [[7, 0]])