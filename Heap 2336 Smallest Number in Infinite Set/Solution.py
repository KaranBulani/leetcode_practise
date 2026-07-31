'''
Pointer + Min Heap + Hash Set

The infinite set is: {1, 2, 3, 4, 5, ...}

Instead of storing infinitely many numbers, we only keep track of:
* curr → the smallest number that has never been popped.
* A min heap → numbers that were popped earlier but later added back.
* A hash set → prevents duplicate entries in the heap.

Idea
There are two possible smallest numbers:
1. A number that was added back (stored in the heap).
2. The next untouched number (curr).

Whenever we need the smallest:
* If the heap has elements, return the heap's minimum.
* Otherwise, return curr and increment it.

####################################################################################################
Example

Initial:
	curr = 1
	heap = []
	set = {}

popSmallest()
	Heap empty.
	Return 1.
	curr = 2
	heap = []

popSmallest()
	Return 2
	curr = 3

addBack(1)
	Since 1 < curr and isn't already available,
	heap = [1]
	set = {1}

popSmallest()
	Heap has 1.
	Return 1.
	heap = []
	set = {}
	curr = 3

popSmallest()
	Heap empty.
	Return 3.
	curr = 4

Sequence returned:	1, 2, 1, 3
Exactly as expected.

####################################################################################################
Algorithm

popSmallest()

	If heap not empty:
		remove smallest from heap
		remove from set
		return it
	answer = curr
	curr += 1
	return answer

addBack(num)

Only add if:
* it has already been popped (num < curr)
* it isn't already in the heap.

	if num < curr and num not in set:
		push into heap
		add to set

####################################################################################################
Dry Run

curr = 1
heap = []

pop()
	→ 1
	curr = 2

pop()
	→ 2
	curr = 3

addBack(1)

	heap = [1]

pop()
	→ 1
	heap = []

pop()
	→ 3
	curr = 4

addBack(2)
	heap = [2]

pop()
	→ 2

Returned order: 1, 2, 1, 3, 2

####################################################################################################

Complexity Analysis

popSmallest()
* Heap empty: O(1)
* Heap has elements: O(log n)

addBack()
* Heap insertion: O(log n)

Space Complexity
* Heap + hash set store only numbers that have been added back.
Space: O(n), where n is the number of added-back elements.
'''

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.heap = []
        self.available = set()

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.available.remove(smallest)
            return smallest

        smallest = self.curr
        self.curr += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.available:
            heapq.heappush(self.heap, num)
            self.available.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

if __name__ == "__main__":

    print("========== Test Case 1: Example from Question ==========")
    obj = SmallestInfiniteSet()

    obj.addBack(2)
    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2
    print(obj.popSmallest())  # Expected: 3
    obj.addBack(1)
    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 4
    print(obj.popSmallest())  # Expected: 5

    print("\n========== Test Case 2: addBack on existing element ==========")
    obj = SmallestInfiniteSet()

    obj.addBack(1)
    obj.addBack(2)

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2
    print(obj.popSmallest())  # Expected: 3

    print("\n========== Test Case 3: Add back after removal ==========")
    obj = SmallestInfiniteSet()

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2

    obj.addBack(1)

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 3
    print(obj.popSmallest())  # Expected: 4

    print("\n========== Test Case 4: Multiple addBack calls ==========")
    obj = SmallestInfiniteSet()

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2

    obj.addBack(1)
    obj.addBack(1)
    obj.addBack(1)

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 3
    print(obj.popSmallest())  # Expected: 4

    print("\n========== Test Case 5: Add back larger removed numbers ==========")
    obj = SmallestInfiniteSet()

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2
    print(obj.popSmallest())  # Expected: 3
    print(obj.popSmallest())  # Expected: 4
    print(obj.popSmallest())  # Expected: 5

    obj.addBack(3)
    obj.addBack(5)

    print(obj.popSmallest())  # Expected: 3
    print(obj.popSmallest())  # Expected: 5
    print(obj.popSmallest())  # Expected: 6
    print(obj.popSmallest())  # Expected: 7

    print("\n========== Test Case 6: Interleaved operations ==========")
    obj = SmallestInfiniteSet()

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 2

    obj.addBack(1)

    print(obj.popSmallest())  # Expected: 1
    print(obj.popSmallest())  # Expected: 3

    obj.addBack(2)

    print(obj.popSmallest())  # Expected: 2
    print(obj.popSmallest())  # Expected: 4
    print(obj.popSmallest())  # Expected: 5

    print("\n========== Test Case 7: Consecutive pops only ==========")
    obj = SmallestInfiniteSet()

    for _ in range(10):
        print(obj.popSmallest())  # Expected: 1 2 3 4 5 6 7 8 9 10

    print("\n========== Test Case 8: Reinsert several values ==========")
    obj = SmallestInfiniteSet()

    for _ in range(6):
        print(obj.popSmallest())  # Expected: 1 2 3 4 5 6

    obj.addBack(2)
    obj.addBack(4)
    obj.addBack(6)

    print(obj.popSmallest())  # Expected: 2
    print(obj.popSmallest())  # Expected: 4
    print(obj.popSmallest())  # Expected: 6
    print(obj.popSmallest())  # Expected: 7
    print(obj.popSmallest())  # Expected: 8