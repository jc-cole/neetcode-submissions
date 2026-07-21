class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        lowPtr = 0
        longest = 0
        for i in range(len(s)):

            while (s[i] in seen) and (lowPtr < i):
                toRemove = s[lowPtr]
                seen.remove(toRemove)
                lowPtr += 1
            
            seen.add(s[i])
            
            longest = max(longest, (i - lowPtr) + 1)
        
        return longest

                    
