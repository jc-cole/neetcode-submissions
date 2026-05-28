class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            if char in [')', ']', '}']:
                if not stack or char != open_to_close[stack[-1]]:
                    return False
                else:
                    stack.pop()
                
        return True if not stack else False