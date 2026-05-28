class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}]{s}"
        return encoded

    def decode(self, s: str) -> List[str]:

        print(s)

        if s == "": return []

        next_substring_len = ""
        for i, char in enumerate(s):
            if char == "]":
                next_substring = s[i+1:i+1+int(next_substring_len)]
                remaining = s[i+1+int(next_substring_len):]
                return [next_substring] + Solution.decode(self, remaining)
            else:
                next_substring_len += char
