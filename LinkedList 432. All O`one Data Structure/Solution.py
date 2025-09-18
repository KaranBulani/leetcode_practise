'''
Time Complexity:  O(n+m)				(for Traversing both)
Space Complexity: O(1)               	(for pA, pB)
'''

class Bucket:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = self.next = None

class AllOne:
    def __init__(self):
        # Dummy head and tail with boundary frequency
        self.keyStore = {}
        self.minPt = Bucket(float("-inf"))
        self.maxPt = Bucket(float("inf"))
        self.minPt.next, self.maxPt.prev = self.maxPt, self.minPt

    # Helper: insert new node after "curr"
    def _add_right_node(self, curr, key, freq):
        newNode = Bucket(freq)
        newNode.keys.add(key)
        newNode.next = curr.next
        newNode.prev = curr
        curr.next.prev = newNode
        curr.next = newNode

    # Helper: remove a node from list
    def _remove_node(self, curr):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.prev = curr.next = None

    # Increment key count
    def inc(self, key: str) -> None:
        if key in self.keyStore:
            curr = self.keyStore[key]
            curr.keys.remove(key)

            # move to next freq node or create one
            if curr.next.freq == curr.freq + 1:
                curr.next.keys.add(key)
            else:
                self._add_right_node(curr, key, curr.freq + 1)
            self.keyStore[key] = curr.next

            if not curr.keys:
                self._remove_node(curr)
        else:
            # key not present
            if self.minPt.next.freq == 1:
                self.minPt.next.keys.add(key)
                self.keyStore[key] = self.minPt.next
            else:
                self._add_right_node(self.minPt, key, 1)
                self.keyStore[key] = self.minPt.next

    # Decrement key count
    def dec(self, key: str) -> None:
        curr = self.keyStore[key]
        curr.keys.remove(key)

        if curr.freq == 1:
            del self.keyStore[key]  # remove key completely
        else:
            if curr.prev.freq == curr.freq - 1:
                curr.prev.keys.add(key)
                self.keyStore[key] = curr.prev
            else:
                self._add_right_node(curr.prev, key, curr.freq - 1)
                self.keyStore[key] = curr.prev

        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        if self.maxPt.prev == self.minPt:
            return ""
        return next(iter(self.maxPt.prev.keys))

    def getMinKey(self) -> str:
        if self.minPt.next == self.maxPt:
            return ""
        return next(iter(self.minPt.next.keys))

if __name__ == "__main__":
    obj = AllOne()

    # Example from the question
    print("Test 1")
    obj.inc("hello")
    obj.inc("hello")
    print(obj.getMaxKey())   # Expected: "hello"
    print(obj.getMinKey())   # Expected: "hello"
    obj.inc("leet")
    print(obj.getMaxKey())   # Expected: "hello"
    print(obj.getMinKey())   # Expected: "leet"

    # Reset for fresh tests
    obj = AllOne()

    # Test 2: Single element increment/decrement
    print("\nTest 2")
    obj.inc("a")
    print(obj.getMaxKey())   # Expected: "a"
    print(obj.getMinKey())   # Expected: "a"
    obj.dec("a")             # should remove "a"
    print(obj.getMaxKey())   # Expected: ""
    print(obj.getMinKey())   # Expected: ""

    # Test 3: Multiple keys with same frequency
    print("\nTest 3")
    obj.inc("apple")
    obj.inc("banana")
    obj.inc("cherry")
    # All counts = 1
    print(obj.getMaxKey())   # Expected: one of "apple"/"banana"/"cherry"
    print(obj.getMinKey())   # Expected: one of "apple"/"banana"/"cherry"
    obj.inc("banana")
    obj.inc("banana")
    print(obj.getMaxKey())   # Expected: "banana"
    print(obj.getMinKey())   # Expected: "apple" or "cherry"

    # Test 4: Decrementing and removing keys
    print("\nTest 4")
    obj.dec("banana")        # banana count -> 2
    print(obj.getMaxKey())   # Expected: "banana"
    obj.dec("banana")        # banana count -> 1
    obj.dec("banana")        # banana removed
    print(obj.getMaxKey())   # Expected: "apple" or "cherry"
    print(obj.getMinKey())   # Expected: "apple" or "cherry"

    # Test 5: Stress with multiple increments
    print("\nTest 5")
    obj = AllOne()
    for _ in range(5):
        obj.inc("x")
    for _ in range(3):
        obj.inc("y")
    for _ in range(2):
        obj.inc("z")
    print(obj.getMaxKey())   # Expected: "x"
    print(obj.getMinKey())   # Expected: "z"