'''
Time Complexity => Sorting(SlogS + TlogT)
Space Complexity => Extra space which merge sort takes O(2S) + O(2T)
                 => 2S: 1 for right and 1 for left
'''

class Solution:
    def merge(self, stringArr: list[str], start: int, mid: int, end: int):
        L = stringArr[start: mid + 1] #mid + 1 to include mid
        R = stringArr[mid + 1: end + 1] #end + 1 to include end

        l, r, n = 0, 0, start

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                stringArr[n] = L[l]
                l += 1
            else:
                stringArr[n] = R[r]
                r += 1
            n += 1

        while l < len(L):
            stringArr[n] = L[l]
            l += 1
            n += 1
        while r < len(R):
            stringArr[n] = R[r]
            r += 1
            n += 1

    def mergeSort(self, stringArr: list[str], start: int, end: int ) -> list[str]:
        if end - start  <= 0:
            return stringArr

        mid = (start + end)// 2
        self.mergeSort(stringArr, start, mid)
        self.mergeSort(stringArr, mid + 1, end)
        self.merge(stringArr, start, mid , end)

        return stringArr

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = ''.join(self.mergeSort(list(s), 0, len(s)) )
        sorted_t = ''.join(self.mergeSort(list(t), 0, len(t)) )

        if sorted_s == sorted_t:
            return True
        return False

if __name__ == "__main__":
    solution = Solution()
    s = "anagrama"#"rat"
    t = "nagaram"#"car"
    result = solution.isAnagram(s, t)
    print(result)