class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []

        def dfs(start):
            if start == len(digits):
                return [[]]
            
            result = []
            for c in digitsToLetters[digits[start]]:
                possibleSuffixes = dfs(start + 1)
                for suffix in possibleSuffixes:
                    suffix.append(c)
                    result.append(suffix)
            return result
        
        return ["".join(arr[::-1]) for arr in dfs(0)]