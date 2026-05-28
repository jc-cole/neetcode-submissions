class Solution:
    # no isalnum
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while not Solution.is_alphanumeric(s[l]) and l < r:
                l += 1
            while not Solution.is_alphanumeric(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    @staticmethod
    def is_alphanumeric(char: str) -> bool:
        av = ord(char)
        return (ord('a') <= av <= ord('z') or
                ord('A') <= av <= ord('Z') or
                ord('0') <= av <= ord('9'))

