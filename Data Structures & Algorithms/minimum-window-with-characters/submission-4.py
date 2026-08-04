class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        target, window = {}, {}
        for c in t:
            target[c] = 1 + target.get(c, 0)
        have, need = 0, len(target)
        res, leng = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):

            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in target and window[c] == target[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < leng:
                    res = [l, r]
                    leng = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        if res[0] == -1:
            return ""
        else:
            return s[res[0]: res[1] + 1]
                



        
