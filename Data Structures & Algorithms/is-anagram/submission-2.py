class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars, t_chars = {}, {}
        for i in range(len(s)):
            if s[i] in s_chars:
                s_chars[s[i]] += 1
            else:
                s_chars[s[i]] = 1
            if t[i] in t_chars:
                t_chars[t[i]] += 1
            else:
                t_chars[t[i]] = 1
        return s_chars == t_chars
