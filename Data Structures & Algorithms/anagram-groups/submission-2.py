class Solution:

    @staticmethod
    def get_char_count(s):
        offset = ord('a')
        char_count = [0 for i in range(26)]
        for char in s:
            char_count[ord(char) - offset] += 1
        return tuple(char_count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_counts = defaultdict(list)

        for s in strs:
            char_counts[Solution.get_char_count(s)].append(s)

        return char_counts.values()
        