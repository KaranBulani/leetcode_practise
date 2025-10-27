'''
####################################################################################################
############################################ Iterative #############################################
####################################################################################################

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res

####################################################################################################
########################################### Backtracking ###########################################
####################################################################################################

Time complexity:  O(n×4^n)		 			At each of the n positions (digits), we branch into 3 or 4 recursive calls
											Note:
												O(3^n) (if all digits map to 3 letters) OR
												O(4^n) (if all digits map to 4 letters)

											For each recursive call, we perform string concatenation currStr + c which costs O(n) (since strings are immutable in Python).
											Hence total time:  O(n×4^n)

Space complexity: O(n×4^n)		 			Number of combinations = up to 4^n, Each combination length = n ⟹ O(n × 4^n)
											The recursion depth = n ⟹ O(n)
'''
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        alphabets = {
            "2": "abc"
            , "3": "def"
            , "4": "ghi"
            , "5": "jkl"
            , "6": "mno"
            , "7": "pqrs"
            , "8": "tuv"
            , "9": "wxyz"
        }

        def backtrack(i: int, currStr: str):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            # This is not needed as eventually above will be executed
            if i >= len(digits):
                return

            char = alphabets[digits[i]]
            for c in char:
                backtrack(i + 1, currStr + c)

        backtrack(0, "")
        return res


if __name__ == "__main__":
    solution = Solution()

    # Example cases from the problem
    print(solution.letterCombinations("23"))  # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(solution.letterCombinations("2"))  # Expected: ["a","b","c"]

    # Edge case: empty input
    print(solution.letterCombinations(""))  # Expected: []

    # Edge case: maximum input length (4 digits)
    print(solution.letterCombinations("2798"))  # Expected: (multiple combinations)

    # Case: all digits mapping to 3 letters
    print(solution.letterCombinations("234"))  # Expected: (3*3*3 = 27 combinations)

    # Case: digits that map to 4 letters
    print(solution.letterCombinations("79"))  # Expected: (4*4 = 16 combinations)