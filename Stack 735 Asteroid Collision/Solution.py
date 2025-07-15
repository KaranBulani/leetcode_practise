'''
MY COMPLEX SOLUTION

stack = []
for a in asteroids:
    # 1) only safe to just append when there's no chance of collision
    if not stack or stack[-1] < 0 and a > 0:
        stack.append(a)
    else:
        # 2) collision loop: only enters when stack[-1]>0 and a<0
        alive = True
        # keep colliding while both exist and are moving toward each other
        while alive and stack and stack[-1] > 0 and a < 0:
            if stack[-1] == -a:
                # same size → both explode
                stack.pop()
                alive = False
            elif stack[-1] < -a:
                # incoming asteroid is larger → destroy the stack top and retry
                stack.pop()
                # (alive remains True, loop continues against new top)
            else:
                # stack top is larger → incoming explodes
                alive = False
        # if it survived all collisions (or stack emptied), append it
        if alive:
            stack.append(a)
return stack

Time Complexity: O(n) (go through list)
Space Complexity: O(n) for stack
'''

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []  # Stack to keep track of surviving asteroids

        for a in asteroids:
            # Check for collision: current asteroid 'a' is moving left (<0) and top of stack is moving right (>0)
            while stack and stack[-1] > 0 > a:
                diff = stack[-1] + a  # Sum of sizes (taking sign into account)

                if diff > 0:
                    # Stack top asteroid is bigger — current asteroid 'a' explodes
                    a = 0  # Set to 0 so it doesn't get added to the stack
                elif diff < 0:
                    # Current asteroid 'a' is bigger — pop the top and check again with new top
                    stack.pop()
                    # Don't set 'a' to 0 yet; it may still collide with new top of stack
                else:
                    # Both asteroids are equal in size — both explode
                    stack.pop()
                    a = 0  # Set to 0 so 'a' doesn't get added
            if a:
                # If 'a' survived all possible collisions, add to stack
                stack.append(a)

        return stack  # Final state of surviving asteroids


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [5, 10, -5],
        [8, -8],
        [10, 2, -5],
    ]

    for asteroids in test_cases:
        result = solution.asteroidCollision(asteroids)
        print(f"Input: {asteroids} -> Output: {result}")
