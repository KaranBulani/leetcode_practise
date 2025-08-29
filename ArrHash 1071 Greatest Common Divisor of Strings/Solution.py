'''
Time Complexity:  O(n + m)              (for concatenation check)
Space Complexity: O(1)              	(for Variables, indexes)
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Euclidean algorithm for gcd
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        # If str1+str2 != str2+str1, they don't share a common base
        if str1 + str2 != str2 + str1:
            return ""

        length = gcd(len(str1), len(str2))
        return str1[:length]

# Place this after the Solution class from LeetCode (which should define gcdOfStrings)
if __name__ == "__main__":
    solution = Solution()

    # Test cases: (str1, str2, expected)
    tests = [
        # Examples from prompt
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),

        # Basic / trivial
        ("A", "A", "A"),
        ("A", "AA", "A"),
        ("AA", "AAA", "A"),

        # One is exact multiple of the other
        ("XYZ", "XYZXYZ", "XYZ"),
        ("ABCABCABC", "ABCABC", "ABCABC"),
        ("ABAB", "AB", "AB"),
        ("ABABAB", "AB", "AB"),

        # Same strings (gcd is the string itself)
        ("ABCD", "ABCD", "ABCD"),

        # Repeated single-character patterns
        ("AAAA", "AA", "AA"),
        ("AAAAAAAA", "AAAA", "AAAA"),

        # No common divisor (should return "")
        ("ABC", "DEF", ""),
        ("ABAB", "ABA", ""),    # lengths and patterns incompatible
        ("AB", "BA", ""),

        # Tricky pattern mismatches
        ("AAABAAAB", "AAAB", "AAAB"),
        ("ABCABCABD", "ABC", ""),  # last char mismatch -> no gcd

        # Different lengths but with a smaller gcd
        ("RATATATATA", "RATATA", "RATA"),  # example (verify with your code)
    ]

    # Run tests and print results
    for idx, (s1, s2, expected) in enumerate(tests, start=1):
        actual = solution.gcdOfStrings(s1, s2)
        status = "PASS" if actual == expected else "FAIL"
        print(f"Test {idx:02d}:")
        print(f"  str1     = {s1!r}")
        print(f"  str2     = {s2!r}")
        print(f"  expected = {expected!r}")
        print(f"  actual   = {actual!r}")
        print(f"  -> {status}")
        print("-" * 50)