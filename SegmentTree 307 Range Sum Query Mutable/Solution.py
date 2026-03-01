'''
Time Complexity:
    Initialization → O(n)               build being implement for Segment Tree which is of length 4 * n
    update → O(log n)
    sumRange → O(log n)

Space Complexity
    Tree storage → O(n)                 which is 4 * n
    Recursion stack → O(log n)
'''
from typing import List

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.Tree = [0] * 4 * self.n
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], index: int, left: int, right: int) -> None:
        if left == right:
            self.Tree[index] = nums[left]
            return
        mid = (left + right) // 2
        self._build(nums, 2 * index + 1, left, mid)
        self._build(nums, 2 * index + 2, mid + 1, right)

        self.Tree[index] = self.Tree[2 * index + 1] + self.Tree[2 * index + 2]

    def _update(self, index: int, left: int, right: int, pos: int, value: int) -> None:
        if left == right:
            self.Tree[index] = value
            return
        mid = (left + right) // 2
        if pos <= mid:
            self._update(2 * index + 1, left, mid, pos, value)
        else:
            self._update(2 * index + 2, mid + 1, right, pos, value)

        self.Tree[index] = self.Tree[2 * index + 1] + self.Tree[2 * index + 2]

    def _query(self, index: int, left: int, right: int, ql: int, qr: int) -> int:
        # section of [left, right] fully outside [ql, qr] hence return nothing
        # Points would be like [left, right, ql, qr] or [ql, qr, left, right]
        # condition should be like right < ql or qr < left
        if ql > right or qr < left:
            return 0

        # section of [left, right] is inside [ql, qr] hence return segmentTree value
        # Points would be like [ql, left, right, qr]
        if ql <= left and right <= qr:
            return self.Tree[index]

        mid = (left + right) // 2

        return (
                self._query(2 * index + 1, left, mid, ql, qr)
                + self._query(2 * index + 2, mid + 1, right, ql, qr)
        )


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.obj = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.obj._update(0, 0, len(self.nums) - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.obj._query(0, 0, len(self.nums) - 1, left, right)

if __name__ == "__main__":
    # Example 1: From problem statement
    print("Example 1:")
    obj = NumArray([1, 3, 5])
    print(obj.sumRange(0, 2))  # Expected: 9
    obj.update(1, 2)
    print(obj.sumRange(0, 2))  # Expected: 8

    # Example 2: Single element array
    print("\nExample 2:")
    obj = NumArray([10])
    print(obj.sumRange(0, 0))  # Expected: 10
    obj.update(0, -5)
    print(obj.sumRange(0, 0))  # Expected: -5

    # Example 3: Multiple updates
    print("\nExample 3:")
    obj = NumArray([2, 4, 6, 8, 10])
    print(obj.sumRange(1, 3))  # Expected: 18 (4+6+8)
    obj.update(2, 1)  # nums = [2, 4, 1, 8, 10]
    print(obj.sumRange(1, 3))  # Expected: 13 (4+1+8)
    obj.update(4, 0)  # nums = [2, 4, 1, 8, 0]
    print(obj.sumRange(0, 4))  # Expected: 15

    # Example 4: Edge case - all negatives
    print("\nExample 4:")
    obj = NumArray([-1, -2, -3, -4])
    print(obj.sumRange(0, 3))  # Expected: -10
    obj.update(2, 5)  # nums = [-1, -2, 5, -4]
    print(obj.sumRange(1, 3))  # Expected: -1 (-2+5-4)

    # Example 5: Edge case - left == right
    print("\nExample 5:")
    obj = NumArray([5, 7, 9])
    print(obj.sumRange(1, 1))  # Expected: 7
    obj.update(1, 10)  # nums = [5, 10, 9]
    print(obj.sumRange(1, 1))  # Expected: 10

    # Example 6: Edge case - update first and last element
    print("\nExample 6:")
    obj = NumArray([3, 3, 3, 3])
    obj.update(0, 1)  # nums = [1, 3, 3, 3]
    obj.update(3, 6)  # nums = [1, 3, 3, 6]
    print(obj.sumRange(0, 3))  # Expected: 13
    print(obj.sumRange(1, 2))  # Expected: 6