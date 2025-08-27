'''
####################################################################################################
######################################### Doubly LinkedList ########################################
####################################################################################################
Time Complexity:  O(n/2)              	(for Get, Add, Delete)
Space Complexity: O(n)              	(for LinkedList)

class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)    # dummy head
        self.tail = Node(0)    # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        # Choose direction: from head or tail
        if index < self.size // 2:
            curr = self.head
            for _ in range(index + 1):  # move forward
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):  # move backward
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        self.size += 1
        newNode = Node(val)
        newNode.prev = pred
        newNode.next = succ
        pred.next = newNode
        succ.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # Find predecessor and successor
        if index < self.size//2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            toDelete = pred.next
            succ = toDelete.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            toDelete = succ.prev
            pred = toDelete.prev

        self.size -= 1
        pred.next = succ
        succ.prev = pred


####################################################################################################
######################################### Singly LinkedList ########################################
####################################################################################################

Time Complexity:  O(n)              	(for Get, Add, Delete)
Space Complexity: O(n)              	(for LinkedList)

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        # As 0 indexed even size shouldn't exist
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):  # move index+1 times (because dummy head)
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        self.size += 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        newNode = ListNode(val)
        newNode.next = prev.next
        prev.next = newNode


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        prev = self.head
        # To delete node at index i:
        # prev stops at (i-1) → the node before target
        # e.g. i=0 → prev=head, i=1 → prev at index 0, i=last → prev at size-2
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next


if __name__ == "__main__":
    myLinkedList = MyLinkedList()

    # Example from question
    myLinkedList.addAtHead(1)  # LinkedList: 1
    myLinkedList.addAtTail(3)  # LinkedList: 1 -> 3
    myLinkedList.addAtIndex(1, 2)  # LinkedList: 1 -> 2 -> 3
    print(myLinkedList.get(1))  # Expected: 2
    myLinkedList.deleteAtIndex(1)  # LinkedList: 1 -> 3
    print(myLinkedList.get(1))  # Expected: 3

    print("----- Extra Edge Cases -----")

    # Edge case 1: get from empty list
    emptyList = MyLinkedList()
    print(emptyList.get(0))  # Expected: -1 (nothing inside)

    # Edge case 2: add at index 0 in empty list
    emptyList.addAtIndex(0, 10)  # LinkedList: 10
    print(emptyList.get(0))  # Expected: 10

    # Edge case 3: add at index greater than length (should not insert)
    emptyList.addAtIndex(5, 20)  # No change
    print(emptyList.get(0))  # Expected: 10

    # Edge case 4: delete from invalid index
    emptyList.deleteAtIndex(5)  # No change
    print(emptyList.get(0))  # Expected: 10

    # Edge case 5: add multiple at head
    myLinkedList2 = MyLinkedList()
    myLinkedList2.addAtHead(5)  # 5
    myLinkedList2.addAtHead(4)  # 4 -> 5
    myLinkedList2.addAtHead(3)  # 3 -> 4 -> 5
    print(myLinkedList2.get(0))  # Expected: 3
    print(myLinkedList2.get(2))  # Expected: 5

    # Edge case 6: add at tail repeatedly
    myLinkedList2.addAtTail(6)  # 3 -> 4 -> 5 -> 6
    myLinkedList2.addAtTail(7)  # 3 -> 4 -> 5 -> 6 -> 7
    print(myLinkedList2.get(4))  # Expected: 7

    # Edge case 7: delete head
    myLinkedList2.deleteAtIndex(0)  # LinkedList: 4 -> 5 -> 6 -> 7
    print(myLinkedList2.get(0))  # Expected: 4

    # Edge case 8: delete tail
    myLinkedList2.deleteAtIndex(3)  # LinkedList: 4 -> 5 -> 6
    print(myLinkedList2.get(2))  # Expected: 6

    # Edge case 9: delete last remaining element
    singleNode = MyLinkedList()
    singleNode.addAtHead(99)  # LinkedList: 99
    singleNode.deleteAtIndex(0)  # LinkedList: []
    print(singleNode.get(0))  # Expected: -1
