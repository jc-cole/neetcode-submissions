class Solution:
    def validPalindrome(self, s: str) -> bool:
        high = len(s) - 1
        low = 0
        strike = False
        while high > low:
            if s[high] == s[low]:
                low += 1
                high -= 1
            elif s[low + 1] == s[high]:
                if strike:
                    return False
                strike = True
                low += 2
                high -= 1
                continue
            elif s[high - 1] == s[low]:
                if strike:
                    return False
                strike = True
                low += 1
                high -= 2
                continue
            else:
                return False
        return True