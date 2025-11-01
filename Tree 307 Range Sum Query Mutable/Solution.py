'''
####################################################################################################

get_parent
To get parent ➔ x - (x & -x) ➔ where x & -x is LSB (Least Significant Bit) of x.
1) 2's complement(invert bits then add 1) to get minus of index.
2) AND result with index
3) Subtract that from index
So we are just removing LSB of x from x || 1010(10), 1100(12) - LSB = 1000(8) || So, parent of 10,12 is 8

get_next
To get next:
1) 2's complement of get minus of index
2) AND this with index
3) Add it to index
Adding LSB of x to x || 110(6) + 10(2) = 1000(8) || 111(7) + 1(1) = 1000(8) || So, next of 6,7 is 8

get_sum
Start from index+1. If you want prefix sum 0 to index ➔ Keep adding value of parent till you reach 0

####################################################################################################
Time complexity:  O(logn)		 		For Update, get_sum
Space complexity: O(n)		 			For Update, get_sum
'''

class Fenwick:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.nums = [0] + arr  # 1-based
        self.BITtree = [0] * (self.n + 1)  # 1-based

        for i, num in enumerate(arr):
            self.add(i, num)

    def add(self, index: int, amount) -> None:
        index += 1  # 0-index ➔ 1-based
        while index <= self.n:
            self.BITtree[index] += amount
            index = self.get_next(index)

    def get_sum(self, index: int) -> int:
        sum = 0
        index += 1  # 0-index ➔ 1-based
        while index > 0:
            sum += self.BITtree[index]
            index = self.get_parent(index)
        return sum

    def get_parent(self, index: int) -> int: \
            return index - (index & -index)

    def get_next(self, index: int) -> int:
        return index + (index & -index)

class NumArray:
    def __init__(self, nums: list[int]):
        self.obj = Fenwick(nums)

    def update(self, index: int, val: int) -> None:
        delta = val - self.obj.nums[index + 1]
        self.obj.nums[index + 1] = val  # keep nums updated
        self.obj.add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self.obj.get_sum(right) - self.obj.get_sum(left - 1)


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