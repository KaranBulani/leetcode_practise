'''

def __init__(self):
	self.sourceSet = set()

def insert(self, val: int) -> bool:
	if val in self.sourceSet:
		return False
	self.sourceSet.add(val)
	return True

def remove(self, val: int) -> bool:
	if val in self.sourceSet:
		self.sourceSet.remove(val)
		return True
	return False

converting set to list is O(n) hence this solution wont work, rather below we are by default creating a list
def getRandom(self) -> int:
	return random.choice(list(self.sourceSet))
'''
import random

class Solution:
    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)

if __name__ == "__main__":
    obj = Solution()
    param_1 = obj.insert(3)
    param_2 = obj.remove(0)
    param_3 = obj.getRandom()