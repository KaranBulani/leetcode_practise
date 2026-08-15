'''
1. Using bin() (Includes 0b Prefix)
The built-in bin() function converts an integer into a binary string prefixed with 0b.
    number = 10
    print(bin(number))  # Output: '0b1010'
####################################################################################################
2. Using Slicing (Removes 0b Prefix)
If you only want the raw 0 and 1 digits, use string slicing [2:] to strip the first two characters.
    number = 10
    print(bin(number)[2:])  # Output: '1010'

####################################################################################################
3. Using F-Strings or format()
(Clean Formatting)You can use the b format specifier inside an f-string or the format() function to get the raw binary string directly.

    number = 10

    # Using f-string
    print(f"{number:b}")  # Output: '1010'

    # Using format()
    print(format(number, "b"))  # Output: '1010'

####################################################################################################
4. Pad with Leading Zeros (Fixed Width)
To make your binary representation a fixed length (e.g., 8 bits for a byte), add a number before the b in your format string.

    number = 10

    # Zero-pad to 8 characters
    print(f"{number:08b}")  # Output: '00001010'

####################################################################################################
####################################################################################################
Same way to implement both solution
####################################################################################################
####################################################################################################

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res=0

        while a or b or c:
            a_bit=a&1
            b_bit=b&1
            c_bit=c&1

            if c_bit==0:
                res+=a_bit+b_bit

            else:
                if a_bit==0 and b_bit==0:
                    res+=1

            a>>=1
            b>>=1
            c>>=1

        return res

####################################################################################################
####################################################################################################

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        max_bit_length = max(a.bit_length(), b.bit_length(), c.bit_length())
        ans = 0
        for a_bit, b_bit, c_bit in zip(
            f"{a:0{max_bit_length}b}",
            f"{b:0{max_bit_length}b}",
            f"{c:0{max_bit_length}b}",
        ):
            if c_bit == "0":
                ans += int(a_bit) + int(b_bit)
            elif c_:
                if a_bit == "0" and b_bit == "0":
                    ans += 1

        return ans
'''


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        # DiverseExamplesFromQuestion
        ((2, 6, 5), 3),  # Example 1
        ((4, 2, 7), 1),  # Example 2
        ((1, 2, 3), 0),  # Example 3

        # Additional edge cases
        ((1, 1, 1), 0),  # Already satisfies: 1 | 1 = 1
        ((1, 1, 2), 2),  # Both 1-bits need to be flipped off
        ((2, 2, 1), 2),  # 10 | 10 -> 01 requires two flips
        ((8, 0, 8), 0),  # Already satisfies: 1000 | 0000 = 1000
        ((8, 0, 0), 1),  # 1000 needs to become 0000
        ((0, 0, 7), 3),  # Need to create three 1-bits
        ((7, 7, 0), 6),  # All six 1-bits must be flipped off
        ((5, 3, 7), 0),  # 101 | 011 = 111
        ((5, 3, 4), 2),  # Extra 1-bits must be removed
        ((10, 5, 15), 0),  # 1010 | 0101 = 1111

        # Larger values
        ((10 ** 9, 10 ** 9, 10 ** 9), 0),
        ((10 ** 9, 0, 0), 13),
        ((0, 10 ** 9, 0), 13),
    ]

    for inputs, expected in test_cases:
        result = solution.minFlips(*inputs)

        print(
            f"Input: a={inputs[0]}, b={inputs[1]}, c={inputs[2]} "
            f"| Output: {result} "
            f"| Expected: {expected} "
            f"| {'PASS' if result == expected else 'FAIL'}"
        )