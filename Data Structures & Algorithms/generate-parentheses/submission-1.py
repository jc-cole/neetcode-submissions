class Solution:
    
    def generateParenthesis(self, n: int, seen=None) -> List[str]:
        if seen == None:
            seen = {0: [""], 1: ["()"]}
            return self.generateParenthesis(n, seen=seen)
        if n in seen:
            return seen[n]
        
        result = []
        for i in range(n):
            leftCall = self.generateParenthesis(i, seen=seen)
            rightCall = self.generateParenthesis(n-i-1, seen=seen)

            for left in leftCall:
                for right in rightCall:
                    result.append(f"({left}){right}")
        
        seen[n] = result
        return result
