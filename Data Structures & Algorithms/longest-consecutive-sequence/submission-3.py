from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for num in nums:
            if num-1 not in s:
                seq_len = 1
                current_num = num
                while current_num+1 in s:
                    current_num = current_num+1
                    seq_len += 1
                if seq_len > max_len:
                    max_len = seq_len
        return max_len