class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqVector = [0 for _ in range(26)]
        result = 1
        lowPtr = 0
        freqVector[ord(s[0]) - ord('A')] += 1
        for highPtr in range(1, len(s)):
            freqVector[ord(s[highPtr]) - ord('A')] += 1

            while (highPtr - lowPtr + 1) - max(freqVector) > k:
               freqVector[ord(s[lowPtr]) - ord('A')] -= 1
               lowPtr += 1
            
            result = max(result, (highPtr - lowPtr + 1))
        
        return result


                
                
            