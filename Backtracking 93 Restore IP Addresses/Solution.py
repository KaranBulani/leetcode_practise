'''
Time complexity:  O(3⁴ × L)

1. conceptually we are building a recursion tree with branching factor ≤ 3 `we call recursion from start to start + 3` and depth ≤ 4 `because curr cannot go more than 4`
2. At each level, you can make up to 3 choices (segment lengths 1–3). | __ . __ . __ . __ |
   You stop when you’ve taken 4 segments or reached the end of the string.

3. within each recursive call, we slice strings and convert them to integers, which costs O(1) for short (≤3 character) slices.

4. Joining 4 segments costs O(L) time where L = length of the string (≤12).

Space complexity: O(n × 3⁴)

1. Recursive call stack -> Maximum depth = 4 (since 4 segments)
2. The total count is bounded by the number of possible 4-part splits (≤ 81 again). Each IP string is length O(n).
→ O(n × 3⁴)

'''
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res, curr = [], []

        def backtrack(start: int):
            if len(curr) > 4: return

            if start == len(s) and len(curr) == 4:
                res.append(".".join(curr))
                return

            for end in range(start, min(len(s), start + 3)):
                seg = s[start: end + 1]
                # str(int(s)) removes 0s from start
                if len(seg) != len(str(int(seg))) or int(seg) > 255:
                    continue
                curr.append(seg)
                backtrack(end + 1)  # here we pass end + 1
                curr.pop()

        if 4 <= len(s) <= 12:
            backtrack(0)

        return res


if __name__ == "__main__":
    solution = Solution()

    # Diverse test cases
    test_cases = [
        "25525511135",  # example from prompt
        "0000",  # all zeros
        "101023",  # mix of valid/invalid segments
        "1111",  # smallest valid 4-part segmentation
        "010010",  # tests leading zero behavior
        "256256256256",  # segments exceeding 255
        "123",  # too short to form IP
        "123456789012",  # long string but still possible
        "192168011",  # includes zeros, realistic IP-like sequence
        "0279245587303",  # leading zeros and large numbers
    ]

    for s in test_cases:
        result = solution.restoreIpAddresses(s)
        print(f"Input: {s}")
        print(f"Output: {result}")
        print("-" * 60)