class Solution:

    @staticmethod
    def get_char_count(s):
        offset = ord('a')
        char_count = [0 for i in range(26)]
        for char in s:
            char_count[ord(char) - offset] += 1
        return tuple(char_count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_counts = {}

        for s in strs:
            char_count = Solution.get_char_count(s)
            if char_count in char_counts:
                char_counts[char_count].append(s)
            else:
                char_counts[char_count] = [s]
        
        return list(char_counts.values())
        