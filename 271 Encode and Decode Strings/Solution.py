class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> list[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j + 1: j + 1 + length])  # j+1 to skip #
            i = j + 1 + length
        return decoded

if __name__ == "__main__":
    solution = Solution()
    strs = ["we","say",":","yes","!@#$%^&*()"]#["neet","code","love","you"]#["we","say",":","yes"]
    encoded = solution.encode(strs)
    print(encoded)
    decoded = solution.decode(encoded)
    print(decoded)
