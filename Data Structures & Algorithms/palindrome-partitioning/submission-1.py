class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def dfs(start):
            if start == len(s):
                return [[]]
            
            result = []
            for i in range(start + 1, len(s) + 1):
                substr = s[start:i]
                print(substr)

                if substr == substr[::-1]:
                    suffixPartitions = dfs(i)

                    for part in suffixPartitions:
                        result.append([substr] + part)
            
            return result
        
        return dfs(0)