class Solution:

    # @staticmethod
    # def get_char_count(s):
    #     char_count = {}
    #     for char in s:
    #         if char in char_count:
    #             char_count[char] += 1
    #         else:
    #             char_count[char] = 1
    #     return str(char_count)

    @staticmethod
    def get_sorted_str(s):
        return "".join(sorted(list(s)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_strs = {}

        for s in strs:
            sorted_str = Solution.get_sorted_str(s)
            if sorted_str in sorted_strs:
                sorted_strs[sorted_str].append(s)
            else:
                sorted_strs[sorted_str] = [s]
        
        return list(sorted_strs.values())
        