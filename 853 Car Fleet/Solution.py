'''
Time Complexity: O(nlogn) (sort + go through)
Space Complexity: O(n) for stack
'''
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [ (p,s) for p, s in zip(position, speed)]
        pair = sorted(pair, key = lambda x: x[0], reverse = True)

        stack = []
        for p,s in pair:
            timeTaken = (target - p)/s
            if not stack or stack[-1] < timeTaken:
                stack.append(timeTaken)
        return len(stack)

if __name__ == "__main__":
    solution = Solution()

    examples = [
        # (target, position_list, speed_list) 3, 1, 1
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]),
        (10, [3], [3]),
        (100, [0, 2, 4], [4, 2, 1])
    ]

    for idx, (target, position, speed) in enumerate(examples, start=1):
        result = solution.carFleet(target, position, speed)
        print(f"Example {idx}: carFleet({target}, {position}, {speed}) -> {result}")