'''
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        var = self.stack[0]
        del self.stack[0]
        return var
    def peek(self):
        return self.stack[0]
    def empty(self):
        if self.stack:
            return False
        return True
Above solution works on leetcode but cannot be used to submit as accessing index [0] is not a valid stack operation.

Time Complexity: All are O(1) push, pop, top, getMin
Space Complexity: O(2n) for 2 stacks/Lists
'''

class MyQueue(object):
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def push(self, x):
        self.pushStack.append(x)

    def pop(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
        return self.popStack[-1] #This is acceptable because it's a valid stack operation

    def empty(self):
        return max(len(self.popStack), len(self.pushStack)) == 0

if __name__ == "__main__":
    commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    values = [[], [1], [2], [], [], []]
    output = []

    obj = None

    for cmd, val in zip(commands, values):
        if cmd == "MyQueue":
            obj = MyQueue()
            output.append(None)
        elif cmd == "push":
            obj.push(val[0])
            output.append(None)
        elif cmd == "pop":
            output.append(obj.pop())
        elif cmd == "peek":
            output.append(obj.peek())
        elif cmd == "empty":
            output.append(obj.empty())

    print(output)