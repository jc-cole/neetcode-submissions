from collections import deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences = {}

        for num in nums:
            if num in sequences:
                continue
            elif num-1 in sequences and num+1 in sequences:
                sequences[num+1].appendleft(num)
                sequences[num-1].extend(sequences[num+1])
                sequences[sequences[num-1][-1]] = sequences[num-1]
                sequences[num] = deque()
            elif num-1 in sequences:
                sequences[num-1].append(num)
                sequences[num] = sequences[num-1]
            elif num+1 in sequences:
                sequences[num+1].appendleft(num)
                sequences[num] = sequences[num+1]
            elif num not in sequences:
                sequences[num] = deque()
                sequences[num].append(num)
    
        max = float("-inf")
        for k, v in sequences.items():
            if len(v) > max:
                max = len(v)

        return max if max != float("-inf") else 0
