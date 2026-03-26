'''
####################################################################################################
class MyCalendar:
    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        low, high = 0, len(self.arr)

        # Find insertion index
        while low < high:
            mid = (low + high) // 2
            if self.arr[mid][0] < start:
                low = mid + 1
            else:
                high = mid

        # Check previous
        if low > 0 and self.arr[low - 1][1] > start:
            return False

        # Check next
        if low < len(self.arr) and self.arr[low][0] < end:
            return False

        self.arr.insert(low, [start, end])
        return True

🚀 Complexity
Time: O(log N + N) (binary search + insert)
Space: O(N)

####################################################################################################

| Operation | Complexity       |
| --------- | ---------------- |
| Book      | O(log N)         |
| Space     | O(N log N) worst |

'''
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.booked = False

class MyCalendar:
    def __init__(self):
        self.root = Node()
        self.START = 0
        self.END = 10**9

    def book(self, start: int, end: int) -> bool:
        if self._query(self.root, self.START, self.END, start, end - 1): # 1. Why end - 1? Problem uses: [start, end). Segment tree works on closed intervals, so convert: [start, end-1]
            return False

        self._update(self.root, self.START, self.END, start, end - 1)
        return True

    def _query(self, node, l, r, start, end):
        if node is None:
            return False

        if start <= l and r <= end:
            return node.booked

        mid = (l + r) // 2

        if end <= mid:
            return self._query(node.left, l, mid, start, end)
        elif start > mid:
            return self._query(node.right, mid + 1, r, start, end)
        else:
            return (
                self._query(node.left, l, mid, start, mid) or
                self._query(node.right, mid + 1, r, mid + 1, end)
            )

    def _update(self, node, l, r, start, end):
        if start <= l and r <= end:
            node.booked = True
            node.left = None
            node.right = None
            return

        mid = (l + r) // 2

        if start <= mid:
            if not node.left:
                node.left = Node()
            self._update(node.left, l, mid, start, end)

        if end > mid:
            if not node.right:
                node.right = Node()
            self._update(node.right, mid + 1, r, start, end)

        node.booked = (
            node.left is not None and node.left.booked and
            node.right is not None and node.right.booked
        )

def run_test(test_id, operations, inputs, expected):
    obj = None
    actual = []

    for i, op in enumerate(operations):
        if op == "MyCalendar":
            obj = MyCalendar()
            actual.append(None)
        elif op == "book":
            start, end = inputs[i]
            actual.append(obj.book(start, end))

    print(f"Test Case {test_id}:")
    print("Expected:", expected)
    print("Actual  :", actual)
    print("Pass    :", expected == actual)
    print("-" * 50)

if __name__ == "__main__":

    # -------------------------------
    # 1. Basic Example (Given)
    # -------------------------------
    ops1 = ["MyCalendar","book","book","book","book","book","book"]
    inp1 = [[],[10,20],[15,25],[30,40],[20,30],[1,11],[0,10]]
    exp1 = [None, True, False, True, True, False, True]

    run_test(1, ops1, inp1, exp1)

    # -------------------------------
    # 2. No Overlaps (Strictly increasing)
    # -------------------------------
    ops2 = ["MyCalendar","book","book","book"]
    inp2 = [[],[1,5],[5,10],[10,15]]
    exp2 = [None, True, True, True]

    run_test(2, ops2, inp2, exp2)

    # -------------------------------
    # 3. Complete Overlap
    # -------------------------------
    ops3 = ["MyCalendar","book","book"]
    inp3 = [[],[10,20],[10,20]]
    exp3 = [None, True, False]

    run_test(3, ops3, inp3, exp3)

    # -------------------------------
    # 4. Partial Overlap (Left side)
    # -------------------------------
    ops4 = ["MyCalendar","book","book"]
    inp4 = [[],[10,20],[5,15]]
    exp4 = [None, True, False]

    run_test(4, ops4, inp4, exp4)

    # -------------------------------
    # 5. Partial Overlap (Right side)
    # -------------------------------
    ops5 = ["MyCalendar","book","book"]
    inp5 = [[],[10,20],[15,25]]
    exp5 = [None, True, False]

    run_test(5, ops5, inp5, exp5)

    # -------------------------------
    # 6. Touching boundary (Important edge)
    # -------------------------------
    ops6 = ["MyCalendar","book","book"]
    inp6 = [[],[10,20],[20,30]]
    exp6 = [None, True, True]

    run_test(6, ops6, inp6, exp6)

    # -------------------------------
    # 7. Insert in between
    # -------------------------------
    ops7 = ["MyCalendar","book","book","book"]
    inp7 = [[],[10,20],[30,40],[20,30]]
    exp7 = [None, True, True, True]

    run_test(7, ops7, inp7, exp7)

    # -------------------------------
    # 8. Large values
    # -------------------------------
    ops8 = ["MyCalendar","book","book"]
    inp8 = [[],[0, 10**9],[10**9 - 1, 10**9]]
    exp8 = [None, True, False]

    run_test(8, ops8, inp8, exp8)

    # -------------------------------
    # 9. Many small non-overlapping intervals
    # -------------------------------
    ops9 = ["MyCalendar"] + ["book"] * 5
    inp9 = [[]] + [[i, i+1] for i in range(5)]
    exp9 = [None, True, True, True, True, True]

    run_test(9, ops9, inp9, exp9)

    # -------------------------------
    # 10. Random overlap mix
    # -------------------------------
    ops10 = ["MyCalendar","book","book","book","book"]
    inp10 = [[],[5,10],[15,20],[10,15],[7,12]]
    exp10 = [None, True, True, True, False]

    run_test(10, ops10, inp10, exp10)