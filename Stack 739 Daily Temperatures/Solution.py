'''
Time : O(n) as going through all list
Space : O(n) as stack is dependent on n and will materialize when temp in decreasing order
'''

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = [] #pair : [temp : index]
        for i, temp in enumerate(temperatures): #old data in stack, iterating new
            while stack and temp > stack[-1][0]: #-1 for top, 1 for V in K,V
                # if stack itself doesn't exist then no point in popping
                stackT, stackI = stack.pop() #gets K,V as that's what is appended
                answer[stackI] = i - stackI
            stack.append([temp, i])
        return answer

if __name__ == "__main__":
    solution = Solution()
    temp1 = [73,74,75,71,69,72,76,73]
    temp2 = [30,40,50,60]
    temp3 = [30,60,90]
    result = solution.dailyTemperatures(temp1)
    print(result)