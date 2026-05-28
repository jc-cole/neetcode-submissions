class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        current_idx = 0
        while current_idx < min_len:
            for s in strs:
                if s[current_idx] != strs[0][current_idx]:
                    return strs[0][:current_idx]
            current_idx += 1
        return strs[0][:min_len]

        