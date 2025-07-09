'''
Time Complexity: O(n) (go through)
Space Complexity: O(n) for stack
'''


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Initialize the maximum area to 0
        maxArea = 0
        # Stack will store pairs of [start_index, height]
        stack = []

        # Iterate through each bar in the histogram
        for index, height in enumerate(heights):
            # backtrack holds the earliest index this height could extend to
            backtrack = index

            # While the current bar is lower than the last one in the stack,
            # we have found the right boundary for that taller bar
            while stack and height < stack[-1][1]:
                # Pop the last bar's starting index and height
                topIndex, topHeight = stack.pop()
                # Calculate area with topHeight as the smallest bar
                # Width is current index minus the popped bar's start
                area = topHeight * (index - topIndex)
                # Update maxArea if we found a larger area
                maxArea = max(maxArea, area)
                # Update backtrack to the popped bar's start, so
                # the new bar can extend back further
                backtrack = topIndex

            # Push the current bar onto the stack with its effective start
            stack.append([backtrack, height])

        # After processing all bars, some bars may extend to the end
        while stack:
            topIndex, topHeight = stack.pop()
            # Width is total length minus the bar's start index
            area = topHeight * (len(heights) - topIndex)
            maxArea = max(maxArea, area)

        # Return the largest area found
        return maxArea


if __name__ == "__main__":
    solution = Solution()
    # Diverse examples from the problem statement
    test_cases = [
        [2, 1, 5, 6, 2, 3],  # expected output: 10
        [2, 4]  # expected output: 4
    ]

    for heights in test_cases:
        result = solution.largestRectangleArea(heights)
        print(f"Input: {heights} -> Output: {result}")