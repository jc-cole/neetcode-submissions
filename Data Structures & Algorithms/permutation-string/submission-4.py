class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        vectorTarget = [0 for _ in range(26)]
        for char in s1:
            vectorTarget[ord(char) - ord('a')] += 1
        
        vectorWindow = [0 for _ in range(26)]
        for i in range(len(s1)):
            vectorWindow[ord(s2[i]) - ord('a')] += 1
        
        if all(vectorTarget[i] == vectorWindow[i] for i in range(26)):
            return True
            
        lowPtr = 0
        for highPtr in range(len(s1), len(s2)):
            vectorWindow[ord(s2[lowPtr]) - ord('a')] -= 1
            vectorWindow[ord(s2[highPtr]) - ord('a')] += 1
            if all(
                vectorTarget[i] == vectorWindow[i] for i in range(len(vectorTarget))
            ):
                return True
            lowPtr += 1
        
        return False